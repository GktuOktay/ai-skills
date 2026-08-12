import os
import subprocess
import shutil

skills_src = r"C:\Users\goktay\.gemini\antigravity\scratch\ai-skills\skills"
rules_src = r"C:\Users\goktay\.gemini\antigravity\scratch\ai-skills\rules"

gemini_config_dir = r"C:\Users\goktay\.gemini\config"
gemini_skills_target = r"C:\Users\goktay\.gemini\config\skills"

cursor_dir = r"C:\Users\goktay\.cursor"
cursor_rules_target = r"C:\Users\goktay\.cursor\rules"

os.makedirs(gemini_config_dir, exist_ok=True)
os.makedirs(cursor_dir, exist_ok=True)

# Function to create junction or copy
def setup_link(target, source, name):
    print(f"Setting up {name}: {target} -> {source}")
    if os.path.exists(target) or os.path.islink(target):
        if os.path.isdir(target) and not os.path.islink(target):
            # Check if it's a junction point
            try:
                os.rmdir(target)
            except Exception:
                shutil.rmtree(target)
        else:
            os.remove(target)
    
    # Try creating directory junction
    cmd = f'cmd /c mklink /J "{target}" "{source}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[OK] Created junction for {name}")
    else:
        print(f"[WARN] Junction failed, copying folder instead: {res.stderr}")
        shutil.copytree(source, target)
        print(f"[OK] Copied files for {name}")

setup_link(gemini_skills_target, skills_src, "Antigravity (Skills)")
setup_link(cursor_rules_target, rules_src, "Cursor (Rules)")
print("[OK] Done!")
