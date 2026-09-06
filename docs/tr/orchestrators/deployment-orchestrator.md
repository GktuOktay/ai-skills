# 🎼 Deployment & CI/CD Orchestrator

[🇺🇸 English Documentation](../../en/orchestrators/deployment-orchestrator.md)


**Görevi:** Kodun canlıya alınması, konteynerleştirme ve bulut altyapı süreçlerini yönetir.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[deployment-orchestrator]
    Root --> |Delege Eder| Sub_CICDEngineer[CI/CD Engineer]
    Root --> |Delege Eder| Sub_ContainerMaster[Container Master]
    Root --> |Delege Eder| Sub_CloudDeployer[Cloud Deployer]
    Root --> |Delege Eder| Sub_GitOpsManager[GitOps Manager]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_CICDEngineer sub
    class Sub_ContainerMaster sub
    class Sub_CloudDeployer sub
    class Sub_GitOpsManager sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
