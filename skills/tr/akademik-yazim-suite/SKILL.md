---
name: akademik-yazim-suite
description: Tez, makale, denetim, claim-evidence audit, citation integrity audit ve style review işlemleri arasında seçim yapan agent-bağımsız akademik yazım orkestratörü. Doğrudan metin üretmek yerine uygun alt skill'i seçer ve süreç akışını korur.
---

# Akademik Yazım Suite

Bu skill bir orkestratördür. Asıl yazım, denetim veya biçim kontrolü işini alt skill'ler yapar.

## Ne zaman kullanılır?

Kullanıcı aşağıdakilerden birini istediğinde bu skill'i kullan:

- Türkçe tez bölümü yazmak, genişletmek veya düzenlemek.
- Tez metnini danışman, jüri veya savunma öncesi bakışla değerlendirmek.
- OMÜ LaTeX şablonuna ve tez yazım kurallarına uyumu kontrol etmek.
- İngilizce makale bölümü yazmak veya revize etmek.
- Makaleyi hakem bakışıyla değerlendirmek.
- Metindeki iddiaların kanıtla uyumunu kontrol etmek.
- Kaynak, atıf ve referans tutarlılığını denetlemek.
- AI tarafından üretilmiş gibi duran akademik metni daha doğal, ölçülü ve hatasız hâle getirmek.

## Otomatik seçim ilkesi

Kullanıcı açıkça skill adı vermediyse niyeti anahtar ifadelerden çıkar:

- `tez`, `bölüm`, `giriş`, `literatür`, `yöntem`, `bulgular`, `tartışma`, `sonuç`, `özet` ve `Türkçe` ifadeleri geçiyorsa varsayılan skill `tez-yazimi-tr` olmalıdır.
- `jüri`, `savunma`, `danışman gözüyle`, `risk`, `eleştir`, `zayıf noktalar`, `hazır mı` ifadeleri geçiyorsa `tez-denetim-tr` seçilmelidir.
- `OMÜ`, `LaTeX`, `şablon`, `format`, `biçim`, `.cls`, `.sty`, `.tex` ifadeleri geçiyorsa `tez-latex-format-tr` seçilmelidir.
- `yapay duruyor`, `akademik Türkçe`, `üslup`, `doğallaştır`, `sadeleştir`, `çeviri kokuyor` ifadeleri geçiyorsa `turkce-akademik-style-review` seçilmelidir.
- `iddia`, `kanıt`, `destekli mi`, `overclaim`, `abartı` ifadeleri geçiyorsa `claim-evidence-audit` seçilmelidir.
- `kaynakça`, `atıf`, `BibTeX`, `DOI`, `referans` ifadeleri geçiyorsa `citation-integrity-audit` seçilmelidir.

## Alt skill seçim tablosu

| Kullanıcı ihtiyacı | Kullanılacak skill |
|---|---|
| Türkçe tez bölümü yazımı veya revizyonu | `tez-yazimi-tr` |
| Türkçe tez metninin jüri/savunma öncesi denetimi | `tez-denetim-tr` |
| OMÜ LaTeX şablonu ve biçim kontrolü | `tez-latex-format-tr` |
| İngilizce makale bölümü yazımı veya revizyonu | `makale-yazimi-en` |
| İngilizce makale hakem riski denetimi | `makale-denetim-en` |
| Türkçe akademik üslup temizliği | `turkce-akademik-style-review` |
| İngilizce akademik üslup temizliği | `academic-style-review-en` |
| İddia-kanıt eşlemesi | `claim-evidence-audit` |
| Kaynakça/atıf doğrulama | `citation-integrity-audit` |

## Süreç mantığı

### Tez için önerilen sıra

1. `tez-yazimi-tr` ile bölüm veya paragraf düzeyinde çalışma.
2. `claim-evidence-audit` ile temel iddiaları kanıtla eşleştirme.
3. `tez-denetim-tr` ile metodolojik ve yapısal riskleri çıkarma.
4. `turkce-akademik-style-review` ile Türkçe akademik üslubu temizleme.
5. `tez-latex-format-tr` ile OMÜ şablonuna uyum kontrolü.

### Makale için önerilen sıra

1. `makale-yazimi-en` ile bölüm bazlı yazım.
2. `claim-evidence-audit` ile major claims kontrolü.
3. `makale-denetim-en` ile reviewer-risk denetimi.
4. `academic-style-review-en` ile akademik üslup temizliği.
5. `citation-integrity-audit` ile atıf ve kaynakça kontrolü.

## Orkestratör kuralları

- Doğrudan bölüm yazma; uygun alt skill'i seç.
- Kullanıcı yalnızca “tez bölümünü düzenle” diyorsa varsayılan olarak `tez-yazimi-tr` seç.
- Kullanıcı “hakem gibi değerlendir” diyorsa makale için `makale-denetim-en`, tez için `tez-denetim-tr` seç.
- Kullanıcı kaynak/atıf doğruluğu istiyorsa `citation-integrity-audit` seç.
- Kullanıcı “AI yazmış gibi duruyor” diyorsa dile göre style review seç.
- Kullanıcı aynı anda birden çok iş isterse sırayı açıkla ve ilk uygulanacak skill'i belirt.
- Eksik veri varsa bunu uydurma; hangi dosya, tablo, kaynak veya sonuç gerektiğini listele.
- Türkçe tez işlerinde önce akademik savunulabilirliği, sonra üslubu, en son biçimi kontrol et.
- Sadece dil düzeltmesi isteyen kullanıcıda bile güçlü akademik iddia, kaynak veya yöntem riski fark edilirse bunu kısa risk notu olarak bildir.

## Çıktı sözleşmesi

Alt skill yönlendirmesi yaparken şu formatı kullan:

```text
Önerilen skill: <skill-name>
Neden: <kısa gerekçe>
Girdi olarak gerekli materyal: <dosya/metin/veri>
Önerilen sonraki adım: <sıradaki skill veya denetim>
```
