# 🧠 AI Skills & Rules Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Antigravity](https://img.shields.io/badge/Antigravity-Supported-brightgreen.svg)]()
[![Platform: Cursor](https://img.shields.io/badge/Cursor-Supported-blue.svg)]()
[![Platform: Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-orange.svg)]()

Bu depo; **Antigravity (Gemini Agent)**, **Cursor AI** ve **Claude Code** araçları için özelleştirilmiş 58+ adet AI yeteneği (skill) ve sistem kuralı (`.mdc` / markdown rules) barındıran merkezi bir kütüphanedir.

---

## 🌟 Özellikler ve Kategoriler

Kütüphanedeki yetenekler aşağıdaki ana alanlarda yapay zeka asistanlarının otonom ve standartlara uygun çalışmasını sağlar:

- 🏗️ **Yazılım Mimarısı & Kodlama**: `code-orchestrator`, `clean-code-reviewer`, `swift-architecture-auditor`, `schema`, `mcp-builder`, `smart-explore`
- 🛡️ **Güvenlik & Penetrasyon Testleri**: `security-orchestrator`, `api-pentest`, `client-security`, `db-architect-security`, `secret-scanner`, `dependency-audit`
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

`setup.py` otomatik olarak:
1. `build_cursor_rules.py` çalıştırarak `skills/` klasöründen `.mdc` formatında Cursor kuralları (`rules/`) üretir.
2. **Antigravity** için `~/.gemini/config/skills` konumuna bağ kurar.
3. **Claude Code** için `~/.claude/skills` konumuna bağ kurar.
4. **Cursor** için `~/.cursor/rules` konumuna bağ kurar.

---

### Manuel Kurulum (Manual Setup)

İsteğe bağlı olarak bağlantıları manuel olarak da oluşturabilirsiniz:

#### Windows (PowerShell / CMD Admin):
```cmd
:: Cursor kurallarını derleyin
python build_cursor_rules.py

:: Bağlantıları oluşturun (Junction)
mklink /J "%USERPROFILE%\.gemini\config\skills" "%CD%\skills"
mklink /J "%USERPROFILE%\.claude\skills" "%CD%\skills"
mklink /J "%USERPROFILE%\.cursor\rules" "%CD%\rules"
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
3. `python setup.py` çalıştırarak Cursor kurallarını güncelleyin.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
