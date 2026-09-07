---
description: "DateTime.Now kullanımını yasaklayıp UtcNow veya TimeProvider zorunluluğu getiren kapı."
alwaysApply: true
---
<role>Timezone Enforcer Gate</role>
<trigger>WHEN handling dates and times</trigger>
<rules>
- REJECT `DateTime.Now` or local time dependencies.
- FORCE `DateTimeOffset.UtcNow` or `TimeProvider` (in .NET 8) for all time operations.
</rules>
