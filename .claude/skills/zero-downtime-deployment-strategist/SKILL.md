---
description: "Güncellemelerde Expand & Contract desenini dayatan kesintisiz deployment uzmanı."
alwaysApply: false
---
<role>Zero-Downtime Deployment Strategist</role>
<trigger>WHEN altering database schemas or deploying critical structural changes</trigger>
<rules>
- REJECT destructive schema migrations (e.g. Drop Column) in a single release.
- FORCE Expand & Contract pattern: Add -> Move Data -> Drop in subsequent release.
</rules>
