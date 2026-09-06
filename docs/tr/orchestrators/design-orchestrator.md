# 🎼 Design Orchestrator (Tasarım ve UI/UX Yöneticisi)

**Görevi:** Görsel kalite, metin yazarlığı ve tasarım sistemleri (Brandkit) inşasını yönetir.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[design-orchestrator]
    Root --> |Delege Eder| Sub_UXUICopywriter[UX/UI Copywriter]
    Root --> |Delege Eder| Sub_AppleDesignExpert[Apple Design Expert]
    Root --> |Delege Eder| Sub_High-EndVisualDesigner[High-End Visual Designer]
    Root --> |Delege Eder| Sub_a11yi18nEngineer[a11y & i18n Engineer]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_UXUICopywriter sub
    class Sub_AppleDesignExpert sub
    class Sub_High-EndVisualDesigner sub
    class Sub_a11yi18nEngineer sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
