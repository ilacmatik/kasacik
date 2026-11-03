# Kasacık · veri ve web

[Kasacık](https://ilacmatik.github.io/kasacik/) bütçe uygulamasının herkese açık veri sunucusu ve web sayfaları.

## Web sayfaları (GitHub Pages)
- [Gizlilik politikası](https://ilacmatik.github.io/kasacik/gizlilik.html)
- [Hesap ve veri silme](https://ilacmatik.github.io/kasacik/hesap-silme.html)
- [Yasal uyarı](https://ilacmatik.github.io/kasacik/yasal-uyari.html)

## Veri dosyaları
Uygulama bu dosyaları okur; telefonlar fiyat sitelerine doğrudan gitmez.

| Dosya | İçerik | Güncelleme |
|---|---|---|
| `piyasa.json` | Borsa İstanbul (BIST 100) ve ABD hisseleri, endeksler, gümüş, fon listesi (gecikmeli) | Borsa saatlerinde 15 dakikada bir, ABD seansında saatte bir (hafta içi) |
| `veri.json` | Enflasyon (TÜİK, ENAG) ve uygulamadaki oranlar | ENAG: her ayın 3–6'sı, günde üç kez denenir |
| `quiz.json` | Bilgi Kesesi soru bankası (`scripts/quiz_src.py` → `python3 scripts/quiz_src.py > quiz.json`) | Yeni soru paketi eklendikçe |

Güncellemeler `.github/workflows/` içindeki zamanlanmış işlerle yapılır (`piyasa.yml`, `enag.yml`).

Fiyatlar bilgi amaçlıdır ve gecikmelidir; yatırım tavsiyesi değildir.
