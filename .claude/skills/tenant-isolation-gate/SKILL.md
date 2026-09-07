---
description: "B2B projelerde TenantId filtresini mecburi kılan kapı."
alwaysApply: true
---
<role>Tenant Isolation Gate</role>
<trigger>WHEN writing database queries (EF Core, Dapper, SQL)</trigger>
<rules>
- REJECT queries missing explicit `TenantId` filtering.
- FORCE usage of EF Core Global Query Filters for multi-tenant SaaS architectures.
</rules>
