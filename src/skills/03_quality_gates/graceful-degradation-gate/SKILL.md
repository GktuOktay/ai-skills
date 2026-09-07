---
name: graceful-degradation-gate
description: "Backend çöktüğünde Frontend'i Fallback UI çizmeye zorlayan kapı."
alwaysApply: true
---
<role>Graceful Degradation Gate</role>
<trigger>WHEN frontend components consume APIs</trigger>
<rules>
- REJECT blank screens or unhandled 500 errors on API failure.
- FORCE implementation of Fallback UI (Skeleton loaders, cached state, error boundaries).
</rules>
