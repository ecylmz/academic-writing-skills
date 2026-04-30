# Installation Guide

Bu paket, herhangi bir proje dizinine `.agents/skills` yapısı olarak eklenmek üzere hazırlanmıştır.

## 1. Sadece Skill'leri Kurmak

Mevcut çalışma projenizin kök dizininde:

```bash
cp -R academic_writing_skill_suite/.agents .
cp academic_writing_skill_suite/AGENTS.md .
```

Bu kurulum, AI agent'ın proje talimatlarını ve skill klasörlerini okuması için yeterlidir.

## 2. Upstream Takibini de Kurmak

Referans alınan upstream projelerdeki güncellemeleri ayda bir takip etmek için ayrıca şu dosyaları kopyalayın:

```bash
cp -R academic_writing_skill_suite/.upstream .
cp -R academic_writing_skill_suite/.github .
cp -R academic_writing_skill_suite/tools .
```

GitHub reposuna push ettikten sonra `.github/workflows/upstream-watch.yml` her ay otomatik çalışır. Manuel çalıştırmak için GitHub Actions sekmesinden `Upstream Watch` workflow'unu seçip `Run workflow` kullanabilirsiniz.

## 3. Yerel Kontrol

Kurulumdan sonra:

```bash
python tools/check_skill_suite.py
```

Beklenen çıktı `status: ok` içeren bir JSON raporudur.

## 4. Manuel Upstream Kontrolü

GitHub token verilirse rate limit daha yüksek olur:

```bash
GITHUB_TOKEN=ghp_xxx python tools/check_upstream_updates.py \
  --sources .upstream/sources.json \
  --snapshot .upstream/snapshots/latest.json \
  --report .upstream/reports/upstream-report.md
```

Token verilmezse script public GitHub API ile çalışmayı dener; rate limit daha düşük olabilir.

## 5. Önerilen Kullanım

- Tez bölümü yazımı: `tez-yazimi-tr`
- Tez format kontrolü: `tez-latex-format-tr`
- Tez savunma/jüri riski: `tez-denetim-tr`
- İngilizce makale yazımı: `makale-yazimi-en`
- İngilizce makale hakem denetimi: `makale-denetim-en`
- Türkçe akademik üslup temizliği: `turkce-akademik-style-review`
- İngilizce akademik üslup temizliği: `academic-style-review-en`
- İddia–kanıt kontrolü: `claim-evidence-audit`
- Kaynakça ve atıf kontrolü: `citation-integrity-audit`

## 6. OMÜ LaTeX Şablonu

OMÜ tez şablonu dosyalarını tez projenizin içinde tutmanız önerilir. `tez-latex-format-tr` skill'i önce yerel LaTeX dosyalarını okuyacak, sonra kendi referans dosyalarındaki OMÜ kural özetini kullanacaktır.

Önerilen yerleşim:

```text
thesis-project/
  AGENTS.md
  .agents/skills/
  thesis.tex
  omu-thesis.cls
  references.bib
  chapters/
```

Gerçek şablon komutları bulunduğunda genel LaTeX komutlarıyla değiştirilmemelidir.
