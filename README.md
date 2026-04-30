# Academic Writing Skill Suite

Bu proje, tez ve makale yazımında AI destekli fakat insan denetimli akademik üretim için hazırlanmış modüler bir `.agents/skills` paketidir. Amaç tek bir uzun prompt yazmak değil; tez yazımı, makale yazımı, üslup düzeltme, iddia–kanıt denetimi, kaynakça denetimi ve LaTeX format kontrolünü ayrı ama birlikte çalışabilen skill'ler olarak düzenlemektir.

Proje üç upstream yaklaşımdan yararlanır:

1. `agent-style`: akademik/teknik metinlerde AI'ye özgü yazım kalıplarını azaltmaya dönük kural tabanlı ve semantik denetim yaklaşımı.
2. `Research-Paper-Writing-Skills`: abstract, introduction, method, experiments ve review mantığı gibi makale bölümü odaklı yazım rehberleri.
3. `academic-research-skills`: research → write → integrity → review → revise → finalize biçiminde kurgulanan daha geniş akademik üretim pipeline yaklaşımı.

Bu suite, bu projelerin birebir kopyası değildir. Türkçe tez yazımı, OMÜ tez biçim kuralları, yazılım mühendisliği araştırmaları ve İngilizce makale yazımı için sadeleştirilmiş ve yeniden düzenlenmiş bir uyarlamadır.

## Proje Yapısı

```text
.academic_writing_skill_suite/
├── AGENTS.md
├── README.md
├── INSTALL.md
├── SOURCE_NOTES.md
├── PROJECT_MANIFEST.json
├── VALIDATION_REPORT.md
├── .agents/
│   └── skills/
│       ├── akademik-yazim-suite/
│       ├── tez-yazimi-tr/
│       ├── tez-denetim-tr/
│       ├── tez-latex-format-tr/
│       ├── makale-yazimi-en/
│       ├── makale-denetim-en/
│       ├── academic-style-review-en/
│       ├── turkce-akademik-style-review/
│       ├── claim-evidence-audit/
│       ├── citation-integrity-audit/
│       └── _shared/
├── .upstream/
│   ├── README.md
│   ├── sources.json
│   ├── sources.yaml
│   ├── snapshots/
│   └── reports/
├── .github/
│   └── workflows/
│       └── upstream-watch.yml
├── examples/
└── tools/
    ├── check_skill_suite.py
    └── check_upstream_updates.py
```

## Skill Listesi

| Skill | Dil | Temel amaç |
|---|---:|---|
| `akademik-yazim-suite` | TR | Orkestratör skill. Kullanıcının ihtiyacına göre doğru alt skill'i seçtirir. |
| `tez-yazimi-tr` | TR | Türkçe tez bölümü yazma, yeniden yapılandırma ve bölüm bazlı akademik akış kurma. |
| `tez-denetim-tr` | TR | Tezi jüri, danışman ve savunma öncesi kalite bakışıyla denetleme. |
| `tez-latex-format-tr` | TR | OMÜ tez yazım kuralları ve LaTeX şablon uyumluluğu kontrolü. |
| `makale-yazimi-en` | EN | İngilizce araştırma makalesi bölümlerini yazma ve yeniden düzenleme. |
| `makale-denetim-en` | EN | Makaleyi hakem gözüyle değerlendirme; katkı, yöntem, deney ve yazım risklerini çıkarma. |
| `academic-style-review-en` | EN | İngilizce akademik metinde AI tarzı kalıpları, gereksiz sözcükleri ve claim calibration sorunlarını temizleme. |
| `turkce-akademik-style-review` | TR | Türkçe akademik metinde yapay çeviri kokusunu, aşırı kalıplaşmış ifadeleri ve belirsiz genellemeleri düzeltme. |
| `claim-evidence-audit` | TR/EN | İddiaları çıkarma, kanıtla eşleme, desteklenmeyen veya abartılı iddiaları sınıflandırma. |
| `citation-integrity-audit` | TR/EN | Atıf-kaynakça eşleşmesi, eksik kaynaklar, tutarsız citation style ve doğrulanamayan referansları denetleme. |

## Kurulum

Bu projeyi kendi çalışma dizinine kopyalamak için:

```bash
cp -R .agents /path/to/your/project/
cp AGENTS.md /path/to/your/project/
```

Upstream takip sistemi de kullanılacaksa şu dosyaları da kopyalayın:

```bash
cp -R .upstream /path/to/your/project/
cp -R .github /path/to/your/project/
cp -R tools /path/to/your/project/
```

