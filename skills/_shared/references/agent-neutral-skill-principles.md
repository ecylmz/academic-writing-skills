# Agent-Neutral Skill Principles

Bu suite belirli bir agent platformuna bağlı değildir. Skill dosyaları, çalıştırma komutları veya host-specific slash command varsayımları yerine görev, girdi, süreç ve çıktı sözleşmesi tanımlar.

## Genel ilkeler

1. Önce kullanıcının hedefini ve mevcut materyali belirle.
2. Eksik materyal varsa bunu uydurma; `[MATERIAL GAP]` olarak işaretle.
3. Revizyonlarda mevcut anlamı koru; yeni veri, yeni kaynak, yeni sonuç veya yeni deney icat etme.
4. Her önemli iddiayı en az bir destek türüyle eşleştir: kaynak, deney sonucu, tablo/şekil, yöntem gerekçesi veya açık sınırlılık beyanı.
5. LaTeX, Markdown, BibTeX ve kod bloklarının yapısını koru.
6. Çıktıda gerekli olduğunda hem revize metin hem de denetim raporu ver.

## Dosya koruma kuralları

- Kullanıcı açıkça istemedikçe kaynak dosyayı doğrudan değiştirme.
- Revizyon önerisi veriyorsan önce farkları ve gerekçeyi bildir.
- LaTeX komutlarını sadeleştirmek için silme; önce ne işe yaradığını belirle.
- Atıf anahtarlarını değiştirme; bozuk görünüyorsa raporla.
