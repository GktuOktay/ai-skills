#!/usr/bin/env python3
import os
import glob
import re

def convert_skills_to_mdc():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(base_dir, "skills")
    rules_dir = os.path.join(base_dir, "rules")
    
    os.makedirs(rules_dir, exist_ok=True)
    
    # Clear existing .mdc files
    for mdc_file in glob.glob(os.path.join(rules_dir, "*.mdc")):
        os.remove(mdc_file)
        
    for skill_name in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill_name)
        if not os.path.isdir(skill_path):
            continue
            
        md_path = os.path.join(skill_path, "SKILL.md")
        if not os.path.exists(md_path):
            continue
            
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
                
        # Generate .mdc content
        mdc_content = "---\n"
        mdc_content += f"description: {description}\n"
        if always_apply:
            mdc_content += "globs: *\n"
        else:
            mdc_content += f"globs: *{skill_name}*\n" # dummy glob if not always applied, or just let user call it
        mdc_content += "---\n\n"
        mdc_content += body
        
        # Write .mdc
        mdc_filename = f"{skill_name}.mdc"
        mdc_filepath = os.path.join(rules_dir, mdc_filename)
        with open(mdc_filepath, "w", encoding="utf-8") as f:
            f.write(mdc_content)
            
        print(f"Generated {mdc_filename}")

if __name__ == "__main__":
    convert_skills_to_mdc()
