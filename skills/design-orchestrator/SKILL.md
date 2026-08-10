---
name: design-orchestrator
description: "UI/UX tasarım, animasyon, görsel üretim ve frontend estetik süreçlerini yöneten orkestratör. Gerektiğinde alt skill'leri otomatik çağırır."
alwaysApply: false
---

# Design Orchestrator — Tasarım Süreçleri Yöneticisi

Sen bir orkestratörsün. Kullanıcının tasarım, UI/UX, animasyon veya görsel üretim talebini analiz et ve aşağıdaki alt skill'lerden hangilerini kullanman gerektiğini belirleyip **otomatik olarak çağır**.

---

## Yönettiğin Alt Skill'ler

### 1. `design-taste-frontend`
**Ne Zaman Çağır:**
- Yeni bir sayfa veya bileşen tasarlanacağında (tipografi, renk, spacing kararları)
- "Daha premium görünsün", "modern olsun", "profesyonel tasarım" istendiğinde
- Dark mode / light mode tasarımı yapılırken
- Mevcut tasarımın kalite incelemesi istendiğinde
- Bileşen stil standartları (button, card, form, shadow) konuşulduğunda

### 2. `ui-animation`
**Ne Zaman Çağır:**
- "Animasyon ekle", "geçiş efekti", "hover efekti" istendiğinde
- Sayfa geçişleri, modal açılış/kapanış efektleri tasarlanırken
- Mevcut animasyonların performans incelemesi (jank, frame drop) gerektiğinde
- Stagger, parallax, scroll-linked animasyon istendiğinde
- `prefers-reduced-motion` erişilebilirlik uyumu kontrol edilirken

### 3. `imagegen-frontend`
**Ne Zaman Çağır:**
- Hero görseli, illüstrasyon, ikon veya arka plan görseli üretilecekse
- App store screenshot mockup'ları oluşturulacaksa
- Blog/içerik için header görseli gerekiyorsa
- Görsel optimizasyon (WebP/AVIF, sıkıştırma, srcset) planlanıyorsa
- Prompt mühendisliği ile tutarlı marka görselleri üretilecekse

### 4. `product-designer`
**Ne Zaman Çağır:**
- Ürün seviyesinde UX akışı tasarlanacaksa (user journey, wireframe)
- Kullanıcı deneyimi sorunları analiz edilecekse
- Yeni bir özelliğin tasarım planlaması yapılacaksa
- Information architecture (bilgi mimarisi) kurgusunda

### 5. `feature-ideator`
**Ne Zaman Çağır:**
- Yeni ürün fikirleri ve özellik önerileri istendiğinde
- Feature backlog oluşturma veya önceliklendirme yapılırken
- Rakip analizi sonrası "biz ne ekleyelim" sorusu geldiğinde

### 6. `apple-design`
**Ne Zaman Çağır:**
- iOS, macOS veya visionOS projesi tasarlanırken
- Apple Human Interface Guidelines (HIG) standartları sorulduğunda
- SwiftUI tasarım ve navigasyon mimarisi konuşulurken

### 7. `high-end-visual-design`
**Ne Zaman Çağır:**
- Lüks, premium veya çok yüksek kaliteli bir UI hedeflendiğinde
- Glassmorphism, ince detaylar ve mikro-etkileşimler istendiğinde

### 8. `onboarding`
**Ne Zaman Çağır:**
- Yeni kullanıcı deneyimi (FTUE) veya karşılama akışı tasarlanırken
- Boş durumlar (empty states) ve izin isteme (permission requests) tasarlanırken

### 9. `prototype`
**Ne Zaman Çağır:**
- Hızlı prototipleme veya MVP süreçleri planlanırken
- Fikirden koda hızlı geçiş stratejisi gerektiğinde

### 10. `brandkit`
**Ne Zaman Çağır:**
- Marka kimliği (renkler, fontlar, logo kullanımı) oluşturulurken veya korunurken
- Marka ses tonu (tone of voice) belirlenirken

### 11. `copywriting`
**Ne Zaman Çağır:**
- UI içerikleri (microcopy), hata mesajları, buton metinleri yazılırken
- Pazarlama metinleri veya kullanıcıyı yönlendiren metinler oluşturulurken

---

## Orkestrasyon Kuralları

1. **Analiz Et:** Talebin kapsamını belirle — Sadece estetik mi? UX akışı mı? Görsel üretim mi?
2. **Sırala:** Doğal akışı takip et. Önce UX kararları → sonra görsel tasarım → sonra animasyon.
3. **Çağır:** İlgili SKILL.md dosyalarını oku ve talimatlarına göre hareket et.
4. **Tutarlılık:** Birden fazla skill çağırdığında, çıktılar arasında stil tutarlılığını sağla (aynı renk paleti, aynı tipografi, aynı animasyon easing).
5. **Geri Bildir:** Hangi tasarım kararlarını hangi skill ile aldığını belirt.

### Ortak Akış Örnekleri

| Kullanıcı Talebi | Çağrılacak Skill'ler (Sıralı) |
|---|---|
| "Landing page tasarla" | `product-designer` → `design-taste-frontend` → `ui-animation` → `imagegen-frontend` |
| "Bu sayfayı daha modern yap" | `design-taste-frontend` → `ui-animation` |
| "Onboarding akışı tasarla" | `product-designer` → `design-taste-frontend` → `imagegen-frontend` |
| "Hero section için görsel üret" | `imagegen-frontend` |
| "Uygulamaya animasyon ekle" | `ui-animation` |
| "Yeni feature fikirleri ver" | `feature-ideator` → `product-designer` |
| "Dashboard'u redesign et" | `product-designer` → `design-taste-frontend` → `ui-animation` |

---

## Çağırmaman Gereken Durumlar
- Sadece renk kodu veya font ismi soruluyorsa (doğrudan cevap ver)
- Kullanıcı açıkça belirli bir skill istiyorsa, orkestratör yerine o skill'i direkt çağır
