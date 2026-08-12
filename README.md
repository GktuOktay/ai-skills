# 🧠 Universal AI Agent Skills & Rules Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Platform: Antigravity](https://img.shields.io/badge/Antigravity-Supported-brightgreen.svg)]()
[![Platform: Cursor](https://img.shields.io/badge/Cursor-Supported-blue.svg)]()
[![Platform: Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-orange.svg)]()
[![Platform: GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Supported-purple.svg)]()
[![Platform: OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-Supported-black.svg)]()
[![Platform: Windsurf](https://img.shields.io/badge/Windsurf-Supported-teal.svg)]()

> **Universal Open-Source AI Agent Library** providing production-grade engineering skills, orchestrator agents, anti-sycophancy discipline, and specialized rules for **Antigravity (Gemini)**, **Cursor AI**, **Claude Code**, **GitHub Copilot**, **OpenAI Codex**, and **Windsurf**.

---

## 🏛️ Architecture & Orchestration Flow

This repository features a **Master Orchestrator Engine** that coordinates sub-orchestrators and enforces objective code discipline across all LLM tools:

```mermaid
graph TD
    User["User Prompt"] --> MO["master-orchestrator (Central Command Node)"]
    
    subgraph "Gates & Quality Control"
        MO --> AS["anti-sycophancy (Objective Critique Gate)"]
        MO --> SCG["socratic-clarification-gate (Requirement Inspector)"]
    end
    
    subgraph "Specialized Sub-Orchestrators"
        AS --> CO["code-orchestrator (Engineering & Refactoring)"]
        AS --> DO["design-orchestrator (UI/UX & Aesthetics)"]
        AS --> SO["security-orchestrator (Security & Pentest)"]
        AS --> TO["test-orchestrator (QA & Testing)"]
        AS --> GO["git-orchestrator (Git & Releases)"]
        AS --> DocO["docs-orchestrator (Business & Analysis)"]
    end
    
    subgraph "Pre-Delivery Audit"
        CO --> ACR["adversarial-code-reviewer (Showstopper Audit)"]
        CO --> PM["pre-mortem-stress-test (System Stress Test)"]
    end
    
    ACR --> Final["Production-Grade Finalized Output"]
```

---

## 🌟 Universal Agent Compatibility Matrix

| AI Agent / IDE | Native Format | Global Path | Workspace Path |
| :--- | :--- | :--- | :--- |
| 🟢 **Antigravity (Gemini)** | `SKILL.md` | `~/.gemini/config/skills` | `.agents/skills` |
| 🔵 **Cursor AI** | `.mdc` & `skills-cursor` | `~/.cursor/rules` & `skills-cursor` | `.cursor/rules` |
| 🟠 **Claude Code** | `SKILL.md` | `~/.claude/skills` | `.claude/skills` |
| 🟣 **GitHub Copilot** | `copilot-instructions.md` | `~/.github/copilot-instructions.md` | `.github/copilot-instructions.md` |
| 🖤 **OpenAI Codex / CLI** | `SKILL.md` & `AGENTS.md` | `~/.codex/skills` | `.codex/skills` |
| 🪟 **Windsurf / Cascade** | `.windsurfrules` | - | `.windsurfrules` |
| 🤖 **Generic AI Agents** | `AGENTS.md` | `~/.agents/skills` | `AGENTS.md` |

---

## 📚 Complete Skill Catalog (63 Skills)

### 🎯 1. Anti-Sycophancy & Core Discipline
- **`anti-sycophancy`**: Rejects false validation; enforces objective critique, risk exposure, and constructive alternatives.
- **`socratic-clarification-gate`**: Prevents premature code generation on ambiguous prompts; asks targeted clarifying questions.
- **`full-output-enforcement`**: Meta-skill preventing truncated outputs (`...`, `// rest of code unchanged`).

### 🎼 2. Master & Domain Orchestrators
- **`master-orchestrator`**: Central command node routing tasks to sub-orchestrators while enforcing anti-sycophancy gates.
- **`code-orchestrator`**: Manages code architecture, refactoring, and code review flows.
- **`design-orchestrator`**: Coordinates UI/UX design, animations, and frontend aesthetic standards.
- **`security-orchestrator`**: Coordinates cybersecurity audits, pentesting, and vulnerability scans.
- **`test-orchestrator`**: Coordinates QA suites, unit testing, E2E scenarios, and load testing.
- **`git-orchestrator`**: Coordinates commit discipline, PR reviews, issue management, and versioning.
- **`docs-orchestrator`**: Coordinates technical business analysis, spec writing, and document generation.

### 🛡️ 3. Security & Vulnerability Auditing
- **`api-pentest`**: Endpoint security, rate limiting, SQL/NoSQL injection prevention, and JWT authorization tests.
- **`client-security`**: Frontend security, XSS/CSRF prevention, CSP headers, and DOM vulnerability audits.
- **`secret-scanner`**: Scans codebase for leaked API keys, credentials, certificates, and `.env` misconfigurations.
- **`dependency-audit`**: Dependency vulnerability auditing (npm, pip, etc.), CVE scanning, and supply chain security.
- **`db-architect-security`**: Database schema safety, ORM query optimization, and SQL injection prevention.

### 🔍 4. Code Quality & Adversarial Review
- **`clean-code-reviewer`**: SOLID, DRY, YAGNI, and Addy Osmani production-grade engineering principles.
- **`adversarial-code-reviewer`**: Pre-delivery "Devil's Advocate" audit for unhandled exceptions, memory leaks, and showstoppers.
- **`pre-mortem-stress-test`**: Pre-release system stress simulation ("If this system fails, where does it break?").
- **`swift-architecture-auditor`**: Swift, SwiftUI, MVVM/VIPER/TCA architecture and memory leak auditing.

### 🎨 5. UI/UX & Frontend Excellence
- **`high-end-visual-design`**: Premium UI principles, glassmorphism, optical alignment, and micro-interactions.
- **`design-taste-frontend`**: Typography, spacing, color harmonies, and layout patterns for web/mobile.
- **`apple-design`**: Apple Human Interface Guidelines (HIG) compliance for iOS, macOS, and visionOS.
- **`ui-animation`**: Web and mobile animation principles, terminology, and performance optimization.
- **`image-to-code`**: Converts mockups, Figma designs, or screenshots into pixel-perfect responsive code.
- **`imagegen-frontend`**: AI prompt engineering for web hero images, icons, and UI assets.

### 🧪 6. Testing & Quality Assurance
- **`unit-test-architect`**: Unit testing guidelines, mock/stub patterns, and edge-case coverage.
- **`e2e-tester`**: Playwright, Cypress, and Appium end-to-end user scenario testing.
- **`performance-tester`**: Load testing, memory leak detection, benchmarking, and performance optimization.
- **`smoke-monkey-tester`**: Chaos testing, random input stress tests, and smoke test suites.

### 🌿 7. Git & Release Management
- **`git-conventional-commits`**: Enforces Conventional Commits standard and clean branch naming.
- **`git-pr-reviewer`**: Constructive Pull Request code reviews and merge strategies.
- **`git-issue-manager`**: Effective issue reporting, feature request templates, and triage labeling.
- **`git-repo-setup`**: Community repository standards (README, CONTRIBUTING, rules).
- **`version-bump`**: Semantic versioning and automated release notes generation.
- **`change-tracker`**: Automated Markdown changelog and version history maintenance.

### 📄 8. Documentation & Product Analysis
- **`tech-business-analyst`**: Bridges UX concepts into technical specs, data models, and developer task breakdowns.
- **`product-designer`**: Product design, UX wireframing, and user journey mapping.
- **`feature-ideator`**: Product feature ideation and backlog planning.
- **`copywriting`**: Clear CTA, error message, and UI microcopy writing.
- **`docx` / `pdf` / `pptx` / `xlsx`**: Document generation tools for Word, PDF, PowerPoint, and Excel.

### ⚡ 9. Token Efficiency & Caveman Modes
- **`caveman` / `cavecrew` / `caveman-commit` / `caveman-compress` / `caveman-review` / `caveman-stats` / `caveman-help`**: Ultra-compressed communication modes cutting context token usage by ~65%.

---

## 🚀 Quick Start & Installation

Install and link all 63 skills and rules across all installed AI agents with a single command:

```bash
# 1. Clone the repository
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills

# 2. Run universal setup script (Windows, macOS, Linux)
python setup.py
```

`setup.py` automatically compiles Cursor `.mdc` rules, generates `copilot-instructions.md`, `AGENTS.md`, `.windsurfrules`, and links all skills to global and local agent directories.

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting Pull Requests.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
