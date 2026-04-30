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

## Yazılım mühendisliği için gruplama örnekleri

- Within-project defect prediction vs cross-project defect prediction.
- Commit-level, file-level, method-level tahmin.
- Process metrics, static metrics, language-specific metrics.
- Class imbalance ve data balancing yaklaşımları.
- SZZ ve defect labeling yöntemleri.
- Evaluation protocol: random split, time-aware split, LOPO, nested LOPO.
- Model aileleri: classical ML, ensemble, deep learning, transformer-based yaklaşımlar.

## Paragraf kalıbı

Zayıf kalıp:

```text
A çalışması X yapmıştır. B çalışması Y yapmıştır. C çalışması Z yapmıştır.
```

Daha iyi kalıp:

```text
Bu çalışma hattında temel ayrım, tahminin hangi granularity düzeyinde yapıldığıdır. Commit-level çalışmalar değişiklik geçmişinden yararlanırken, file-level çalışmalar modül düzeyindeki yapısal ve süreçsel özelliklere odaklanır. Ancak bu iki yaklaşım, hedef projenin eğitim sürecinden tamamen dışlandığı cross-project senaryolarda farklı geçerlilik riskleri taşır.
```

## Kontrol soruları

- Literatür bölümü tezin araştırma sorularına hizmet ediyor mu?
- Her alt başlık bir tema veya tartışma ekseni kuruyor mu?
- Çalışmalar yalnızca “kim ne yaptı” şeklinde mi anlatılmış?
- Tezin boşluğu sonradan eklenmiş gibi mi duruyor, yoksa literatürden doğal biçimde mi çıkıyor?
