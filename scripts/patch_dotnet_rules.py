import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills/src/skills"

# 1. Patch .NET Architect (Base Service Overriding & Pagination)
dotnet_arch_path = os.path.join(base_dir, "02_specialists", "dotnet-enterprise-architect", "SKILL.md")
if os.path.exists(dotnet_arch_path):
    with open(dotnet_arch_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Base Service vs Specific Queries\nDo not force complex scenarios into a generic `BaseService`. If an endpoint requires multiple `.Include()` calls, complex projections, or domain-specific logic, DO NOT try to hack the Base Service. Instead, write a dedicated, specific method/query (e.g., CQRS Query) for that exact use-case. Leaving unused generic methods in a Base Service is an anti-pattern when custom queries are always used.")

# 2. Patch DB Architect (Pagination & Dynamic Filtering)
db_arch_path = os.path.join(base_dir, "02_specialists", "db-architect-security", "SKILL.md")
if os.path.exists(db_arch_path):
    with open(db_arch_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Pagination & Dynamic Filtering\n- **Lists MUST be Paginated:** Any structure returning a list of items must implement pagination by default.\n- **Dynamic Filtering:** If an API request comes with no filters, return the full paginated dataset. If filters are provided, apply them dynamically. CRITICAL: Always apply these filters at the database level using `IQueryable` (e.g., LINQ `.Where()`) BEFORE materializing the data (never in memory).")

print("DotNet and DB rules patched successfully.")
