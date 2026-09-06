# 🎼 Code Orchestrator (Yazılım Geliştirme Yöneticisi)

**Görevi:** Yazılım mimarisi, kod yazımı ve platform bazlı uzmanların (Backend/Frontend) orkestrasyonundan sorumludur.

## Alt Uzmanlar ve Yetki Dağılımı Diyagramı

```mermaid
flowchart TD
    Root[code-orchestrator]
    Root --> |Delege Eder| Sub_NETEnterpriseArchitect[.NET Enterprise Architect]
    Root --> |Delege Eder| Sub_MobileSwiftFlutterArchitect[Mobile Swift/Flutter Architect]
    Root --> |Delege Eder| Sub_LegacyCodeMigrator[Legacy Code Migrator]
    Root --> |Delege Eder| Sub_EdgeGatewayArchitect[Edge & Gateway Architect]
    Root --> |Delege Eder| Sub_Test-DrivenDevelopmentGate[Test-Driven Development Gate]
    Root --> |Delege Eder| Sub_SwaggerXMLGate[Swagger & XML Gate]

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
*Bu doküman otonom olarak üretilmiştir.*
