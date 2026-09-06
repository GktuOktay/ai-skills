import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills/src/skills"

dotnet_arch_path = os.path.join(base_dir, "02_specialists", "dotnet-enterprise-architect", "SKILL.md")
if os.path.exists(dotnet_arch_path):
    with open(dotnet_arch_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Evolutionary Architecture & Business Rule Shifts\nBusiness requirements evolve. A simple CRUD entity often grows into a complex domain object. When this happens, DO NOT cling to the generic `BaseService`. Be proactive in your refactoring: the moment an operation requires side-effects (e.g., sending emails, complex validation, updating secondary tables), extract it out of the generic Base Service and create a dedicated, use-case specific service/handler. Clinging to generic abstractions during business evolution leads to technical debt.")

print("Evolutionary architecture rule patched successfully.")
