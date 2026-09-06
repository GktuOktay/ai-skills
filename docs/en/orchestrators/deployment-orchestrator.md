# 🎼 Deployment Orchestrator

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/orchestrators/deployment-orchestrator.md)


**Role:** Manages code deployment, containerization, and cloud infrastructure.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[deployment-orchestrator]
    Root --> |Delegates| Sub_CICDEngineer[CI/CD Engineer]
    Root --> |Delegates| Sub_ContainerMaster[Container Master]
    Root --> |Delegates| Sub_CloudDeployer[Cloud Deployer]
    Root --> |Delegates| Sub_GitOpsManager[GitOps Manager]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_CICDEngineer sub
    class Sub_ContainerMaster sub
    class Sub_CloudDeployer sub
    class Sub_GitOpsManager sub
```

---
*This document was autonomously generated.*
