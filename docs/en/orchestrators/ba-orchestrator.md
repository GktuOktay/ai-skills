# 🎼 Business Analysis Orchestrator

**Role:** Gathers business requirements, designs DB schemas, and outputs technical specifications.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[ba-orchestrator]
    Root --> |Delegates| Sub_TechBusinessAnalyst[Tech Business Analyst]
    Root --> |Delegates| Sub_BAElicitor[BA Elicitor]
    Root --> |Delegates| Sub_DBArchitectSecurity[DB Architect & Security]
    Root --> |Delegates| Sub_SchemaSegregationGate[Schema Segregation Gate]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_TechBusinessAnalyst sub
    class Sub_BAElicitor sub
    class Sub_DBArchitectSecurity sub
    class Sub_SchemaSegregationGate sub
```

---
*This document was autonomously generated.*
