import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills"
docs_dir = os.path.join(base_dir, "docs")
os.makedirs(docs_dir, exist_ok=True)

# 1. README.md
readme = """# 🚀 AI-Skills v2.0: The Autonomous Digital Agency

![Architecture: Multi-Agent](https://img.shields.io/badge/Architecture-Multi--Agent-blue)
![Stack: .NET | React | Mobile](https://img.shields.io/badge/Stack-.NET_%7C_React_%7C_Mobile-purple)
![Paradigm: Test--Driven](https://img.shields.io/badge/Paradigm-Test--Driven-success)

Bu depo, standart ve pasif yapay zeka (LLM) prompt yığınlarını reddeden; yerine **karar alabilen, test yazan, birbirine iş devreden ve deterministik kalite kapılarından (Quality Gates) geçen** otonom bir ajan ekosistemidir.

Klasik AI kullanımında geliştirici her detayı anlatmak zorundadır. **v2.0 Mimarisinde ise geliştirici (Kıdemli Mimar) sadece hedefi verir; ajanlar analizi yapar, kodu yazar, test eder, dokümante eder ve devreder.**

## 📊 Ajan Topolojisi ve Veri Akışı

```mermaid
flowchart TB
    User((Kullanıcı)) -->|İş Talebi / Hedef| MO[01: Master Orchestrator]
    
    subgraph Planning [Planlama ve İş Analizi]
        MO --> BA[BA / Sistem Mimarı]
        BA -->|Mimari Şemalar & Kabul Kriterleri| Spec[(Proje Spesifikasyonu)]
    end

    subgraph Execution [Uzman Ajanlar - Execution]
        Spec --> CO[01: Code Orchestrator]
        CO --> Backend[02: .NET Enterprise Architect]
        CO --> Mobile[02: Mobile Swift/Flutter Architect]
        CO --> Migrator[02: Legacy Code Migrator]
    end

    subgraph QualityGates [Zorunlu Kalite Kapıları]
        Backend --> TDD{03: Test-Driven Gate}
        Mobile --> UI{03: Anti-AI Design Gate}
        Migrator --> Sec{03: Security & Logging Gate}
        
        TDD -->|Test Failed| Backend
        TDD -->|Test Passed (Yeşil)| API_Docs
    end

    subgraph Output [İş Akışları & Teslimat]
        API_Docs{03: Swagger & XML Gate} --> Handoff[04: API Handoff Workflow]
        Handoff -->|Frontend İçin Entegrasyon Dokümanı| FinalCheck
        UI --> FinalCheck
        Sec --> FinalCheck
        FinalCheck{03: Turkish Language Enforcer} -->|Saf Türkçe Yanıt| User
    end
    
    classDef orchestrator fill:#2b1b3d,stroke:#9d5bdf,stroke-width:2px,color:#fff
    classDef agent fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    classDef gate fill:#5c1a1b,stroke:#e74c3c,stroke-width:2px,color:#fff
    
    class MO,CO orchestrator
    class BA,Backend,Mobile,Migrator agent
    class TDD,UI,Sec,API_Docs,FinalCheck gate
```

## 📚 Kapsamlı Dokümantasyon

Sistemin derin teknik mimarisi, prensipleri ve iş akışları için aşağıdaki dokümanları inceleyin:

* 🏗️ [Mimarinin Anatomisi (ARCHITECTURE.md)](docs/ARCHITECTURE.md): 5 Ana Departmanın (01-05) teknik hiyerarşisi.
* 🧠 [Çekirdek Prensipler (PRINCIPLES.md)](docs/PRINCIPLES.md): Fail-Fast, Evrimsel Mimari, .NET Base Service İkilemi ve YAGNI.
* 🔄 [Otonom İş Akışları (WORKFLOWS.md)](docs/WORKFLOWS.md): API Devir-Teslimi (Handoff), Proje Kurulumu ve Changelog yönetim süreçleri.

## ⚙️ Kurulum ve Derleme (Build)

Cursor, Claude Code veya Windsurf ortamlarında kuralları (.mdc) üretmek için:

```bash
python3 scripts/build_cursor_rules.py
```
Bu komut, `src/skills/` hiyerarşisini özyineli (recursive) tarayarak 100+ otonom kural dosyasını IDE'nize entegre eder.
"""

