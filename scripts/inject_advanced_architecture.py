import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills/src/skills"

# 1. Update .NET Architect (Base Service Principle)
dotnet_arch_path = os.path.join(base_dir, "02_specialists", "dotnet-enterprise-architect", "SKILL.md")
if os.path.exists(dotnet_arch_path):
    with open(dotnet_arch_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Anti-Pattern Avoidance: Generic Base Services\nApply the YAGNI (You Aren't Gonna Need It) principle strictly. DO NOT blindly inherit from generic `BaseService<T>` or `BaseRepository<T>` that expose full CRUD operations if the entity only needs to be read. Avoid exposing `Update` or `Delete` methods for immutable records. Prefer specific use-case handlers (CQRS/MediatR) or highly targeted services over bloated generic base classes.")

# 2. Update DB Architect (Optimization & Indexing)
db_arch_path = os.path.join(base_dir, "02_specialists", "db-architect-security", "SKILL.md")
if os.path.exists(db_arch_path):
    with open(db_arch_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Advanced Query Optimization & Indexing\n- **Indexing:** Always define logical Composite Indexes, Filtered Indexes, and Covering Indexes for frequently queried columns. Never allow full table scans on large tables.\n- **EF Core Optimization:** Enforce `AsNoTracking()` for read-only queries. Prevent N+1 queries by explicitly using `.Include()` or projection (`.Select()`).\n- Never write a `GetAll` endpoint without Mandatory Pagination.")

# 3. New Gate: Swagger & XML Doc Gate
swagger_gate_dir = os.path.join(base_dir, "03_quality_gates", "swagger-and-xml-doc-gate")
os.makedirs(swagger_gate_dir, exist_ok=True)
with open(os.path.join(swagger_gate_dir, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write("""---
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
""")

# 4. New Workflow: API Handoff & Changelog
handoff_wf_dir = os.path.join(base_dir, "04_workflows", "api-handoff-workflow")
os.makedirs(handoff_wf_dir, exist_ok=True)
with open(os.path.join(handoff_wf_dir, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write("""---
name: api-handoff-workflow
description: "Backend'de bir değişiklik yapıldığında otomatik Changelog çıkaran ve Frontend takımı için eski/yeni API karşılaştırma (Devir-Teslim) dokümanı üreten iş akışı."
---

# Backend-to-Frontend API Handoff Workflow

Whenever a change is made to the Backend APIs, you MUST execute this workflow:

1. **Update Changelog:** Automatically update the project's changelog/tracker with the backend modifications.
2. **Generate API_HANDOFF.md:** Create or update a document specifically for the Frontend/Mobile team.
   - Show the **OLD** Request/Response JSON structure vs the **NEW** structure (Diff).
   - Explain exactly what the Frontend developer needs to do to integrate this change (e.g., "Change the `userId` field to `userGuid` in the Redux store").
   - Highlight any breaking changes in bold.
""")

print("Advanced architectural principles injected successfully.")
