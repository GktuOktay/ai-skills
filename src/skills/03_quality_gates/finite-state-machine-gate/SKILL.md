---
description: "Kompleks durum geçişleri için matematiksel Durum Makinesi (FSM) dayatan kapı."
alwaysApply: true
---
<role>Finite State Machine Gate</role>
<trigger>WHEN managing entity status flows (e.g. Pending -> Paid -> Shipped)</trigger>
<rules>
- REJECT loose `if/else` or raw Enum modifications for critical state transitions.
- FORCE usage of explicit Finite State Machine (FSM) patterns/libraries.
</rules>
