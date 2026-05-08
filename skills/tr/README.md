# Türkçe Akademik Yazım Skill'leri

Bu dizin Türkçe tez yazımı, tez denetimi, OMÜ LaTeX format kontrolü ve Türkçe akademik üslup temizliği için hazırlanmış skill'leri içerir. Temel ilke, metni yalnızca daha akıcı yapmak değil; araştırma problemi, yöntem, kanıt, katkı, sınırlılık ve biçim açısından savunulabilir hâle getirmektir.

## Hangi skill ne zaman kullanılır?

| İhtiyaç | Kullanılacak skill | Tipik çıktı |
|---|---|---|
| Tez bölümü yazmak, genişletmek veya yeniden yapılandırmak | `tez-yazimi-tr` | Mini taslak, paragraf rolleri, revize metin, denetim notları |
| Tezi danışman/jüri/savunma öncesi gözle değerlendirmek | `tez-denetim-tr` | Kritik riskler, iddia-kanıt kontrolü, jüri soruları, revizyon planı |
| OMÜ tez şablonu, LaTeX komutları ve biçim kurallarını kontrol etmek | `tez-latex-format-tr` | Şablon keşfi, OMÜ kural kontrolü, LaTeX riskleri |
| Türkçe akademik metni doğal, ölçülü ve tutarlı hale getirmek | `turkce-akademik-style-review` | Üslup sorunları, revize metin, iddia kalibrasyonu, kalan riskler |
| Hangi skill'in uygun olduğuna karar vermek | `akademik-yazim-suite` | Skill seçimi, gerekçe, gerekli materyal, sonraki adım |

TR iş akışında `claim-evidence-audit` ve `citation-integrity-audit` skill'leri `skills/en` altında dursa da dil bağımsız denetim için kullanılabilir. Tez metninde iddia desteği veya kaynakça tutarlılığı soruluyorsa bu iki skill'i sürece dahil edin.

## Önerilen tez iş akışı

1. `tez-yazimi-tr`: Bölümün amacını, araştırma sorusuyla bağını ve paragraf akışını kur.
2. `claim-evidence-audit`: Güçlü iddiaların kanıtla eşleşip eşleşmediğini denetle.
3. `tez-denetim-tr`: Jüri/danışman bakışıyla metodolojik, yapısal ve savunulabilirlik risklerini çıkar.
4. `turkce-akademik-style-review`: Dil, terim tutarlılığı, ölçülülük ve yapay kalıpları temizle.
5. `citation-integrity-audit`: Atıf-kaynakça eşleşmesi ve kaynak desteğini kontrol et.
6. `tez-latex-format-tr`: OMÜ şablonu, başlıklar, numaralandırma, tablo/şekil ve kaynakça biçimini kontrol et.

Bu sıra zorunlu değildir. Kullanıcının isteği dar ise yalnızca ilgili skill'i kullanın.

## Otomatik tetikleme için anahtar ifadeler

Bir agent skill seçimini otomatik yapacaksa kullanıcı isteğindeki niyeti şu ifadelerle eşleştirebilir:

| Kullanıcı ifadesi | Skill |
|---|---|
| `tez bölümümü yaz`, `giriş bölümünü düzenle`, `literatürü toparla`, `yöntem bölümünü akademik hale getir` | `tez-yazimi-tr` |
| `jüri gözüyle değerlendir`, `savunma öncesi risk`, `danışman gibi eleştir`, `zayıf noktaları bul`, `tez hazır mı` | `tez-denetim-tr` |
| `OMÜ format`, `LaTeX şablonu`, `.cls`, `.sty`, `sayfa numarası`, `tablo/şekil başlığı`, `tez biçimi` | `tez-latex-format-tr` |
| `yapay duruyor`, `akademik Türkçeye çevir`, `üslubu düzelt`, `çeviri kokuyor`, `daha doğal yaz` | `turkce-akademik-style-review` |
| `iddialar destekli mi`, `kanıtla eşleştir`, `abartılı iddia`, `overclaim` | `claim-evidence-audit` |
| `kaynakça kontrolü`, `atıf tutarlılığı`, `BibTeX`, `DOI`, `referans eksik mi` | `citation-integrity-audit` |
| `hangi skill'i kullanmalıyım`, `tez için doğru süreç ne`, `önce ne yapmalıyım` | `akademik-yazim-suite` |

## Kullanım örnekleri

```text
Bu metni tez-yazimi-tr ile giriş bölümü olarak yeniden yapılandır. Araştırma problemi, literatür boşluğu ve katkı daha görünür olsun. Kaynak ve teknik anlam ekleme.
```

```text
Bu yöntemi tez-denetim-tr ile jüri gözüyle değerlendir. Tekrar edilebilirlik, veri sızıntısı, metrik seçimi ve sınırlılıklar açısından riskleri P0-P3 olarak sınıflandır.
```

```text
Bu bölümü turkce-akademik-style-review ile düzelt. Yapay kalıpları temizle, iddiaları kanıt gücüne göre yumuşat, LaTeX komutlarını ve atıfları koru.
```

```text
Bu LaTeX projesini tez-latex-format-tr ile kontrol et. Önce yerel .cls, .sty, ana .tex ve .bib dosyalarını keşfet; sonra OMÜ biçim risklerini raporla.
```

## Girdi hazırlama

İyi sonuç için kullanıcıdan mümkünse şu materyaller istenir:

- Hedef bölüm türü: giriş, literatür, yöntem, bulgular, tartışma, sonuç, özet.
- Mevcut metin veya taslak.
- Araştırma soruları / hipotezler.
- Veri seti, yöntem, deney protokolü veya analiz notları.
- Tablo, şekil, metrik veya sonuç özeti.
- Kullanılan atıf stili ve kaynakça dosyası.
- LaTeX projesi için ana `.tex`, `.cls`, `.sty`, `.bib` ve derleme dosyaları.

Eksik materyal varsa agent bunu uydurmamalı; `[MATERIAL GAP]`, `[VERIFY SOURCE]`, `[METHOD GAP]` veya `requires verification` olarak işaretlemelidir.

## Akademik öncelikler

TR skill'lerde öncelik sırası şudur:

1. Yanlış, desteksiz veya fazla güçlü iddiayı düzeltmek.
2. Araştırma problemi, araştırma sorusu, yöntem, bulgu ve sonuç bağını kurmak.
3. Yöntemi tekrar edilebilir hale getirecek ayrıntıları görünür yapmak.
4. Katkı türünü ve sınırını açık yazmak.
5. Sınırlılıkları ve geçerlilik tehditlerini dürüstçe belirtmek.
6. Terim tutarlılığı, paragraf akışı ve Türkçe akademik üslubu iyileştirmek.
7. OMÜ biçim ve LaTeX şablon uyumunu kontrol etmek.

## Kaçınılması gerekenler

- Kaynak, DOI, veri, sonuç, metrik veya jüri beklentisi uydurmak.
- Eksik kanıtı güçlü akademik üslupla kapatmak.
- Her metni otomatik olarak parlatılmış tanıtım metnine dönüştürmek.
- Tez katkısını veri veya bulguların taşıyabileceğinden geniş yazmak.
- LaTeX komutlarını, atıf anahtarlarını, tablo/şekil referanslarını ve denklem yapılarını anlamadan değiştirmek.
- Style review'i AI kullanımını gizleme amacıyla kullanmak.
