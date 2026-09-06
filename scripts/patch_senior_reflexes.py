import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills/src/skills"

# 1. Update Code Orchestrator (Universal Senior Reflexes)
code_orch_path = os.path.join(base_dir, "01_orchestrators", "code-orchestrator", "SKILL.md")
if os.path.exists(code_orch_path):
    with open(code_orch_path, "a", encoding="utf-8") as f:
        f.write("""

## Universal Senior Developer Reflexes
When orchestrating or writing code across ANY language or framework, you MUST enforce these Principal-level principles:
1. **Fail-Fast & Defensive Programming:** Never assume the "happy path". Always validate inputs at the very boundary of the application. Check for nulls, handle boundary conditions, and throw meaningful custom exceptions immediately rather than letting the system crash deep inside the logic.
2. **Idempotency:** State-changing operations (POST/PUT/PATCH, especially payments or orders) must be designed to be idempotent. If the exact same request arrives twice due to a network retry, the system must handle it gracefully without duplicating transactions.
3. **Security by Default (OWASP Mindset):** Never trust user input. Never expose internal database integer IDs (like Auto-Increment IDs) to the public API; always use secure references like GUIDs/UUIDs to prevent IDOR (Insecure Direct Object Reference) attacks.
""")

# 2. Update .NET Architect (Specific IoC & Testing Reflexes)
dotnet_arch_path = os.path.join(base_dir, "02_specialists", "dotnet-enterprise-architect", "SKILL.md")
if os.path.exists(dotnet_arch_path):
    with open(dotnet_arch_path, "a", encoding="utf-8") as f:
        f.write("""

## Inversion of Control & Testability
- **Abstract Volatile Dependencies:** NEVER use static volatile dependencies directly in business logic (e.g., `DateTime.Now`, `Guid.NewGuid()`, or static file/network access). Always inject them via an interface (e.g., `IDateTimeProvider`) so that the core domain logic remains 100% deterministic and unit-testable.
- **Defensive C#:** Utilize C# features like `ArgumentNullException.ThrowIfNull()`, Pattern Matching, and non-nullable reference types (`#nullable enable`) to bulletproof your domain services.
""")

print("Senior developer reflexes patched successfully.")
