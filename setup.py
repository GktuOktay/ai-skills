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
    print("[1/3] Cursor kurallari derleniyor (build_cursor_rules.py)...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    build_script = os.path.join(base_dir, "build_cursor_rules.py")
    if os.path.exists(build_script):
        res = subprocess.run([sys.executable, build_script], capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] Cursor kurallari basariyla üretildi.")
        else:
            print(f"  [UYARI] Cursor kural üretimi hatasi: {res.stderr}")
    else:
        print("  [ATLANDI] build_cursor_rules.py bulunamadi.")

def setup_link(target_path, source_path, app_name):
    print(f"[{app_name}] baglantisi kuruluyor: {target_path} -> {source_path}")
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    if os.path.exists(target_path) or os.path.islink(target_path):
        if os.path.isdir(target_path) and not os.path.islink(target_path):
            try:
                os.rmdir(target_path)
            except Exception:
                shutil.rmtree(target_path)
        else:
            try:
                os.remove(target_path)
            except Exception:
                pass

    if sys.platform == "win32":
        cmd = f'cmd /c mklink /J "{target_path}" "{source_path}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  [OK] Junction baglantisi kuruldu: {app_name}")
        else:
            shutil.copytree(source_path, target_path)
            print(f"  [OK] Klasor kopyalandi: {app_name}")
    else:
        try:
            os.symlink(source_path, target_path, target_is_directory=True)
            print(f"  [OK] Symlink baglantisi kuruldu: {app_name}")
        except Exception as e:
            shutil.copytree(source_path, target_path)
            print(f"  [OK] Klasor kopyalandi: {app_name}")

def main():
    home = os.path.expanduser("~")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    skills_src = os.path.join(base_dir, "skills")
    rules_src = os.path.join(base_dir, "rules")

    run_build_rules()

    print("\n[2/3] Baglantilar yapilandiriliyor...")
    setup_link(os.path.join(home, ".gemini", "config", "skills"), skills_src, "Antigravity (Gemini)")
    setup_link(os.path.join(home, ".claude", "skills"), skills_src, "Claude Code")
    setup_link(os.path.join(home, ".cursor", "rules"), rules_src, "Cursor Rules")

    print("\n[3/3] Kurulum tamamlandi! Tüm AI yetenekleri ve kurallari global olarak aktif.")

if __name__ == "__main__":
    main()