# 2. ARCHITECTURE.md
architecture = """# 🏗️ Sistemin Anatomisi (Architecture)

Yapay zekanın kontrolü kaybetmemesi ve kod tabanını spagettiye çevirmemesi için sistem **5 Katmanlı Domain-Driven** bir yapıya bölünmüştür. Tüm yetenekler `src/skills/` altında konumlanır.

## 01_orchestrators (Yöneticiler / Karar Vericiler)
Doğrudan kod yazmayan, ancak *Delegation (Yetki Devri)* yapan meta-ajanlardır.
* **Master Orchestrator:** Kullanıcıdan gelen soyut talebi alır, hangi uzmana gideceğine karar verir.
* **Code Orchestrator:** Projedeki Universal Senior (Kıdemli) reflekslerini (Fail-Fast, Idempotency) enforce eder.
* **Project Bootstrap Orchestrator:** Yeni projelerin CLI araçlarıyla (`dotnet new sln`, Clean Architecture) otonom kurulumunu yönetir.

## 02_specialists (Uzman Ajanlar)
İşi fiilen yapan kıdemli geliştiricilerdir.
* **.NET Enterprise Architect:** C# 11+, EF Core optimizasyonları, N+1 sorgu engelleme ve CQRS/MediatR senaryoları.
* **Legacy Code Migrator:** Django, Vue vb. eski veya farklı dildeki yapıları 1:1 kör çeviriyle değil; hedef mimarinin (örn: Clean Architecture) prensiplerine adapte ederek dönüştürür.
* **Mobile Swift/Flutter Architect:** Native IOS (TCA/MVVM) ve Flutter (Riverpod) için State Management ve bellek yönetimi (Memory Leak) uzmanı.
* **Edge & Gateway Architect:** YARP/Nginx gibi Gateway seviyesinde Rate-Limiting, JWT ve Load Balancing kurgular.

## 03_quality_gates (Zorunlu Kalite Kapıları)
Üretilen kodun kullanıcıya ulaşmadan önce geçmek zorunda olduğu **Deterministik Filtrelerdir**.
* **Turkish Language Enforcer:** Ajanların İngilizce düşünme performansını bozmadan, kullanıcıya **daima Türkçe** yanıt vermesini zorunlu kılar.
* **Test-Driven Development Gate:** Yazılan servisin birim testini (Unit Test) yazdırıp terminalde çalıştırmadan kodu kabul etmez.
* **Swagger & XML Doc Gate:** Yazılan her backend endpoint'ine `<summary>` ve HTTP Status attributelarını zorunlu tutar.
* **Structured Logging & Audit Gate:** Tam Req/Res payload loglanmasını yasaklar. Exception loglarının asenkron akmasını ve veritabanındaki Audit (CreatedAt, UpdatedBy) tablolarının kullanılmasını zorunlu tutar.

## 04_workflows (Otonom İş Akışları)
Manuel yapılması gereken hammaliye süreçleri devralan mekanizmalardır.
* Detaylar için bkz: [WORKFLOWS.md](WORKFLOWS.md)

## 05_capabilities (Araçlar ve Modlar)
Ajanların ellerindeki alet çantasıdır (Caveman modu, Graphify Node haritalama, PDF/Excel ayrıştırıcılar).
"""

# 3. PRINCIPLES.md
principles = """# 🧠 Çekirdek Prensipler (Core Principles)

Yapay zeka asistanlarını ortalama (Mid-level) bir yazılımcıdan ayıran, sisteme kazınmış Kıdemli Mimar (Principal Architect) zihniyetidir. 

## 1. Evrimsel Mimari (Evolutionary Architecture)
* **Kural:** Sistemler evrimleşir. Ajanlar başlangıçta basit olan yapıların karmaşıklaştığını fark etmelidir.
* **Davranış:** İş kuralları (Business Logic) karmaşıklaştığında, ajan kodu generic soyutlamalar (abstractions) içine hapsetmekte inat etmemeli; gerekirse kodu söküp Use-Case odaklı bağımsız servislere ayırma (Refactor) cesaretine sahip olmalıdır.

## 2. ".NET Base Service" ve YAGNI İkilemi
* **Kural:** Her Entity için ezbere `BaseService<T>` veya `BaseRepository<T>` türetilmesi **kesinlikle yasaktır.**
* **Davranış:** Sadece okunacak bir veriye sırf Base sınıftan geliyor diye `Update` ve `Delete` yetkisi açılamaz (YAGNI). Özel sorgular, karmaşık `.Include()` zincirleri veya alt sorgular gerektiren işlemler Base Service'e parametre uydurularak çözülmez; derhal CQRS (MediatR) Query'lerine veya spesifik okuma servislerine taşınır.

## 3. Fail-Fast ve Savunmacı Programlama (Defensive Programming)
* **Kural:** Ajan, kodun her zaman "Happy Path" (sorunsuz) çalışacağını varsayamaz.
* **Davranış:** Parametreleri anında kontrol eder (örn: `ArgumentNullException.ThrowIfNull`). Veritabanı veya API bağlantılarının kopabileceğini varsayar. Hatayı yutmak yerine anında ve anlamlı bir `CustomException` fırlatır.

## 4. Güvenlik ve Bağımlılıkların Soyutlanması (IoC)
* **Güvenlik (IDOR):** Dışarıya açılan API DTO'larında fiziksel DB Id'leri (1, 2, 3) kullanılamaz, Guid (UUID) zorunludur.
* **IoC (Inversion of Control):** İş mantığında doğrudan `DateTime.Now` veya `Guid.NewGuid()` gibi statik dış bağımlılıklar kullanılamaz. Test edilebilirliği (Unit Test) sağlamak adına `IDateTimeProvider` gibi arayüzler arkasına soyutlanır.

## 5. İndeksleme ve Pagination (Sayfalama) Şartı
* **Kural:** Liste dönen hiçbir endpoint sayfalama (Pagination) parametresi olmadan yazılamaz.
* **Performans:** Filtreleme işlemleri RAM'e (memory) çekilerek değil, doğrudan veritabanı seviyesinde (`IQueryable`) dinamik olarak gerçekleştirilir. N+1 sorgularından kaçınmak için EF Core Projection (`.Select`) veya `.Include()` kullanılır.
"""

