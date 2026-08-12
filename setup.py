#!/usr/bin/env python3
"""
AI Skills & Rules Installation Script
Supports Windows, macOS, and Linux for Antigravity, Cursor, and Claude Code.
"""

import os
import sys
import shutil
import subprocess

def run_build_rules():
    print("[1/5] Cursor kurallari derleniyor (build_cursor_rules.py)...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    build_script = os.path.join(base_dir, "build_cursor_rules.py")
    if os.path.exists(build_script):
        res = subprocess.run([sys.executable, build_script], capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] Cursor kurallari basariyla uretildi.")
        else:
            print(f"  [UYARI] Cursor kural uretimi hatasi: {res.stderr}")
    else:
        print("  [ATLANDI] build_cursor_rules.py bulunamadi.")

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
                print(f"  [OK] Kopya: {app_name}")
            except Exception:
                pass
    else:
        try:
            os.symlink(source_path, target_path, target_is_directory=True)
            print(f"  [OK] Symlink: {app_name}")
        except Exception:
            try:
                shutil.copytree(source_path, target_path)
                print(f"  [OK] Kopya: {app_name}")
            except Exception:
                pass

def link_individual_cursor_skills(skills_src, cursor_skills_dir):
    os.makedirs(cursor_skills_dir, exist_ok=True)
    folders = [f for f in os.listdir(skills_src) if os.path.isdir(os.path.join(skills_src, f))]
    count = 0
    for folder in folders:
        src = os.path.join(skills_src, folder)
        tgt = os.path.join(cursor_skills_dir, folder)
        if not os.path.exists(tgt) and not os.path.islink(tgt):
            if sys.platform == "win32":
                subprocess.run(f'cmd /c mklink /J "{tgt}" "{src}"', shell=True, capture_output=True)
            else:
                try:
                    os.symlink(src, tgt, target_is_directory=True)
                except Exception:
                    pass
            count += 1
    print(f"  [OK] {len(folders)} adet skill Cursor global yetenekler alanina (~/.cursor/skills-cursor) eklendi.")

def main():
    home = os.path.expanduser("~")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    skills_src = os.path.join(base_dir, "skills")
    rules_src = os.path.join(base_dir, "rules")

    run_build_rules()

    print("\n[2/5] Proje seviyesi Cursor kurallari baglaniyor (.cursor/rules)...")
    local_cursor_rules = os.path.join(base_dir, ".cursor", "rules")
    setup_link(local_cursor_rules, rules_src, "Cursor Proje Rules (.cursor/rules)")

    print("\n[3/5] Cursor Global Skills yapilandiriliyor (~/.cursor/skills-cursor)...")
    link_individual_cursor_skills(skills_src, os.path.join(home, ".cursor", "skills-cursor"))

    print("\n[4/5] Global baglantilar yapilandiriliyor...")
    setup_link(os.path.join(home, ".gemini", "config", "skills"), skills_src, "Antigravity (Gemini)")
    setup_link(os.path.join(home, ".claude", "skills"), skills_src, "Claude Code")
    setup_link(os.path.join(home, ".cursor", "rules"), rules_src, "Cursor Global Rules (~/.cursor/rules)")

    print("\n[5/5] Kurulum tamamlandi! Tüm AI yetenekleri ve kurallari global olarak aktif.")

if __name__ == "__main__":
    main()
