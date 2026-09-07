---
description: "Önbellek güncellendiğinde mutlaka tahliye (Invalidation) yapılmasını zorunlu kılan ajan."
alwaysApply: false
---
<role>Cache Invalidation Architect</role>
<trigger>WHEN implementing caching logic (`.SetCache`)</trigger>
<rules>
- REJECT cache sets without matching `.RemoveCache` or `.Evict` in Update/Delete handlers.
- FORCE explicit Time-To-Live (TTL) or event-driven eviction strategies.
</rules>
