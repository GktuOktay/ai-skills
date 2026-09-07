---
name: stateless-architecture-gate
description: "Bellekte durum tutulmasını yasaklayıp yatay ölçeklenebilirliği zorunlu kılan kapı."
alwaysApply: true
---
<role>Stateless Architecture Gate</role>
<trigger>WHEN handling user sessions or temporary state</trigger>
<rules>
- REJECT `HttpContext.Session` or in-memory static state dictionaries.
- FORCE stateless JWT authentication or Distributed Caching (Redis) for scalability.
</rules>
