# 🏗️ Architecture Anatomy

## 01_orchestrators (Managers)
They do not write code; they plan and delegate. (e.g., Master Orchestrator, Code Orchestrator)

## 02_specialists (Expert Agents)
* **.NET Enterprise Architect:** C# 11+, CQRS, EF Core optimization.
* **Legacy Code Migrator:** Migrates Django -> .NET safely while adapting to Clean Architecture.
* **Mobile Swift/Flutter Architect:** State management and memory leak expert.

## 03_quality_gates (Deterministic Gates)
* **Test-Driven Gate:** Rejects code unless unit tests are written and pass.
* **Structured Logging & Audit Gate:** Enforces structured logs and prevents full payload DB logging.

## 🚥 Production Pipeline & Quality Gates
Uzmanların yazdığı kodlar, aşağıdaki deterministik kapılardan geçmeden ASLA size ulaşmaz.

```mermaid
flowchart LR
    Start([Raw Code]) --> TDD{1. Test-Driven Gate}
    TDD -->|Test Failed| Reject1[Reject Code]
    TDD -->|Test Passed| Log{2. Structured Logging Gate}
    
    Log -->|Plaintext Log| Reject2[Reject Code]
    Log -->|Structured Log| Doc{3. Swagger & XML Gate}
    
    Doc -->|Missing Docs| Reject3[Reject Code]
    Doc -->|Docs Approved| Lang{4. Turkish Enforcer Gate}
    
    Lang -->|English Output| Reject4[Reject Code]
    Lang -->|Turkish Translation| Done([Delivered to User])
    
    style Start fill:#555,color:#fff
    style Done fill:#2d4a22,stroke:#5c9e42,stroke-width:2px,color:#fff
    style Reject1 fill:#5c1a1b,color:#fff
    style Reject2 fill:#5c1a1b,color:#fff
    style Reject3 fill:#5c1a1b,color:#fff
    style Reject4 fill:#5c1a1b,color:#fff
```
