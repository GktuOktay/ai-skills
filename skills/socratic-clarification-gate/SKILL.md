---
name: socratic-clarification-gate
description: Eksik veya varsayımlı taleplerde doğrudan kod yazmak yerine Sokratik sorularla gereksinimleri netleştiren güvenlik kapısı.
alwaysApply: false
---

# Socratic Clarification Gate & Requirement Inspector

Bu skill, kullanıcının talebi muğlak, eksik veya varsayımlara dayalı olduğunda yapay zekanın kendi kendine tahmin yürüterek yanlış kod yazmasını engeller. Doğrudan koda atlamak yerine Sokratik sorgulama yöntemiyle eksik gereksinimleri netleştirir.

---

## 🎯 Ne Zaman Tetiklenir?
- Kullanıcı talebinde mimari mimari detaylar (örn. "Veritabanına bağla", "Yetkilendirme ekle") muğlak kaldığında.
- Talepte 2 veya daha fazla kilit soru (Hangi veritabanı? Hangi ORM? Hangi auth sağlayıcı?) belirsiz olduğunda.
- Kullanıcı "Bunu hemen yap" dediğinde ama teknik bağlam eksik olduğunda.

---

## 🛑 Kurallar ve Kapı Koşulları (Gate Rules)

1. **Varsayımla Kod Yazma Yasağı:** Kullanıcı "Auth ekle" dediğinde sormadan Firebase, JWT veya NextAuth varsayarak 200 satır kod yazma.
2. **Maksimum 3 Odaklı Soru:** Kullanıcıyı bıkktırmamak için tek seferde en fazla 2-3 yüksek kaldıraçlı Sokratik soru sor.
3. **Seçenek Sunma:** Soruları sorarken en mantıklı 2-3 mimari seçeneği kısa gerekçeleriyle sun.

---

## 📐 Yanıt Formatı Örneği

> ✋ **Netleştirme Kapısı (Clarification Gate)**
> 
> İstenen yetkilendirme akışını en doğru mimariyle kurabilmem için 2 kilit noktayı netleştirmemiz gerekiyor:
> 
> 1. **Auth Stratejisi:** JWT tabanlı (Stateless) mı yoksa Session/Database tabanlı mı tercih edersiniz?
> 2. **Kullanıcı Rolleri:** Rol tabanlı erişim (RBAC) olacak mı (Admin, User vb.)?
> 
> *Seçiminize göre mimariyi hemen kurgulayabilirim.*
