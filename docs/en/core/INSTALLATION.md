# ⚙️ Advanced Installation & IDE Integration Guide

[🇺🇸 English Documentation](../../en/core/INSTALLATION.md)

**Autonomous Agency (v2.0)**, IDE'nize doğrudan entegre olan bir mimaridir. Bu rehber, üretilen ajan kurallarını (rules) tercih ettiğiniz kodlama asistanına (Cursor, Windsurf, Claude Code, Copilot/Codex) en doğru şekilde nasıl bağlayacağınızı detaylandırır.

## 1. Compiling the Architecture (Build Process)
Repodaki kaynak dosyalar (`src/skills/`) doğrudan IDE'ler tarafından okunamaz. Sistemin kalbi olan `setup.py` dosyası ile bu kuralları derlemeniz gerekir.

```bash
# 1. Repoyu klonlayın
git clone https://github.com/GktuOktay/autonomous-agency.git
cd autonomous-agency

# 2. SSOT (Single Source of Truth) Derleyicisini çalıştırın
python3 setup.py
```
**Çıktılar:**
Bu işlem bittiğinde şu dosyalar üretilmiş olacaktır:
- `rules/*.mdc` (Cursor için 105+ adet parselize edilmiş kural dosyası)
- `.windsurfrules` (Windsurf için tekil bağlam dosyası)
- `clauderules.md` (Claude Code CLI için global bağlam)

---

## 2. Environment & IDE Integrations

### 🖱️ Cursor (Recommended Environment)
Cursor, `.mdc` (Markdown Cursor) mimarisini desteklediği için 105 ajanın yetkilerini klasör ve dosya uzantılarına göre (globs) otonom olarak devreye sokabilir.

**Steps:**
1. Kendi çalışma projenizin ana dizinine gidin (Örn: `cd ~/Masaustu/E-Ticaret-Projem`).
2. `.cursor/rules` adında gizli bir klasör oluşturun:
   ```bash
   mkdir -p .cursor/rules
   ```
3. `autonomous-agency/rules/` klasöründe üretilen **tüm `.mdc` dosyalarını** bu yeni klasöre kopyalayın.
4. **IDE Ayarı:** Cursor'u yeniden başlatın. `Settings > General > Rules` sekmesinde kopyaladığınız tüm ajanların aktif (Enabled) olarak listelendiğinden emin olun.

### 🏄‍♂️ Windsurf
Windsurf, ajan kurallarını tek bir küresel dosyadan okumayı tercih eder.

**Steps:**
1. Kendi çalışma projenizin ana dizinine gidin.
2. Derleme sonucu oluşan `.windsurfrules` dosyasını ana dizine kopyalayın.
3. Windsurf uygulamasını açın. Cascade (Şelale) modu çalıştığında, ajanlarımız otomatik olarak bu dosyadaki Master Orchestrator kurallarını okumaya başlayacaktır.

### 🤖 Claude Code (Terminal / CLI)
Claude'un CLI versiyonu dosya tabanlı (file-based) bağlam enjeksiyonu ile çalışır.

**Steps:**
1. Oluşan `clauderules.md` dosyasını projenizin kök dizinine alın.
2. Terminalde Claude Code'u başlatırken bağlamı sisteme zorunlu kılın:
   ```bash
   claude --context clauderules.md
   ```

### 💻 GitHub Copilot & OpenAI Codex
Eğer Copilot kullanıyorsanız, ajan kurallarını GitHub'ın standart yönergelerine bağlamanız gerekir.

**Steps:**
1. Projenizde `.github/` klasörü oluşturun.
2. `.windsurfrules` veya `clauderules.md` dosyasının içeriğini alıp, `.github/copilot-instructions.md` adlı bir dosya oluşturarak içine yapıştırın.
3. Copilot Chat, kod üretirken bu kısıtlamaları (Quality Gates) baz alarak hareket edecektir.
