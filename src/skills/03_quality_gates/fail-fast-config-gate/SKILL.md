---
name: fail-fast-config-gate
description: "Ayarları IOptions kullanarak okumayı dayatan ve uygulamanın patlamasını engelleyen kapı."
alwaysApply: true
---
<role>Fail-Fast Configuration Gate</role>
<trigger>WHEN reading environment variables or configuration settings</trigger>
<rules>
- REJECT direct `_configuration["Key"]` reads.
- FORCE `IOptions<T>` pattern with DataAnnotations (`[Required]`) for startup validation.
</rules>
