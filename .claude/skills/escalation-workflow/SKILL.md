---
description: "Kalite kapısında 3 kez takılan işi Baş Mimara havale eden kriz iş akışı."
alwaysApply: true
---
<role>Escalation Workflow</role>
<trigger>WHEN a Specialist fails a Quality Gate 3 consecutive times</trigger>
<rules>
- FORCE termination of the retry loop to prevent token waste.
- REQUIRE generation of a Dispute Report and request Human Principal Architect intervention.
</rules>
