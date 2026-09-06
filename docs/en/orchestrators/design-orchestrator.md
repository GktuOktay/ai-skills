# 🎼 Design Orchestrator

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/orchestrators/design-orchestrator.md)


**Role:** Manages visual quality, copywriting, and design system (Brandkit) construction.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[design-orchestrator]
    Root --> |Delegates| Sub_UXUICopywriter[UX/UI Copywriter]
    Root --> |Delegates| Sub_AppleDesignExpert[Apple Design Expert]
    Root --> |Delegates| Sub_High-EndVisualDesigner[High-End Visual Designer]
    Root --> |Delegates| Sub_a11yi18nEngineer[a11y & i18n Engineer]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_UXUICopywriter sub
    class Sub_AppleDesignExpert sub
    class Sub_High-EndVisualDesigner sub
    class Sub_a11yi18nEngineer sub
```

---
*This document was autonomously generated.*
