# 🎼 Test Orchestrator

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/orchestrators/test-orchestrator.md)


**Role:** Coordinates End-to-End (E2E), Unit, and Smoke tests.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[test-orchestrator]
    Root --> |Delegates| Sub_UnitTestArchitect[Unit Test Architect]
    Root --> |Delegates| Sub_E2ETester[E2E Tester]
    Root --> |Delegates| Sub_SmokeMonkeyTester[Smoke Monkey Tester]
    Root --> |Delegates| Sub_PerformanceTester[Performance Tester]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_UnitTestArchitect sub
    class Sub_E2ETester sub
    class Sub_SmokeMonkeyTester sub
    class Sub_PerformanceTester sub
```

---
*This document was autonomously generated.*
