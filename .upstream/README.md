# Upstream Tracking

Bu dizin, bu skill suite'in beslendiği üç upstream projedeki değişiklikleri takip etmek için kullanılır.

## Dosyalar

- `sources.json`: Makine tarafından okunan takip manifesti.
- `sources.yaml`: İnsan tarafından okunabilir manifest kopyası.
- `snapshots/latest.json`: Son görülen commit kayıtları.
- `reports/`: Aylık fark raporları.

## Politika

Bu proje upstream depoları doğrudan otomatik olarak içeri almaz. Her değişiklik önce raporlanır, sonra insan kararıyla işlenir.

Karar türleri:

- `ignore`: Değişiklik bu projeyi etkilemiyor.
- `port`: Fikir, kontrol listesi veya şablon yerel skill'e uyarlanacak.
- `vendor`: Upstream dosya referans olarak ayrı tutulacak.
- `defer`: Değişiklik sonraki bakım turunda yeniden değerlendirilecek.

## Neden otomatik merge yok?

Bu suite, upstream projelerin birebir kopyası değildir. Türkçe tez yazımı, OMÜ tez şablonu, yazılım mühendisliği makaleleri ve kullanıcıya özgü akademik iş akışı için uyarlanmıştır. Upstream içerik doğrudan merge edilirse yerel terminoloji, Türkçe akademik üslup ve tez formatı kuralları bozulabilir.