# 4. WORKFLOWS.md
workflows = """# 🔄 Otonom İş Akışları (Workflows)

Proje geliştirme sürecindeki departmanlar arası (Backend -> Frontend) sürtünmeyi ve zaman kaybını ortadan kaldıran otonom zincirler.

## 1. Backend-to-Frontend Devir Teslimi (API Handoff)
Bir backend geliştiricinin işi bitirdiğinde frontend geliştiricisine "Ben API'yi güncelledim, Swagger'a bak" demesi süreci yavaşlatır.

**Otonom Akış (`api-handoff-workflow`):**
1. Backend'deki (Örn: .NET) `Controller` ve `Service` kodları güncellenir.
2. Ajan, kodun ilgili kalite kapılarından (Swagger XML Doc, TDD) geçtiğinden emin olur.
3. Otomatik olarak `API_HANDOFF.md` adında bir devir-teslim dokümanı üretilir.
4. **İçerik:** 
   * Eski JSON yapısı (Before) vs Yeni JSON yapısı (After).
   * Kırıcı (Breaking) değişikliklerin kırmızıyla işaretlenmesi.
   * Frontend (React/Flutter) tarafındaki State (Örn: Redux/Riverpod) yapılarında tam olarak hangi değişken isimlerinin değiştirilmesi gerektiğine dair nokta atışı talimatlar.

## 2. Otomatik Proje ve Şema Kurulumu (Project Scaffolding)
Yeni bir projeye veya modüle başlarken klasör açmak ameleliktir.

**Otonom Akış (`project-bootstrap-orchestrator`):**
1. Kullanıcıdan *"Yeni bir Sipariş (Order) mikroservisi başlat"* komutu gelir.
2. Ajan terminalde CLI araçlarını (`dotnet new sln`, `dotnet new webapi`) tetikler.
3. Clean Architecture (Domain, App, Infra, API) klasör ağacını çizer.
4. **Veritabanı Kuralı:** Otonom olarak `db-architect-security` uyanır ve tabloları tek bir `public` veya `dbo` yığınına atmak yerine; `order`, `inventory`, `audit` gibi mantıksal **Şemalara (Schemas)** böler.

## 3. Değişiklik Takibi ve Loglama (Changelog Tracker)
Her sprint veya task tamamlandığında manuel doküman yazılmaz.
1. `update-changelog-workflow` devreye girer.
2. Yazılan özelliklerin (Features), giderilen açıkların (Bugfixes) ve kırıcı değişimlerin (Breaking Changes) dökümünü çıkararak Semantic Versioning (SemVer) standartlarında `CHANGELOG.md` dosyasına ekler.
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)
with open(os.path.join(docs_dir, "ARCHITECTURE.md"), "w", encoding="utf-8") as f:
    f.write(architecture)
with open(os.path.join(docs_dir, "PRINCIPLES.md"), "w", encoding="utf-8") as f:
    f.write(principles)
with open(os.path.join(docs_dir, "WORKFLOWS.md"), "w", encoding="utf-8") as f:
    f.write(workflows)

print("Documentation generated successfully.")
