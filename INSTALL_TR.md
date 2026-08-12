# 📖 AI Skills - Detaylı Evrensel Kurulum ve Kullanım Kılavuzu

[English](INSTALL.md) | [Türkçe](INSTALL_TR.md)

Bu doküman, `ai-skills` reposunu **Antigravity (Gemini)**, **Cursor AI**, **Claude Code**, **GitHub Copilot**, **OpenAI Codex**, **Windsurf** ve **Jenerik AI Agent'lar** ile entegre etmek için hazırlanmıştır.

---

## 🛠️ Gereksinimler

- **Python 3.8+**
- **Git**

---

## 💻 Adım Adım Kurulum

### 1. Depoyu Bilgisayarınıza Klonlayın

```bash
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills
```

### 2. Etkileşimli Kurulum Betiğini Çalıştırın

```bash
# Etkileşimli Dil Seçim Sihirbazı:
python setup.py

# Veya doğrudan Türkçe çalıştırma:
python setup.py --lang tr
```

> **Yapılan İşlemler:**
> 1. Cursor için `.mdc` kurallarını derler (`rules/`).
> 2. GitHub Copilot için `.github/copilot-instructions.md` dosyasını üretir.
> 3. Windsurf ve jenerik agent'lar için `AGENTS.md` ve `.windsurfrules` dosyalarını üretir.
> 4. Tüm AI araçlarının (Antigravity, Cursor, Claude Code, Codex, Copilot) global ve yerel dizinlerine bağlantılar kurar.

---

## 📁 Agent Entegrasyon Matrisi

| Araç / Entegrasyon | Hedef Yapılandırma Yolu | Bağlanan Kaynak Klasör |
| :--- | :--- | :--- |
| **Cursor Dahili Global Skills** | `%USERPROFILE%\.cursor\skills-cursor` | `ai-skills/skills` |
| **Cursor Global Rules** | `%USERPROFILE%\.cursor\rules` | `ai-skills/rules` |
| **Cursor Proje Rules** | `<project_root>\.cursor\rules` | `ai-skills/rules` |
| **Antigravity (Gemini)** | `%USERPROFILE%\.gemini\config\skills` | `ai-skills/skills` |
| **Claude Code** | `%USERPROFILE%\.claude\skills` | `ai-skills/skills` |
| **OpenAI Codex** | `%USERPROFILE%\.codex\skills` | `ai-skills/skills` |
| **GitHub Copilot** | `%USERPROFILE%\.github\copilot-instructions.md` | `ai-skills/.github/copilot-instructions.md` |
| **Windsurf** | `<project_root>\.windsurfrules` | `ai-skills/.windsurfrules` |
