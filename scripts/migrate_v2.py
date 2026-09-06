import os
import shutil

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills"
old_skills_dir = os.path.join(base_dir, "skills")
new_skills_dir = os.path.join(base_dir, "src", "skills")

categories = {
    "01_orchestrators": [],
    "02_specialists": [],
    "03_quality_gates": [],
    "04_workflows": [],
    "05_capabilities": []
}

def determine_category_and_name(old_name):
    name = old_name.lower()
    
    # 01 Orchestrators
    if "orchestrator" in name:
        return "01_orchestrators", name

    # 05 Capabilities / Tools
    caps = ["pdf", "docx", "pptx", "xlsx", "caveman", "skill-creator", "humanizer", "graphify", "mcp-builder", "imagegen", "image-to-code", "learn-codebase", "smart-explore"]
    for c in caps:
        if c in name:
            new_name = name if "mode" in name or "tool" in name or name.startswith("caveman") else f"{name}-tool"
            return "05_capabilities", new_name

    # 04 Workflows
    workflows = ["version-bump", "change-tracker", "standup", "git-repo-setup", "git-conventional-commits"]
    for w in workflows:
        if w in name:
            if name == "change-tracker": return "04_workflows", "update-changelog-workflow"
            if name == "version-bump": return "04_workflows", "manage-versioning-workflow"
            if name == "standup": return "04_workflows", "generate-standup-workflow"
            return "04_workflows", f"{name}-workflow"

    # 03 Quality Gates & Reviewers
    gates = ["anti", "reviewer", "gate", "enforcement", "tester", "audit", "taste", "pre-mortem"]
    for g in gates:
        if g in name and "architect" not in name:
            new_name = name
            if "anti-sycophancy" in name: new_name = "critical-critique-gate"
            elif "full-output" in name: new_name = "no-truncation-gate"
            elif not name.endswith("-gate") and not name.endswith("-reviewer") and not name.endswith("-auditor") and not name.endswith("-tester"):
                new_name = f"{name}-gate"
            return "03_quality_gates", new_name

    # 02 Specialists (Everything else, mainly roles/actions)
    new_name = name
    if new_name.startswith("implementing-"):
        new_name = new_name.replace("implementing-", "") + "-specialist"
    elif new_name.startswith("performing-"):
        new_name = new_name.replace("performing-", "") + "-specialist"
    elif new_name.startswith("testing-"):
        new_name = new_name.replace("testing-", "") + "-pentester"
        
    return "02_specialists", new_name

def migrate():
    if not os.path.exists(old_skills_dir):
        print("Old skills dir not found!")
        return

    # Create new struct
    for cat in categories.keys():
        os.makedirs(os.path.join(new_skills_dir, cat), exist_ok=True)

    moved = 0
    for item in os.listdir(old_skills_dir):
        old_path = os.path.join(old_skills_dir, item)
        if os.path.isdir(old_path):
            cat, new_name = determine_category_and_name(item)
            new_path = os.path.join(new_skills_dir, cat, new_name)
            
            # Move and rename
            shutil.copytree(old_path, new_path, dirs_exist_ok=True)
            moved += 1
            print(f"Moved [{item}] -> [{cat}/{new_name}]")
            
    print(f"Migration complete! Moved {moved} skills.")

if __name__ == "__main__":
    migrate()
