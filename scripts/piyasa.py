#!/usr/bin/env python3
"""
Kasacık veri sunucusu: borsa fiyatlarını günde birkaç kez tek dosyada toplar (piyasa.json).

Telefonlar başka sitelere gitmez; uygulama gecikmeli/gün sonu fiyatı bu dosyadan okur.
Yalnızca Python standart kütüphanesi. GitHub Actions'ta (herkese açık depo → ücretsiz) çalışır.

Çıktı: {"t": <epoch sn>, "q": {"THYAO.IS": [fiyat, önceki_kapanış], "AAPL": [...], "^GSPC": [...]}}
"""
import http.cookiejar
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "piyasa.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"

# Endeksler ve emtialar (üst şerit, gümüş)
INDEX = ["XU100.IS", "XU030.IS", "^GSPC", "^IXIC", "^DJI", "BZ=F", "GC=F", "SI=F", "PL=F", "PA=F"]

# Yurt dışında en çok tutulan hisse ve fonlar (listede olmayanlar uygulamada yedek yoldan gelir)
US = """AAPL MSFT NVDA AMZN GOOGL GOOG META TSLA BRK-B AVGO LLY JPM V MA UNH XOM JNJ PG HD COST ABBV MRK
NFLX ADBE CRM AMD INTC ORCL CSCO PEP KO WMT BAC DIS MCD NKE PFE T VZ QCOM TXN IBM UBER PYPL SHOP SQ PLTR
COIN MSTR SNOW ABNB BABA TSM ASML SONY TM NIO RIVN LCID F GM BA CAT GE MMM HON LMT RTX DE GS MS C WFC
SBUX TGT LOW AMGN GILD BMY CVX COP OXY SLB MU ARM SMCI DELL HPQ SPOT RBLX EA TTWO ROKU ZM DOCU NOW PANW
CRWD NET DDOG MDB TEAM INTU ADP BKNG MAR SPY QQQ DIA IWM VOO VTI VT VEA VWO EEM GLD SLV USO TLT IEF
SHY LQD HYG ARKK XLK XLF XLE XLV SMH SOXX SCHD JEPI""".split()


_jar = http.cookiejar.CookieJar()
_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(_jar))
_crumb = None


