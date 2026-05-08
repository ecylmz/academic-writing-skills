# Bilgisayar Bilimleri ve Yazılım Mühendisliği Tezi İçin Alan-Özel İlkeler

Bu referans; bilgisayar bilimleri, yazılım mühendisliği, yapay zekâ/makine öğrenmesi, sistemler, HCI, veri bilimi ve benzer teknik alanlardaki ampirik tezler için ek kurallar içerir. Hata tahmini, CPDP, SZZ veya Go veri kümeleri yalnızca örnek alt alanlardır.

## Deney protokolü şeffaflığı

- Hangi veri, benchmark, proje, katılımcı, iş yükü veya sistem ortamının hangi aşamada kullanıldığı açık yazılmalıdır.
- Test verisi, hedef domain/proje/kullanıcı/benchmark veya değerlendirme etiketi preprocessing, model/prompt seçimi, tuning, threshold belirleme veya feature selection aşamalarında kullanılmamalıdır.
- Random split kullanıldıysa temporal, project-aware, user-aware, domain-aware veya deployment-like split seçeneklerinin neden tercih edilmediği açıklanmalıdır.
- Stokastik deneylerde seed, tekrar sayısı, varyans, güven aralığı veya istatistiksel test bilgisi verilmelidir.

## Veri, ölçüm ve artifact anlatımı

- Veri veya benchmark seçim kriterleri.
- Zaman aralığı, kapsam, örneklem veya workload tanımı.
- Etiketleme, anotasyon, ölçüm, instrumentation veya veri toplama yöntemi.
- Label noise, annotation disagreement, measurement error veya sampling bias riskleri.
- Kullanılan araç, model, paket, donanım, sürüm, commit veya konfigürasyon bilgisi.
- Kod, veri, model, prompt, benchmark veya deney betiği paylaşımı ve erişim sınırları.

## Sonuç yorumlama

- Tek metrikle güçlü sonuç kurulmaz; görev türüne uygun metrikler birlikte yorumlanmalıdır.
- Dengesiz veride accuracy tek başına yeterli değildir; positive-class metrikler, MCC, PR-AUC veya göreve uygun alternatifler düşünülmelidir.
- Çok yüksek performans varsa leakage, benchmark contamination, duplicate data veya kolay örnek baskınlığı ayrıca kontrol edilmelidir.
- Negatif, karışık veya sınırlı sonuçlar saklanmamalıdır; hangi koşullarda yöntemin zorlandığı açıklanmalıdır.
- Genelleme iddiası veri, sistem, kullanıcı, domain, benchmark veya deney kapsamıyla sınırlanmalıdır.

## Tez katkısı türleri

- Yeni veri seti, benchmark veya artifact.
- Yeni yöntem, model, sistem, araç veya protokol.
- Yeni analiz, ölçüm, etiketleme veya değerlendirme hattı.
- Az çalışılmış bir alan, dil, domain, kullanıcı grubu veya sistem bağlamında ampirik bulgu.
- Granularity, domain, benchmark, model, kullanıcı veya workload karşılaştırması.
- Ablation, robustness veya validity odaklı metodolojik katkı.
- Tekrar edilebilirliği veya leakage kontrolünü güçlendiren deney tasarımı.

## Alt alan örnekleri

- Hata tahmini / CPDP: hedef projenin eğitim, preprocessing ve tuning dışında tutulması; SZZ veya etiketleme varsayımları; sınıf dengesizliği.
- ML/NLP/CV: benchmark contamination, prompt/model selection leakage, seed varyansı, veri sızıntısı.
- Sistemler: workload temsiliyeti, donanım/yazılım ortamı, warm-up, tekrar sayısı, tail latency.
- HCI: katılımcı seçimi, görev tasarımı, etik kurul, nitel kodlama güvenirliği, etki büyüklüğü.
- Veri madenciliği: örnekleme çerçevesi, deduplication, temporal leakage, kaynak güvenilirliği.
