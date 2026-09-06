---
name: swagger-and-xml-doc-gate
description: "Backend kodunda (özellikle .NET) yazılan her endpoint için XML Doc, Summary ve profesyonel Swagger yapılandırmasını zorunlu kılan kapı."
---

# Swagger & XML Documentation Gate

CRITICAL RULE: Code without documentation is rejected.

For every API endpoint or Controller written in the backend:
1. You MUST include `/// <summary>` tags explaining what the endpoint does.
2. You MUST include `<param>` and `<returns>` XML tags where applicable.
3. You MUST explicitly decorate the endpoint with Swagger attributes (e.g., `[ProducesResponseType(StatusCodes.Status200OK, Type = typeof(Dto))]`, `400 BadRequest`, `404 NotFound`).
4. Ensure the Swagger UI becomes a self-explanatory, maximum-professional-grade documentation portal.
