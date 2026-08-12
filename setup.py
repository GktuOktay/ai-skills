#!/usr/bin/env python3
"""
AI Skills & Rules Universal Setup Script
Supports: Antigravity (Gemini), Cursor, Claude Code, GitHub Copilot, OpenAI Codex, Windsurf, and Generic Agents.
Supports Interactive Language Prompt (English / Turkce).
"""

import os
import sys
import shutil
import subprocess

def parse_language_preference():
    lang = None
    for arg in sys.argv[1:]:
        if arg.startswith("--lang="):
            lang = arg.split("=")[1].strip().lower()
        elif arg == "--lang" and sys.argv.index(arg) + 1 < len(sys.argv):
            lang = sys.argv[sys.argv.index(arg) + 1].strip().lower()

    if lang in ["en", "english"]:
        return "en"
    elif lang in ["tr", "turkce", "turkish"]:
        return "tr"

    # Interactive prompt if stdin is tty
    if sys.stdin.isatty():
        print("\n=======================================================")
        print("  Select Setup Language / Kurulum Dilini Secin:")
        print("  [1] English")
        print("  [2] Turkce (Varsayilan / Default)")
        print("=======================================================")
        choice = input("Select / Seciminiz [1/2]: ").strip()
        if choice == "1":
            return "en"
        else:
            return "tr"
    return "en"

def run_build_rules(lang):
    title = "[1/6] Compiling Cursor rules (build_cursor_rules.py)..." if lang == "en" else "[1/6] Cursor kurallari derleniyor (build_cursor_rules.py)..."
    print(title)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    build_script = os.path.join(base_dir, "build_cursor_rules.py")
    if os.path.exists(build_script):
        res = subprocess.run([sys.executable, build_script], capture_output=True, text=True)
        if res.returncode == 0:
            msg = "  [OK] Cursor rules (.mdc) compiled successfully." if lang == "en" else "  [OK] Cursor kurallari (.mdc) basariyla uretildi."
            print(msg)
        else:
            print(f"  [WARN] Cursor rule build error: {res.stderr}")

def generate_copilot_instructions(base_dir, lang):
    title = "[2/6] Generating GitHub Copilot instructions (.github/copilot-instructions.md)..." if lang == "en" else "[2/6] GitHub Copilot talimatlari uretiliyor (.github/copilot-instructions.md)..."
    print(title)
    github_dir = os.path.join(base_dir, ".github")
    os.makedirs(github_dir, exist_ok=True)
    copilot_file = os.path.join(github_dir, "copilot-instructions.md")

    skills_dir = os.path.join(base_dir, "skills")
    key_skills = ["anti-sycophancy", "master-orchestrator", "code-orchestrator", "clean-code-reviewer", "socratic-clarification-gate", "full-output-enforcement"]
    
    content = "# Universal AI Agent Instructions (GitHub Copilot & Agents)\n\n"
    content += "You are an expert AI agent. Enforce the following core skills and principles:\n\n"
    
    for sk in key_skills:
        sk_path = os.path.join(skills_dir, sk, "SKILL.md")
        if os.path.exists(sk_path):
            with open(sk_path, "r", encoding="utf-8") as f:
                txt = f.read()
                if txt.startswith("---"):
                    end_idx = txt.find("---", 3)
                    if end_idx != -1:
                        txt = txt[end_idx+3:].strip()
                content += f"## Skill: {sk}\n\n{txt}\n\n---\n\n"

    with open(copilot_file, "w", encoding="utf-8") as f:
        f.write(content)
    msg = "  [OK] GitHub Copilot instructions generated: .github/copilot-instructions.md" if lang == "en" else "  [OK] GitHub Copilot talimati uretildi: .github/copilot-instructions.md"
    print(msg)
    return copilot_file

def generate_agents_md(base_dir, copilot_file, lang):
    title = "[3/6] Generating Generic AGENTS.md and Windsurf (.windsurfrules)..." if lang == "en" else "[3/6] Generic AGENTS.md ve Windsurf (.windsurfrules) uretiliyor..."
    print(title)
    agents_file = os.path.join(base_dir, "AGENTS.md")
    windsurf_file = os.path.join(base_dir, ".windsurfrules")
    shutil.copyfile(copilot_file, agents_file)
    shutil.copyfile(copilot_file, windsurf_file)
    msg = "  [OK] AGENTS.md and .windsurfrules generated." if lang == "en" else "  [OK] AGENTS.md ve .windsurfrules uretildi."
    print(msg)

