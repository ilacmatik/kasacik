# Kasacık "Günün Yarışması" soru kaynağı. quiz.json bu dosyadan üretilir:
#   python3 scripts/quiz_src.py > quiz.json
# Kurallar: her soru doğrulanmış bir bilgiye dayanır (kaynak alanı), kimseyi aşağılamaz; din, siyaset,
# etnik köken ve tartışmalı konulara girilmez. Her gün 5 soru (kolaydan zora) sırayla gelir.
# Alanlar: c=kategori, d=zorluk 1-5, q=soru, o=şıklar, a=doğru şık, x=açıklama, s=kaynak,
#          h=Kesecik'in ipucu (joker), k=Akçe'nin esprisi, y=yıl (zaman yolculuğu haritası), t=kart adı
import json
import sys

Q = []


def q(c, d, soru, o, a, x, s, h, k, y=None, t=None):
    Q.append({"c": c, "d": d, "q": soru, "o": o, "a": a, "x": x, "s": s, "h": h, "k": k, **({"y": y, "t": t} if y is not None else {})})


NIS = "Nişanyan Sözlük"
TDK = "TDK Güncel Türkçe Sözlük"
TCMB = "TCMB"
DAR = "Darphane"
BRIT = "Britannica"
PAM = "Ş. Pamuk, Osmanlı İmparatorluğu'nun Parasal Tarihi"
PAK = "M. Z. Pakalın, Osmanlı Tarih Deyimleri"

# ---- Gün 1
q("kelime", 1, "Cebimizdeki \"kuruş\" kelimesi aslında hangi dilden geldi?", ["Arapça", "Almanca", "Farsça", "Rumca"], 1,
  "Avrupa'nın gümüş parası Groschen (\"kalın para\") Osmanlı'ya guruş olarak girdi, zamanla kuruş oldu. Bozuk para dediğimiz şey aslında \"kalın\" paraymış!",
  NIS, "Avrupa'nın ortasında basılan bir gümüş paranın adından geliyor.", "Kalın para mı? Benim kesem hep ince 😅")
q("tarih", 2, "Osmanlı'nın ilk gümüş parası \"akçe\" ne demek?", ["Küçük altın", "Beyazımsı", "Kral parası", "Yuvarlak"], 1,
  "Akçe, \"ak\" (beyaz) + \"-çe\" ekinden gelir: beyazımsı. Gümüşün parlak rengi yüzünden bu adı aldı. Orhan Gazi döneminde basılmaya başlandı.",
  PAM, "Rengiyle ilgili. Gümüş ne renktir?", "Adımı söylediniz, buradayım! ✨", -1, None)
q("altin", 2, "Çeyrek altın kaç gramdır?", ["1 gram", "1,75 gram", "2,5 gram", "3,5 gram"], 1,
  "Çeyrek altın 22 ayar ve 1,75 gramdır. Yarım 3,5, tam (ziynet) altın ise 7 gramdır: adı gibi tamın dörtte biri.",
  DAR, "Tam altın 7 gram. Çeyreği kaç eder?", "Düğünde takılınca hepsi ağır gelir ama 😄")
q("deyim", 3, "\"Kesenin ağzını açmak\" ne demektir?", ["Sır vermek", "Cömertçe harcamaya başlamak", "Borç istemek", "Kavga başlatmak"], 1,
  "Eskiden para, ağzı iple bağlanan keselerde taşınırdı. Keseyi açmak, parayı harcamaya başlamak demekti; bugün cömert davranmak için kullanılır.",
  TDK, "Kese nedir, içinde ne vardır?", "Bizimki bu deyimi hiç kullanmaz, kesesi hep sıkı 🙈")
q("tarih", 4, "Osmanlı'da büyük ödemeler sayılmaz, \"kese\" ile yapılırdı. Bir kese kaç kuruştu?", ["50 kuruş", "100 kuruş", "500 kuruş", "1.000 kuruş"], 2,
  "Büyük tutarlar tek tek sayılmaz, mühürlü keselerle hesaplanırdı: 1 kese = 500 kuruş. Kesecik de adını bu keseden alıyor.",
  PAK, "Yüzlerce kuruş eder, ama bin değil.", "Kesecik'in adı buradan; evde her gün anlatıyor zaten 😌")

# ---- Gün 2
q("kelime", 1, "\"Banka\" kelimesi aslında neyi anlatıyordu?", ["Kasa", "Tezgâh, sıra", "Kale", "Defter"], 1,
  "İtalyan sarraflar paralarını bir tezgâhın (banco/banca) üstünde bozardı. \"Banka\" kelimesi bu tezgâhtan gelir.",
  NIS, "Sarrafın önünde duran bir mobilya.", "Yani ilk bankalar bir masaydı, ben de bir masa açayım 🪑")
q("kelime", 2, "\"Bankrupt\" (iflas) kelimesinin asıl anlamı nedir?", ["Kırık tezgâh", "Boş kasa", "Kayıp anahtar", "Yanmış defter"], 0,
  "Borcunu ödeyemeyen sarrafın tezgâhı kırılırdı: banca rotta. İngilizcedeki bankrupt buradan gelir.",
  BRIT, "Bir önceki sorudaki tezgâha ne olmuş olabilir?", "Tezgâhımı kırmasınlar, borcum yok! 🙅‍♀️")
q("kelime", 2, "\"Maaş\" kelimesinin kökü ne anlama gelir?", ["Ödül", "Geçim, yaşam", "Altın", "Emek"], 1,
  "Maaş, Arapça \"yaşamak\" kökünden gelir ve \"geçimlik\" demektir. Maaş tam da geçinmek için verilen paradır.",
  NIS, "Ayın sonunu getirmek için ne lazım?", "Ay sonuna kadar yaşatan şey, çok doğru 😄")
q("kelime", 3, "İngilizcedeki \"salary\" (maaş) kelimesi hangi kelimeden türemiştir?", ["Altın", "Tuz", "Buğday", "Gümüş"], 1,
  "Latince salarium, sal (tuz) kelimesinden türemiştir. Tuz, eski dünyada çok değerli bir maldı.",
  BRIT, "Yemeğe atılan bir şey.", "Maaşım tuzlu olsun da az olmasın 🧂")
q("dunya", 4, "\"Dolar\" adı nereden geliyor?", ["Bir Amerikan şehrinden", "Bir Çek vadisindeki gümüş madeninden", "İspanyol kralından", "Hollanda'daki bir kanaldan"], 1,
  "Bohemya'daki Joachimsthal (bugün Çekya) vadisinde basılan gümüş paralara thaler denirdi. Thaler zamanla dolar oldu.",
  BRIT, "Avrupa'nın ortasında bir vadi ve gümüş madeni.", "Dolar Amerikalı değilmiş, şok! 😮")

# ---- Gün 3
q("kelime", 1, "\"Kasa\" kelimesi hangi dilden gelir?", ["İtalyanca", "Arapça", "Rusça", "Japonca"], 0,
  "İtalyanca cassa \"kutu, sandık\" demektir. Kasacık'ın adı da buradan: küçük kasa.",
  NIS, "Bankacılığın ilk dili gibi düşün.", "Kasacık da küçük kasa demek, aile işi 😉")
q("kelime", 2, "\"Bütçe\" kelimesinin aslı neydi?", ["Küçük kese, çanta", "Hesap defteri", "Kral hazinesi", "Maaş listesi"], 0,
  "Fransızca budget, eski Fransızca bougette \"küçük kese, çanta\" kelimesinden gelir. Bütçe aslında küçük bir kesedir!",
  BRIT, "Bizim ailenin adını düşün.", "Kese her yerde, gurur duyuyorum 👜")
