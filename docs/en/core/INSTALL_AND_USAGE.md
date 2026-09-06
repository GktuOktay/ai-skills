# 🛠️ Installation & Usage Guide

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/core/INSTALL_AND_USAGE.md)

This guide explains step-by-step how to integrate the **Autonomous Agency** ecosystem into your local project and how to manage the 105 agents.

## 1. Prerequisites
- **Python 3.8+** must be installed on your machine (for the build script).
- You must be using a supported AI IDE (Cursor, Windsurf) or CLI Tool (Claude Code) to execute the agents.

## 2. Building the System
This repository contains the source code for the agent rules. To use them in your own project, you must build them first:

1. Clone the repository:
   ```bash
   git clone https://github.com/GktuOktay/autonomous-agency.git
   cd autonomous-agency
   ```
2. Run the setup script:
   ```bash
   python3 setup.py
   ```
   *This command parses the raw data in `src/skills/` and generates the `rules/` directory, `.windsurfrules`, and `clauderules.md`.*

## 3. IDE Integration

### 🖱️ For Cursor
1. After running `setup.py`, copy all the `.mdc` files generated inside the `rules/` directory.
2. In your target project's root directory, create a `.cursor/rules/` folder (if it doesn't exist).
3. Paste all the `.mdc` files there. Cursor will automatically detect the agents.

### 🏄‍♂️ For Windsurf
1. After running `setup.py`, copy the generated `.windsurfrules` file.
2. Paste it directly into the root directory of your target project.

### 🤖 For Claude Code (CLI)
1. Copy the generated `clauderules.md` file to your working directory and provide it as context when launching Claude Code.

---

## 4. Usage Discipline (How to communicate)
When communicating with the agents, do not treat them like a standard "ChatGPT". The system relies on strict hierarchy.

### ❌ Bad Practice (Commanding Specialists Directly)
> *"Build me a login page, connect the database, and write the tests."*
**(Error:** Specific agents (e.g., .NET Architect) cannot draw frontend UI. The agent will get confused and fail the Quality Gates.)

### ✅ Best Practice (Triggering Orchestrators)
Always direct your requests to the **Master Orchestrator** or the relevant department manager:
> *"Act as the Master Orchestrator: I want an e-commerce cart structure similar to Amazon. Coordinate the Code Orchestrator and Design Orchestrator to complete this task."*

Once the manager (Orchestrator) receives this command, it will autonomously wake up the Database Architect, have the Backend specialist write the code, and enforce the Quality Gates sequentially.
