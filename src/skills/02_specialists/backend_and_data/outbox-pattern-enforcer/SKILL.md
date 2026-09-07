---
name: outbox-pattern-enforcer
description: "DB kaydı ve RabbitMQ event'inin aynı anda atılmasını sağlayıp mesaj kaybını önleyen ajan."
alwaysApply: true
---
<role>Outbox Pattern Enforcer</role>
<trigger>WHEN saving entity state AND publishing a domain event</trigger>
<rules>
- REJECT dual-writes (saving to DB and publishing to bus independently).
- FORCE Outbox Pattern (save event to DB transactionally, publish via background worker).
</rules>
