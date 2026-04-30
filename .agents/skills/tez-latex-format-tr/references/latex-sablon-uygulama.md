# LaTeX Şablon Uygulama Rehberi

Bu rehber, OMÜ LaTeX şablonu yerel projeye eklendiğinde agent'ın nasıl davranması gerektiğini tanımlar.

## Önce keşif

Agent önce dosya yapısını çıkarmalıdır:

```text
.
├── main.tex / thesis.tex / tez.tex
├── *.cls
├── *.sty
├── references.bib
├── chapters/
├── figures/
└── tables/
```

## Komut çıkarımı

Aşağıdaki komut ve ortamlar listelenmelidir:

- `\documentclass{...}`
- `\usepackage{...}`
- Kapak bilgisi komutları
- Danışman/jüri/ana bilim dalı komutları
- Özet/abstract komutları
- Bölüm ekleme komutları
- Kaynakça komutları
- Şekil/tablo/denklem komutları
- Özel sayfa komutları

## Güvenli revizyon ilkeleri

- Şablonun tanımladığı komutları koru.
- Kullanılmayan gibi görünen komutları silmeden önce nerede işlendiğini bul.
- `\include`, `\input`, `\bibliography`, `\addcontentsline`, `\frontmatter`, `\mainmatter` benzeri yapıları dikkatli incele.
- Türkçe karakter ve font ayarlarını rastgele değiştirme.
- XeLaTeX/LuaLaTeX/pdfLaTeX derleme farklarını kontrol et.
- Kullanıcı istemedikçe `.cls` dosyasında değişiklik yapma.

## Raporlama

```text
## Şablon Dosya Haritası
## Özel Komutlar
## OMÜ Kural Uyumu
## Riskli Noktalar
## Önerilen Düzeltmeler
```

## Farklılık yönetimi

Eğer yerel şablon kılavuzdan farklı bir biçim uyguluyorsa:

1. Farkı açıkça yaz.
2. Şablonun resmi kaynak olup olmadığını sor.
3. Kesin biçimsel değişiklik önermeden önce kullanıcıdan veya enstitü güncel dokümanından doğrulama iste.
