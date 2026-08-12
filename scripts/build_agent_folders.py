import os
import shutil

base_dir = r"C:\Users\goktay\.gemini\antigravity\scratch\ai-skills"
agents_dir = os.path.join(base_dir, "agents")

os.makedirs(agents_dir, exist_ok=True)

# Agent specific subdirectories
antigravity_dir = os.path.join(agents_dir, "antigravity")
cursor_dir = os.path.join(agents_dir, "cursor")
claude_dir = os.path.join(agents_dir, "claude-code")
copilot_dir = os.path.join(agents_dir, "copilot")
codex_dir = os.path.join(agents_dir, "codex")
windsurf_dir = os.path.join(agents_dir, "windsurf")

for d in [antigravity_dir, cursor_dir, claude_dir, copilot_dir, codex_dir, windsurf_dir]:
    os.makedirs(d, exist_ok=True)

# Copy/Link files for each agent
# 1. Antigravity
ag_skills = os.path.join(antigravity_dir, "skills")
if not os.path.exists(ag_skills) and not os.path.islink(ag_skills):
    if os.name == 'nt':
        os.system(f'cmd /c mklink /J "{ag_skills}" "{os.path.join(base_dir, "skills")}"')
    else:
        os.symlink(os.path.join(base_dir, "skills"), ag_skills, target_is_directory=True)

# 2. Cursor
cs_rules = os.path.join(cursor_dir, "rules")
if not os.path.exists(cs_rules) and not os.path.islink(cs_rules):
    if os.name == 'nt':
        os.system(f'cmd /c mklink /J "{cs_rules}" "{os.path.join(base_dir, "rules")}"')
    else:
        os.symlink(os.path.join(base_dir, "rules"), cs_rules, target_is_directory=True)

# 3. Claude Code
cl_skills = os.path.join(claude_dir, "skills")
if not os.path.exists(cl_skills) and not os.path.islink(cl_skills):
    if os.name == 'nt':
        os.system(f'cmd /c mklink /J "{cl_skills}" "{os.path.join(base_dir, "skills")}"')
    else:
        os.symlink(os.path.join(base_dir, "skills"), cl_skills, target_is_directory=True)

# 4. Copilot
cop_inst = os.path.join(base_dir, ".github", "copilot-instructions.md")
if os.path.exists(cop_inst):
    shutil.copyfile(cop_inst, os.path.join(copilot_dir, "copilot-instructions.md"))

# 5. Codex
cx_skills = os.path.join(codex_dir, "skills")
if not os.path.exists(cx_skills) and not os.path.islink(cx_skills):
    if os.name == 'nt':
        os.system(f'cmd /c mklink /J "{cx_skills}" "{os.path.join(base_dir, "skills")}"')
    else:
        os.symlink(os.path.join(base_dir, "skills"), cx_skills, target_is_directory=True)

# 6. Windsurf
ws_file = os.path.join(base_dir, ".windsurfrules")
if os.path.exists(ws_file):
    shutil.copyfile(ws_file, os.path.join(windsurf_dir, ".windsurfrules"))

print("[OK] Agent folders structured successfully under agents/")
