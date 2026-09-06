# Autonomous Agency (v2.0)

[🇹🇷 Türkçe Dokümantasyon (Turkish)](README.tr.md)

![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent_Ecosystem-blue)
![Quality Gates](https://img.shields.io/badge/Quality_Gates-Strict_Enforcement-red)
![Total Agents](https://img.shields.io/badge/Active_Specialists-105-success)

**Autonomous Agency** is an enterprise-grade, multi-agent AI ecosystem designed to replace standard conversational coding with a deterministic, autonomous software factory. It enforces Test-Driven Development (TDD), Strict Architectural Patterns (e.g., CQRS, .NET Clean Architecture), and automated API handoffs.

## 🚀 Key Differentiators
* **Not a Prompt Library:** It is a hierarchical company of agents (Orchestrators, Specialists, and Quality Gates).
* **Strict Quality Gates:** Code is rejected if it lacks unit tests, swagger documentation, or structured logging.
* **Single Source of Truth (SSOT):** Over 100 skills compiled dynamically for multiple IDEs (Cursor, Claude Code, Windsurf) from a single `src/skills/` directory.

## 📚 Technical Documentation & Whitepapers
This repository contains deep architectural insights. Below is the index of all core system documents and what they govern:

### 1. System Constitution & Constraints
* ⚖️ **[Hierarchy & Delegation Protocol](docs/en/core/HIERARCHY_PROTOCOL.md)** 
  * Defines the hard constraints of the ecosystem: Why Orchestrators are prohibited from writing code, why Quality Gates are Read-Only (they cannot fix code, only reject it), and the exact state-machine lifecycle of a user request.

### 2. Architectural Design
* 🏗️ **[Architecture Deep-Dive](docs/en/core/ARCHITECTURE.md)** 
  * Explains the 5-layer Anatomy of the agency (01 to 05). Details the "Abstract Syntax Tree" parsing of user requests and the explicit fallback mechanisms when code fails a Quality Gate.

### 3. Engineering Mindset
* 🧠 **[Core Engineering Principles](docs/en/core/PRINCIPLES.md)** 
  * Documents the "Principal Architect" mindset embedded in the agents. Includes C# code snippets demonstrating Anti-Patterns (e.g., Over-engineered BaseServices) versus Best Practices (CQRS, Defensive Programming, IoC, Database Schema Segregation).

### 4. Process Automation
* 🔄 **[Autonomous Workflows](docs/en/core/WORKFLOWS.md)** 
  * Details the automated routines that eliminate boilerplate. Explains the API Handoff Algorithm (how the system generates JSON diffs between Backend and Frontend) and the exact CLI sequence executed during Project Scaffolding.

## 📋 The Agency Departments & Skill Catalog
The ecosystem consists of **105 strictly defined roles** grouped by professional domains (e.g., `backend_and_data`, `security_and_pentest`). 
👉 **[View the Complete Catalog of all 105 Agents & Skills](docs/en/catalogs/SKILLS_CATALOG.md)**

### 🗺️ Orchestrator Maps
Curious about who reports to whom? Explore the specific delegation diagrams (Mermaid) for our core managers:
* [Master Orchestrator](docs/en/orchestrators/master-orchestrator.md) — The CEO agent.
* [Code Orchestrator](docs/en/orchestrators/code-orchestrator.md) — Manages Backend, Frontend, and Migrations.
* [Security Orchestrator](docs/en/orchestrators/security-orchestrator.md) — Manages Pentesters and IDOR/JWT Specialists.
* [Design Orchestrator](docs/en/orchestrators/design-orchestrator.md) — Manages UX/UI, Brandkit, and Copywriting.
* [Test Orchestrator](docs/en/orchestrators/test-orchestrator.md) — Manages Unit, Smoke, and E2E Testing.
* *(See the [Catalog](docs/en/catalogs/SKILLS_CATALOG.md) for BA, Deployment, and Marketing Orchestrators).*

## ⚙️ Installation & Build
Autonomous Agency uses a centralized SSOT compiler. To inject all 105 rules into your IDEs:

```bash
python3 setup.py
```
This generates the required `.mdc` files for Cursor, `.windsurfrules` for Windsurf, and `clauderules.md` for Claude.

---
*Built for Principal Engineers who demand determinism, not just suggestions.*
