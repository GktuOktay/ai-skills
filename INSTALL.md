# 📖 AI Skills - Detaylı Kurulum ve Kullanım Kılavuzu

Bu doküman, `ai-skills` reposunu **Antigravity (Gemini Agent)**, **Cursor AI** ve **Claude Code** araçlarıyla sorunsuz bir şekilde entegre etmeniz için hazırlanmıştır.

---

## 🛠️ Gereksinimler

- **Python 3.8+** (Cursor kural derleyicisi ve çapraz platform kurulum betiği için)
- **Git**

---

## 💻 Adım Adım Kurulum

### 1. Depoyu Bilgisayarınıza Klonlayın

Terminal veya PowerShell açıp depoyu klonlayın:

```bash
git clone https://github.com/GktuOktay/ai-skills.git
cd ai-skills
```

### 2. Kurulum Betiğini Çalıştırın

Kurulumu otomatik tamamlamak için `setup.py` dosyasını çalıştırın:

```bash
python setup.py
```

> **Çıktı Özeti:**
> - `skills/` dizinindeki tüm `SKILL.md` dosyaları okunur ve Cursor için `.mdc` kurallarına dönüştürülür (`rules/`).
> - **Antigravity** (`~/.gemini/config/skills`), **Claude Code** (`~/.claude/skills`) ve **Cursor** (`~/.cursor/rules`) için işletim sisteminize uygun dizin bağlantıları (Symlink / Directory Junction) oluşturulur.

---

## 📁 Dizin Yapısı ve Entegrasyon Noktaları

| Araç | Hedef Yapılandırma Yolu | Bağlanan Kaynak Klasör |
| :--- | :--- | :--- |
| **Antigravity (Gemini)** | `%USERPROFILE%\.gemini\config\skills` | `ai-skills/skills` |
| **Claude Code** | `%USERPROFILE%\.claude\skills` | `ai-skills/skills` |
| **Cursor AI** | `%USERPROFILE%\.cursor\rules` | `ai-skills/rules` |

---

## ❓ Sıkça Sorulan Sorular & Sorun Giderme

### 1. Kurulum sonrasında yeni eklediğim skill görünmüyor?
Yeni bir skill eklediğinizde `skills/` klasörüne ekleme yapıp ardından terminalde tekrar:
```bash
python setup.py
```
komutunu çalıştırarak Cursor kurallarını derlemeniz ve bağlantıları tazelemeniz yeterlidir.

### 2. Windows üzerinde yetki hatası alırsam ne yapmalıyım?
Betik (`setup.py`) varsayılan olarak NTFS **Junction Point** kullanır. Bu işlem yönetici (Administrator) hakları gerektirmez. Ancak yine de bir erişim kısıtlaması yaşarsanız varsayılan olarak betik dosyaları otomatik olarak kopyalama moduna geçirecektir.