def _open(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9"})
    with _opener.open(req, timeout=timeout) as r:
        return r.read()


def session() -> None:
    """Yahoo oturumu: çerez + crumb (bulut sunucularından çerezsiz istekler 429 alıyor)."""
    global _crumb
    for url in ("https://fc.yahoo.com", "https://finance.yahoo.com/quote/AAPL"):
        try:
            _open(url)
        except Exception:  # noqa: BLE001  (404 dönse de çerez gelir)
            pass
    for host in ("query2", "query1"):
        try:
            c = _open(f"https://{host}.finance.yahoo.com/v1/test/getcrumb").decode().strip()
            if c and "<" not in c:
                _crumb = c
                return
        except Exception as e:  # noqa: BLE001
            print(f"uyarı: crumb {host}: {e}", file=sys.stderr)


def get(url: str) -> dict:
    if _crumb:
        url += ("&" if "?" in url else "?") + "crumb=" + urllib.parse.quote(_crumb)
    return json.loads(_open(url).decode("utf-8"))


def spark(symbols: list) -> dict:
    """Sembol → [son fiyat, önceki kapanış]. Önce toplu "quote" (50'şerli), olmazsa "spark" (20'şerli)."""
    out = {}
    for i in range(0, len(symbols), 50):
        chunk = symbols[i : i + 50]
        q = ",".join(urllib.parse.quote(s) for s in chunk)
        data = None
        for host in ("query2", "query1"):
            try:
                data = get(f"https://{host}.finance.yahoo.com/v7/finance/quote?symbols={q}")
                break
            except Exception as e:  # noqa: BLE001
                print(f"uyarı: quote {host} {chunk[0]}…: {e}", file=sys.stderr)
                time.sleep(3)
        rows = ((data or {}).get("quoteResponse") or {}).get("result") or []
        for r in rows:
            p = r.get("regularMarketPrice")
            prev = r.get("regularMarketPreviousClose")
            if isinstance(p, (int, float)) and p > 0:
                out[r.get("symbol")] = [round(p, 6), round(prev, 6) if isinstance(prev, (int, float)) and prev > 0 else None]
        if not rows:
            out.update(_spark(chunk))
        time.sleep(0.6)
    return out


def _spark(symbols: list) -> dict:
    out = {}
    for i in range(0, len(symbols), 20):
        chunk = symbols[i : i + 20]
        q = ",".join(urllib.parse.quote(s) for s in chunk)
        try:
            data = get(f"https://query1.finance.yahoo.com/v8/finance/spark?symbols={q}&range=1d&interval=1d")
        except Exception as e:  # noqa: BLE001
            print(f"uyarı: spark {chunk[0]}…: {e}", file=sys.stderr)
            continue
        for s in chunk:
            e = data.get(s) or {}
            closes = [c for c in (e.get("close") or []) if isinstance(c, (int, float)) and c > 0]
            if not closes:
                continue
            prev = e.get("chartPreviousClose")
            prev = prev if isinstance(prev, (int, float)) and prev > 0 else None
            out[s] = [round(closes[-1], 6), round(prev, 6) if prev else None]
        time.sleep(0.6)
    return out


def tv_scan(market: str, payload: dict) -> list:
    req = urllib.request.Request(
        f"https://scanner.tradingview.com/{market}/scan",
        data=json.dumps(payload).encode(),
        headers={"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8")).get("data") or []


def _row(close, chg):
    if not isinstance(close, (int, float)) or close <= 0:
        return None
    prev = close / (1 + chg / 100) if isinstance(chg, (int, float)) and chg > -100 else None
    return [round(close, 6), round(prev, 6) if prev else None]


def tradingview(bist: list) -> dict:
    """Tüm BIST hisseleri tek istekte; ABD listesi ve endeksler. Anahtarlar uygulamanın beklediği biçimde."""
    out = {}
    want = {c.removesuffix(".IS") for c in bist}
    try:
        rows = tv_scan("turkey", {"columns": ["name", "close", "change"], "range": [0, 2000]})
        for r in rows:
            name, close, chg = (r.get("d") or [None, None, None])[:3]
            if name in want and (v := _row(close, chg)):
                out[name + ".IS"] = v
    except Exception as e:  # noqa: BLE001
        print(f"uyarı: tv turkey: {e}", file=sys.stderr)
    try:
        tv_names = {u.replace("-", "."): u for u in US}
        rows = tv_scan(
            "america",
            {
                "filter": [{"left": "name", "operation": "in_range", "right": list(tv_names)}],
                "columns": ["name", "close", "change"],
                "range": [0, 1000],
            },
        )
        for r in rows:
            name, close, chg = (r.get("d") or [None, None, None])[:3]
            key = tv_names.get(name)
            if key and key not in out and (v := _row(close, chg)):
                out[key] = v
    except Exception as e:  # noqa: BLE001
        print(f"uyarı: tv america: {e}", file=sys.stderr)
    idx = {
        "BIST:XU100": "XU100.IS",
        "BIST:XU030": "XU030.IS",
        "SP:SPX": "^GSPC",
        "NASDAQ:IXIC": "^IXIC",
        "DJ:DJI": "^DJI",
        "TVC:UKOIL": "BZ=F",
        "ICEEUR:BRN1!": "BZ=F",
        "NYMEX:BZ1!": "BZ=F",
        "COMEX:GC1!": "GC=F",
        "COMEX:SI1!": "SI=F",
        "NYMEX:PL1!": "PL=F",
        "NYMEX:PA1!": "PA=F",
    }
    try:
        rows = tv_scan("global", {"symbols": {"tickers": list(idx)}, "columns": ["close", "change"]})
        for r in rows:
            key = idx.get(r.get("s"))
            close, chg = (r.get("d") or [None, None])[:2]
            if key and key not in out and (v := _row(close, chg)):
                out[key] = v
    except Exception as e:  # noqa: BLE001
        print(f"uyarı: tv global: {e}", file=sys.stderr)
    return out


def main() -> int:
    with open(os.path.join(HERE, "bist.json"), encoding="utf-8") as f:
        bist = [c + ".IS" for c in json.load(f)]
    quotes = tradingview(bist)
    # Eksik kalanlar için Yahoo (bulut sunucularından çoğu zaman kapalı; yalnızca yedek)
    missing = [x for x in INDEX + US + bist if x not in quotes]
    if missing and len(quotes) < 300:
        session()
        quotes.update({k: v for k, v in spark(missing).items() if k not in quotes})
    print(f"{len(quotes)} fiyat (BIST {sum(1 for k in quotes if k.endswith('.IS'))})")
    # Kaynak kapalıysa eski dosyayı bozma: çok az fiyat geldiyse yazma
    if len(quotes) < 100:
        print("hata: çok az fiyat geldi, dosya güncellenmedi", file=sys.stderr)
        return 1
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"t": int(time.time()), "q": quotes}, f, separators=(",", ":"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
