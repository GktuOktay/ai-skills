---
description: "Hataların RFC 7807 standartlarına uygun JSON dönmesini zorunlu kılan kapı."
alwaysApply: true
---
<role>ProblemDetails Gate</role>
<trigger>WHEN throwing exceptions or returning API error responses</trigger>
<rules>
- REJECT unstructured error strings or random JSON formats.
- FORCE Global Exception Handlers mapping to RFC 7807 `ProblemDetails` standard.
</rules>
