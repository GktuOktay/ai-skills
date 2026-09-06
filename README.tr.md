# Autonomous Agency: Otonom Dijital Ajans (v2.0)

[🇺🇸 English Documentation](README.md)

![Architecture](https://img.shields.io/badge/Mimari-Multi--Agent_Ekosistemi-blue)
![Quality Gates](https://img.shields.io/badge/Kalite_Kapilari-Kesin_Denetim-red)
![Total Agents](https://img.shields.io/badge/Aktif_Uzman-105-success)

**Autonomous Agency**, standart sohbet tabanlı kodlamayı reddeden; bunun yerine kararlı (deterministik) ve otonom bir yazılım fabrikası kurmayı hedefleyen kurumsal düzeyde bir çoklu ajan ekosistemidir. Test Güdümlü Geliştirmeyi (TDD), katı mimari prensipleri (CQRS, .NET Clean Architecture) ve otomatik API devir-teslimlerini zorunlu kılar.

## 🚀 Temel Farklar
* **Prompt Kütüphanesi Değildir:** Yöneticiler (Orchestrators), Uzmanlar ve Kalite Kapılarından oluşan hiyerarşik bir şirkettir.
* **Katı Kalite Kapıları:** Birim testi (Unit Test), Swagger dokümanı veya yapısal loglaması (Structured Logging) olmayan kod sistemden geçemez ve reddedilir.
* **Tek Doğru Kaynağı (SSOT):** 100'den fazla yetenek tek bir `src/skills/` klasöründen okunarak birden fazla IDE (Cursor, Claude Code, Windsurf) için dinamik olarak derlenir.

## 📚 Teknik Dokümantasyon ve İzahnameler
Bu depo derin mimari prensipler barındırır. Tüm çekirdek sistem belgeleri ve yönettikleri alanlar aşağıdadır:

### 1. Sistem Anayasası ve Kısıtlamalar
* ⚖️ **[Hiyerarşi ve Yetki Devri Protokolü](docs/tr/core/HIERARCHY_PROTOCOL.md)** 
  * Ekosistemin kesin sınırlarını çizer: Neden Yöneticilerin kod yazmasının yasak olduğu, Kalite Kapılarının neden sadece "Okuma" (Read-Only) yetkisine sahip olduğu (kodu düzeltemez, sadece reddederler) ve bir kullanıcı isteğinin durum-makinesi (state-machine) döngüsü.

### 2. Mimari Tasarım
* 🏗️ **[Mimarinin Anatomisi](docs/tr/core/ARCHITECTURE.md)** 
  * Ajansın 5 katmanlı yapısını (01'den 05'e) açıklar. Kullanıcı isteklerinin nasıl bir "Abstract Syntax Tree" gibi parçalandığını ve kodun Kalite Kapısından geçemediğinde devreye giren geri dönüş (Fallback) mekanizmalarını detaylandırır.

### 3. Mühendislik Zihniyeti
* 🧠 **[Çekirdek Mühendislik Prensipleri](docs/tr/core/PRINCIPLES.md)** 
  * Ajanların beynine kazınmış "Baş Mimar" (Principal Architect) zihniyetini belgeler. Yanlış (Örn: Şişirilmiş BaseService kullanımı) ve Doğru (CQRS, Savunmacı Programlama, IoC, Şema Ayrıştırması) C# kod örneklerini içerir.

### 4. Süreç Otomasyonu
* 🔄 **[Otonom İş Akışları](docs/tr/core/WORKFLOWS.md)** 
  * Hammaliye süreçlerini ortadan kaldıran otomatik rutinleri detaylandırır. API Devir-Teslim (Handoff) algoritmasını (Backend ve Frontend arasındaki JSON diff üretimi) ve Proje Kurulumu (Scaffolding) sırasında çalışan tam CLI komut dizisini açıklar.

## 📋 Ajans Departmanları ve Yetenek Envanteri
Ekosistem, mesleki alanlara (Örn: `backend_and_data`, `security_and_pentest`) göre gruplandırılmış **105 kesin tanımlı rolden** oluşur.
👉 **[105 Ajan ve Yeteneğin Tam Kataloğunu Görüntüle](docs/tr/catalogs/SKILLS_CATALOG.md)**

### 🗺️ Orkestratör (Yönetici) Haritaları
Kimin kime rapor verdiğini merak mı ediyorsunuz? Temel yöneticilerimiz için özel yetki devri diyagramlarını (Mermaid) inceleyin:
* [Master Orchestrator](docs/tr/orchestrators/master-orchestrator.md) — CEO ajan.
* [Code Orchestrator](docs/tr/orchestrators/code-orchestrator.md) — Backend, Frontend ve Dönüşümleri yönetir.
* [Security Orchestrator](docs/tr/orchestrators/security-orchestrator.md) — Pentester, IDOR ve JWT Uzmanlarını yönetir.
* [Design Orchestrator](docs/tr/orchestrators/design-orchestrator.md) — UX/UI, Brandkit ve Metin Yazarlarını yönetir.
* [Test Orchestrator](docs/tr/orchestrators/test-orchestrator.md) — Unit, Smoke ve E2E testlerini yönetir.
* *(BA, Deployment ve Marketing orkestratörleri için [Kataloga](docs/tr/catalogs/SKILLS_CATALOG.md) bakın).*

## ⚙️ Kurulum ve Derleme (Build)
Autonomous Agency, merkezi bir SSOT derleyici kullanır. Tüm 105 kuralı IDE'lerinize enjekte etmek için:

```bash
python3 setup.py
```
Bu komut; Cursor için `.mdc`, Windsurf için `.windsurfrules` ve Claude için `clauderules.md` dosyalarını üretir.

---
*Sadece öneri değil, kesinlik talep eden Baş Mimarlar (Principal Engineers) için inşa edilmiştir.*