q("deyim", 2, "\"Ak akçe kara gün içindir\" atasözü ne öğütler?", ["Gümüşü sakla", "Zor günler için birikim yap", "Parayı hemen harca", "Borç ver"], 1,
  "Ak akçe yani temiz para, kara gün yani zor zamanlar içindir. Kısacası: birikim yap.",
  TDK, "Kara gün ne demek?", "Benim adım geçiyor, kesin bilge bir söz 😎")
q("kelime", 3, "\"Borsa\" kelimesi İtalyancada başka ne anlama gelir?", ["Kese, para çantası", "Pazar yeri", "Teraziler", "Liman"], 0,
  "İtalyanca borsa \"kese\" demektir. Belçika'nın Brugge kentinde tüccarların buluştuğu Van der Beurse hanı da borsanın adının kaynağı sayılır.",
  NIS, "Yine bir para taşıma aracı.", "Kese, borsa, bütçe... Kesecik her yerde, evde de 🙄")
q("tarih", 4, "Bilinen ilk madeni paralar nerede basıldı?", ["Mısır", "Lidya (Anadolu)", "Roma", "Çin"], 1,
  "MÖ 7. yüzyılda Anadolu'daki Lidya'da, altın-gümüş karışımı elektrumdan ilk madeni paralar basıldı. Yani para bu topraklarda doğdu.",
  BRIT, "Cevap bizim topraklarda, Batı Anadolu'da.", "Paranın memleketi Anadolu, ne güzel 🥰", -630, "Lidya Sikkesi")

# ---- Gün 4
q("altin", 1, "Saf altın kaç ayardır?", ["14", "18", "22", "24"], 3,
  "Ayar, 24 parça içinde kaç parçanın altın olduğunu gösterir. 24 ayar saf altındır; 22 ayarda 24 parçanın 22'si altındır.",
  DAR, "En büyük sayı.", "Ben 24 ayar, Kesecik 22. Şaka şaka, ikimiz de altın gibiyiz 💛")
q("altin", 2, "Altın fiyatlarında kullanılan \"ons\" kaç gramdır?", ["10 gram", "28,35 gram", "31,10 gram", "50 gram"], 2,
  "Değerli madenlerde kullanılan troy ons 31,1035 gramdır. Mutfaktaki ons (28,35 g) ile karıştırılmamalı!",
  BRIT, "30'dan biraz fazla.", "Mutfak onsu başka, kuyumcu onsu başka. Kafam karıştı 😵")
q("deyim", 2, "\"Damlaya damlaya göl olur\" ne anlatır?", ["Su israf edilmemeli", "Küçük birikimler zamanla büyür", "Yağmur bereket getirir", "Sabırsız olma"], 1,
  "Küçük ama düzenli birikimler zamanla büyük bir varlığa dönüşür. Kasacık'ın da en sevdiği söz.",
  TDK, "Damlalar ne olur?", "Ben de her gün bir sikke atıyorum keseye 🪙")
q("tarih", 3, "Osmanlı'da 1 kuruş kaç \"para\" ederdi?", ["10", "20", "40", "100"], 2,
  "Osmanlı'da para birimi küçük gümüş paraydı ve 40 para 1 kuruş ederdi. \"Beş para etmez\" deyimindeki para da budur.",
  PAM, "Yirmiden büyük, yüzden küçük.", "Beş para etmez demek ki çok az demekmiş 🤏")
q("kelime", 4, "\"İflas\" kelimesinin kökündeki \"fels\" neydi?", ["Küçük bakır para", "Banka defteri", "Altın külçe", "Ticaret gemisi"], 0,
  "Fels, küçük bakır paraydı. İflas, \"elinde tek bir fels bile kalmamak\" yani beş parasız kalmak demektir.",
  NIS, "Bir para türü, hem de en değersizi.", "Bir fels bile yok mu? Kesemi kontrol ediyorum 👀")

# ---- Gün 5
q("deyim", 1, "\"Ayağını yorganına göre uzat\" neyi öğütler?", ["Erken yat", "Gelirine göre harca", "Yorgan al", "Spor yap"], 1,
  "Yorgan gelirdir, ayak harcamalar. Harcamalarını gelirini aşmayacak şekilde ayarla demektir: bütçenin özü.",
  TDK, "Yorgan neyi temsil ediyor olabilir?", "Benim yorganım kısa, kıvrılıp yatıyorum 😄")
q("kelime", 2, "\"Kredi\" kelimesinin Latince kökü ne demek?", ["Ödemek", "İnanmak, güvenmek", "Ödünç", "Faiz"], 1,
  "Credere \"inanmak\" demektir. Kredi, birinin sana güvenmesidir; o yüzden zamanında ödemek önemli.",
  BRIT, "Kredi verilen kişiye ne duyulur?", "Bana güvenin, yarın öderim 🤞")
q("kelime", 2, "\"Para\" kelimesi Farsçada ne anlama gelir?", ["Altın", "Parça", "Değer", "Para kesesi"], 1,
  "Farsça pāre \"parça\" demektir. Osmanlı'da küçük gümüş paranın adı oldu, sonra tüm paralara verildi.",
  NIS, "Bir bütünün bölümü.", "Paramparça olmasın da 😅")
q("dunya", 3, "Euro banknotlarındaki köprü ve kapılar hangi ülkede?", ["Fransa", "Almanya", "Hiçbiri, hayalidir", "İtalya"], 2,
  "Euro banknotlarındaki köprüler ve kapılar gerçek yapılar değildir; hiçbir ülke kayırılmasın diye hayali çizildi.",
  "Avrupa Merkez Bankası", "Ortak para; kimse küsmesin diye düşünülmüş.", "Hayali köprüden geçelim mi? 🌉")
q("tarih", 4, "Osmanlı'nın ilk kâğıt parası \"kaime\" ilk kez hangi yıl çıktı?", ["1789", "1840", "1876", "1914"], 1,
  "Kaime ilk kez 1840'ta, Sultan Abdülmecid döneminde çıkarıldı. İlk kaimeler elle yazılıp mühürlenirdi.",
  PAM, "Tanzimat yıllarına yakın.", "El yazısıyla para! Benim imzam da güzel ✍️", 1840, "İlk Kaime")

# ---- Gün 6
q("kelime", 1, "\"Taksit\" kelimesi ne demektir?", ["Faiz", "Paylara bölme", "Gecikme", "Kart"], 1,
  "Arapça kökenli taksit \"paylara bölme\" demektir. Borcu parça parça ödemek.",
  NIS, "Bütünü parçalara ayırmak.", "Benim çikolata da taksitle bitiyor 🍫")
q("kelime", 2, "\"Nakit\" kelimesinin asıl anlamı nedir?", ["Sayılmış, peşin para", "Banka parası", "Bozuk para", "Kredi"], 0,
  "Nakit, Arapça \"sayılmış, ayıklanmış para\" demektir; yani o an elde olan, peşin para.",
  NIS, "Elle tutulur, hemen ödenir.", "Nakit en iyisi, kart beni korkutuyor 😬")
q("tarih", 2, "Mecidiye altını hangi padişah döneminde basıldı?", ["Fatih Sultan Mehmed", "Kanuni", "Abdülmecid", "II. Abdülhamid"], 2,
  "1844'teki para reformuyla Abdülmecid döneminde basıldı ve adını ondan aldı. 100 kuruş değerindeydi.",
  PAM, "Altının adında padişahın adı gizli.", "Adından belli zaten, kolay soru 😏", 1844, "Mecidiye Altını")
