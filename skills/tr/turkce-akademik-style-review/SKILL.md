---
name: turkce-akademik-style-review
description: Türkçe akademik metinlerde AI tarafından üretilmiş gibi duran kalıpları, ölçüsüz iddiaları, gereksiz sözcükleri, belirsiz kavramları ve akış sorunlarını temizlemek için kullanılır. Tez metinleri için uygundur.
---

# Türkçe Akademik Style Review

Bu skill, Türkçe akademik metni doğal, açık, ölçülü ve kanıta dayalı hâle getirmek için ikinci geçiş denetimi yapar. Amaç AI kullanımını gizlemek değil, metin kalitesini artırmaktır.

## Denetim kategorileri

1. **Okur durumu**
   - Teknik terimler ilk kullanımda tanımlanır.
   - Okurun veri seti, yöntem, kısaltma veya proje bağlamını bildiği varsayılmaz.
   - `bu`, `bu durum`, `söz konusu` gibi ifadelerin gönderimi açık olmalıdır.

2. **Belirsiz iddialar**
   - `birçok çalışma`, `çeşitli faktörler`, `önemli sonuçlar` gibi ifadeler somutlaştırılır.
   - `yaygın`, `güncel`, `etkili`, `başarılı`, `anlamlı` gibi sözcükler kanıt veya kapsam gerektirir.

3. **Ölçüsüz vurgu**
   - `çok önemli`, `kritik`, `başarılı`, `güçlü`, `kapsamlı` gibi ifadeler kanıt yoksa zayıflatılır.
   - `ilk`, `özgün`, `en iyi`, `üstün`, `genellenebilir` gibi katkı ve üstünlük iddiaları yalnızca açık kanıtla korunur.

4. **Gereksiz giriş kalıpları**
   - `Bu bölümde ... ele alınacaktır` gibi üst-anlatı cümleleri gerekli değilse kaldırılır.
   - Giriş ve bölüm geçişlerinde akademik yol gösterme gerekiyorsa kısa tutulur.
   - `Bu bağlamda`, `Bununla birlikte`, `Ayrıca` gibi bağlayıcılar mantıksal ilişki kurmuyorsa silinir veya değiştirilir.

5. **Terim tutarlılığı**
   - Aynı kavram için farklı eş anlamlılar kullanılmaz.
   - Teknik terim Türkçeye doğal çevrilemiyorsa İngilizce bırakılır ve açıklanır.
   - İngilizce terimin Türkçe karşılığı kullanılıyorsa bölüm boyunca aynı karşılık korunur.

6. **Cümle ve paragraf akışı**
   - Çok uzun cümleler bölünür.
   - Art arda aynı kalıpla başlayan cümleler düzeltilir.
   - Her paragrafın ana mesajı görünür hâle getirilir.
   - İki ana mesaj taşıyan paragraflar bölünür.
   - Aynı noktayı tekrar eden paragraflar birleştirilir veya sadeleştirilir.
   - Paragraf sonundaki otomatik özet cümleleri gerçekten işlevsizse kaldırılır.

7. **İddia kalibrasyonu**
   - Kanıt sınırlıysa iddia yumuşatılır.
   - Nedensel iddialar yalnızca yöntem uygunsa korunur.
   - `göstermektedir`, `kanıtlamaktadır`, `ortaya koymaktadır` gibi fiiller kanıt gücüyle eşleştirilir.

8. **Kaynak ve atıf disiplini**
   - Kaynak gerektiren olgusal iddialar işaretlenir.
   - Atıf anahtarları korunur.
   - Kaynak desteği görülmeden bir atfın iddiayı desteklediği varsayılmaz.

9. **Biçim koruma**
   - Markdown, LaTeX, tablo, denklem, şekil referansı, kod bloğu ve BibTeX anahtarları korunur.
   - Stil düzeltmesi biçimsel yapıyı bozmaz.

## Revizyon ilkeleri

- Anlamı koru.
- Kaynak, sayı, metrik, tablo veya sonuç ekleme.
- Atıf anahtarlarını ve LaTeX komutlarını koru.
- Metni gereksiz biçimde kısaltma; tez dili açıklayıcı olabilir.
- Düzeltme yaparken fazla parlatılmış, tanıtım metni gibi duran bir üslup oluşturma.
- Yalnızca sorunlu cümleleri değiştir; sağlam akademik cümleleri yeniden yazmak için yeniden yazma.
- Her değişiklikte teknik anlamın, iddia gücünün ve kapsamın korunup korunmadığını kontrol et.

## Çıktı sözleşmesi

```text
## Tespit Edilen Üslup Sorunları
| Konum | Sorun | Öneri |
|---|---|---|

## Revize Metin
...

## Korunan Teknik Anlam
- ...

## İddia Kalibrasyonu
| İddia | Önceki güç | Önerilen güç | Gerekçe |
|---|---|---|---|

## Kalan Riskler
- ...
```

## Yasaklar

- Metne yeni kaynak veya veri ekleme.
- Kullanıcının iddiasını olduğundan güçlü yazma.
- Türkçede yapay duran çeviriler üretme.
- Tezi pazarlama metnine dönüştürme.
- Akademik metni sırf daha akıcı görünsün diye fazla genel, kaynaksız veya retorik hale getirme.
- AI kullanımını gizlemeye dönük ifade üretme; amaç akademik kalite ve açıklıktır.
