---
name: tez-latex-format-tr
description: OMÜ tez yazım kılavuzu ve kullanıcının yerel LaTeX şablonu ile uyumlu tez biçim kontrolü yapmak için kullanılır. Sayfa düzeni, başlıklar, numaralandırma, özet, tablo/şekil, denklem, kaynakça ve LaTeX komutları korunarak denetlenir.
---

# Tez LaTeX Format TR

Bu skill, tez metninin içerik kalitesinden çok biçim, LaTeX şablon uyumu ve OMÜ tez yazım kurallarıyla ilgilenir.

## Öncelik sırası

1. Yerel LaTeX şablonu varsa önce onu oku.
2. Şablonun tanımladığı komutları ve dosya yapısını koru.
3. OMÜ tez yazım kılavuzundaki biçim kurallarını uygula.
4. Şablon ile kılavuz arasında fark varsa kesin karar verme; farkı raporla.
5. Kullanıcı istemedikçe ana `.tex` dosyasını yeniden yazma.

## Yerel şablon keşfi

Çalışmaya başlamadan önce proje dizininde şunları ara:

- Ana dosya: `main.tex`, `tez.tex`, `thesis.tex`, `omu_tez.tex` veya benzeri.
- Sınıf/stil: `.cls`, `.sty`.
- Bibliography: `.bib`.
- Derleme dosyaları: `Makefile`, `.latexmkrc`, `latexmkrc`.
- Bölüm dosyaları: `chapters/`, `sections/`, `bolumler/`.
- Şekil ve tablo dizinleri: `figures/`, `tables/`, `images/`.

Bulunanları raporla:

```text
Ana dosya:
Sınıf/stil dosyaları:
Kaynakça dosyası:
Bölüm dosyaları:
Derleme yöntemi:
Şablona özgü komutlar:
```

## OMÜ biçim kuralları

Bu skill, `references/omu-tez-kurallari.md` dosyasındaki kuralları ana kontrol listesi olarak kullanır. Kısa özet:

- A4 kâğıt.
- Sol kenar 4 cm; diğer kenarlar 2.5 cm.
- Sayfa numaraları altta ve ortada.
- Ön kısım Romen rakamlarıyla; numaralama Özet sayfasında iii ile başlar.
- Metin kısmı 1'den başlayarak Batı Arap rakamlarıyla numaralanır.
- Times New Roman 12 punto; ana bölüm başlıkları 14 punto; dipnotlar 10 punto.
- Ana metin 1.5 satır aralığı; özet, abstract, içindekiler, dizinler, kaynaklar ve öz geçmiş tek satır aralığı.
- Ana bölüm başlıkları büyük harf ve koyu; alt başlıklar yalnızca baş harfleri büyük olacak biçimde koyu.
- Paragraflar iki yana yaslı, 1 cm ilk satır girintili, paragraf sonrası 6 nk.
- Tablo başlıkları tablonun üstünde; şekil başlıkları şeklin altında.
- Şekil ve tablo numaraları bölüm numarasıyla başlar: `Şekil 2.1.`, `Tablo 3.2.`.
- Denklem numaraları bölüm içinde başlar: `(1.1)`, `(2.1)`.

## Kontrol akışı

1. LaTeX dosyalarını keşfet.
2. Şablonun komutlarını çıkar.
3. OMÜ kural listesiyle karşılaştır.
4. Sorunları kategoriye ayır:
   - `format-critical`: teslimde sorun çıkarabilecek biçim hatası
   - `template-risk`: şablon komutlarının yanlış kullanımı
   - `latex-error`: derleme hatası oluşturabilecek sorun
   - `consistency`: başlık/atıf/numara/tutarlılık sorunu
   - `style`: küçük görünüm ve okunabilirlik sorunu
5. Düzeltme önerilerini ver; kullanıcı isterse patch formatında sun.

## Çıktı sözleşmesi

```text
## Şablon Keşfi
...

## OMÜ Kural Kontrolü
| Kural | Durum | Kanıt / Dosya | Öneri |
|---|---|---|---|

## LaTeX Riskleri
| Öncelik | Dosya | Sorun | Düzeltme |
|---|---|---|---|

## Güvenli Düzeltme Planı
1. ...
```

## Yasaklar

- Şablonu baştan yazma.
- `.cls` veya `.sty` dosyalarını gerekçesiz değiştirme.
- Kapak, kabul/onay veya etik beyan komutlarını silme.
- Atıf anahtarlarını otomatik yeniden adlandırma.
- OMÜ kılavuzunda olmayan biçim kararlarını kesin kural gibi dayatma.