q("dunya", 3, "Pound (sterlin) adı aslında neyi anlatıyordu?", ["Bir şehri", "Bir ağırlık birimini", "Bir kralı", "Bir nehri"], 1,
  "Pound bir ağırlık birimidir; ilk başta bir pound gümüş anlamına geliyordu. £ işareti de Latince libra (terazi, ağırlık) kelimesinden gelir.",
  BRIT, "Manavda da kullanılır.", "Paranın kilosu mu olur? Olurmuş 🏋️‍♀️")
q("kelime", 4, "Roma'da para anlamına gelen \"pecunia\" hangi kelimeden türedi?", ["Sığır", "Altın", "Tahıl", "Taş"], 0,
  "Pecunia, sürü hayvanı anlamındaki pecus kelimesinden gelir. Paradan önce değer, hayvan sürüsüyle ölçülürdü.",
  BRIT, "Eskiden zenginlik çiftlikte ölçülürdü.", "Keseye inek sığmaz ama 🐄")

# ---- Gün 7
q("deyim", 1, "\"Eli sıkı\" biri nasıldır?", ["Güçlü", "Para harcamayı sevmeyen", "Çalışkan", "Sinirli"], 1,
  "Eli sıkı, parasını kolay kolay harcamayan, tutumlu, bazen de cimri kişi demektir.",
  TDK, "Eli sıkı olan parayı bırakır mı?", "Kesecik! Tam olarak Kesecik 😂")
q("kelime", 2, "\"Sermaye\" kelimesi Farsçada ne demektir?", ["Baş mal, ana mal", "Hazine", "Altın", "Gelir"], 0,
  "Ser \"baş\", maye \"mal, maya\" demektir. İşin başındaki ana mal: sermaye.",
  NIS, "Her şeyin başındaki maya.", "Benim sermayem bu tatlı gülüşüm 😁")
q("tarih", 2, "Yeni Türk Lirası'nda (YTL) kaç sıfır atıldı?", ["3", "4", "6", "9"], 2,
  "1 Ocak 2005'te 6 sıfır atıldı: 1.000.000 TL, 1 YTL oldu.",
  TCMB, "Bir milyon eski lira, bir yeni lira oldu.", "Milyoner olmak kolaymış eskiden 😄", 2005, "Yeni Türk Lirası")
q("kelime", 3, "\"Peşin\" kelimesinin kökü ne demektir?", ["Ön, önde", "Tam", "Altın", "Hızlı"], 0,
  "Farsça pīş \"ön\" demektir. Peşin, malı almadan önce ödenen paradır.",
  NIS, "Arka değil...", "Peşin peşin söyleyeyim, bunu biliyordum 😎")
q("dunya", 4, "Bilinen ilk kâğıt para nerede kullanıldı?", ["Venedik", "Çin", "Mısır", "Hindistan"], 1,
  "11. yüzyılda Çin'de, Song Hanedanı döneminde jiaozi adlı kâğıt paralar kullanıldı. Ağır demir paraları taşımak zordu.",
  BRIT, "Kâğıdın da icat edildiği ülke.", "Kâğıt varsa para da olur, mantıklı 📜", 1024, "Jiaozi")

# ---- Gün 8
q("deyim", 1, "\"Borç yiğidin kamçısıdır\" ne demek?", ["Borç kötüdür", "Borç insanı daha çok çalışmaya iter", "Yiğitler borç almaz", "Borç at alır"], 1,
  "Borç, insanı daha çok çalışmaya ve ödemeye zorlar, tıpkı atı koşturan kamçı gibi.",
  TDK, "Kamçı ne işe yarar?", "Bende kamçı yok, sadece kese var 😌")
q("kelime", 2, "\"Mevduat\" kelimesi ne anlama gelir?", ["Emanet edilenler", "Faizler", "Hesaplar", "Kazançlar"], 0,
  "Arapça vedia \"emanet\" kökünden gelir. Bankaya yatırılan para, bankaya emanet edilen paradır.",
  NIS, "Bir şeyi birine güvenip bırakmak.", "Paramı Kesecik'e emanet ederim, kuruşu kuruşuna saklar 😌")
q("altin", 2, "Cumhuriyet altını (ata lira) kaç gramdır?", ["5 gram", "6,5 gram", "7,216 gram", "8 gram"], 2,
  "Cumhuriyet altını 22 ayar ve 7,216 gramdır; tam (ziynet) altından biraz ağırdır.",
  DAR, "Tam altından biraz ağır.", "Küsuratlı ağırlık, kuyumcu işi 🤓")
q("kelime", 3, "\"Kalpazan\" (sahte para basan) kelimesindeki \"kalp\" ne anlama gelir?", ["Yürek", "Sahte, değiştirilmiş", "Kalıp", "Gizli"], 1,
  "Buradaki kalp, Arapça \"değiştirme, bozma\" kökünden gelir ve \"sahte\" demektir; yürekle ilgisi yok.",
  NIS, "Kalbe değil, sahteciliğe bak.", "Kalbimi çalan yok, paramı da çalamaz 💔")
q("tarih", 4, "Osmanlı Bankası (Bank-ı Osmani) hangi yıl kuruldu?", ["1838", "1863", "1888", "1923"], 1,
  "Osmanlı Bankası 1863'te kuruldu ve uzun yıllar kâğıt para basma yetkisini elinde tuttu.",
  PAM, "Kaimeden sonra, Cumhuriyet'ten önce.", "Bankaların dedesi 👴", 1863, "Osmanlı Bankası")

# ---- Gün 9
q("kelime", 1, "\"Vergi\" kelimesi hangi fiilden gelir?", ["Varmak", "Vermek", "Vurmak", "Vazgeçmek"], 1,
  "Vergi, öz Türkçe \"vermek\" fiilinden türemiştir: verilen şey.",
  TDK, "Vergiyi ne yaparız?", "Vergi vermek, adı üstünde 🧾")
q("kelime", 2, "\"Çarşı\" kelimesinin Farsçadaki anlamı nedir?", ["Dört yön, dört yol", "Pazar yeri", "Kapalı yer", "Kalabalık"], 0,
  "Farsça çār-sū \"dört yön\" demektir. Çarşılar çoğunlukla dört yolun birleştiği yerde kurulurdu.",
  NIS, "Bir sayı ve yön.", "Dört yol ağzında kaybolurum ben 😵‍💫")
q("tarih", 2, "İstanbul Kapalıçarşı'nın yapımı hangi padişah döneminde başladı?", ["Fatih Sultan Mehmed", "Yavuz Sultan Selim", "Kanuni", "IV. Murad"], 0,
  "Kapalıçarşı'nın çekirdeği olan bedesten Fatih Sultan Mehmed döneminde, 1460'larda yapıldı ve zamanla büyüdü.",
  "İstanbul Ansiklopedisi", "İstanbul'u alan padişah.", "Alışverişin sultanı kim? 🛍️", 1461, "Kapalıçarşı")
q("kelime", 3, "\"Bedesten\" kelimesi aslında ne demek?", ["Kumaşçılar çarşısı", "Altın deposu", "Kervansaray", "Kale"], 0,
  "Bedesten, Farsça bezzāzistān yani bez (kumaş) satılan yer demektir. Sonra değerli malların satıldığı kapalı çarşı oldu.",
  NIS, "İçinde \"bez\" geçiyor.", "Bez alırım, kese dikerim 🧵")
