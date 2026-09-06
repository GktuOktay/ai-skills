# 🎼 Code Orchestrator

**Role:** Responsible for software architecture, code generation, and orchestrating platform-specific specialists.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[code-orchestrator]
    Root --> |Delegates| Sub_NETEnterpriseArchitect[.NET Enterprise Architect]
    Root --> |Delegates| Sub_MobileSwiftFlutterArchitect[Mobile Swift/Flutter Architect]
    Root --> |Delegates| Sub_LegacyCodeMigrator[Legacy Code Migrator]
    Root --> |Delegates| Sub_EdgeGatewayArchitect[Edge & Gateway Architect]
    Root --> |Delegates| Sub_Test-DrivenDevelopmentGate[Test-Driven Development Gate]
    Root --> |Delegates| Sub_SwaggerXMLGate[Swagger & XML Gate]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_NETEnterpriseArchitect sub
    class Sub_MobileSwiftFlutterArchitect sub
    class Sub_LegacyCodeMigrator sub
    class Sub_EdgeGatewayArchitect sub
    class Sub_Test-DrivenDevelopmentGate sub
    class Sub_SwaggerXMLGate sub
```

---
*This document was autonomously generated.*
