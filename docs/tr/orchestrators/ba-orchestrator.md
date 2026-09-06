# 🎼 Business Analysis (BA) Orchestrator

[🇺🇸 English Documentation](../../en/orchestrators/ba-orchestrator.md)


**Görevi:** İş gereksinimlerini toplar, veritabanı şemalarını çizer ve projeyi teknik spesifikasyonlara döker.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[ba-orchestrator]
    Root --> |Delege Eder| Sub_TechBusinessAnalyst[Tech Business Analyst]
    Root --> |Delege Eder| Sub_BAElicitor[BA Elicitor]
    Root --> |Delege Eder| Sub_DBArchitectSecurity[DB Architect & Security]
    Root --> |Delege Eder| Sub_SchemaSegregationGate[Schema Segregation Gate]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_TechBusinessAnalyst sub
    class Sub_BAElicitor sub
    class Sub_DBArchitectSecurity sub
    class Sub_SchemaSegregationGate sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
