# 🛠️ Kurulum ve Kullanım Kılavuzu (Installation & Usage)

[🇺🇸 English Documentation](../../en/core/INSTALL_AND_USAGE.md)

Bu kılavuz, **Autonomous Agency** ekosistemini yerel (local) projenize nasıl entegre edeceğinizi ve 105 ajanı nasıl yöneteceğinizi adım adım açıklar.

## 1. Ön Koşullar (Prerequisites)
- Bilgisayarınızda **Python 3.8+** yüklü olmalıdır (Build scripti için).
- Ajanları çalıştırabilmek için desteklenen bir Yapay Zeka IDE'si (Cursor, Windsurf) veya CLI Aracı (Claude Code) kullanıyor olmalısınız.

## 2. Sistemi Derleme (Build Süreci)
Bu depo (repo), ajanların kurallarını tutan kaynak koddur. Kendi projenizde kullanmak için önce derlemeniz gerekir:

1. Repoyu bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/GktuOktay/autonomous-agency.git
   cd autonomous-agency
   ```
2. Kurulum scriptini çalıştırın:
   ```bash
   python3 setup.py
   ```
   *Bu komut, `src/skills/` klasöründeki ham datayı okuyarak sizin için `rules/` klasörünü, `.windsurfrules` ve `clauderules.md` dosyalarını üretecektir.*

## 3. IDE Entegrasyonu

### 🖱️ Cursor İçin
1. `setup.py` çalıştıktan sonra oluşan `rules/` klasörünün içindeki tüm `.mdc` dosyalarını kopyalayın.
2. Kendi çalışma projenizin ana dizininde `.cursor/rules/` adında bir klasör oluşturun (Eğer yoksa).
3. Kopyaladığınız tüm `.mdc` dosyalarını bu klasörün içine yapıştırın. Cursor, ajanları otomatik olarak tanıyacaktır.

### 🏄‍♂️ Windsurf İçin
1. `setup.py` çalıştıktan sonra ana dizinde oluşan `.windsurfrules` dosyasını kopyalayın.
2. Kendi çalışma projenizin kök dizinine (Root directory) yapıştırın.

### 🤖 Claude Code (CLI) İçin
1. Oluşan `clauderules.md` dosyasını çalışma dizininize alın ve Claude Code'u başlatırken bağlam (context) olarak verin.

---

## 4. Kullanım Disiplini (Nasıl Konuşulmalı?)
Ajanlarla iletişim kurarken standart bir "ChatGPT" ile konuşur gibi davranmamalısınız. Sistem hiyerarşiye dayalıdır.

### ❌ Yanlış Kullanım (Doğrudan Uzmana Emir Vermek)
> *"Bana login sayfası çiz, veritabanını da bağla, testlerini de yaz."*
**(Hata:** Sistemdeki spesifik ajanlar (Örn: .NET Mimarı) frontend çizemez. Ajanın kafası karışır ve kalite kapılarından geçemez.)

### ✅ Doğru Kullanım (Orkestratörü Tetiklemek)
Taleplerinizi her zaman **Master Orchestrator** veya ilgili departman yöneticisine iletin:
> *"Master Orchestrator olarak bu görevi devral: Trendyol benzeri bir e-ticaret sepet yapısı istiyorum. Code Orchestrator ve Design Orchestrator'ı koordine ederek işi bitir."*

Yönetici (Orkestratör) bu komutu aldığında, arka planda Veritabanı Mimarını uyandıracak, ardından Backend uzmanın kodu yazdıracak ve en son Kalite Kapılarını zorunlu kılacaktır.
