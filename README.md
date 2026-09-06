# 🚀 AI-Skills v2.0 (The Autonomous Agency)

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
