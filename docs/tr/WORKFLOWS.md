# 🔄 Otonom İş Akışları

## 1. Backend-to-Frontend Devir Teslimi (API Handoff)
Backend'de bir API değiştiğinde ajan otomatik olarak `API_HANDOFF.md` oluşturur. Eski JSON ve Yeni JSON farklarını (Diff) ve Frontend'in ne yapması gerektiğini yazar.

## 2. Otonom Proje Kurulumu
`project-bootstrap-orchestrator` ile klasör mimarisi, `dotnet new` komutları ve temel ayarlar CLI üzerinden otomatik kurulur.

## ⏱️ API Devir-Teslim (Handoff) Akış Şeması
Backend'in kodu bitirmesinden Frontend'e devrine kadar geçen otonom süre.

```mermaid
sequenceDiagram
    actor User as Kullanıcı
    participant CTO as Code Orchestrator
    participant BE as .NET Architect
    participant Tracker as Changelog Workflow
    participant FE as Swift/Flutter Architect
    
    User->>CTO: Yeni sepet(cart) API'si yaz.
    CTO->>BE: İşi Delege Et
    
    Note over BE: Kod yazılır, Test edilir,<br/>Swagger dokümanı basılır.
    
    BE-->>Tracker: Endpoint değişti!
    Tracker->>Tracker: CHANGELOG.md güncellendi.
    Tracker->>Tracker: API_HANDOFF.md oluşturuldu (Eski JSON vs Yeni JSON)
    
    Tracker->>FE: API_HANDOFF dokümanını incele!
    
    Note over FE: Frontend State (Riverpod/Redux)<br/>yeni JSON yapısına göre güncellenir.
    
    FE-->>User: Sepet entegrasyonu tamamlandı (Türkçe)
```
