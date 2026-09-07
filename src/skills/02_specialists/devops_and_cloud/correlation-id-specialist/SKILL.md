---
description: "İsteklere X-Correlation-ID ekletip tüm loglarda izlenebilirliği sağlayan uzman."
alwaysApply: false
---
<role>Correlation ID Specialist</role>
<trigger>WHEN handling incoming HTTP requests or producing logs</trigger>
<rules>
- FORCE extraction or generation of `X-Correlation-ID`.
- REQUIRE correlation ID propagation to LogContext and all outgoing HTTP/Messagebus calls.
</rules>
