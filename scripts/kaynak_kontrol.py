#!/usr/bin/env python3
"""Uygulamanın kullandığı veri kaynaklarına ulaşılıyor mu? (teşhis; Actions → "Kaynak kontrolü")"""
import json, time, urllib.request

UA = "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/126 Mobile Safari/537.36"
URLS = {
    "piyasa.json (bizim)": "https://ilacmatik.github.io/kasacik/piyasa.json",
    "veri.json (bizim)": "https://ilacmatik.github.io/kasacik/veri.json",
    "quiz.json (bizim)": "https://ilacmatik.github.io/kasacik/quiz.json",
    "ForexFactory haftalık": "https://nfs.faireconomy.media/ff_calendar_thisweek.json",
    "TCMB PPK": "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi/PPK/2026",
    "TCMB 1 hafta repo": "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi/Merkez+Bankasi+Faiz+Oranlari/1+Hafta+Repo",
    "Binance USDTTRY": "https://api.binance.com/api/v3/ticker/price?symbol=USDTTRY",
    "Binance vision PAXG": "https://data-api.binance.vision/api/v3/ticker/price?symbol=PAXGUSDT",
    "CoinGecko": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try",
    "Truncgil": "https://finans.truncgil.com/v4/today.json",
    "Yahoo THYAO": "https://query1.finance.yahoo.com/v8/finance/chart/THYAO.IS?range=1d&interval=5m",
    "Frankfurter": "https://api.frankfurter.app/latest?from=GBP&to=TRY",
    "TEFAS": "https://www.tefas.gov.tr/api/DB/BindHistoryInfo",
}
for name, url in URLS.items():
    t = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read()
            code = r.status
    except Exception as e:  # noqa: BLE001
        code, body = getattr(e, "code", "HATA"), str(e).encode()
    ms = int((time.time() - t) * 1000)
    head = body[:160].decode("utf-8", "replace").replace("\n", " ")
    extra = ""
    if name.startswith("piyasa") and code == 200:
        d = json.loads(body); age = (time.time() - d["t"]) / 60
        extra = f" · {len(d['q'])} fiyat · {age:.0f} dk önce · THYAO={d['q'].get('THYAO.IS')} XU100={d['q'].get('XU100.IS')}"
    if name.startswith("ForexFactory") and code == 200:
        try:
            a = json.loads(body); keys = sorted(a[0].keys()) if a else []
            extra = f" · {len(a)} olay · alanlar={keys} · {a[0]['date'] if a else ''}→{a[-1]['date'] if a else ''}"
        except Exception as e:  # noqa: BLE001
            extra = f" · JSON değil ({e})"
    print(f"{name:24} {code} {ms:5} ms {len(body):7} B{extra}\n    {head}")
