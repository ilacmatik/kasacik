#!/usr/bin/env python3
"""
ENAG (Enflasyon Araştırma Grubu) aylık/yıllık oranını bulup veri.json'a yazar.

1) ENAG'ın kendi sitesi (enagrup.org) — sayfa metninde "<Ay> <Yıl>" yakınındaki aylık/yıllık oran.
2) Site kapalıysa: haber başlıklarından (yalnızca sunucuda okunur; uygulamada haber gösterilmez),
   en az iki başlıkta aynı geçen değer seçilir.
Bulunamazsa çıkış kodu 2 (iş akışı bildirim açar). Yalnızca Python standart kütüphanesi.
"""
import datetime as dt
import email.utils
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(HERE, "..", "veri.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
AYLAR = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]
NUM = r"(\d{1,3}[,.]\d{1,2})"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "tr-TR,tr;q=0.9"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", errors="replace")


def num(s: str) -> float:
    return float(s.replace(",", "."))


def lower_tr(s: str) -> str:
    return s.replace("I", "ı").replace("İ", "i").lower()


def from_site(month: dt.date):
    """enagrup.org ana sayfası ve bülten sayfasında aranan ayın oranları."""
    ay = AYLAR[month.month - 1]
    for url in ("https://enagrup.org/", "https://enagrup.org/bultenler"):
        try:
            text = lower_tr(html.unescape(re.sub(r"<[^>]+>", " ", fetch(url))))
        except Exception as e:  # noqa: BLE001
            print(f"uyarı: {url}: {e}", file=sys.stderr)
            continue
        text = re.sub(r"\s+", " ", text)
        for m in re.finditer(rf"{ay}\s*{month.year}", text):
            win = text[m.start() : m.start() + 600]
            y = re.search(rf"yıllık[^0-9%]{{0,40}}(?:%|yüzde)\s*{NUM}", win)
            a = re.search(rf"aylık[^0-9%]{{0,40}}(?:%|yüzde)\s*{NUM}", win)
            if y:
                yearly = num(y.group(1))
                monthly = num(a.group(1)) if a else None
                if 10 <= yearly <= 300 and (monthly is None or 0 <= monthly <= 15):
                    return yearly, monthly, "enagrup.org"
    return None


def from_news(month: dt.date):
    """Haber başlıkları: yayın tarihi ayın ilk 7 günü, ENAG geçen ve TÜİK geçmeyen başlıklar."""
    q = urllib.parse.quote("ENAG enflasyon")
    try:
        xml = fetch(f"https://news.google.com/rss/search?q={q}+when:10d&hl=tr&gl=TR&ceid=TR:tr")
    except Exception as e:  # noqa: BLE001
        print(f"uyarı: haberler: {e}", file=sys.stderr)
        return None
    pub = (month.replace(day=28) + dt.timedelta(days=4)).replace(day=1)  # açıklandığı ay
    yearly, monthly = Counter(), Counter()
    for item in re.findall(r"<item>(.*?)</item>", xml, re.S):
        t = re.search(r"<title>(.*?)</title>", item, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", item)
        if not t or not d:
            continue
        try:
            date = email.utils.parsedate_to_datetime(d.group(1))
        except Exception:  # noqa: BLE001
            continue
        if (date.year, date.month) != (pub.year, pub.month) or date.day > 7:
            continue
        title = html.unescape(t.group(1)).rsplit(" - ", 1)[0]
        low = lower_tr(title)
        if "enag" not in low or "tüik" in low or "tuik" in low:
            continue
        for v in re.findall(rf"enag(?:'[ıi]n|'[ae] göre|'a|'e| ise|:)?\s*(?:yıllık\s*)?(?:%|yüzde)\s*{NUM}", low) + re.findall(
            rf"yıllık(?: enflasyon| artış)?[^0-9%]{{0,20}}(?:%|yüzde)\s*{NUM}", low
        ):
            if 10 <= num(v) <= 300:
                yearly[num(v)] += 1
        for v in re.findall(rf"(?:aylık(?: bazda)?|ayında)\s*(?:%|yüzde)\s*{NUM}", low):
            if 0 <= num(v) <= 15:
                monthly[num(v)] += 1
    if not yearly:
        return None
    y, n = yearly.most_common(1)[0]
    if n < 2:  # tek başlığa güvenme
        return None
    m = monthly.most_common(1)[0][0] if monthly else None
    return y, m, "haber başlıkları"


def main() -> int:
    today = dt.date.today()
    month = (today.replace(day=1) - dt.timedelta(days=1)).replace(day=1)  # geçen ay
    key = month.strftime("%Y-%m")
    with open(VERI, encoding="utf-8") as f:
        veri = json.load(f)
    enag = veri.get("enag") or []
    if any(row[0] == key for row in enag):
        print(f"{key} zaten var.")
        return 0
    found = from_site(month) or from_news(month)
    if not found:
        print(f"{key} bulunamadı (henüz açıklanmamış olabilir).")
        return 2
    yearly, monthly, src = found
    enag = [r for r in enag if r[0] != key] + [[key, yearly, monthly]]
    enag.sort(key=lambda r: r[0])
    veri["enag"] = enag[-24:]
    veri["version"] = max(veri.get("version", ""), today.isoformat())
    with open(VERI, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{key}: yıllık %{yearly}, aylık %{monthly} ({src})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
