# 🎼 Project Bootstrap (Proje Başlatma Yöneticisi)

**Görevi:** Sıfırdan projelerin (CLI üzerinden) klasör yapısını, boilerplate kodlarını ve mimarisini kurar.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[project-bootstrap-orchestrator]
    Root --> |Delege Eder| Sub_GitRepoSetupWorkflow[Git Repo Setup Workflow]
    Root --> |Delege Eder| Sub_CleanArchitectureGenerator[Clean Architecture Generator]
    Root --> |Delege Eder| Sub_ObservabilitySetup[Observability Setup]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_GitRepoSetupWorkflow sub
    class Sub_CleanArchitectureGenerator sub
    class Sub_ObservabilitySetup sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