Kurulum sonrası kontrol:

```bash
python tools/check_skill_suite.py
```

## Temel Kullanım

AI aracına şu türden açık komutlar verilebilir:

```text
Tezimin giriş bölümünü tez-yazimi-tr skill'ine göre değerlendir ve yeniden yapılandır.
```

```text
Use makale-yazimi-en to rewrite my Introduction. Preserve all claims and do not add unsupported citations.
```

```text
Bu bölümü claim-evidence-audit ile denetle. Her iddia için kanıt durumunu tablo halinde ver.
```

```text
Tezimi OMÜ LaTeX format kurallarına göre kontrol et. Yerel şablon dosyalarını önce oku.
```

## Önerilen Türkçe Tez İş Akışı

Türkçe tez yazımında tek seferde tüm tezi üretmeye çalışmak yerine bölüm bölüm ilerleyin.

```text
1. tez-yazimi-tr
   - bölüm amacı
   - bölüm taslağı
   - paragraf rolleri
   - ilk akademik taslak

2. claim-evidence-audit
   - ana iddialar
   - veri / literatür / yöntem kanıtları
   - desteklenmeyen ifadeler

3. turkce-akademik-style-review
   - yapay duran kalıplar
   - belirsiz genellemeler
   - gereksiz önem vurguları
   - Türkçeye uygun akademik ifade

4. tez-denetim-tr
   - jüri soruları
   - yöntemsel açıklar
   - savunma öncesi riskler
   - düzeltme öncelikleri

5. tez-latex-format-tr
   - OMÜ biçim kuralları
   - LaTeX komutları
   - sayfa, başlık, tablo, şekil, denklem, kaynakça kontrolü
```

## Önerilen İngilizce Makale İş Akışı

```text
1. makale-yazimi-en
   - paper story
   - section outline
   - paragraph roles
   - section draft

2. claim-evidence-audit
   - claim registry
   - claim-evidence alignment
   - unsupported or overstated claims

3. citation-integrity-audit
   - in-text citation / reference list consistency
   - missing references
   - citation style issues

4. academic-style-review-en
   - AI-like phrasing
   - excessive transitions
   - weak claim calibration
   - vague terms

5. makale-denetim-en
   - reviewer-risk analysis
   - contribution clarity
   - method soundness
   - experiment completeness
```

## OMÜ Tez ve LaTeX Şablonu Kullanımı

`tez-latex-format-tr` skill'i OMÜ tez yazım kurallarını ve kullanıcının yerel LaTeX şablonunu birlikte dikkate alacak şekilde tasarlanmıştır.

Öncelik sırası:

1. Kullanıcının proje dizinindeki gerçek OMÜ LaTeX şablon dosyaları.
2. Kullanıcının paylaştığı veya tez projesinde tuttuğu `.cls`, `.sty`, `.tex`, `.bib`, `Makefile`, `latexmkrc` dosyaları.
3. Skill içindeki `references/omu-tez-kurallari.md` dosyasında özetlenen OMÜ tez yazım kuralları.
4. Genel LaTeX iyi uygulamaları.

Skill, yerel şablon dosyaları varken genel bir LaTeX yapısı üretmemelidir. Var olan şablon komutları, bölüm sırası ve özel makrolar korunmalıdır.

## İddia–Kanıt Disiplini

Bu suite'te en önemli kalite ilkesi şudur: akademik metindeki her güçlü iddia ya çalışmanın kendi bulgusuyla ya da doğrulanabilir literatürle desteklenmelidir.

Örnek tablo:

| Claim | Evidence | Status | Action |
|---|---|---|---|
| Commit-level model outperforms file-level model. | Results Table 4, MCC/F1 comparison. | supported | Keep. |
| The proposed method is generally superior. | No cross-dataset evidence. | overstated | Narrow the claim. |
| Prior work ignores Go-specific features. | Literature review incomplete. | needs evidence | Add citations or weaken. |

Bu yaklaşım hem tez hem makale için geçerlidir.

## Upstream Takip Sistemi

Proje, referans aldığı üç upstream depoyu ayda bir otomatik kontrol edecek şekilde hazırlanmıştır.

İlgili dosyalar:

```text
.upstream/sources.json
.upstream/sources.yaml
.upstream/snapshots/latest.json
.upstream/reports/upstream-report.md
.github/workflows/upstream-watch.yml
tools/check_upstream_updates.py
```

GitHub Actions workflow'u her ayın ilk günü çalışır. Ayrıca manuel çalıştırmak için GitHub arayüzünden `workflow_dispatch` kullanılabilir.

