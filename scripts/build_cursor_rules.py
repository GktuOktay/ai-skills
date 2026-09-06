#!/usr/bin/env python3
import os
import glob

def convert_skills_to_mdc():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(base_dir, "src", "skills") # Updated to src/skills
    rules_dir = os.path.join(base_dir, "rules")
    
    os.makedirs(rules_dir, exist_ok=True)
    
    # Clear existing .mdc files
    for mdc_file in glob.glob(os.path.join(rules_dir, "*.mdc")):
        os.remove(mdc_file)
        
    generated_count = 0
    # Recursively find all SKILL.md files
    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file == "SKILL.md":
                skill_path = root
                skill_name = os.path.basename(skill_path)
                md_path = os.path.join(skill_path, file)
                
                with open(md_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                if not content.startswith("---"):
                    continue
                    
                end_idx = content.find("---", 3)
                if end_idx == -1:
                    continue
                    
                frontmatter = content[3:end_idx].strip()
                body = content[end_idx+3:].strip()
                
                # Extract description and alwaysApply
                description = ""
                always_apply = False
                
                for line in frontmatter.split("\n"):
                    line = line.strip()
                    if line.startswith("description:"):
                        description = line.replace("description:", "").strip().strip("\"").strip("'")
                    if line.startswith("alwaysApply:") and "true" in line.lower():
                        always_apply = True
                        
                # Enforce Turkish response globally in all rules
                body += "\n\nCRITICAL INSTRUCTION: You MUST communicate and explain everything to the user in fluent Turkish. Code, variable names, and technical terms should remain in English, but the prose MUST be Turkish."

                # Generate .mdc content
                mdc_content = "---\n"
                mdc_content += f"description: {description}\n"
                if always_apply or "enforcer" in skill_name or "gate" in skill_name:
                    mdc_content += "globs: *\n"
                else:
                    mdc_content += f"globs: *{skill_name}*\n"
                mdc_content += "---\n\n"
                mdc_content += body
                
                # Write .mdc
                mdc_filename = f"{skill_name}.mdc"
                mdc_filepath = os.path.join(rules_dir, mdc_filename)
                with open(mdc_filepath, "w", encoding="utf-8") as f:
                    f.write(mdc_content)
                generated_count += 1
                
    print(f"Recursively generated {generated_count} .mdc files with Turkish enforcement.")

if __name__ == "__main__":
    convert_skills_to_mdc()
