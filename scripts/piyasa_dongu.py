#!/usr/bin/env python3
"""
piyasa.py'yi seans boyunca aralıklarla çalıştırıp piyasa.json'u yayınlar.

GitHub'ın zamanlanmış işleri saatlerce gecikebiliyor ya da hiç çalışmıyor (3–4 Kasım'da
seansın bir kısmı kaçtı). Bu yüzden iş bir zincir gibi çalışır: her tur en çok ~5 sa 45 dk
döner, süresi dolunca kendini yeniden başlatır (.devam → iş akışındaki "Devam ettir" adımı).
Gece ve hafta sonu fiyat çekmeden bekler; böylece ertesi sabah açılış zamanlayıcıya kalmaz.
Zamanlanmış tetiklemeler yalnızca zincir koparsa yeniden başlatmak için.

  - BIST seansı (TR 10:00–18:20, UTC 07:00–15:20): 15 dakikada bir
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
OPEN_UTC = dt.time(7, 0, 30)
SESSION_END_UTC = dt.time(15, 20)
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


def next_open(now: dt.datetime) -> dt.datetime:
    """Bir sonraki hafta içi açılış (UTC 07:00:30)."""
    d = now.date()
    cand = dt.datetime.combine(d, OPEN_UTC, tzinfo=dt.timezone.utc)
    if cand <= now:
        d += dt.timedelta(days=1)
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    return dt.datetime.combine(d, OPEN_UTC, tzinfo=dt.timezone.utc)


def next_slot(now: dt.datetime) -> dt.datetime:
    t = now.time()
    if now.weekday() < 5:
        if t < OPEN_UTC:
            return next_open(now)
        if t < SESSION_END_UTC:
            base = now.replace(minute=0, second=30, microsecond=0)
            return base + dt.timedelta(minutes=(now.minute // 15 + 1) * 15)
        cand = now.replace(minute=31, second=0, microsecond=0)
        cand = cand if cand > now else cand + dt.timedelta(hours=1)
        if cand.time() <= END_UTC and cand.date() == now.date():
            return cand
    return next_open(now)


def in_window(now: dt.datetime) -> bool:
    return now.weekday() < 5 and dt.time(6, 55) <= now.time() <= END_UTC


def main() -> None:
    start = time.time()
    if in_window(dt.datetime.now(dt.timezone.utc)):
        publish()
    while True:
        now = dt.datetime.now(dt.timezone.utc)
        nxt = next_slot(now)
        wait = (nxt - now).total_seconds()
        left = LIMIT - (time.time() - start)
        if wait > left:
            # Süre dolmadan bekle, sonra zinciri devam ettir
            time.sleep(max(0, left - 30))
            print(f"Tur süresi doldu; yeni tur başlatılacak (sonraki çekim {nxt:%a %H:%M} UTC).", flush=True)
            open(os.path.join(ROOT, ".devam"), "w").close()
            return
        print(f"Sonraki: {nxt:%a %H:%M} UTC ({wait / 60:.0f} dk)", flush=True)
        time.sleep(max(0, wait))
        publish()


if __name__ == "__main__":
    main()
