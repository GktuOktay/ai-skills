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

> **Çıktı Özeti ve Yapılan İşlemler:**
> 1. `skills/` dizinindeki tüm `SKILL.md` dosyaları okunur ve Cursor için `.mdc` kurallarına dönüştürülür (`rules/`).
> 2. **Proje Seviyesi Cursor Kuralları**: Çalışılan mevcut dizindeki `.cursor/rules` klasörüne kural bağlantıları kurulur.
> 3. **Cursor Global Dahili Skills (`~/.cursor/skills-cursor`)**: Tüm 58 yetenek klasörü Cursor'ın dahili global yetenek merkezine bağlanır. Bu sayede hangi projede olursanız olun tüm yetenekler aktifleşir.
> 4. **Cursor Global Rules (`~/.cursor/rules`)**: `.mdc` kuralları global Cursor kural alanına bağlanır.
> 5. **Antigravity (`~/.gemini/config/skills`)** & **Claude Code (`~/.claude/skills`)**: Yetenekler Antigravity ve Claude Code yapılandırma alanlarına aktarılır.

---

## 📁 Dizin Yapısı ve Entegrasyon Noktaları

| Araç / Entegrasyon | Hedef Yapılandırma Yolu | Bağlanan Kaynak Klasör |
| :--- | :--- | :--- |
| **Cursor Dahili Global Skills** | `%USERPROFILE%\.cursor\skills-cursor\<skill_name>` | `ai-skills/skills/<skill_name>` |
| **Cursor Global Rules** | `%USERPROFILE%\.cursor\rules` | `ai-skills/rules` |
| **Cursor Proje Rules** | `<project_root>\.cursor\rules` | `ai-skills/rules` |
| **Antigravity (Gemini)** | `%USERPROFILE%\.gemini\config\skills` | `ai-skills/skills` |
| **Claude Code** | `%USERPROFILE%\.claude\skills` | `ai-skills/skills` |

---

## ❓ Sıkça Sorulan Sorular & Sorun Giderme

### 1. Cursor üzerinde kuralları ve yetenekleri nasıl doğrularım?
- **Global Yetenekler**: Cursor AI Chat / Composer içerisinde `@` yazıp istediğiniz skill ismini (örneğin `@code-orchestrator` veya `@caveman`) çağırmanız yeterlidir.
- **Project Rules**: Herhangi bir projeyi Cursor ile açtığınızda `Cursor Settings -> Rules for AI` ekranında `.mdc` kurallarının listelendiğini görebilirsiniz.

### 2. Yeni bir skill eklediğimde ne yapmalıyım?
Yeni bir skill eklediğinizde `skills/` klasörüne ekleme yapıp ardından terminalde tekrar:
```bash
python setup.py
```
komutunu çalıştırarak Cursor kurallarını derlemeniz ve tüm global bağlantıları tazelemeniz yeterlidir.

### 3. Windows üzerinde yetki hatası alırsam ne yapmalıyım?
Betik (`setup.py`) varsayılan olarak NTFS **Junction Point** kullanır. Bu işlem yönetici (Administrator) hakları gerektirmez. Ancak erişim kısıtlaması yaşanması durumunda betik otomatik olarak kopyalama moduna geçer.
