#!/usr/bin/env python3
"""
piyasa.py'yi seans boyunca aralıklarla çalıştırıp piyasa.json'u yayınlar.

GitHub'ın zamanlanmış işleri sık aralıklarda saatlerce gecikebiliyor ya da hiç çalışmıyor
(3 Kasım'da BIST seansında 15 dakikada bir yerine tek çalışma oldu). Bu yüzden iş birkaç kez
tetiklenir ve her tetiklenişte en çok ~5 saat 45 dakika boyunca kendi içinde döner:
  - BIST seansı (TR 09:55–18:20, UTC 06:55–15:20): 15 dakikada bir
  - ABD seansı ve kapanış (UTC 21:15'e kadar): saatte bir (:31)
"""
import datetime as dt
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
LIMIT = 5 * 3600 + 45 * 60
END_UTC = dt.time(21, 15)


def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=ROOT)


def publish() -> None:
    if run([sys.executable, os.path.join(HERE, "piyasa.py")]) != 0:
        print("uyarı: piyasa.py hata verdi, sonraki turda yeniden denenecek", flush=True)
        return
    if subprocess.call(["git", "diff", "--quiet", "--", "piyasa.json"], cwd=ROOT) == 0:
        print("Değişiklik yok.", flush=True)
        return
    run(["git", "add", "piyasa.json"])
    run(["git", "commit", "-q", "-m", "piyasa.json güncellendi"])
    for _ in range(3):
        if run(["git", "pull", "-q", "--rebase", "origin", "main"]) == 0 and run(["git", "push", "-q"]) == 0:
            return
        time.sleep(10)
    print("uyarı: gönderilemedi", flush=True)


def next_slot(now: dt.datetime) -> dt.datetime:
    t = now.time()
    if dt.time(6, 55) <= t < dt.time(15, 20):
        m = (now.minute // 15 + 1) * 15
        base = now.replace(minute=0, second=30, microsecond=0)
        return base + dt.timedelta(minutes=m)
    # Seans dışı: saat başı :31 (açılıştan önceyse açılışta)
    cand = now.replace(minute=31, second=0, microsecond=0)
    cand = cand if cand > now else cand + dt.timedelta(hours=1)
    opening = now.replace(hour=7, minute=0, second=30, microsecond=0)
    return opening if now < opening < cand else cand


def main() -> None:
    start = time.time()
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        if now.time() > END_UTC or now.weekday() >= 5:
            print("Günün penceresi bitti.", flush=True)
            return
        publish()
        nxt = next_slot(dt.datetime.now(dt.timezone.utc))
        wait = (nxt - dt.datetime.now(dt.timezone.utc)).total_seconds()
        if time.time() - start + wait > LIMIT or nxt.time() > END_UTC:
            print("Bu turun süresi doldu; sonraki tetikleme devam ettirir.", flush=True)
            return
        print(f"Sonraki: {nxt:%H:%M} UTC ({wait / 60:.0f} dk)", flush=True)
        time.sleep(max(0, wait))


if __name__ == "__main__":
    main()