Yerelde manuel kontrol:

```bash
GITHUB_TOKEN=... python tools/check_upstream_updates.py \
  --sources .upstream/sources.json \
  --snapshot .upstream/snapshots/latest.json \
  --report .upstream/reports/upstream-report.md
```

İlk çalıştırmada snapshot doldurulur. Sonraki çalıştırmalarda son görülen commit ile güncel commit karşılaştırılır ve sadece `watch_paths` içindeki değişiklikler raporlanır.

### Upstream Değişiklikleri İçin Karar Türleri

| Karar | Anlamı |
|---|---|
| `ignore` | Değişiklik bu projeyi etkilemiyor. |
| `port` | Fikir veya kontrol listesi yerel skill'e uyarlanacak. |
| `vendor` | Upstream dosya referans olarak saklanacak. |
| `defer` | Şimdilik bekletilecek, sonraki bakım turunda değerlendirilecek. |

Bu proje otomatik merge yapmaz. Bunun nedeni yerel uyarlamaların korunmasıdır.

## `agent-style` İçin Özel Politika

`agent-style` diğer upstream kaynaklardan farklıdır; yalnızca yazım rehberi değil, mekanik ve semantik denetim mantığı da içerir. Bu nedenle:

- `RULES.md` değişirse İngilizce ve Türkçe style-review skill'leri gözden geçirilmelidir.
- Python/NPM review modülleri değişirse bu değişiklikler doğrudan kopyalanmamalıdır.
- Türkçe akademik üslup kuralları İngilizceden birebir çevrilmemelidir.
- Gerekirse `academic-style-review-en` ve `turkce-akademik-style-review` ayrı ayrı güncellenmelidir.

## Bakım Akışı

Aylık upstream raporu geldiğinde:

```text
1. .upstream/reports/upstream-report.md dosyasını oku.
2. Relevant Changed Files listesini incele.
3. Her repo için ignore / port / vendor / defer kararı ver.
4. Port edilecekse ilgili yerel skill veya reference dosyasını düzenle.
5. python tools/check_skill_suite.py çalıştır.
6. SOURCE_NOTES.md dosyasını gerekirse güncelle.
7. Değişiklikleri commit et.
```

## Doğrulama

Bu pakette temel yapısal doğrulama aracı vardır:

```bash
python tools/check_skill_suite.py
```

Kontrol edilenler:

- Beklenen 10 skill dizini var mı?
- Her skill içinde `SKILL.md` var mı?
- Frontmatter `name` alanı dizin adıyla uyumlu mu?
- `SKILL.md` içinde anılan `references/` ve `templates/` dosyaları mevcut mu?
- `AGENTS.md`, upstream manifestleri ve GitHub Actions workflow'u mevcut mu?

## Tasarım Kararları

### Neden tek bir skill dosyası değil?

Tek dosya yaklaşımı hızlı görünür; fakat akademik yazımda kaliteyi sağlayan şey yalnızca birkaç talimat değildir. Bölüm şablonları, denetim listeleri, claim-evidence tabloları, citation kontrolü ve format kuralları ayrı dosyalarda tutulduğunda agent yalnızca gerekli bağlamı yükler. Bu da daha kontrollü ve sürdürülebilir sonuç verir.

### Neden upstream projeler doğrudan kullanılmadı?

Upstream projeler güçlüdür; ancak bu suite'in hedefi Türkçe tez yazımı, OMÜ LaTeX şablonu, İngilizce yazılım mühendisliği makaleleri ve kullanıcının doktora/makale iş akışıdır. Bu nedenle upstream mantığı korunmuş, içerik ise yerel ihtiyaca göre sadeleştirilmiş ve yeniden düzenlenmiştir.

### Neden otomatik update yok?

Akademik yazım kuralları ve tez biçim kuralları bağlama duyarlıdır. Upstream değişiklikler faydalı olabilir; fakat doğrudan merge edilirse yerel tez dili, OMÜ formatı veya software engineering odaklı denetimler bozulabilir. Bu nedenle otomatik rapor + insan kontrollü port yaklaşımı tercih edilmiştir.

## Lisans ve Atıf Notu

Bu proje, referans alınan upstream projelerden fikir ve yapı düzeyinde yararlanır. Ayrıntılar `SOURCE_NOTES.md` dosyasındadır. Eğer bu suite kamuya açık biçimde paylaşılacaksa upstream projelerin lisans koşulları ayrıca kontrol edilmelidir.