q("dunya", 4, "Mikronezya'daki Yap adasında para olarak ne kullanılırdı?", ["Deniz kabukları", "Dev taş diskler", "Balık", "Tuz"], 1,
  "Yap adasında \"rai\" denen, ortası delik dev taş diskler para olarak kullanılırdı. Bazıları o kadar büyüktü ki yerinden hiç oynatılmazdı.",
  BRIT, "Cebe sığmayacak kadar büyük ve ağır.", "Kesem taş taşıyamaz, pas geçiyorum 🪨")

# ---- Gün 10
q("deyim", 1, "\"Kuruşu kuruşuna\" ne demek?", ["Eksiksiz, tam olarak", "Çok az", "Bozuk parayla", "Hızlıca"], 0,
  "Bir hesabı kuruşu kuruşuna ödemek, tek kuruş eksik bırakmadan tam ödemek demektir.",
  TDK, "Hiç eksik yok.", "Kasacık da kuruşu kuruşuna hesaplar 🧮")
q("kelime", 2, "\"Sarraf\" kimdir?", ["Para bozan, değiştiren", "Terzi", "Gemici", "Yazıcı"], 0,
  "Sarraf, para bozan ve değiştiren, altın alıp satan kişidir. Arapça \"değiştirmek\" kökünden gelir.",
  NIS, "Döviz bürosu gibi düşün.", "Benim gibi gümüşü sever 🪙")
q("tarih", 2, "Türkiye Cumhuriyet Merkez Bankası hangi yıl faaliyete başladı?", ["1923", "1927", "1931", "1950"], 2,
  "Kanunu 1930'da çıktı, banka 1931'de çalışmaya başladı.",
  TCMB, "1930'ların hemen başı.", "Merkez Bankası da benim kadar ciddi 😤", 1931, "Merkez Bankası")
q("kelime", 3, "\"Kambiyo\" kelimesi İtalyancada ne demek?", ["Değişim, takas", "Kâr", "Liman", "Kasa"], 0,
  "İtalyanca cambio \"değiştirme\" demektir. Kambiyo, dövizlerin birbirine çevrilmesidir.",
  NIS, "Döviz bürosunda ne yaparsın?", "Kesecik'le hediyeleri değişiriz, buna ev içi kambiyo diyoruz 😄")
q("altin", 4, "Altının kimyasal simgesi \"Au\" hangi kelimeden gelir?", ["Aurum (Latince)", "Altun", "Aura", "Austria"], 0,
  "Au, Latince aurum kelimesinden gelir; \"parlak şafak\" anlamıyla ilişkilendirilir.",
  BRIT, "Romalıların dili.", "Kimya dersinde altın notu bende 🥇")

# ---- Gün 11
q("kelime", 1, "\"Zam\" kelimesi ne demektir?", ["Ekleme, katma", "Kesinti", "Ödeme", "İndirim"], 0,
  "Zam, Arapça \"ekleme, katma\" demektir. Fiyata eklenen tutar.",
  NIS, "İndirimin tersi.", "Zam lafını duymak bile istemiyorum 🙉")
q("kelime", 2, "\"Tahvil\" kelimesinin anlamı nedir?", ["Çevirme, dönüştürme", "Borç", "Kazanç", "Mektup"], 0,
  "Tahvil, Arapça \"çevirme, dönüştürme\" demektir. Borç senedi zamanı gelince paraya dönüştüğü için bu adı alır.",
  NIS, "Bir şeyi başka bir şeye çevirmek.", "Ben de çikolatayı mutluluğa tahvil ederim 🍫")
q("dunya", 2, "Euro hangi yıl cebe girdi, yani madeni ve kâğıt olarak kullanılmaya başladı?", ["1992", "1999", "2002", "2008"], 2,
  "Euro 1999'da hesaplarda kullanılmaya başladı, banknot ve madeni paralar ise 1 Ocak 2002'de çıktı.",
  "Avrupa Merkez Bankası", "2000'lerin hemen başı.", "Yılbaşı hediyesi gibi gelmiş 🎁", 2002, "Euro")
q("kelime", 3, "\"Temettü\" (hisse kâr payı) kelimesinin anlamı nedir?", ["Faydalanma, yararlanma", "Hediye", "Bölüşme", "Vergi"], 0,
  "Temettü, Arapça \"faydalanma\" demektir. Şirketin kârından ortakların faydalanmasıdır.",
  NIS, "Bir şeyden yarar görmek.", "Ortak kesemizin temettüsü: Kesecik'in gülümsemesi 😇")
q("tarih", 4, "Bugünkü Borsa İstanbul'un öncülü sayılan Dersaadet Tahvilat Borsası hangi yıl kuruldu?", ["1866", "1908", "1929", "1985"], 0,
  "Dersaadet Tahvilat Borsası 1866'da İstanbul'da kuruldu. Dersaadet, İstanbul'un eski adlarından biridir.",
  "Borsa İstanbul", "Osmanlı Bankası'ndan üç yıl sonra.", "Borsa da kese demekti, hatırlarsın 😉", 1866, "Dersaadet Tahvilat Borsası")

# ---- Gün 12
q("deyim", 1, "\"Dişinden tırnağından artırmak\" ne demek?", ["Diş fırçalamak", "Büyük fedakârlıkla biriktirmek", "Kavga etmek", "Hızlı yemek"], 1,
  "Kendi ihtiyaçlarından bile kısarak, büyük fedakârlıkla para biriktirmek demektir.",
  TDK, "Ne kadar zor bir birikim olabilir?", "Ben tırnaklarıma dokunmam, manikürlü 💅")
q("kelime", 2, "\"Senet\" kelimesinin kökü ne demektir?", ["Dayanak, güvence", "Kâğıt", "Borç", "İmza"], 0,
  "Senet, Arapça \"dayanak\" demektir. Bir borcun yazılı dayanağıdır.",
  NIS, "Bir iddiayı destekleyen şey.", "Kesecik'ten senet alacağım, bana bir dondurma borcu var 📝")
q("dunya", 2, "Dünyanın ilk kredi kartı sayılan Diners Club kartı hangi yıl çıktı?", ["1920", "1950", "1975", "1990"], 1,
  "1950'de New York'ta, restoranlarda yemek yiyip sonra ödemek için Diners Club kartı çıkarıldı. \"Diners\" yemek yiyenler demek.",
  BRIT, "Adı yemekle ilgili; 20. yüzyılın ortası.", "Yemek yiyip sonra ödemek mi? İlk icadı ben yapmalıydım 🍝", 1950, "İlk Kredi Kartı")
q("kelime", 3, "\"Sigorta\" kelimesi İtalyancada ne anlama gelir?", ["Güvence, emniyet", "Tehlike", "Para", "Liman"], 0,
  "İtalyanca sicurtà \"güvence\" demektir. Ticaret gemilerinin riskini paylaşmak için doğdu.",
  NIS, "Seni neye karşı korur?", "Kesemi sigortalatacağım 🛡️")
q("tarih", 4, "Hangi ünlü bilim insanı yıllarca İngiliz Kraliyet Darphanesi'nin başında bulundu ve kalpazanlarla mücadele etti?", ["Galileo", "Isaac Newton", "Albert Einstein", "Charles Darwin"], 1,
  "Isaac Newton 1696'dan ölümüne kadar Kraliyet Darphanesi'nde görev yaptı; paraları yeniden basmayı yönetti ve kalpazanların peşine düştü. Madeni paraların tırtıklı kenarı da kenardan gümüş kırpılmasını önlemek içindir.",
  BRIT, "Başına elma düştüğü anlatılır.", "Elma düştü, kalpazan yakalandı 🍎")

