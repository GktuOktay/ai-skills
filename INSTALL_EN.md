# 📖 AI Skills - Comprehensive Installation & Usage Guide

[Türkçe](INSTALL.md) | [English](INSTALL_EN.md)

This guide provides step-by-step instructions to integrate `ai-skills` across **Antigravity (Gemini)**, **Cursor AI**, **Claude Code**, **GitHub Copilot**, **OpenAI Codex**, **Windsurf**, and **Generic AI Agents**.

---

## 🛠️ Prerequisites

- **Python 3.8+**
- **Git**

---

## 💻 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills
```

### 2. Run the Universal Setup Wizard

```bash
# Interactive Language Wizard:
python setup.py

# Or pass explicit language flag:
python setup.py --lang en
```

> **What `setup.py` automatically does:**
> 1. Compiles `.mdc` rules for Cursor (`rules/*.mdc`).
> 2. Generates `.github/copilot-instructions.md` for GitHub Copilot.
> 3. Generates `AGENTS.md` and `.windsurfrules` for Windsurf & Generic AI agents.
> 4. Establishes directory links/junctions for Antigravity, Claude Code, Cursor, Codex, and Copilot.

---

## 📁 Agent Integration Matrix

| Agent / IDE | Configuration Path | Linked Source Folder |
| :--- | :--- | :--- |
| **Cursor Global Skills** | `%USERPROFILE%\.cursor\skills-cursor` | `ai-skills/skills` |
| **Cursor Global Rules** | `%USERPROFILE%\.cursor\rules` | `ai-skills/rules` |
| **Cursor Project Rules** | `<project_root>\.cursor\rules` | `ai-skills/rules` |
| **Antigravity (Gemini)** | `%USERPROFILE%\.gemini\config\skills` | `ai-skills/skills` |
| **Claude Code** | `%USERPROFILE%\.claude\skills` | `ai-skills/skills` |
| **OpenAI Codex** | `%USERPROFILE%\.codex\skills` | `ai-skills/skills` |
| **GitHub Copilot** | `%USERPROFILE%\.github\copilot-instructions.md` | `ai-skills/.github/copilot-instructions.md` |
| **Windsurf** | `<project_root>\.windsurfrules` | `ai-skills/.windsurfrules` |
