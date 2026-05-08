# Yöntem Bölümü Rehberi

Yöntem bölümü, tezin tekrar edilebilirliğinin ana dayanağıdır. Bu bölümde okuyucu çalışmanın nasıl yürütüldüğünü, hangi verilerin kullanıldığını ve analizlerin hangi protokolle yapıldığını açıkça izleyebilmelidir.

## Temel içerik

- Araştırma tasarımı
- Veri seti veya materyal
- Veri toplama/etiketleme süreci
- Özellik çıkarımı veya ölçüm süreci
- Deney protokolü
- Model, algoritma veya analiz araçları
- Değerlendirme metrikleri
- Geçerlilik tehditleri ve önlemler

## Bilgisayar bilimleri ve yazılım mühendisliği için zorunlu açıklık noktaları

1. Veri, benchmark, proje, katılımcı, iş yükü veya artifact kapsamı:
   - örneklem / veri büyüklüğü,
   - alan, domain, dil, sistem veya kullanıcı grubu,
   - analiz birimi,
   - zaman aralığı,
   - dahil etme / dışlama ölçütleri.

2. Etiketleme, anotasyon, ölçüm veya veri toplama:
   - etiket / ölçüm tanımı,
   - kullanılan araç, protokol veya insan değerlendirmesi,
   - yanlış pozitif/yanlış negatif, annotation disagreement veya measurement error riskleri,
   - filtreleme, deduplication veya cleaning varsa gerekçe.

3. Temsil ve özellikler:
   - feature families, model inputs, prompts, system measurements veya intervention components,
   - feature extraction / instrumentation aracı ve sürümü,
   - preprocessing, normalization, balancing veya transformation adımları.

4. Deney protokolü:
   - train/test ayrımı,
   - cross-domain, cross-project, user-level, temporal veya benchmark-level yapı,
   - preprocessing işlemlerinin yalnızca eğitim verisinde yapılıp yapılmadığı,
   - model seçimi ve hiperparametre ayarının fold-local olup olmadığı.

5. Metrikler:
   - göreve uygun başarı / hata / maliyet / kullanım / kalite metrikleri,
   - sınıf dengesizliği varsa positive-class F1, MCC, precision, recall, PR-AUC veya uygun alternatifler,
   - belirsizlik, varyans, güven aralığı, etki büyüklüğü veya istatistiksel test gerekçesi.

## İyi yöntem cümlesi

```text
Her dış fold’da hedef domain değerlendirme dışında tutulmuş; preprocessing, model seçimi ve hiperparametre ayarı yalnızca eğitim domainleri üzerinde yürütülmüştür. Böylece hedef domain, eğitim sürecinin hiçbir aşamasında kullanılmamıştır.
```

## Kaçınılacaklar

- “Veriler temizlenmiştir” deyip hangi işlemlerin yapıldığını yazmamak.
- “Modeller optimize edilmiştir” deyip arama uzayını ve doğrulama protokolünü belirtmemek.
- Test verisine uygulanan işlemleri eğitim süreciyle karıştırmak.
- Metrik seçimini gerekçelendirmemek.