# ---- Gün 13
q("kelime", 1, "\"İndirim\" kelimesi hangi dilden?", ["Türkçe", "Arapça", "Farsça", "Fransızca"], 0,
  "İndirim, öz Türkçe \"indirmek\" fiilinden türetilmiştir.",
  TDK, "Fiyatı aşağı ...", "En sevdiğim kelime, hiç şüphesiz 🛍️")
q("kelime", 2, "\"Esnaf\" kelimesi aslında hangi kelimenin çoğuludur?", ["Sınıf", "Sanat", "Satış", "Şehir"], 0,
  "Esnaf, Arapça sınıf kelimesinin çoğuludur: sınıflar. Her meslek bir sınıf, hepsi esnaf.",
  NIS, "Okulda da var.", "Esnafın hası, kesenin aşkı 😄")
q("altin", 2, "Reşat altını adını kimden alır?", ["Bir kuyumcudan", "Sultan Mehmed Reşad'dan", "Bir şehirden", "Bir vezirden"], 1,
  "Reşat altını, 1909-1918 yılları arasında tahtta kalan Sultan Mehmed Reşad döneminde basıldı.",
  DAR, "Adı bir padişahın adı.", "Reşat altını takan da çok yakışıklı olur 😄")
q("kelime", 3, "\"Kumbara\" kelimesinin Farsça aslı ne demektir?", ["Küçük küp, toprak testi", "Gizli dolap", "Domuz", "Altın kutu"], 0,
  "Farsça khumbara \"küçük küp\" demektir. Eski kumbaralar topraktan yapılırdı, para alınırken kırılırdı.",
  NIS, "Topraktan yapılmış bir kap.", "Kırılan kumbaraya hep üzülmüşümdür 🥲")
q("dunya", 4, "İngilizcede kumbaraya neden \"piggy bank\" (domuzcuk) denir?", ["Domuz bereket simgesi olduğu için", "Kumbaraların yapıldığı \"pygg\" adlı kilden", "Bir masaldan", "Bir bankanın logosundan"], 1,
  "Orta Çağ İngiltere'sinde kaplar \"pygg\" adlı turuncu bir kilden yapılırdı. Zamanla pygg kavanozu, domuz (pig) biçiminde kumbaraya dönüştü.",
  BRIT, "Domuzla ilgisi sonradan gelmiş.", "Domuzcuk değilmiş, kil kavanozmuş 🐷", None, None)

# ---- Gün 14
q("deyim", 1, "\"Beş para etmez\" ne demek?", ["Hiç değeri yok", "Ucuz ama iyi", "Beş kuruş", "Pahalı"], 0,
  "Para, kuruşun kırkta biriydi; beş para bile etmeyen şey neredeyse hiçbir değeri olmayan şeydir.",
  TDK, "Para çok küçük bir birimdi.", "Isınma turu, rahat ol 😉")
q("kelime", 2, "\"Pazar\" kelimesi hangi dilden gelir ve İngilizceye nasıl geçmiştir?", ["Farsça, bazaar olarak", "Arapça, market olarak", "Latince, forum olarak", "Yunanca, agora olarak"], 0,
  "Pazar, Farsça bāzār kelimesinden gelir; İngilizceye de bazaar olarak geçmiştir.",
  NIS, "İngilizcede de neredeyse aynı söylenir.", "Pazar günü pazara gideriz 🥬")
q("tarih", 2, "Türkiye İş Bankası hangi yıl kuruldu?", ["1920", "1924", "1938", "1950"], 1,
  "İş Bankası, Atatürk'ün girişimiyle 26 Ağustos 1924'te kuruldu ve Cumhuriyet'in ilk ulusal bankalarındandır.",
  "Türkiye İş Bankası", "Cumhuriyet'in ilk yılları.", "Ağustos sonu doğmuş, aslan burcu 🦁", 1924, "İş Bankası")
q("kelime", 3, "\"Rehin\" verilen bir şeyin bugünkü karşılığı nedir?", ["Teminat", "Hediye", "Kira", "Satış"], 0,
  "Rehin, bir borca karşılık güvence olarak bırakılan maldır; bugün teminat denir.",
  TDK, "Borcun güvencesi.", "Kesecik'in gözlüğünü rehin aldım, bulaşıkları yıkayınca geri veririm 🤓")
q("dunya", 4, "\"Bitcoin Pizza Günü\" neden kutlanır?", ["İlk bitcoin madenciliği", "Bitcoin'le yapılan ilk bilinen alışveriş", "Bitcoin'in yasaklanması", "İlk bitcoin ATM'si"], 1,
  "22 Mayıs 2010'da bir programcı 10.000 bitcoin vererek iki pizza aldı. Bu, bitcoin'le yapılan ilk bilinen alışveriş sayılır.",
  BRIT, "Bir yemek siparişiyle ilgili.", "O pizzalar dünyanın en pahalı pizzası oldu 🍕", 2010, "Pizza Günü")

# ---- Gün 15
q("deyim", 1, "\"Haraç mezat satmak\" ne demek?", ["Çok pahalıya satmak", "Yok pahasına satmak", "Takas etmek", "Kiralamak"], 1,
  "Mezat açık artırmadır. Haraç mezat, bir malı neredeyse bedavaya, çok ucuza elden çıkarmak demektir.",
  TDK, "İyi bir satış değil.", "Benim kurdelemi haraç mezat satamazsınız 🎀")
q("kelime", 2, "\"Cüzdan\" kelimesi ilk olarak neyin kabı demekti?", ["Kitap bölümü (cüz) kabı", "Para kesesi", "Tütün kutusu", "Mektup zarfı"], 0,
  "Cüzdan, cüz yani kitap bölümü konulan kılıf demekti; sonra para ve kâğıt taşınan küçük çantanın adı oldu.",
  NIS, "İçinde \"cüz\" geçiyor.", "Benim cüzdanım hep boş, kesem dolu 😄")
q("altin", 2, "Gümüşün kimyasal simgesi Ag hangi ülkenin adıyla akrabadır?", ["Arjantin", "Avusturya", "Angola", "Ermenistan"], 0,
  "Ag, Latince argentum (gümüş) kelimesinden gelir. Arjantin de adını gümüşten alır: gümüş ülkesi.",
  BRIT, "Güney Amerika'da bir ülke.", "Akçe de gümüş demek, akrabayız 😍")
q("kelime", 3, "\"Poliçe\" kelimesi hangi dilden gelir?", ["İtalyanca", "İngilizce", "Arapça", "Rusça"], 0,
  "Poliçe, İtalyanca polizza kelimesinden gelir. Bankacılık ve sigortacılığın birçok terimi İtalyan tüccarlardan yayıldı.",
  NIS, "Banka ve kasa kelimeleriyle aynı yerden.", "İtalyanlar her şeyi icat etmiş, makarna dahil 🍝")
q("tarih", 4, "İlk ATM (bankamatik) hangi şehirde kuruldu?", ["New York", "Londra", "Tokyo", "Paris"], 1,
  "İlk ATM 1967'de Londra'da, bir Barclays şubesinde çalışmaya başladı.",
  BRIT, "Big Ben'in şehri.", "Para veren makine, rüya gibi 🏧", 1967, "İlk ATM")

