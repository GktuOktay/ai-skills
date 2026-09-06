# 🎼 Security Orchestrator (Güvenlik Yöneticisi)

[🇺🇸 English Documentation](../../en/orchestrators/security-orchestrator.md)


**Görevi:** Sistemdeki güvenlik zafiyetlerini (OWASP), penetrasyon testlerini ve audit süreçlerini yönetir.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[security-orchestrator]
    Root --> |Delege Eder| Sub_APIPentester[API Pentester]
    Root --> |Delege Eder| Sub_JWTSecuritySpecialist[JWT Security Specialist]
    Root --> |Delege Eder| Sub_IDORVulnerabilityHunter[IDOR Vulnerability Hunter]
    Root --> |Delege Eder| Sub_StructuredLoggingGate[Structured Logging Gate]
    Root --> |Delege Eder| Sub_SecretScanner[Secret Scanner]

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
*Bu doküman otonom olarak üretilmiştir.*
