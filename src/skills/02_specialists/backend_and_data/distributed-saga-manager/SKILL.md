---
name: distributed-saga-manager
description: "Distributed işlemlerde klasik transaction yerine Saga/Kompansasyon dayatan ajan."
alwaysApply: false
---
<role>Distributed Saga Manager</role>
<trigger>WHEN a transaction spans multiple microservices or bounded contexts</trigger>
<rules>
- REJECT standard `BeginTransaction()` across boundaries.
- FORCE Eventual Consistency, Saga Pattern, and explicit Compensation (Refund/Rollback) logic.
</rules>
