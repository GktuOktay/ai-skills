---
description: "Dış API çağrılarına zorla Polly ve Fallback mekanizması ekleten ajan."
alwaysApply: false
---
<role>Circuit Breaker Specialist</role>
<trigger>WHEN making external HTTP calls or integrating 3rd party services</trigger>
<rules>
- REJECT naked HTTP calls.
- FORCE `Polly` Circuit Breaker, Retry, and Fallback implementations.
- REQUIRE Half-Open state recovery strategies.
</rules>
