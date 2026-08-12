# 🧠 AI Skills & Rules Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Antigravity](https://img.shields.io/badge/Antigravity-Supported-brightgreen.svg)]()
[![Platform: Cursor](https://img.shields.io/badge/Cursor-Supported-blue.svg)]()
[![Platform: Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-orange.svg)]()
[![Platform: GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Supported-purple.svg)]()
[![Platform: OpenAI Codex](https://img.shields.io/badge/OpenAI%20Codex-Supported-black.svg)]()
[![Platform: Windsurf](https://img.shields.io/badge/Windsurf-Supported-teal.svg)]()

Bu depo; **Antigravity (Gemini Agent)**, **Cursor AI**, **Claude Code**, **GitHub Copilot**, **OpenAI Codex**, **Windsurf** ve jenerik tüm AI agent araçları için 63+ adet özelleştirilmiş AI yeteneği (skill) ve sistem kuralı barındıran evrensel kütüphanedir.

---

## 🌟 Özellikler ve Kategoriler

Kütüphanedeki yetenekler aşağıdaki ana alanlarda yapay zeka asistanlarının otonom ve standartlara uygun çalışmasını sağlar:

- 🏗️ **Yazılım Mimarisi & Kodlama**: `code-orchestrator`, `clean-code-reviewer`, `swift-architecture-auditor`, `schema`, `mcp-builder`, `smart-explore`
- 🛡️ **Güvenlik & Penetrasyon Testleri**: `security-orchestrator`, `api-pentest`, `client-security`, `db-architect-security`, `secret-scanner`, `dependency-audit`
- 🎯 **Eleştirel Düşünce & Anti-Sycophancy**: `anti-sycophancy` *(Hatalı yönlendirmelere yapıcı itiraz, dalkavukluk ve boş övgü engelleme)*
- 🎨 **UI/UX & Görsel Tasarım**: `design-orchestrator`, `apple-design`, `high-end-visual-design`, `design-taste-frontend`, `ui-animation`, `imagegen-frontend`, `image-to-code`
- 🧪 **Test & Kalite Güvence**: `test-orchestrator`, `unit-test-architect`, `e2e-tester`, `performance-tester`, `smoke-monkey-tester`, `testing-master`
- 🌿 **Git & Sürüm Yönetimi**: `git-orchestrator`, `git-conventional-commits`, `git-pr-reviewer`, `git-issue-manager`, `git-repo-setup`, `version-bump`, `change-tracker`
- 📄 **Dokümantasyon & Analiz**: `docs-orchestrator`, `tech-business-analyst`, `product-designer`, `feature-ideator`, `copywriting`, `docx`, `pdf`, `pptx`, `xlsx`
- ⚡ **Token Tasarrufu & Caveman Modları**: `caveman`, `cavecrew`, `caveman-commit`, `caveman-compress`, `caveman-review`, `caveman-stats`, `caveman-help`

---

## 🚀 Hızlı Kurulum Rehberi (Installation Guide)

Bu kütüphanedeki tüm yetenekleri ve kuralları sisteminize tek bir komutla ekleyebilirsiniz.

### Otomatik Kurulum (Tüm Platformlar: Windows, macOS, Linux)

Depoyu bilgisayarınıza klonlayın ve kurulum betiğini çalıştırın:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills

# 2. Kurulum betiğini çalıştırın
python setup.py
```

`setup.py` otomatik olarak şu 5 adımı gerçekleştirir:
1. `build_cursor_rules.py` çalıştırarak `skills/` klasöründen `.mdc` formatında Cursor kuralları (`rules/`) üretir.
2. **Cursor Global Skills**: 58 adet yeteneği Cursor'ın dahili global yetenek alanına (`~/.cursor/skills-cursor`) ekler.
3. **Cursor Global Rules**: `.mdc` kurallarını `~/.cursor/rules` konumuna bağlar.
4. **Antigravity (Gemini)**: Global yetenekleri `~/.gemini/config/skills` konumuna bağlar.
5. **Claude Code**: Global yetenekleri `~/.claude/skills` konumuna bağlar.

---

### Manuel Kurulum (Manual Setup)

İsteğe bağlı olarak bağlantıları manuel olarak da oluşturabilirsiniz:

#### Windows (PowerShell / CMD Admin):
```cmd
:: Cursor kurallarını derleyin
python build_cursor_rules.py

:: Bağlantıları oluşturun (Junction Point)
mklink /J "%USERPROFILE%\.gemini\config\skills" "%CD%\skills"
mklink /J "%USERPROFILE%\.claude\skills" "%CD%\skills"
mklink /J "%USERPROFILE%\.cursor\rules" "%CD%\rules"

:: Dilerseniz Cursor dahili yetenek alanına da klasörleri bağlayabilirsiniz:
:: "%USERPROFILE%\.cursor\skills-cursor\<skill-name>" -> "%CD%\skills\<skill-name>"
```

#### macOS / Linux (Bash / Zsh):
```bash
# Bash betiğine çalıştırma yetkisi verin
chmod +x setup.sh
./setup.sh
```

---

## 🛠️ Yeni Yetenek (Skill) Ekleme

Yeni bir yetenek eklemek için:

1. `skills/` altında yeni bir klasör oluşturun (Örn: `skills/my-new-skill/`).
2. İçerisine `SKILL.md` dosyası ekleyin ve YAML frontmatter kullanın:
   ```markdown
   ---
   name: my-new-skill
   description: Skill açıklamasını buraya yazın.
   ---
   # Skill Talimatları
   ...
   ```
3. `python setup.py` çalıştırarak Cursor kurallarını ve tüm bağları güncelleyin.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
