# 🧠 Universal AI Agent Skills & Rules Library

[Türkçe](README.md) | [English](README_EN.md)

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

## 🙏 Acknowledgements & Credits

We extend our deep gratitude to the open-source creators and maintainers whose work inspired and paved the way for this library:

- **[PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)** - Cursor Rules ecosystem & anti-sycophancy code discipline.
- **[0xcjl/anti-sycophancy](https://github.com/0xcjl/anti-sycophancy)** - Three-layer anti-sycophancy defense & ArXiv *"Ask Don't Tell"* research.
- **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** - Addy Osmani's production-grade engineering principles.
- **[anthropics/skills](https://github.com/anthropics/skills)** - Official Anthropic `SKILL.md` format standard.
- **[SwePalm/socratic-skill](https://github.com/SwePalm/socratic-skill)** & **[m4vic/socratic](https://github.com/m4vic/socratic)** - Socratic clarification gate.
- **[vlad-ko/claude-wizard](https://github.com/vlad-ko/claude-wizard)** - Adversarial code review & showstopper auditing.
- **[ColdIQ/ColdIQ-s-GTM-Skills](https://github.com/Cold-IQ/ColdIQ-s-GTM-Skills)** - Pre-Mortem system stress testing.
- **[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** - Cybersecurity, API testing, and Pentest skill scenarios.

For full attribution details, see **[CREDITS.md](CREDITS.md)** | **[CREDITS_EN.md](CREDITS_EN.md)**.

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
    
```

### Project Directory Tree
```text
ai-skills/
├── .github/                       # GitHub templates & Copilot global instructions
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md
├── agents/                        # Agent-specific modular configurations
│   ├── antigravity/               # Antigravity (Gemini) skills
│   ├── claude-code/               # Claude Code skills
│   ├── codex/                     # OpenAI Codex skills
│   ├── copilot/                   # GitHub Copilot instructions
│   ├── cursor/                    # Cursor rules (.mdc) & skills
│   └── windsurf/                  # Windsurf / Cascade rules
├── docs/                          # Clean documentation folder
│   ├── INSTALL.md                 # Türkçe Kurulum Kılavuzu
│   ├── INSTALL_EN.md              # English Installation Guide
│   ├── CREDITS.md                 # Türkçe Atıflar & Teşekkürler
│   ├── CREDITS_EN.md              # English Acknowledgements & Credits
│   ├── CONTRIBUTING.md            # Katkıda Bulunma Rehberi
│   └── CODE_OF_CONDUCT.md         # Topluluk Kuralları
├── skills/                        # 63+ Modular AI Agent Skills (SKILL.md)
│   ├── anti-sycophancy/
│   ├── master-orchestrator/
│   ├── code-orchestrator/
│   └── ...
├── rules/                         # Compiled Cursor Rules (.mdc)
│   ├── anti-sycophancy.mdc
│   ├── master-orchestrator.mdc
│   └── ...
├── scripts/                       # Internal build & utility scripts
│   ├── build_agent_folders.py
│   ├── build_cursor_rules.py
│   └── update_skill_descriptions.py
├── AGENTS.md                      # Universal Agents definition
├── .windsurfrules                 # Windsurf / Cascade rules
├── LICENSE                        # MIT License
├── README.md                      # Default Turkish Homepage
├── README_EN.md                    # English Homepage
└── setup.py                       # Universal Setup Wizard
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

## 🚀 Quick Start & Installation

Install and link all skills across all installed AI agents with an interactive setup wizard:

```bash
# 1. Clone the repository
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills

# 2. Run universal setup script
python setup.py

# Or run non-interactively with a language flag:
python setup.py --lang en
python setup.py --lang tr
```

For detailed setup instructions, see **[INSTALL.md](INSTALL.md)** | **[INSTALL_EN.md](INSTALL_EN.md)**.

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
