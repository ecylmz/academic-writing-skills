# Literatür Bölümü Rehberi

Literatür bölümü çalışmaların arka arkaya özetlendiği bir katalog olmamalıdır. Bu bölüm, tezin problemini kuran ve çalışmanın konumunu gösteren analitik bir bölüm olmalıdır.

## Temel amaç

- Alanın hangi problemler etrafında geliştiğini göstermek.
- Mevcut yöntemleri tematik veya yöntemsel olarak gruplamak.
- Tezin hangi boşluğu veya sınırlılığı ele aldığını kanıtlamak.
- Kullanılan kavramları ve kuramsal zemini yerleştirmek.

## Önerilen yapı

1. Kavramsal zemin
2. Ana araştırma hattı
3. Yöntemsel yaklaşımlar
4. Veri setleri ve deney protokolleri
5. Eksik kalan noktalar
6. Bu tezin konumu

## Bilgisayar bilimleri ve yazılım mühendisliği için gruplama örnekleri

- Problem veya görev türleri.
- Model, yöntem, sistem, algoritma veya araç aileleri.
- Veri seti, benchmark, workload, domain, kullanıcı grubu veya analiz birimi.
- Etiketleme, anotasyon, ölçüm, instrumentation veya veri toplama yaklaşımları.
- Evaluation protocol: random split, temporal split, cross-domain, cross-project, user-level, nested validation.
- Metrik, baseline, ablation, robustness ve leakage-control yaklaşımları.
- Artifact, kod, veri ve tekrar edilebilirlik uygulamaları.

## Paragraf kalıbı

Zayıf kalıp:

```text
A çalışması X yapmıştır. B çalışması Y yapmıştır. C çalışması Z yapmıştır.
```

Daha iyi kalıp:

```text
Bu çalışma hattında temel ayrım, değerlendirmenin hangi bağlamda ve hangi analiz biriminde yapıldığıdır. Bazı çalışmalar örnek veya veri seti düzeyinde performansa odaklanırken, bazıları domain, proje, kullanıcı, zaman veya sistem ortamı düzeyinde genelleme risklerini inceler. Bu ayrımlar, eğitim ve değerlendirme verisinin nasıl ayrıldığına bağlı olarak farklı geçerlilik riskleri taşır.
```

## Kontrol soruları

- Literatür bölümü tezin araştırma sorularına hizmet ediyor mu?
- Her alt başlık bir tema veya tartışma ekseni kuruyor mu?
- Çalışmalar yalnızca “kim ne yaptı” şeklinde mi anlatılmış?
- Tezin boşluğu sonradan eklenmiş gibi mi duruyor, yoksa literatürden doğal biçimde mi çıkıyor?
