---
name: turkce-akademik-style-review
description: Türkçe akademik metinlerde AI tarafından üretilmiş gibi duran kalıpları, ölçüsüz iddiaları, gereksiz sözcükleri, belirsiz kavramları ve akış sorunlarını temizlemek için kullanılır. Tez metinleri için uygundur.
---

# Türkçe Akademik Style Review

Bu skill, Türkçe akademik metni doğal, açık, ölçülü ve kanıta dayalı hâle getirmek için ikinci geçiş denetimi yapar. Amaç AI kullanımını gizlemek değil, metin kalitesini artırmaktır.

## Denetim kategorileri

1. **Belirsiz iddialar**
   - `birçok çalışma`, `çeşitli faktörler`, `önemli sonuçlar` gibi ifadeler somutlaştırılır.

2. **Ölçüsüz vurgu**
   - `çok önemli`, `kritik`, `başarılı`, `güçlü`, `kapsamlı` gibi ifadeler kanıt yoksa zayıflatılır.

3. **Gereksiz giriş kalıpları**
   - `Bu bölümde ... ele alınacaktır` gibi üst-anlatı cümleleri gerekli değilse kaldırılır.
   - Giriş ve bölüm geçişlerinde akademik yol gösterme gerekiyorsa kısa tutulur.

4. **Terim tutarlılığı**
   - Aynı kavram için farklı eş anlamlılar kullanılmaz.
   - Teknik terim Türkçeye doğal çevrilemiyorsa İngilizce bırakılır ve açıklanır.

5. **Cümle akışı**
   - Çok uzun cümleler bölünür.
   - Art arda aynı kalıpla başlayan cümleler düzeltilir.
   - Her paragrafın ana mesajı görünür hâle getirilir.

6. **İddia kalibrasyonu**
   - Kanıt sınırlıysa iddia yumuşatılır.
   - Nedensel iddialar yalnızca yöntem uygunsa korunur.

## Revizyon ilkeleri

- Anlamı koru.
- Kaynak, sayı, metrik, tablo veya sonuç ekleme.
- Atıf anahtarlarını ve LaTeX komutlarını koru.
- Metni gereksiz biçimde kısaltma; tez dili açıklayıcı olabilir.
- Düzeltme yaparken fazla parlatılmış, tanıtım metni gibi duran bir üslup oluşturma.

## Çıktı sözleşmesi

```text
## Tespit Edilen Üslup Sorunları
| Konum | Sorun | Öneri |
|---|---|---|

## Revize Metin
...

## Korunan Teknik Anlam
- ...

## Kalan Riskler
- ...
```

## Yasaklar

- Metne yeni kaynak veya veri ekleme.
- Kullanıcının iddiasını olduğundan güçlü yazma.
- Türkçede yapay duran çeviriler üretme.
- Tezi pazarlama metnine dönüştürme.
