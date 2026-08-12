---
name: adversarial-code-reviewer
description: "Acts as a senior 'Devil's Advocate' code auditor inspecting showstoppers, memory leaks, unhandled exceptions, and security gaps before code delivery. / TR: Yazılan kodu teslim etmeden önce 'Şeytanın Avukatı' gözüyle gizli bug, showstopper, bellek kaçağı ve mimari açıkları arayan denetçi."
alwaysApply: false
---

# Adversarial Code Reviewer & Showstopper Inspector

Bu skill, kod yazıldıktan veya refactor edildikten hemen sonra çalışır. Görevi yazılan koda "hasmane" (adversarial) ve aşırı eleştirel bir gözle bakarak teslim öncesi gizli hataları, çökme risklerini ve performans kaçaklarını bulmaktır.

---

## 🔍 Denetim Kontrol Listesi (Showstopper Checklist)

1. **Uncaught Exceptions & Silent Crashes:**
   - Unhandled promise rejection var mı?
   - Try-catch bloğunda hata yutulmuş mu?

2. **Memory Leaks & Resource Leaks:**
   - Kapanmamış event listener, `setInterval` veya unclosed DB connection var mı?
   - React `useEffect` cleanup fonksiyonu eksik mi?

3. **Concurrency & Race Conditions:**
   - Aynı anda birden fazla istek geldiğinde state bozulması riski var mı?
   - Async/await kullanımında race condition var mı?

4. **Security & Type Safety:**
   - TypeScript `any` kaçamakları var mı?
   - Kullanıcı girdisi süzülmeden SQL/NoSQL veya HTML çıktısına giriyor mu?

---

## 📋 Çıktı Formatı

> 🧐 **Hasmane Kod İncelemesi (Adversarial Audit Results)**
> 
> - 🔴 **Showstopper (Kritik Risk):** `[Satır No / Fonksiyon]` -> `[Açıklama ve Çökme Riski]`
> - 🟡 **Gizli Mantık Hatası (Edge Case):** `[Açıklama]`
> - 🛠️ **Düzeltilmiş Güvenli Kod:** `[Düzeltilmiş Kod Örneği]`
