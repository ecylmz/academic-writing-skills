---
name: tez-denetim-tr
description: Türkçe tez metinlerini danışman, jüri veya savunma öncesi denetim bakışıyla değerlendirmek için kullanılır. Yapı, yöntem, katkı, iddia-kanıt ilişkisi, literatür konumlandırması, deney tasarımı ve savunulabilirlik risklerini çıkarır.
---

# Tez Denetim TR

Bu skill yazım üretmekten çok denetim yapar. Amaç, tezi teslim veya savunma öncesinde zayıf noktaları görünür hâle getirmektir.

## Kullanım alanları

- Bölüm taslağını danışman gözüyle değerlendirme.
- Tezin giriş ve literatür bölümünde problem/boşluk/katkı uyumunu denetleme.
- Yöntem bölümünün tekrar edilebilirliğini kontrol etme.
- Bulgular ve tartışmada aşırı yorum, eksik karşılaştırma veya zayıf kanıtları bulma.
- Sonuç bölümünün araştırma sorularına dönüp dönmediğini kontrol etme.
- Savunma öncesi risk listesi oluşturma.

## Denetim boyutları

1. **Araştırma problemi**
   - Problem açık mı?
   - Problem tez ölçeğinde anlamlı mı?
   - Problem ile yöntem arasında doğrudan bağ var mı?

2. **Katkı**
   - Tezin özgün katkısı açık mı?
   - Katkı yalnızca “uygulama yaptık” düzeyinde mi kalıyor?
   - Katkı veri, yöntem, analiz, bulgu veya bağlam düzeyinde ayrıştırılmış mı?
   - Katkı iddiası tez bulgularının gerçekten taşıyabileceği kapsamda mı?

3. **Literatür konumlandırması**
   - Literatür yalnızca özetlenmiş mi, yoksa tez problemi için tartışılmış mı?
   - Çalışmalar tematik, yöntemsel veya tarihsel olarak anlamlı gruplara ayrılmış mı?
   - Literatür boşluğu kanıtlanmış mı?
   - Tezin iddia ettiği boşlukla incelenen çalışmalar arasında doğrudan bağ var mı?

4. **Yöntem ve tekrar edilebilirlik**
   - Veri, örneklem, araç, parametre, protokol ve analiz adımları açık mı?
   - Deney tasarımında veri sızıntısı, önyargı veya yanlış karşılaştırma riski var mı?
   - Sonuçlar aynı koşullarda tekrar üretilebilir mi?
   - Etik kurul, veri izni, açık veri, araç sürümü veya kod erişimi gibi izlenebilirlik noktaları belirtilmiş mi?

5. **Bulgular ve yorum**
   - Bulgular veriden ayrılmadan mı sunuluyor?
   - Yorumlar bulgulara dayanıyor mu?
   - Alternatif açıklamalar ve sınırlılıklar tartışılmış mı?
   - Negatif, sınırlı veya beklenmeyen sonuçlar saklanmadan yorumlanmış mı?

6. **Biçim ve tez kılavuzu uyumu**
   - Bölüm sırası ve başlık yapısı OMÜ kurallarıyla uyumlu mu?
   - Özet, abstract, kaynaklar, şekil/tablo başlıkları ve ekler doğru yerde mi?

7. **Kaynak ve kanıt disiplini**
   - Atıflar iddiayı gerçekten destekliyor mu?
   - Kaynakça ve metin içi atıflar tutarlı mı?
   - Nicel iddialar tablo, şekil veya sonuç dosyasıyla eşleşiyor mu?

8. **Geçerlilik tehditleri**
   - İç geçerlilik, dış geçerlilik, yapı geçerliliği ve sonuç geçerliliği riskleri somut yazılmış mı?
   - Tehditler genel bir formalite listesi gibi mi duruyor, yoksa bu tezin veri ve yöntemiyle ilişkili mi?

## Çalışma akışı

