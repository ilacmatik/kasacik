#!/usr/bin/env python3
"""
Kasacık veri sunucusu: borsa fiyatlarını günde birkaç kez tek dosyada toplar (piyasa.json).

Telefonlar başka sitelere gitmez; uygulama gecikmeli/gün sonu fiyatı bu dosyadan okur.
Yalnızca Python standart kütüphanesi. GitHub Actions'ta (herkese açık depo → ücretsiz) çalışır.

Çıktı: {"t": <epoch sn>, "q": {"THYAO.IS": [fiyat, önceki_kapanış], "AAPL": [...], "^GSPC": [...]}}
"""
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


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def spark(symbols: list) -> dict:
    """20'şerli: sembol → [son fiyat, önceki kapanış]."""
    out = {}
    for i in range(0, len(symbols), 20):
        chunk = symbols[i : i + 20]
        q = ",".join(urllib.parse.quote(s) for s in chunk)
        for host in ("query2", "query1"):
            try:
                data = get(f"https://{host}.finance.yahoo.com/v8/finance/spark?symbols={q}&range=1d&interval=1d")
                break
            except Exception as e:  # noqa: BLE001
                data = None
                print(f"uyarı: {host} {chunk[0]}…: {e}", file=sys.stderr)
                time.sleep(2)
        if not data:
            continue
        for s in chunk:
            e = data.get(s) or {}
            closes = [c for c in (e.get("close") or []) if isinstance(c, (int, float)) and c > 0]
            if not closes:
                continue
            prev = e.get("chartPreviousClose")
            prev = prev if isinstance(prev, (int, float)) and prev > 0 else None
            out[s] = [round(closes[-1], 6), round(prev, 6) if prev else None]
        time.sleep(0.4)
    return out


def main() -> int:
    with open(os.path.join(HERE, "bist.json"), encoding="utf-8") as f:
        bist = [c + ".IS" for c in json.load(f)]
    quotes = {}
    quotes.update(spark(INDEX))
    quotes.update(spark(US))
    quotes.update(spark(bist))
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
