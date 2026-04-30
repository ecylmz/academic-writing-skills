# Yazılım Mühendisliği Tezi İçin Alan-Özel İlkeler

Bu referans, yazılım hata tahmini, hataya yatkınlık tahmini, veri seti oluşturma, makine öğrenmesi deneyleri ve cross-project defect prediction çalışmaları için ek kurallar içerir.

## Deney protokolü şeffaflığı

- Hangi veri hangi aşamada kullanıldı açık yazılmalıdır.
- Target repository, preprocessing/tuning/model selection sürecinden dışlanmışsa bu açıkça belirtilmelidir.
- Feature selection, scaling, balancing ve imputation işlemleri train-only değilse risk olarak işaretlenmelidir.
- Random split kullanıldıysa neden time-aware veya project-aware split tercih edilmediği açıklanmalıdır.

## Veri seti anlatımı

- Repository seçim kriterleri
- Zaman aralığı
- Commit/file/method etiket sayıları
- Etiketleme algoritması ve varsayımlar
- Noise ve validity riskleri
- Dil-özel özelliklerin nasıl çıkarıldığı

## Sonuç yorumlama

- Accuracy tek başına yeterli değildir.
- Dengesiz veride positive-class F1 ve MCC birlikte yorumlanmalıdır.
- Çok yüksek performans varsa leakage ihtimali ayrıca kontrol edilmelidir.
- Negatif sonuçlar saklanmamalıdır; hangi koşullarda transferin zor olduğu açıklanmalıdır.

## Tez katkısı türleri

- Yeni veri seti
- Yeni etiketleme veya özellik çıkarımı hattı
- Yeni deney protokolü
- Go gibi az çalışılmış bir dil bağlamında ampirik bulgu
- Granularity karşılaştırması
- Dil-özel feature ablation
- Leakage azaltan deney tasarımı
