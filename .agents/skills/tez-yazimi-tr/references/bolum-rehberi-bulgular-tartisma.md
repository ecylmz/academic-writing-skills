# Bulgular ve Tartışma Rehberi

Bulgular ve tartışma aynı bölümde veya ayrı bölümlerde yer alabilir. Ayrıysa bulgular veri odaklı, tartışma yorum odaklı olmalıdır.

## Bulgular bölümü

Bulgular bölümünde amaç, sonuçları açık ve izlenebilir biçimde sunmaktır.

- Tablo ve şekillere doğrudan referans ver.
- En önemli sonucu metinde belirt; tüm tabloyu düz yazıya çevirme.
- Sınıf dengesizliği, örneklem büyüklüğü veya varyans gibi yorum için kritik bağlamları ver.
- Sürpriz veya beklenmeyen bulguları görünür kıl.

## Tartışma bölümü

Tartışma bölümünde amaç, bulguların ne anlama geldiğini açıklamaktır.

- Bulguları araştırma sorularıyla ilişkilendir.
- Literatürle uyum ve ayrışma noktalarını belirt.
- Alternatif açıklamaları değerlendir.
- Yöntemsel sınırlılıkları saklama.
- Katkı iddiasını bulguların taşıyabileceği düzeyde tut.

## Yazılım hata tahmini bağlamında yorum ilkeleri

- Commit-level sonuçlar güçlü, file-level sonuçlar zayıfsa bunu granularity farkı, etiket güvenilirliği ve feature representation üzerinden tartış.
- MCC düşük ama F1 yüksekse prevalence ve sınıf dengesizliği bağlamını açıkla.
- Ablation sonucunda dil-özel metrik katkısı sınırlıysa bunu açık yaz; katkıyı abartma.
- Cross-project performans düşükse bunun negatif sonuç olarak değerini tartış.
- Bazı projelerde performans sapıyorsa repository heterogeneity, domain farkı veya veri kalitesiyle ilişkilendir.

## Güçlü tartışma paragrafı yapısı

1. Bulguyu açıkla.
2. Bu bulgunun araştırma sorusu için anlamını belirt.
3. Literatür veya yöntemsel beklentiyle ilişkilendir.
4. Alternatif açıklama veya sınırlılığı ekle.
5. Sonraki bulguya geçiş yap.

## Kaçınılacaklar

- Bulgular bölümünde uzun teorik yorum.
- Tartışmada tablo tekrarı.
- Beklenen sonucu desteklemeyen bulguları saklama.
- “Bu durum yöntemin başarılı olduğunu göstermektedir” gibi geniş ve kanıtsız sonuç.
