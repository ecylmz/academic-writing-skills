---
name: tez-yazimi-tr
description: Türkçe yüksek lisans/doktora tezi bölümlerini akademik, açık, kanıta dayalı ve OMÜ tez yazım kılavuzu ile uyumlu biçimde yazmak veya revize etmek için kullanılır. Giriş, literatür, yöntem, bulgular, tartışma, sonuç, özet ve bölüm geçişlerinde uygundur.
---

# Tez Yazımı TR

Bu skill Türkçe tez yazımı içindir. Hedef, metni yalnızca daha düzgün yapmak değil; tez mantığını, bölüm işlevini, iddia-kanıt ilişkisini ve Türkçe akademik anlatımı güçlendirmektir.

## Kullanım alanları

- Giriş bölümü yazımı veya revizyonu.
- Literatür/kaynak özeti yazımı.
- Yöntem, materyal, veri seti, deney tasarımı veya analiz protokolü anlatımı.
- Bulgular ve tartışma bölümü.
- Sonuç ve öneriler.
- Türkçe özet ve İngilizce abstract taslağı için içerik hazırlığı.
- Paragraf akışı, bölüm bütünlüğü ve ters taslak çıkarma.

## Öncelik sırası

1. Tezin ana iddiasını ve araştırma problemini koru.
2. Bölümün işlevine göre yaz; her bölüm aynı retorik yapıda olmamalıdır.
3. Her paragrafın tek ana mesajı olmalıdır.
4. Önemli iddialar kaynak, yöntem, deney sonucu, tablo, şekil veya açık gerekçeyle desteklenmelidir.
5. Türkçe akademik dil açık, ölçülü ve doğrudan olmalıdır.
6. OMÜ biçim kurallarıyla çelişen öneriler yapma; biçimsel kontrol için `tez-latex-format-tr` referanslarına başvur.

## Zorunlu referans dosyaları

Göreve göre aşağıdaki dosyalardan yalnızca gerekli olanları oku:

- `references/tez-bolum-akisi.md`
- `references/turkce-akademik-uslup.md`
- `references/bolum-rehberi-giris.md`
- `references/bolum-rehberi-literatur.md`
- `references/bolum-rehberi-yontem.md`
- `references/bolum-rehberi-bulgular-tartisma.md`
- `references/bolum-rehberi-sonuc.md`
- `references/ozet-ve-abstract.md`
- `references/iddia-kanit-tez.md`
- `references/yazilim-muhendisligi-tezi.md`

## Çalışma akışı

1. Kullanıcının hedefini belirle: yazım mı, revizyon mu, genişletme mi, sadeleştirme mi?
2. Bölüm türünü belirle: giriş, literatür, yöntem, bulgular, tartışma, sonuç, özet.
3. Önce mini taslak çıkar:
   - bölümün amacı,
   - ana iddia,
   - paragraf rolleri,
   - gerekli kanıtlar,
   - eksik materyaller.
4. Verilen metin varsa ters taslak çıkar:
   - her paragrafın ana mesajı,
   - iddia-kanıt durumu,
   - tekrar veya kopukluklar.
5. Revizyon yaparken anlamı değiştirme; eksik veri varsa uydurma.
6. Sonunda kısa bir denetim raporu ver.

## Türkçe akademik dil kuralları

- “Bu çalışma önemlidir” gibi çıplak önem iddiaları yazma; önemi problem, boşluk veya sonuç üzerinden göster.
- “Kapsamlı”, “yenilikçi”, “güçlü”, “başarılı” gibi sıfatları kanıt yoksa kullanma.
- İngilizce terimi Türkçeye doğal çeviremiyorsan terimi koru ve ilk kullanımda açıklama ver.
- Aynı kavram için bölüm boyunca aynı terimi kullan.
- Uzun cümleleri böl; ancak metni kesik ve madde madde hâle getirme.
- Tez dilinde aşırı pazarlama tonu, abartılı katkı iddiası ve belirsiz genellemelerden kaçın.
- “Literatürde boşluk vardır” deniyorsa bu boşluğun hangi çalışmalar, hangi yöntemler veya hangi bağlam açısından oluştuğu belirtilmelidir.
- Bulgular bölümünde yorum sınırlı olmalı; yorum ve anlamlandırma tartışmada geliştirilmelidir.
- Sonuç bölümünde yeni kaynak, yeni veri veya yeni tartışma başlatma.

## Yazılım mühendisliği tezleri için özel kurallar

Kullanıcı yazılımda hata tahmini, cross-project defect prediction, Go veri kümeleri, deney protokolleri veya makine öğrenmesi metni yazıyorsa:

- Veri kümesi düzeyi, etiketleme süreci, granularity, train/test ayrımı ve leakage riskleri açık yazılmalıdır.
- Model başarısı tek metrikle sunulmamalıdır; sınıf dengesizliği varsa MCC, F1, recall, precision gibi metriklerin yorumu ayrıştırılmalıdır.
- Cross-project veya leave-one-project-out protokollerde hedef projenin preprocessing, tuning ve model seçimi dışında kaldığı açıkça belirtilmelidir.
- Ablation, robustness ve baseline açıklamaları yöntem veya deney bölümünde izlenebilir olmalıdır.
- “Genellenebilir” iddiası yalnızca veri kümesi kapsamı ve deney tasarımı izin veriyorsa kullanılmalıdır.

## Çıktı sözleşmesi

Yazım veya revizyon çıktısında şu yapı kullanılmalıdır:

1. **Mini Taslak**
   - Bölüm amacı
   - Ana mesaj
   - Paragraf rolleri
2. **Revize Metin**
   - Akademik Türkçe
   - Bölüm türüne uygun akış
   - Kaynak/atıf yerleri korunmuş
3. **Denetim Notları**
   - Güçlenen noktalar
   - Eksik kanıtlar
   - Fazla güçlü iddialar
   - Sonraki önerilen kontrol: `claim-evidence-audit`, `tez-denetim-tr` veya `tez-latex-format-tr`

## Yasaklar

- Kaynak uydurma.
- Deney sonucu, sayı, tablo veya metrik icat etme.
- Danışman veya jüri onayı gerektiren biçim değişikliğini kesin bilgi gibi sunma.
- LaTeX komutlarını anlamadan silme.
- Verilen metindeki teknik anlamı yalnızca dilsel güzelleştirme için değiştirme.
