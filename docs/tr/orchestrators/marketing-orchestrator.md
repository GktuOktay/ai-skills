# 🎼 Marketing Orchestrator (Pazarlama Yöneticisi)

[🇺🇸 English Documentation](../../en/orchestrators/marketing-orchestrator.md)


**Görevi:** Ürünün lansman öncesi pazarlama stratejilerini, kopyalarını ve marka iletişimini yönetir.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[marketing-orchestrator]
    Root --> |Delege Eder| Sub_ProductMarketer[Product Marketer]
    Root --> |Delege Eder| Sub_Pre-LaunchStrategist[Pre-Launch Strategist]
    Root --> |Delege Eder| Sub_CopywritingSpecialist[Copywriting Specialist]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_ProductMarketer sub
    class Sub_Pre-LaunchStrategist sub
    class Sub_CopywritingSpecialist sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
