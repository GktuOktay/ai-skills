#!/usr/bin/env python3
"""
AI-Skills v2.0 - Universal Enterprise Build Script
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
    
    global_enforcer = "\n\nCRITICAL INSTRUCTION: You MUST communicate and explain everything to the user in fluent Turkish. Code, variable names, and technical terms should remain in English, but the prose MUST be Turkish.\n"
    
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
            
            body += global_enforcer
            
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
        
    print(f"\n✅ Build Complete!")
    print(f"   - {cursor_count} rules compiled for Cursor (.mdc)")
    print(f"   - 1 global rule file compiled for Windsurf (.windsurfrules)")
    print(f"   - 1 global rule file compiled for Claude (clauderules.md)")

if __name__ == "__main__":
    clean_old_artifacts()
    build()
