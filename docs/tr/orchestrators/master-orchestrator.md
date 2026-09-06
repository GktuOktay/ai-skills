# 🎼 Master Orchestrator (Genel Yönlendirici)

[🇺🇸 English Documentation](../../en/orchestrators/master-orchestrator.md)


**Görevi:** Kullanıcıdan gelen ham talebi alır ve hangi alt orkestratörün (Departmanın) devreye gireceğine karar verir.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[master-orchestrator]
    Root --> |Delege Eder| Sub_code-orchestrator[code-orchestrator]
    Root --> |Delege Eder| Sub_design-orchestrator[design-orchestrator]
    Root --> |Delege Eder| Sub_security-orchestrator[security-orchestrator]
    Root --> |Delege Eder| Sub_test-orchestrator[test-orchestrator]
    Root --> |Delege Eder| Sub_ba-orchestrator[ba-orchestrator]
    Root --> |Delege Eder| Sub_marketing-orchestrator[marketing-orchestrator]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_code-orchestrator sub
    class Sub_design-orchestrator sub
    class Sub_security-orchestrator sub
    class Sub_test-orchestrator sub
    class Sub_ba-orchestrator sub
    class Sub_marketing-orchestrator sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
