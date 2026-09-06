import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills"
skills_dir = os.path.join(base_dir, "src", "skills")

# 1 & 3: New Skills
new_skills = {
    "03_quality_gates/test-driven-development-gate": {
        "desc": "Kod üretildikten sonra AI'ın ilgili birim testlerini (Unit Test) yazıp terminalde çalıştırmasını zorunlu kılan kapı.",
        "content": "# Test-Driven Execution Gate\n\nCRITICAL RULE: When you write new logic, controllers, or services, you MUST NOT just present the code and stop.\n\n1. Write the corresponding unit test (xUnit for .NET, Jest for JS, etc.).\n2. Run the test command in the terminal (e.g., `dotnet test`).\n3. Show the output to the user. Only when the test is GREEN (passing) is the task considered complete."
    },
    "01_orchestrators/project-bootstrap-orchestrator": {
        "desc": "Yeni projelere başlarken CLI araçlarını kullanarak klasör mimarisini, Docker ve temel ayarları otomatik kuran orkestratör.",
        "content": "# Project Bootstrap Orchestrator\n\nYou are responsible for scaffolding new projects from scratch using CLI tools in Claude Code or Cursor.\n\n- **.NET Projects:** Use `dotnet new sln`, `dotnet new webapi`, etc. Scaffold a Clean Architecture structure (Domain, Application, Infrastructure, Presentation).\n- **Frontend:** Use official CLI tools (Vite, Next.js, Flutter CLI).\n- Always initialize a git repository (`git init`) and create a standard `.gitignore`."
    }
}

for path, data in new_skills.items():
    full_path = os.path.join(skills_dir, path)
    os.makedirs(full_path, exist_ok=True)
    with open(os.path.join(full_path, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(f"---\nname: {path.split('/')[-1]}\ndescription: \"{data['desc']}\"\n---\n\n{data['content']}\n")

# 2: Update Migration Specialist
migration_path = os.path.join(skills_dir, "02_specialists/legacy-code-migrator-specialist/SKILL.md")
if os.path.exists(migration_path):
    with open(migration_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Custom Architectural Adaptation\nDO NOT perform a blind 1:1 translation. Before writing code, ask the user about their target architectural principles (e.g., Clean Architecture, specific DDD patterns, Custom Repository patterns). Adapt the migrated code strictly to the user's bespoke architecture, discarding legacy anti-patterns.")

# 5: Rewrite README.md
readme_content = """# 🚀 AI-Skills v2.0 (The Autonomous Agency)

Bu depo, yapay zeka kodlama araçları (Cursor, Claude Code, Windsurf vb.) için tasarlanmış **hiyerarşik, otonom ve deterministik** bir yetenek (skill) ekosistemidir.

Klasik "prompt yığınlarının" aksine, bu sistem tıpkı bir dijital yazılım şirketi gibi çalışır.

## 🏗️ Mimari ve Klasör Yapısı (`src/skills/`)

Sistem 5 ana departmandan oluşur:

1. **`01_orchestrators/` (Yöneticiler):** İşi alır, planlar ve diğer uzmanlara devreder. Doğrudan kod yazmazlar. (Örn: `master-orchestrator`, `project-bootstrap-orchestrator`)
2. **`02_specialists/` (Uzmanlar):** İşi fiilen yapan kıdemli geliştiriciler ve tasarımcılardır. Belirli bir teknoloji yığınına veya işe odaklanırlar. (Örn: `dotnet-enterprise-architect`, `legacy-code-migrator-specialist`)
3. **`03_quality_gates/` (Kalite Kapıları):** Kodun ve çıktıların kullanıcıya ulaşmadan önce geçtiği zorunlu denetim noktalarıdır. (Örn: `test-driven-development-gate`, `critical-critique-gate`, `turkish-language-enforcer-gate`)
4. **`04_workflows/` (İş Akışları):** Sürekli tekrarlanan otomasyon ve standartlaşma görevleridir. (Örn: `update-changelog-workflow`, `git-conventional-commits-workflow`)
5. **`05_capabilities/` (Araçlar ve Modlar):** Ajanların kullandığı sistem araçları veya çalışma kipleridir. (Örn: `caveman-mode` (token tasarrufu), `graphify-tool`)

## 🛠️ Temel Prensipler

* **Türkçe Arayüz, İngilizce Zeka:** Yapay zekanın çekirdek talimatları maksimum performans için İngilizcedir. Ancak `turkish-language-enforcer-gate` sayesinde yapay zeka sizinle **her zaman Türkçe** iletişim kurar.
* **Kanıt Odaklı (Evidence-Based):** Ajanlar kodu yazıp bırakmaz; testleri çalıştırıp sonucunu size kanıtlamak zorundadır.
* **Anti-AI Tasarım:** Tasarım orkestratörleri, yapay zekanın varsayılan klişelerinden (mor gradyanlar, yuvarlak SaaS kartları) kaçınacak şekilde programlanmıştır.

## ⚙️ Kurulum ve Derleme (Build)

Sisteme yeni bir ajan (Skill) eklediğinizde veya değişiklik yaptığınızda, IDE'lerin bunu algılayabilmesi için derleme scriptini çalıştırmanız gerekir.

```bash
# Cursor ve diğer IDE'ler için .mdc kurallarını yeniden derler
python3 scripts/build_cursor_rules.py
```
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Final updates applied and README rewritten.")
