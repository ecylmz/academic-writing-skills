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

3. **Literatür konumlandırması**
   - Literatür yalnızca özetlenmiş mi, yoksa tez problemi için tartışılmış mı?
   - Çalışmalar tematik, yöntemsel veya tarihsel olarak anlamlı gruplara ayrılmış mı?
   - Literatür boşluğu kanıtlanmış mı?

4. **Yöntem ve tekrar edilebilirlik**
   - Veri, örneklem, araç, parametre, protokol ve analiz adımları açık mı?
   - Deney tasarımında veri sızıntısı, önyargı veya yanlış karşılaştırma riski var mı?
   - Sonuçlar aynı koşullarda tekrar üretilebilir mi?

5. **Bulgular ve yorum**
   - Bulgular veriden ayrılmadan mı sunuluyor?
   - Yorumlar bulgulara dayanıyor mu?
   - Alternatif açıklamalar ve sınırlılıklar tartışılmış mı?

6. **Biçim ve tez kılavuzu uyumu**
   - Bölüm sırası ve başlık yapısı OMÜ kurallarıyla uyumlu mu?
   - Özet, abstract, kaynaklar, şekil/tablo başlıkları ve ekler doğru yerde mi?

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

## Yazılım mühendisliği / hata tahmini tezleri için özel riskler

- Veri seti oluşturma sürecinde etiket doğruluğu yeterince açıklanmamış olabilir.
- SZZ veya benzeri hata-inducing commit tespitinde varsayımlar net olmayabilir.
- Project split, cross-project split veya nested LOPO protokolünde leakage riski olabilir.
- Preprocessing tüm veri üzerinde yapılmışsa deney geçerliliği zedelenebilir.
- Class imbalance için yalnızca accuracy verilmişse sonuç yorumu zayıflar.
- Model seçimi, hiperparametre ayarı ve threshold belirleme fold-local değilse hakem/jüri sorusu doğar.
- Ablation sonuçları ana katkıyı gerçekten desteklemiyor olabilir.
- Dil-özel metriklerin katkısı ayrı test edilmemiş olabilir.

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
