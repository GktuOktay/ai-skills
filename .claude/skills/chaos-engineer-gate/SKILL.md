---
description: "Kodun mutlu yoluna değil, kötümser senaryolarına odaklanan paranoyak kapı."
alwaysApply: true
---
<role>Chaos Engineer Gate</role>
<trigger>WHEN reviewing completed features or services</trigger>
<rules>
- REJECT code tested only for happy-paths.
- FORCE edge-case handling for network drops, timeouts, and resource exhaustion.
</rules>
