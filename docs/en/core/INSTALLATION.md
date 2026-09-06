# ⚙️ Advanced Installation & IDE Integration Guide

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/core/INSTALLATION.md)

**Autonomous Agency (v2.0)** is an architecture directly integrated into your IDE. This guide details how to seamlessly link the generated agent rules to your preferred AI coding assistant (Cursor, Windsurf, Claude Code, Copilot/Codex).

## 1. Compiling the Architecture (Build Process)
The source files in the repository (`src/skills/`) cannot be read directly by IDEs. You must compile these rules using the `setup.py` file, which is the heart of the system.

```bash
# 1. Clone the repository
git clone https://github.com/GktuOktay/autonomous-agency.git
cd autonomous-agency

# 2. Run the SSOT (Single Source of Truth) Compiler
python3 setup.py
```
**Outputs:**
When this process finishes, the following files will be generated:
- `rules/*.mdc` (109 parsed rule files for Cursor)
- `.windsurfrules` (Global context file for Windsurf)
- `clauderules.md` (Global context for Claude Code CLI)
- `.clinerules` (Global context for Roo Code)
- `CONVENTIONS.md` (Global context for Aider / Copilot)

---

## 2. Environment & IDE Integrations

### 🖱️ Cursor (Recommended Environment)
Because Cursor supports the `.mdc` (Markdown Cursor) architecture, it can autonomously activate the permissions of all 109 agents based on folders and file extensions (globs).

**Steps:**
1. Navigate to the root directory of your own working project (e.g., `cd ~/Desktop/My-Ecommerce-Project`).
2. Create a hidden folder named `.cursor/rules`:
   ```bash
   mkdir -p .cursor/rules
   ```
3. Copy **all `.mdc` files** generated in the `autonomous-agency/rules/` folder to this new folder.
4. **IDE Setting:** Restart Cursor. Ensure all copied agents are listed as active (Enabled) under `Settings > General > Rules`.

### 🏄‍♂️ Windsurf
Windsurf prefers reading agent rules from a single global file.

**Steps:**
1. Navigate to the root directory of your own working project.
2. Copy the `.windsurfrules` file generated from the compilation to the root directory.
3. Open the Windsurf application. When Cascade mode runs, our agents will automatically start reading the Master Orchestrator rules from this file.

### 🤖 Claude Code (Terminal / CLI)
Claude's CLI version works with file-based context injection.

**Steps:**
1. Move the generated `clauderules.md` file to your project's root directory.
2. Force the context into the system when launching Claude Code in the terminal:
   ```bash
   claude --context clauderules.md
   ```

### 💻 GitHub Copilot & OpenAI Codex & Aider
If you are using Copilot or Aider, you must link the agent rules to standard guidelines.

**Steps:**
1. Create a `.github/` folder in your project.
2. Take the content of the `CONVENTIONS.md` file, create a file named `.github/copilot-instructions.md`, and paste it inside.
3. Chat interfaces will base their code generation on these constraints and Quality Gates.
