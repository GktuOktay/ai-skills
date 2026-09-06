# AI-Skills: Autonomous Digital Agency (v2.0)

![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent_Ecosystem-blue)
![Quality Gates](https://img.shields.io/badge/Quality_Gates-Strict_Enforcement-red)
![Total Agents](https://img.shields.io/badge/Active_Specialists-105-success)

**AI-Skills** is an enterprise-grade, multi-agent AI ecosystem designed to replace standard conversational coding with a deterministic, autonomous software factory. It enforces Test-Driven Development (TDD), Strict Architectural Patterns (e.g., CQRS, .NET Clean Architecture), and automated API handoffs.

## 🚀 Key Differentiators
* **Not a Prompt Library:** It is a hierarchical company of agents (Orchestrators, Specialists, and Quality Gates).
* **Strict Quality Gates:** Code is rejected if it lacks unit tests, swagger documentation, or structured logging.
* **Single Source of Truth (SSOT):** Over 100 skills compiled dynamically for multiple IDEs (Cursor, Claude Code, Windsurf) from a single `src/skills/` directory.

## 📋 The Agency Departments
The ecosystem consists of **105 strictly defined roles** distributed across 5 departments:
1. `01_orchestrators`: Meta-agents that plan, delegate, and manage workflows.
2. `02_specialists`: Domain-specific engineers (.NET, Mobile, Security, UX/UI, DB Architects).
3. `03_quality_gates`: Deterministic rule-checkers (TDD Enforcer, Turkish Language Enforcer).
4. `04_workflows`: Automated routines (API Handoff generation, Project Scaffolding).
5. `05_capabilities`: Tooling for agents (Code parsing, document generation).

👉 **[View the Complete Catalog of all 105 Agents & Skills](docs/SKILLS_CATALOG.md)**

## 📚 Technical Documentation (Whitepapers)
Deep architectural insights and execution logic:
* 🏗️ [Architecture Deep-Dive](docs/en/ARCHITECTURE.md) *(also in [TR](docs/tr/ARCHITECTURE.md))*
* 🧠 [Core Engineering Principles](docs/en/PRINCIPLES.md) *(also in [TR](docs/tr/PRINCIPLES.md))*
* 🔄 [Autonomous Workflows](docs/en/WORKFLOWS.md) *(also in [TR](docs/tr/WORKFLOWS.md))*

## ⚙️ Installation & Build
AI-Skills uses a centralized SSOT compiler. To inject all 105 rules into your IDEs:

```bash
python3 setup.py
```
This generates the required `.mdc` files for Cursor, `.windsurfrules` for Windsurf, and `clauderules.md` for Claude.

---
*Built for Principal Engineers who demand determinism, not just suggestions.*
