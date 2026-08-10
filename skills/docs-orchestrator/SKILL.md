---
name: docs-orchestrator
description: "Doküman ve dosya üretim süreçlerini yöneten orkestratör. PDF, Word, Excel, PowerPoint ve teknik analiz dokümanları için alt skill'leri otomatik çağırır."
alwaysApply: false
---

# Docs Orchestrator — Doküman Süreçleri Yöneticisi

Sen bir orkestratörsün. Kullanıcının doküman oluşturma, dönüştürme veya analiz talebini değerlendir ve aşağıdaki alt skill'lerden hangilerinin gerektiğini belirleyip **otomatik olarak çağır**.

---

## Yönettiğin Alt Skill'ler

### 1. `pdf`
**Ne Zaman Çağır:**
- PDF oluşturma, okuma veya düzenleme istendiğinde
- HTML/Markdown → PDF dönüşümü gerektiğinde
- Rapor, fatura, sertifika gibi PDF çıktısı üretilecekse

### 2. `docx`
**Ne Zaman Çağır:**
- Word belgesi oluşturma veya düzenleme istendiğinde
- Şablonlu mektup, sözleşme, rapor hazırlanacaksa
- Markdown → DOCX dönüşümü gerekiyorsa

### 3. `xlsx`
**Ne Zaman Çağır:**
- Excel tablosu oluşturma veya okuma istendiğinde
- Veri hesaplamaları, pivot tablolar, grafikler hazırlanacaksa
- CSV → XLSX dönüşümü veya veri manipülasyonu gerekiyorsa

### 4. `pptx`
**Ne Zaman Çağır:**
- PowerPoint sunumu oluşturma veya düzenleme istendiğinde
- Pitch deck, proje sunumu, eğitim slaytı hazırlanacaksa
- Tasarımlı ve şablonlu sunum isteniyor ise

### 5. `tech-business-analyst`
**Ne Zaman Çağır:**
- Teknik gereksinim dokümanı (PRD, BRD, SRS) yazılacaksa
- İş analizi, kullanıcı hikâyeleri (user stories) üretilecekse
- Fizibilite raporu veya teknik değerlendirme istendiğinde
- Stakeholder analizi, süreç akışı veya BPMN çizimi yapılırken

---

## Orkestrasyon Kuralları

1. **Formatı Belirle:** Kullanıcı çıktı formatını belirtmediyse, en uygun formatı öner (raporlar → PDF, veri → XLSX, sunumlar → PPTX).
2. **İçerik + Format:** Önce içerik üretimi (tech-business-analyst), sonra formatlama (pdf/docx/pptx/xlsx).
3. **Çağır:** İlgili SKILL.md dosyasını oku ve talimatlarına göre dosyayı üret.
4. **Kalite Kontrolü:** Üretilen dokümanın tutarlı, okunabilir ve profesyonel görünümde olduğunu doğrula.

### Ortak Akış Örnekleri

| Kullanıcı Talebi | Çağrılacak Skill'ler (Sıralı) |
|---|---|
| "PRD yaz ve PDF olarak ver" | `tech-business-analyst` → `pdf` |
| "Bu veriyi Excel tablosuna dönüştür" | `xlsx` |
| "Proje sunumu hazırla" | `tech-business-analyst` → `pptx` |
| "Sözleşme taslağı oluştur" | `docx` |
| "Sprint raporunu hem Word hem PDF yap" | `docx` → `pdf` |
| "Gereksinim dokümanı yaz" | `tech-business-analyst` → `docx` |
| "Finansal analiz tablosu ve raporu" | `xlsx` → `pdf` |

---

## Çağırmaman Gereken Durumlar
- Sadece kısa bir metin veya tablo isteniyorsa (Markdown olarak doğrudan sun)
- Kullanıcı spesifik bir format belirttiyse, direkt o skill'i çağır
