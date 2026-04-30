# Source Notes

Bu paket doğrudan kopyalanmış bir upstream dağıtımı değildir. Aşağıdaki projelerdeki fikirler sentezlenerek, tez ve makale yazımı için daha sade ve agent-bağımsız bir yapıya dönüştürülmüştür.

## İncelenen projeler

- `yzhao062/agent-style`: teknik ve akademik metinlerde okuyucu bilgisi, somut dil, gereksiz sözcükleri azaltma, claim calibration, citation discipline ve AI-output kalıplarını azaltma ilkeleri.
- `Master-cai/Research-Paper-Writing-Skills`: abstract/introduction/method/experiment gibi makale bölümleri için story-first writing, reverse outlining, paragraph role ve claim-evidence map yaklaşımı.
- `Imbad0202/academic-research-skills`: akademik pipeline, integrity gate, citation check, reviewer simulation, style calibration ve writing quality check kavramları.

## OMÜ tez kuralları

Tez skill'leri, Ondokuz Mayıs Üniversitesi Lisansüstü Eğitim Enstitüsü'nün resmi tez yazım sayfasında yayımlanan tez yazım kılavuzundaki biçim ve bölüm kurallarına göre hazırlanmıştır. LaTeX ZIP dosyası bu ortamda açılamadığı için gerçek şablon komutları birebir çıkarılamamıştır. Bunun yerine:

1. Resmi kılavuzdaki biçim kuralları `tez-latex-format-tr/references/omu-tez-kurallari.md` dosyasına aktarıldı.
2. Skill'lere, yerel LaTeX şablonu mevcutsa önce `.cls`, `.sty`, ana `.tex` ve örnek dosyaları okuma kuralı eklendi.
3. Agent'ın OMÜ şablonunda tanımlı komutları yeniden yazmaması, mevcut komutları ve dosya düzenini koruması istendi.

## Kullanım sınırı

Bu skill'ler akademik yazımı, tutarlılığı ve denetimi destekler; bilimsel kararın, yöntemsel sorumluluğun ve son metin onayının yerini almaz. Özellikle tez ve makalede kullanılan deney sonuçları, istatistikler, kaynaklar ve etik beyanlar araştırmacı tarafından doğrulanmalıdır.

## Upstream Tracking Policy

This suite now includes a lightweight upstream tracking system under `.upstream/` and `.github/workflows/upstream-watch.yml`.

Tracked sources:

1. `yzhao062/agent-style`
2. `Master-cai/Research-Paper-Writing-Skills`
3. `Imbad0202/academic-research-skills`

The tracking system reports relevant upstream changes but does not merge or overwrite local files. All updates must be reviewed manually because this suite contains Turkish thesis writing adaptations, OMÜ thesis-format references, and software-engineering-specific academic writing rules.

When upstream content is ported into this suite, update this file with a short note describing:

- upstream repository and file consulted,
- local file changed,
- whether the change was translated, summarized, or structurally adapted,
- date of the maintenance decision.
