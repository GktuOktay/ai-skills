#!/usr/bin/env python3
"""
Autonomous Agency v2.0 - Universal Enterprise Build Script
This script acts as the Single Source of Truth (SSOT) compiler.
It reads from 'src/skills/' and generates the required artifacts for Cursor, Claude, and Windsurf.
No symlink spaghetti, no hidden folders. Just pure artifact generation.
"""

import os
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
skills_dir = os.path.join(base_dir, "src", "skills")
cursor_rules_dir = os.path.join(base_dir, "rules")

def clean_old_artifacts():
    print("[1/3] Cleaning old IDE artifacts...")
    if os.path.exists(cursor_rules_dir):
        for f in glob.glob(os.path.join(cursor_rules_dir, "*.mdc")):
            os.remove(f)
    else:
        os.makedirs(cursor_rules_dir, exist_ok=True)

def build():
    print("[2/3] Compiling Single Source of Truth (src/skills/)...")
    
    
    global_persona = """
# GLOBAL PERSONA & BEHAVIORAL DIRECTIVES
You are a Principal Software Architect within an Autonomous Agency. You MUST strictly adhere to the following behavioral traits in every response:
1. **Anti-Sycophancy:** NEVER use robotic apologies ("I apologize"), sycophantic praise ("Great question!"), or filler phrases ("As an AI"). Be cold, deterministic, authoritative, and fiercely professional.
2. **Zero-Fluff (No Yapping):** Provide only the requested architecture or code. Do not explain line-by-line what the code does unless explicitly triggered by a `/teach-me` command.
3. **The Challenger:** If the user requests an anti-pattern or a bad architectural decision, DO NOT blindly obey. Push back, highlight the risks, and enforce the Enterprise standard.
4. **Zero-Assumption Protocol:** Never guess missing requirements. If a task is ambiguous, halt execution immediately and present the user with a choice to resolve the ambiguity (Fail-fast).
5. **Incremental Builder:** Do not dump massive walls of code. Break complex tasks into iterative steps. Ask for user approval after completing a logical boundary before moving to the next.
6. **Security Paranoia:** Always assume external inputs are malicious. Inherently apply Defensive Programming reflexes without needing to be told.
7. **Reusability Hunter (DRY):** Before writing net-new code, ALWAYS scan the codebase for existing generic abstractions (components, repositories, utilities). Reuse existing structures rather than duplicating logic.
8. **Scientific Debugger:** When encountering errors, DO NOT use random trial-and-error code mutations. Stop, analyze the logs, state a clear hypothesis for the root-cause, and ONLY then apply a targeted fix.
9. **Lean & Cost-Aware:** Strictly oppose adding heavy external dependencies (npm/NuGet packages) if the problem can be solved natively with a few lines of code. Always favor the most performant and cloud-cost-efficient architecture.
"""

    global_enforcer = "\n\nCRITICAL INSTRUCTION: You MUST communicate and explain everything to the user in fluent Turkish. Code, variable names, and technical terms should remain in English, but the prose MUST be Turkish.\n"
    
    global_combined = global_persona + global_enforcer

    
    cursor_count = 0
    windsurf_content = "## Windsurf Global Rules\n\n"
    claude_content = "## Claude Code Global Rules\n\n"
    
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            skill_name = os.path.basename(root)
            md_path = os.path.join(root, "SKILL.md")
            
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            if not content.startswith("---"): continue
            end_idx = content.find("---", 3)
            if end_idx == -1: continue
            
            frontmatter = content[3:end_idx].strip()
            body = content[end_idx+3:].strip()
            
            description = ""
            always_apply = False
            for line in frontmatter.split("\n"):
                line = line.strip()
                if line.startswith("description:"):
                    description = line.replace("description:", "").strip().strip('"').strip("'")
                if line.startswith("alwaysApply:") and "true" in line.lower():
                    always_apply = True
            
            body += global_combined
            
            # 1. Cursor (.mdc) Generation
            mdc_content = f"---\ndescription: {description}\nglobs: *\n" if always_apply or "gate" in skill_name or "enforcer" in skill_name else f"---\ndescription: {description}\nglobs: *{skill_name}*\n"
            mdc_content += f"---\n\n{body}"
            
            with open(os.path.join(cursor_rules_dir, f"{skill_name}.mdc"), "w", encoding="utf-8") as f:
                f.write(mdc_content)
            cursor_count += 1
            
            if "gate" in skill_name or "orchestrator" in skill_name or "workflow" in skill_name:
                section = f"### {skill_name}\n{description}\n{body}\n\n"
                windsurf_content += section
                claude_content += section
                
    print("[3/3] Generating IDE specific artifacts...")
    with open(os.path.join(base_dir, ".windsurfrules"), "w", encoding="utf-8") as f:
        f.write(windsurf_content)
    with open(os.path.join(base_dir, "clauderules.md"), "w", encoding="utf-8") as f:
        f.write(claude_content)
        
    # NEW: Roo Code (Cline) Support

" + claude_content.replace("## Claude Code Global Rules

", "")
    with open(os.path.join(base_dir, ".clinerules"), "w", encoding="utf-8") as f:
        f.write(roo_content)

    # NEW: Aider / Copilot Conventions Support

" + claude_content.replace("## Claude Code Global Rules

", "")
    with open(os.path.join(base_dir, "CONVENTIONS.md"), "w", encoding="utf-8") as f:
        f.write(aider_content)
        
    print(f"
✅ Build Complete!")
    print(f"   - {cursor_count} rules compiled for Cursor (.mdc)")
    print(f"   - 1 global rule file compiled for Windsurf (.windsurfrules)")
    print(f"   - 1 global rule file compiled for Claude (clauderules.md)")
    print(f"   - 1 global rule file compiled for Roo Code (.clinerules)")
    print(f"   - 1 global rule file compiled for Aider/Copilot (CONVENTIONS.md)")

if __name__ == "__main__":
    clean_old_artifacts()
    build()
    # NEW: Roo Code (Cline) Support
    roo_content = "# Roo Code / Cline Global Rules\n\n" + claude_content.replace("## Claude Code Global Rules\n\n", "")
    with open(os.path.join(base_dir, ".clinerules"), "w", encoding="utf-8") as f:
        f.write(roo_content)

    # NEW: Aider / Copilot Conventions Support
    aider_content = "# Aider / GitHub Copilot Conventions\n\n" + claude_content.replace("## Claude Code Global Rules\n\n", "")
    with open(os.path.join(base_dir, "CONVENTIONS.md"), "w", encoding="utf-8") as f:
        f.write(aider_content)
        
    print(f"\n✅ Build Complete!")
    print(f"   - {cursor_count} rules compiled for Cursor (.mdc)")
    print(f"   - 1 global rule file compiled for Windsurf (.windsurfrules)")
    print(f"   - 1 global rule file compiled for Claude (clauderules.md)")
    print(f"   - 1 global rule file compiled for Roo Code (.clinerules)")
    print(f"   - 1 global rule file compiled for Aider/Copilot (CONVENTIONS.md)")

if __name__ == "__main__":
    clean_old_artifacts()
    build()
