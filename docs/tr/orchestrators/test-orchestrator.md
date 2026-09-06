# 🎼 Test Orchestrator (QA Yöneticisi)

**Görevi:** Uçtan uca testleri (E2E), birim testleri (Unit) ve duman testlerini (Smoke) koordine eder.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[test-orchestrator]
    Root --> |Delege Eder| Sub_UnitTestArchitect[Unit Test Architect]
    Root --> |Delege Eder| Sub_E2ETester[E2E Tester]
    Root --> |Delege Eder| Sub_SmokeMonkeyTester[Smoke Monkey Tester]
    Root --> |Delege Eder| Sub_PerformanceTester[Performance Tester]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_UnitTestArchitect sub
    class Sub_E2ETester sub
    class Sub_SmokeMonkeyTester sub
    class Sub_PerformanceTester sub
```

---
*Bu doküman otonom olarak üretilmiştir.*
