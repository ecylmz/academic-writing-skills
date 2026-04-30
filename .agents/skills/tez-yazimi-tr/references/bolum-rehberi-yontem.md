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

## Yazılım hata tahmini için zorunlu açıklık noktaları

1. Veri setinin kapsamı:
   - proje sayısı,
   - programlama dili,
   - commit/file/method sayıları,
   - zaman aralığı,
   - filtreleme ölçütleri.

2. Etiketleme:
   - hata-inducing ve bug-fixing commit tanımı,
   - kullanılan SZZ varyantı veya pratik yaklaşım,
   - yanlış pozitif/yanlış negatif riskleri,
   - ignore list veya filtreleme varsa gerekçe.

3. Özellikler:
   - process metrics,
   - static metrics,
   - language-specific metrics,
   - feature extraction aracı ve sürümü.

4. Deney protokolü:
   - train/test ayrımı,
   - cross-project veya leave-one-project-out yapı,
   - preprocessing işlemlerinin yalnızca eğitim verisinde yapılıp yapılmadığı,
   - model seçimi ve hiperparametre ayarının fold-local olup olmadığı.

5. Metrikler:
   - positive-class F1,
   - MCC,
   - precision,
   - recall,
   - AUC veya diğerleri,
   - class imbalance bağlamında yorum gerekçesi.

## İyi yöntem cümlesi

```text
Her dış fold’da bir Go deposu hedef proje olarak ayrılmış; preprocessing, model seçimi ve hiperparametre ayarı yalnızca kalan eğitim projeleri üzerinde yürütülmüştür. Böylece hedef proje, eğitim sürecinin hiçbir aşamasında kullanılmamıştır.
```

## Kaçınılacaklar

- “Veriler temizlenmiştir” deyip hangi işlemlerin yapıldığını yazmamak.
- “Modeller optimize edilmiştir” deyip arama uzayını ve doğrulama protokolünü belirtmemek.
- Test verisine uygulanan işlemleri eğitim süreciyle karıştırmak.
- Metrik seçimini gerekçelendirmemek.
