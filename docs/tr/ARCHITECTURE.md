# 🏗️ Sistemin Anatomisi (Architecture)

## 01_orchestrators (Yöneticiler)
Kod yazmaz, işi planlar ve delege eder. (Örn: Master Orchestrator, Code Orchestrator)

## 02_specialists (Uzman Ajanlar)
* **.NET Enterprise Architect:** C# 11+, CQRS, EF Core.
* **Legacy Code Migrator:** Django -> .NET veya Vue -> React göçlerini mimariye uygun yapar.
* **Mobile Swift/Flutter Architect:** Native (TCA/MVVM) ve Cross-platform (Riverpod) uzmanı.

## 03_quality_gates (Kalite Kapıları)
* **Turkish Language Enforcer:** Çıktının her zaman Türkçe olmasını sağlar.
* **Test-Driven Gate:** Test yazılıp başarılı olmadan kodu kabul etmez.
* **Structured Logging & Audit Gate:** Tam Payload loglanmasını engeller, ActionType loglamayı zorunlu tutar.

## 🚥 Üretim Bandı ve Kalite Kapıları (Quality Pipeline)
Uzmanların yazdığı kodlar, aşağıdaki deterministik kapılardan geçmeden ASLA size ulaşmaz.

```mermaid
flowchart LR
    Start([Ham Kod]) --> TDD{1. Test-Driven Gate}
    TDD -->|Test Yok/Hatalı| Reject1[Kodu Geri Çevir]
    TDD -->|Test Başarılı| Log{2. Structured Logging Gate}
    
    Log -->|Düz Metin Log| Reject2[Kodu Geri Çevir]
    Log -->|Yapısal JSON Log| Doc{3. Swagger & XML Gate}
    
    Doc -->|Doküman Eksik| Reject3[Kodu Geri Çevir]
    Doc -->|Swagger Tamam| Lang{4. Turkish Enforcer Gate}
    
    Lang -->|İngilizce Açıklama| Reject4[Kodu Geri Çevir]
    Lang -->|Saf Türkçe| Done([Kullanıcıya Teslim])
    
    style Start fill:#555,color:#fff
    style Done fill:#2d4a22,stroke:#5c9e42,stroke-width:2px,color:#fff
    style Reject1 fill:#5c1a1b,color:#fff
    style Reject2 fill:#5c1a1b,color:#fff
    style Reject3 fill:#5c1a1b,color:#fff
    style Reject4 fill:#5c1a1b,color:#fff
```
