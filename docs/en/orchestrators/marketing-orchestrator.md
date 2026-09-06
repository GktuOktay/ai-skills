# 🎼 Marketing Orchestrator

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/orchestrators/marketing-orchestrator.md)


**Role:** Manages pre-launch marketing strategies, copy, and brand communication.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[marketing-orchestrator]
    Root --> |Delegates| Sub_ProductMarketer[Product Marketer]
    Root --> |Delegates| Sub_Pre-LaunchStrategist[Pre-Launch Strategist]
    Root --> |Delegates| Sub_CopywritingSpecialist[Copywriting Specialist]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_ProductMarketer sub
    class Sub_Pre-LaunchStrategist sub
    class Sub_CopywritingSpecialist sub
```

---
*This document was autonomously generated.*
