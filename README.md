# 🚀 AI-Skills v2.0: The Autonomous Digital Agency

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