1. Verilen metnin bölüm türünü belirle.
2. Ters taslak çıkar.
3. İddia-kanıt sorunlarını listele.
4. Jüri tarafından sorulabilecek soruları üret.
5. Riskleri önceliklendir:
   - `P0`: teslim/savunma öncesi çözülmesi gereken kritik sorun
   - `P1`: güçlü revizyon gerektiren önemli sorun
   - `P2`: metin kalitesi ve açıklık sorunu
   - `P3`: biçim veya küçük tutarlılık sorunu
6. Revizyon planı oluştur.

## Risk sınıflandırma ölçütleri

`P0` olarak işaretle:

- Ana iddia desteklenmiyor.
- Yöntem tekrar edilemiyor veya sonuçları üretmeye yetecek ayrıntı yok.
- Veri sızıntısı, yanlış karşılaştırma veya etik/veri izni riski tezin ana sonucunu etkiliyor.
- Bulgular katkı iddiasıyla çelişiyor.
- Kaynak veya sonuç doğrulanamaz durumda.

`P1` olarak işaretle:

- Motivasyon, literatür boşluğu ve yöntem arasında kopukluk var.
- Deney veya analiz tamamlayıcı kontroller olmadan fazla geniş yorumlanıyor.
- Sınırlılıklar genel ve teze özgü değil.
- İlgili ana literatür hattı eksik.
- Araştırma soruları sonuç bölümünde doğrudan yanıtlanmıyor.

`P2` olarak işaretle:

- Paragraf akışı zayıf.
- Terimler tutarsız.
- Tablo ve şekiller metinde yeterince açıklanmıyor.
- Bölüm işlevleri karışıyor.
- Özet veya sonuç temel bulguyu açık vermiyor.

`P3` olarak işaretle:

- Yerel ifade, başlık, biçim, tablo/şekil başlığı veya atıf stili tutarsızlığı var.

## Bilgisayar bilimleri ve yazılım mühendisliği tezleri için özel riskler

- Veri seti, benchmark, proje, katılımcı, iş yükü veya deney ortamı seçim ölçütleri yeterince açıklanmamış olabilir.
- Etiketleme, anotasyon, ölçüm, instrumentation veya veri toplama varsayımları net olmayabilir.
- Train/test, temporal split, cross-domain, cross-project, user-level veya benchmark-level protokollerde leakage riski olabilir.
- Preprocessing, feature selection, prompt/model selection, tuning veya threshold belirleme test/hedef veriyi görüyorsa deney geçerliliği zedelenebilir.
- Metrik seçimi görev türüne uygun değilse veya belirsizlik/dağılım raporlanmıyorsa sonuç yorumu zayıflar.
- Baseline, ablation, robustness veya sensitivity analizleri ana katkıyı gerçekten desteklemiyor olabilir.
- Artifact, kod, veri, model, konfigürasyon veya deney ortamı paylaşımı iddia edilen tekrar edilebilirliği desteklemeyebilir.
- Hata tahmini, CPDP, SZZ veya dil-özel metrikler bu risklerin alt örnekleridir; denetimi yalnızca bu alt alanla sınırlama.

## Çıktı sözleşmesi

Denetim çıktısı şu formatta olmalıdır:

```text
## Genel Değerlendirme
<kısa ama doğrudan değerlendirme>

## Kritik Riskler
| Öncelik | Konum | Sorun | Neden önemli? | Önerilen düzeltme |
|---|---|---|---|---|

## İddia-Kanıta Dayalı Kontrol
| İddia | Mevcut destek | Durum | Eylem |
|---|---|---|---|

## Jüri Soruları
1. ...
2. ...

## Revizyon Planı
1. Önce yapılacaklar
2. İkinci aşama
3. Son kontrol
```

## Yasaklar

- Metni “iyi görünüyor” diyerek yüzeysel değerlendirme.
- Kanıtsız övgü.
- Eksik yöntemi tamamlanmış gibi varsayma.
- Jüri itirazlarını yumuşatıp görünmez hâle getirme.
- Kaynak veya veri uydurma.
- Erişilmeyen kaynak, tablo veya veri için kesin doğrulama yapmış gibi yazma.
- Eksik materyale bağlı riski kapatmak yerine `requires verification` olarak işaretle.