# ---- Gün 16
q("kelime", 1, "\"Harcamak\" fiilinin kökündeki \"harç\" ne demektir?", ["Gider, masraf", "Sıva", "Toprak", "Para kesesi"], 0,
  "Harç, Arapça kharj \"gider, masraf\" demektir; harcamak da buradan türemiştir.",
  NIS, "Bir masraf türü.", "Harç da harcamak da kesemi boşaltıyor 🥲")
q("kelime", 2, "\"Tüccar\" kelimesi aslında hangi kelimenin çoğuludur?", ["Tacir", "Ticaret", "Tecrübe", "Taşır"], 0,
  "Tüccar, Arapça tacir (ticaret yapan) kelimesinin çoğuludur. Türkçede tek kişi için de kullanılır.",
  NIS, "Ticaret yapan kişi.", "Bir tüccar, iki tüccar... 🤔")
q("tarih", 2, "Türk lirası simgesi ₺ hangi yıl kabul edildi?", ["2005", "2009", "2012", "2016"], 2,
  "₺ simgesi 1 Mart 2012'de kabul edildi. Çapa biçimi güveni, yukarı yönelen çizgiler değer artışını anlatır.",
  TCMB, "YTL'den sonra, 2010'ların başı.", "Benim sikkemdeki işaret! 🪙", 2012, "₺ Simgesi")
q("kelime", 3, "\"Hisse\" kelimesinin anlamı nedir?", ["Pay", "Duygu", "Kâr", "Senet"], 0,
  "Hisse, Arapça \"pay\" demektir. Hisse senedi, şirketten bir pay sahibi olduğunu gösterir.",
  NIS, "Bütünden düşen parça.", "Pastadan hissemi isterim 🎂")
q("dunya", 4, "İngilizcedeki \"fee\" (ücret) kelimesi Eski İngilizcede ne anlama geliyordu?", ["Sığır, hayvan", "Altın", "Toprak", "Kral"], 0,
  "Eski İngilizcede feoh \"sığır, mal varlığı\" demekti. Tıpkı Latince pecunia gibi, değer hayvanla ölçülürdü.",
  BRIT, "Roma'daki pecunia sorusunu hatırla.", "Yine mi inek? Bu hayvanlar ekonomiyi taşımış 🐮")

# ---- Gün 17
q("deyim", 1, "\"Züğürt\" kime denir?", ["Parasız, yoksul kişi", "Zengin kişi", "Yaşlı kişi", "Gezgin"], 0,
  "Züğürt, parasız kalmış kişidir. \"Züğürt tesellisi\" de elde olmayanla avunmak demektir.",
  TDK, "Cebi boş biri.", "Ay sonunda hepimiz biraz züğürdüz 🙃")
q("kelime", 2, "\"Faiz\" kelimesi Arapçada neyi anlatır?", ["Taşan, fazla gelen", "Borç", "Zaman", "Ceza"], 0,
  "Faiz, Arapça \"taşan, fazla gelen\" kökünden gelir: anaparanın üstüne eklenen fazlalık.",
  NIS, "Ana paranın üstüne gelen.", "Taşan su gibi, ama kesemden taşmasın 💧")
q("altin", 2, "Pırlantada kullanılan \"karat\" kelimesi neyin tohumundan gelir?", ["Keçiboynuzu", "Fasulye", "Buğday", "Mısır"], 0,
  "Yunanca keration \"keçiboynuzu çekirdeği\" demektir. Eskiden küçük ağırlıklar bu çekirdeklerle tartılırdı.",
  BRIT, "Uzun, kahverengi, tatlı bir meyve.", "Keçiboynuzu severim, pırlantayı daha çok 💎")
q("kelime", 3, "\"Lonca\" (esnaf birliği) kelimesi hangi dilden gelir?", ["İtalyanca", "Arapça", "Farsça", "Türkçe"], 0,
  "Lonca, İtalyanca loggia \"üstü kapalı toplantı yeri\" kelimesinden gelir. Esnafın buluştuğu yer zamanla birliğin adı oldu.",
  NIS, "Kasa ve banka kelimelerinin kardeşi.", "Kese ile Akçe loncası kuralım mı? 🤝")
q("tarih", 4, "Ahilik teşkilatı hangi alanda örgütlenmişti?", ["Esnaf ve zanaatkârlar", "Denizciler", "Askerler", "Çiftçiler"], 0,
  "Ahilik, Anadolu'da esnaf ve zanaatkârların dayanışma ve meslek ahlakı örgütüydü. Dürüst ticaret ve çırak yetiştirme esastı.",
  "Kültür ve Turizm Bakanlığı", "Ahi Evran'ı hatırla; dükkân sahipleri.", "Dürüst esnaf en güzeli 🧑‍🔧")

# ---- Gün 18
q("kelime", 1, "\"Bozuk para\" neden \"bozuk\"?", ["Büyük paranın bozdurulmasından kalır", "Kırık olduğu için", "Değeri düştüğü için", "Eski olduğu için"], 0,
  "Büyük bir parayı küçüklere ayırmaya \"bozdurmak\" denir. Ortaya çıkan küçük paralar da bozuk para olur.",
  TDK, "Bozdurmak fiilini düşün.", "Bozuk param var ama kalbim sağlam 💛")
q("kelime", 2, "\"Kâr\" kelimesi Farsçada ne demektir?", ["İş, kazanç", "Kar yağışı", "Fazla", "Değer"], 0,
  "Farsça kār \"iş\" demektir. Bir işten elde edilen kazanç da kâr oldu.",
  NIS, "Bir şey yapmak, çalışmak.", "Kar değil kâr, şapkası var! 🎩")
q("dunya", 2, "Mısır piramitlerinde çalışan işçilere ücret yerine sıklıkla ne verilirdi?", ["Ekmek ve bira", "Altın", "Toprak", "Deniz kabuğu"], 0,
  "Kayıtlar, işçilere günlük erzak olarak ekmek ve bira verildiğini gösteriyor. Para henüz yoktu.",
  BRIT, "Yiyecek ve içecek.", "Maaşı ekmek olan işçi, karnı tok 🍞")
q("kelime", 3, "\"Hamiline\" yazan bir çek kime ödenir?", ["Onu elinde tutana", "Yalnızca banka sahibine", "Devlete", "Yazanın ailesine"], 0,
  "Hamil \"taşıyan\" demektir. Hamiline yazılı çek, onu elinde bulundurana ödenir; o yüzden iyi saklanmalı.",
  NIS, "Hamil kelimesi taşımakla ilgili.", "Çeki taşıyan kazanır, ben taşırım 💪")
q("tarih", 4, "Bugünkü Ziraat Bankası'nın kökeni sayılan \"Memleket Sandıkları\" hangi devlet adamının girişimiyle kuruldu?", ["Mithat Paşa", "Sokullu Mehmed Paşa", "Koca Ragıp Paşa", "Fuad Paşa"], 0,
  "Mithat Paşa 1863'te Niş'te, çiftçilere kredi vermek için Memleket Sandıkları'nı kurdu. Ziraat Bankası 1888'de bu temel üzerine kuruldu.",
  "Ziraat Bankası", "Anayasa ile de adı anılan bir vali.", "Sandık dediğin, kesenin büyüğü 📦", 1888, "Ziraat Bankası")

