# 🎼 Security Orchestrator

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/orchestrators/security-orchestrator.md)


**Role:** Manages system vulnerabilities (OWASP), penetration tests, and audit processes.

## Sub-Specialists and Delegation Diagram

```mermaid
flowchart TD
    Root[security-orchestrator]
    Root --> |Delegates| Sub_APIPentester[API Pentester]
    Root --> |Delegates| Sub_JWTSecuritySpecialist[JWT Security Specialist]
    Root --> |Delegates| Sub_IDORVulnerabilityHunter[IDOR Vulnerability Hunter]
    Root --> |Delegates| Sub_StructuredLoggingGate[Structured Logging Gate]
    Root --> |Delegates| Sub_SecretScanner[Secret Scanner]

    classDef orch fill:#2b1b3d,stroke:#9d5bdf,stroke-width:3px,color:#fff
    classDef sub fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    class Root orch
    class Sub_APIPentester sub
    class Sub_JWTSecuritySpecialist sub
    class Sub_IDORVulnerabilityHunter sub
    class Sub_StructuredLoggingGate sub
    class Sub_SecretScanner sub
```

---
*This document was autonomously generated.*