def setup_link(target_path, source_path, app_name):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    if os.path.exists(target_path) or os.path.islink(target_path):
        if os.path.isdir(target_path) and not os.path.islink(target_path):
            try:
                os.rmdir(target_path)
            except Exception:
                return
        else:
            try:
                os.remove(target_path)
            except Exception:
                return

    if sys.platform == "win32":
        cmd = f'cmd /c mklink /J "{target_path}" "{source_path}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [OK] Junction: {app_name}")
        else:
            try:
                shutil.copytree(source_path, target_path)
                print(f"  [OK] Copy: {app_name}")
            except Exception:
                pass
    else:
        try:
            os.symlink(source_path, target_path, target_is_directory=True)
            print(f"  [OK] Symlink: {app_name}")
        except Exception:
            try:
                shutil.copytree(source_path, target_path)
                print(f"  [OK] Copy: {app_name}")
            except Exception:
                pass

def link_individual_skills(skills_src, target_dir, app_name, lang):
    os.makedirs(target_dir, exist_ok=True)
    folders = [f for f in os.listdir(skills_src) if os.path.isdir(os.path.join(skills_src, f))]
    for folder in folders:
        src = os.path.join(skills_src, folder)
        tgt = os.path.join(target_dir, folder)
        if not os.path.exists(tgt) and not os.path.islink(tgt):
            if sys.platform == "win32":
                subprocess.run(f'cmd /c mklink /J "{tgt}" "{src}"', shell=True, capture_output=True)
            else:
                try:
                    os.symlink(src, tgt, target_is_directory=True)
                except Exception:
                    pass
    msg = f"  [OK] Linked {len(folders)} skills to {app_name}." if lang == "en" else f"  [OK] {len(folders)} adet skill {app_name} alanina baglandi."
    print(msg)

def main():
    lang = parse_language_preference()
    home = os.path.expanduser("~")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    skills_src = os.path.join(base_dir, "skills")
    rules_src = os.path.join(base_dir, "rules")

    run_build_rules(lang)
    copilot_file = generate_copilot_instructions(base_dir, lang)
    generate_agents_md(base_dir, copilot_file, lang)

    title4 = "\n[4/6] Linking project-level Agent rules/skills..." if lang == "en" else "\n[4/6] Proje seviyesi Agent baglantilari kuruluyor..."
    print(title4)
    setup_link(os.path.join(base_dir, ".cursor", "rules"), rules_src, "Cursor Project Rules (.cursor/rules)")
    setup_link(os.path.join(base_dir, ".agents", "skills"), skills_src, "Antigravity Project Skills (.agents/skills)")
    setup_link(os.path.join(base_dir, ".claude", "skills"), skills_src, "Claude Code Project Skills (.claude/skills)")
    setup_link(os.path.join(base_dir, ".codex", "skills"), skills_src, "Codex Project Skills (.codex/skills)")

    title5 = "\n[5/6] Configuring global Agent skills & rules..." if lang == "en" else "\n[5/6] Global Agent yetenek ve kural baglantilari yapilandiriliyor..."
    print(title5)
    link_individual_skills(skills_src, os.path.join(home, ".cursor", "skills-cursor"), "Cursor Global Skills (~/.cursor/skills-cursor)", lang)
    setup_link(os.path.join(home, ".cursor", "rules"), rules_src, "Cursor Global Rules (~/.cursor/rules)")
    setup_link(os.path.join(home, ".gemini", "config", "skills"), skills_src, "Antigravity Global (~/.gemini/config/skills)")
    setup_link(os.path.join(home, ".claude", "skills"), skills_src, "Claude Code Global (~/.claude/skills)")
    setup_link(os.path.join(home, ".codex", "skills"), skills_src, "OpenAI Codex Global (~/.codex/skills)")
    setup_link(os.path.join(home, ".agents", "skills"), skills_src, "Generic Agents Global (~/.agents/skills)")
    
    global_copilot_dir = os.path.join(home, ".github")
    os.makedirs(global_copilot_dir, exist_ok=True)
    shutil.copyfile(copilot_file, os.path.join(global_copilot_dir, "copilot-instructions.md"))
    msg_copilot = "  [OK] GitHub Copilot Global Instructions (~/.github/copilot-instructions.md) created." if lang == "en" else "  [OK] GitHub Copilot Global Talimati (~/.github/copilot-instructions.md) olusturuldu."
    print(msg_copilot)

    final_msg = "\n[6/6] CONGRATULATIONS! Universal AI Agent setup complete for all agents." if lang == "en" else "\n[6/6] TEBRIKLER! Tum AI Agent'lar icin evrensel kurulum tamamlandi."
    print(final_msg)

if __name__ == "__main__":
    main()