# ---- Gün 19
q("deyim", 1, "\"Parayı veren düdüğü çalar\" ne demek?", ["Masrafı karşılayan söz sahibi olur", "Müzik pahalıdır", "Para kazanan mutludur", "Herkes eşittir"], 0,
  "Bir işin parasını kim veriyorsa, karar verme hakkı da genellikle onda olur.",
  TDK, "Kim karar verir?", "Düdüğü ben çalarım, Kesecik notaları sayar 🎶")
q("kelime", 2, "\"Tasarruf\" kelimesinin asıl anlamı nedir?", ["Bir şeyi kullanma, elinde tutma hakkı", "Biriktirme", "Cimrilik", "Faiz"], 0,
  "Tasarruf, aslında \"bir şeyi dilediği gibi kullanma\" demektir. Bugün ise daha çok biriktirmek, idareli kullanmak anlamında kullanılır.",
  TDK, "Mülkiyetle ilgili bir hak.", "Benim tasarrufum: kurdele koleksiyonu 🎀")
q("altin", 2, "Altın neden yıllarca paslanmadan kalır?", ["Çok az tepkimeye giren bir metal olduğu için", "Yağlandığı için", "Ağır olduğu için", "Sarı olduğu için"], 0,
  "Altın, havadaki oksijen ve nemle neredeyse hiç tepkimeye girmez. Bu yüzden binlerce yıllık altın eserler hâlâ parlar.",
  BRIT, "Kimyasal bir özellik.", "Altın gibi kalpler de paslanmaz 💛")
q("dunya", 3, "Dolar işareti \"$\" için en yaygın açıklama nedir?", ["İspanyol pesosunun \"ps\" kısaltmasından", "ABD bayrağından", "Bir yılan figüründen", "Amerikan kartalından"], 0,
  "En yaygın görüşe göre $, İspanyol pesosunun \"ps\" kısaltmasının zamanla üst üste yazılmasından doğdu.",
  BRIT, "Amerika'dan önce bir İspanyol parası vardı.", "Yılan değilmiş, rahatladım 🐍")
q("kelime", 4, "\"Mezat\" (açık artırma) kelimesi Arapçada ne anlama gelir?", ["Artırma, fiyat yükseltme", "Pazar yeri", "Satış belgesi", "Eski eşya"], 0,
  "Mezat, Arapça \"artırma\" kökünden gelir. Açık artırmada fiyat sürekli artırılır, en yüksek veren alır.",
  NIS, "Fiyatın yönünü düşün.", "Kurdelem mezatta olsa çok pahalıya giderdi 🎀")

# ---- Gün 20
q("deyim", 1, "\"Bir elin nesi var, iki elin sesi var\" ne anlatır?", ["Birlikte çalışmanın gücünü", "El çırpmayı", "Müziği", "Elleri yıkamayı"], 0,
  "Tek başına yapılamayan işler birlikte kolayca başarılır. Ortak bütçe de böyle!",
  TDK, "Tek el alkış yapabilir mi?", "Kese ile Akçe, iki el bir ses 👏")
q("kelime", 2, "\"Çek\" kelimesi Türkçeye hangi dilden girdi?", ["İngilizce", "Çekçe", "Arapça", "Türkçe \"çekmek\"ten"], 0,
  "Çek, İngilizce check/cheque kelimesinden gelir. \"Çekmek\" fiiliyle benzerliği tesadüftür.",
  NIS, "Çek Cumhuriyeti ile ilgisi yok.", "Çek de çekmek de beni yoruyor 😅")
q("tarih", 2, "\"Yeni Türk Lirası\" adındaki \"Yeni\" ibaresi hangi yıl kaldırıldı?", ["2007", "2009", "2012", "2015"], 1,
  "2009'un ilk günü \"Yeni\" ibaresi kalktı ve paramızın adı yeniden Türk lirası oldu.",
  TCMB, "₺ simgesinden önce.", "Yeni değilmiş artık, büyüdü 😄", 2009, "Türk Lirası")
q("kelime", 3, "\"Kâr payı\" anlamına gelen \"dividend\" Latincede ne demektir?", ["Bölünecek olan", "Kazanılan", "Biriktirilen", "Verilen"], 0,
  "Latince dividendum \"bölünecek olan\" demektir. Kâr, ortaklar arasında bölünür.",
  BRIT, "Matematikteki bölme işlemini düşün.", "Bölüşmeyi severim, pastayı da 🍰")
q("dunya", 4, "Bugün para birimlerinde kullanılan üç harfli kodlarda (TRY, USD, EUR) Türk lirasının eski kodu neydi?", ["TRL", "TLR", "TUR", "TKL"], 0,
  "Sıfırlar atılmadan önceki Türk lirasının kodu TRL'ydi. 2005'te YTL ile birlikte TRY kodu kullanılmaya başlandı.",
  "ISO 4217", "TR ile başlar, lira ile biter.", "Kod adı TRY, kulağa \"dene\" gibi geliyor 😄")

# ---- Gün 21
q("deyim", 1, "\"Sakla samanı, gelir zamanı\" ne öğütler?", ["Şimdi gereksiz görünen şey ileride işe yarar", "Saman pahalıdır", "Çiftçi ol", "Hiçbir şey saklama"], 0,
  "Bugün değersiz görünen bir şey ileride işine yarayabilir; o yüzden kolayca harcama, sakla.",
  TDK, "Samanın değeri ne zaman anlaşılır?", "Ben her şeyi saklarım, Kesecik \"yer kalmadı\" diye söylenir 🙈")
q("kelime", 2, "\"Fatura\" kelimesi hangi dilden gelir?", ["İtalyanca", "Fransızca", "Arapça", "İngilizce"], 0,
  "Fatura, İtalyanca fattura \"yapılmış iş\" kelimesinden gelir.",
  NIS, "Banka, kasa, poliçe ile aynı memleketten.", "Faturaları görünce kurdelem düşüyor 😩")
q("altin", 2, "22 ayar altında 24 parçanın kaçı altındır?", ["18", "20", "22", "24"], 2,
  "22 ayarda 24 parçanın 22'si altın, 2'si sertlik versin diye eklenen başka metaldir. Yani yaklaşık %91,6 altın.",
  DAR, "Adında yazıyor.", "Bu soru beleş çıktı 😄")
q("kelime", 3, "\"Komisyon\" ile aynı kökten gelen, \"birine iş vermek, görevlendirmek\" anlamındaki Latince kelime hangisidir?", ["Committere", "Communis", "Comitas", "Comedere"], 0,
  "Komisyon, Latince committere \"emanet etmek, görevlendirmek\" kökünden gelir. Aracıya verilen iş karşılığı ücrettir.",
  BRIT, "İçinde \"mit\" geçiyor, emanet etmek.", "Ben komisyonu çikolatayla alırım 🍫")
q("tarih", 4, "Bugünkü Borsa İstanbul'un öncülü İMKB (İstanbul Menkul Kıymetler Borsası) hangi yıl kuruldu?", ["1975", "1985", "1995", "2005"], 1,
  "İMKB 1985'te kuruldu, işlemler 1986'da başladı. 2013'te Borsa İstanbul adını aldı.",
  "Borsa İstanbul", "1980'lerin ortası.", "Borsa yine kese demekti, unutmadık 😉", 1985, "İMKB")

# ---- Gün 22
q("deyim", 1, "\"Tutumlu\" kime denir?", ["Parasını ölçülü harcayana", "Çok konuşana", "Herkesi tutana", "Sinirli olana"], 0,
  "Tutumlu, parasını ve eşyasını gereksiz yere harcamayan, idareli kullanan kişidir. Cimrilikten farkı, gereken yerde harcamasıdır.",
  TDK, "Parayı nasıl kullanır?", "Kesecik tutumlu, ben akıllı harcarım. Aradaki fark bütçe defteri 😄")
q("kelime", 2, "\"Kira\" kelimesi hangi dilden gelir?", ["Arapça", "Farsça", "Yunanca", "Türkçe"], 0,
  "Kira, Arapça \"bir şeyin kullanımı için ödenen bedel\" anlamındaki kelimeden gelir.",
  NIS, "Faiz, mevduat, senet ile aynı dilden.", "Kirayı gördükçe yanaklarım sönüyor 🎈")
q("dunya", 2, "Bazı Afrika ve Asya ülkelerinde uzun süre para olarak kullanılan deniz canlısının kabuğu hangisidir?", ["Cowrie (kauri) kabuğu", "İstiridye", "Midye", "Yengeç"], 0,
  "Küçük ve parlak cowrie kabukları dayanıklı ve sahtesi zor olduğu için yüzyıllarca para olarak kullanıldı.",
  BRIT, "Küçük, parlak, beyaz bir kabuk.", "Kabuk para olsaydı kesem deniz kokardı 🐚")
q("kelime", 3, "\"Esham\" kelimesi neyin çoğuludur?", ["Hisse (sehim, pay)", "Senet", "Kâr", "Ortak"], 0,
  "Esham, Arapça sehm (pay, hisse) kelimesinin çoğuludur. Eskiden hisse senetlerine \"esham\" denirdi.",
  NIS, "Bir önceki günlerde pay anlamına gelen kelime vardı.", "Eski kelimeleri de biliyorum, aferin bana 👑")
q("tarih", 4, "Osmanlı'da ilk gümüş kuruş hangi yüzyılın sonunda basıldı?", ["15. yüzyıl", "16. yüzyıl", "17. yüzyıl", "19. yüzyıl"], 2,
  "Osmanlı'da gümüş kuruş, Avrupa'nın büyük gümüş paralarına karşılık olarak 1690'da, 17. yüzyılın sonunda basıldı.",
  PAM, "1600'lerin sonu.", "Kuruş, akçeden sonra gelmiş, ben önceyim 💁‍♀️", 1690, "Osmanlı Kuruşu")

# ---- Gün 23
q("deyim", 1, "\"Göz hakkı\" ne demektir?", ["Görene verilen küçük pay", "Göz doktoru ücreti", "Gözlük parası", "Bakma cezası"], 0,
  "Bir şeyi gören, isteyen kişiye ikram edilen küçük pay. Komşuya yemekten bir tabak göndermek gibi güzel bir gelenektir.",
  TDK, "Bakan, gören biri.", "Gözlüğüm var, göz hakkım iki kat 🤓")
q("kelime", 2, "\"Teminat\" kelimesinin anlamı nedir?", ["Güvence", "Ceza", "Kâr", "Fiyat"], 0,
  "Teminat, Arapça \"güvence\" demektir. Bir borcun ödeneceğine dair verilen güvence.",
  NIS, "Rehin sorusunu hatırla.", "Kurdelem teminatım olsun 🎀")
q("altin", 2, "Altın en çok hangi ülkenin merkez bankasında saklanır?", ["ABD", "Çin", "İsviçre", "Japonya"], 0,
  "Resmi altın rezervleri en yüksek olan ülke ABD'dir; 8.000 tonu aşan altını vardır.",
  "Dünya Altın Konseyi", "En büyük ekonomi.", "8.000 ton! Kesem patlar 🤯")
q("kelime", 3, "\"Bilanço\" kelimesi hangi dilden gelir ve aslında neyi anlatır?", ["İtalyanca, teraziyi (denge)", "Arapça, hesabı", "Fransızca, kitabı", "Latince, yazıyı"], 0,
  "Bilanço, İtalyanca bilancio (terazi, denge) kelimesinden gelir. Varlıklar ile borçlar terazinin iki kefesi gibi dengelenir.",
  NIS, "İki kefeli bir alet.", "Benim bilançom: kurdele + çikolata = mutluluk ⚖️")
q("dunya", 4, "Japonya'nın para birimi \"yen\" ne anlama gelir?", ["Yuvarlak", "Güneş", "Altın", "Ada"], 0,
  "Yen, Japoncada \"yuvarlak\" demektir; yuvarlak madeni paralardan adını alır. Çin'deki yuan ve Kore'deki won da aynı kökten gelir.",
  BRIT, "Paraların şekli.", "Bütün paralar yuvarlak, yen adını almış 😄")

# ---- Gün 24
q("deyim", 1, "\"Para parayı çeker\" ne demek?", ["Birikimi olan daha kolay kazanır", "Mıknatıs gibi", "Para düşer", "Paralar çekişir"], 0,
  "Sermayesi olan kişi onu işletip daha fazla kazanabilir. Küçük de olsa birikim yapmanın önemi buradan gelir.",
  TDK, "Zenginliğin nasıl büyüdüğünü düşün.", "Kesemiz parayı çeksin, Kesecik de beni 😍")
q("kelime", 2, "\"Ödünç\" kelimesi hangi dilden?", ["Türkçe", "Arapça", "Farsça", "Yunanca"], 0,
  "Ödünç, eski Türkçeden beri kullanılan öz Türkçe bir kelimedir: geri verilmek üzere alınan şey.",
  TDK, "Vergi gibi öz Türkçe.", "Kesecik'ten ödünç kalem aldım, üç yıldır bende 🙊")
q("dunya", 2, "Bileşik faizde paranın yaklaşık kaç yılda ikiye katlanacağını bulmak için kullanılan pratik kural hangisidir?", ["72 kuralı", "50 kuralı", "100 kuralı", "12 kuralı"], 0,
  "72'yi yıllık getiri oranına bölersin: %12 getiriyle para yaklaşık 72/12 = 6 yılda ikiye katlanır. Enflasyonu da hesaba katmayı unutma!",
  BRIT, "Bir yılın aylarının 6 katı.", "Matematik bana hep 72 gibi geliyor 😵")
q("kelime", 3, "\"İskonto\" kelimesi hangi dilden gelir?", ["İtalyanca", "İspanyolca", "Arapça", "Fransızca"], 0,
  "İskonto, İtalyanca sconto \"indirim\" kelimesinden gelir. Vadesi gelmemiş senedin erken ödenirken düşülen tutara da denir.",
  NIS, "Yine bankacıların dili.", "İtalyanlar yine iş başında 🇮🇹")
q("altin", 4, "Darphane'nin bugün madeni para bastığı tesisler hangi şehirde?", ["Ankara", "İstanbul", "İzmir", "Bursa"], 1,
  "Darphane ve Damga Matbaası Genel Müdürlüğü İstanbul'dadır. Osmanlı döneminde darphane Topkapı Sarayı'nın içindeydi.",
  DAR, "Osmanlı'nın başkenti.", "Paralar orada doğuyor, ziyarete gidelim 🏛️")

for i, x in enumerate(Q):
    x["id"] = f"q{i + 1:03d}"
    assert 0 <= x["a"] < 4 and len(x["o"]) == 4, x["q"]
    if x.get("y") == -1:
        x["y"] = 1327
        x["t"] = "İlk Akçe"

out = {
    "version": "2026-11-03",
    "start": "2026-11-03",
    "perDay": 5,
    "questions": Q,
}
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
print(f"{len(Q)} soru", file=sys.stderr)
