# 🚀 AI-Skills v2.0: Otonom Dijital Ajans

[English Documentation (README_EN.md)](README_EN.md)

Bu depo, standart ve pasif yapay zeka (LLM) prompt yığınlarını reddeden; yerine **karar alabilen, test yazan, birbirine iş devreden ve deterministik kalite kapılarından (Quality Gates) geçen** otonom bir ajan ekosistemidir.

## 📊 Ajan Topolojisi ve Detaylı Veri Akışı
```mermaid
flowchart TB
    %% Kullanici İstegi
    User((Kullanıcı)) -->|İş Talebi| MO[01: Master Orchestrator]

    %% Faz 1: Analiz ve Mimari
    subgraph Phase1 [Faz 1: Analiz ve Mimari Kilitlenmesi]
        direction TB
        MO --> BA[02: Business Analyst & Architect]
        BA -->|1. Şema Tasarımı| DB_Gate{DB Schema Bölme Kuralı}
        DB_Gate -->|identity, audit, business şemaları| DB[(Veritabanı)]
        BA -->|2. Kabul Kriterleri| Spec[Proje & API Dokümanı]
    end

    %% Faz 2: Geliştirme (Execution)
    subgraph Phase2 [Faz 2: Dikey Uzmanlarla Geliştirme]
        direction TB
        Spec --> CO[01: Code Orchestrator]
        CO --> Backend[02: .NET Enterprise Architect]
        CO --> Frontend[02: Mobile Swift/Flutter Architect]
        CO --> Migrator[02: Legacy Code Migrator]
        
        Backend --> Logic[İş Kuralları - CQRS/MediatR]
        Migrator --> Logic
        Frontend --> UI[UI ve State Management]
    end

    %% Faz 3: Kalite Kapıları
    subgraph Phase3 [Faz 3: Deterministik Kalite Kapıları]
        direction LR
        Logic --> TDD{03: Test-Driven Gate}
        TDD -->|Birim Testi Hatalı| Backend
        TDD -->|Birim Testi Başarılı| Sec{03: Security & Logging Gate}
        
        Sec -->|Hata: Düz Metin Log| Backend
        Sec -->|Başarılı: Structured Log| Swagger{03: Swagger & XML Gate}
    end

    %% Faz 4: Teslimat
    subgraph Phase4 [Faz 4: Devir Teslim ve Yayın]
        direction TB
        Swagger -->|Onaylandı| Handoff[04: API Handoff Workflow]
        Handoff -->|Eski/Yeni API Farkı| UIDocs[Frontend Entegrasyon Dokümanı]
        
        UIDocs --> LangGate{03: Turkish Language Enforcer}
        UI --> LangGate
        LangGate -->|Saf Türkçe Çıktı| User
    end

    %% Stiller
    classDef orchestrator fill:#2b1b3d,stroke:#9d5bdf,stroke-width:2px,color:#fff
    classDef specialist fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    classDef gate fill:#5c1a1b,stroke:#e74c3c,stroke-width:2px,color:#fff
    classDef database fill:#2d4a22,stroke:#5c9e42,stroke-width:2px,color:#fff
    
    class MO,CO orchestrator
    class BA,Backend,Frontend,Migrator specialist
    class DB_Gate,TDD,Sec,Swagger,LangGate gate
    class DB database
```

## 📚 Kapsamlı Dokümantasyon (Türkçe)
* 🏗️ [Mimarinin Anatomisi (ARCHITECTURE.md)](docs/tr/ARCHITECTURE.md)
* 🧠 [Çekirdek Prensipler (PRINCIPLES.md)](docs/tr/PRINCIPLES.md)
* 🔄 [Otonom İş Akışları (WORKFLOWS.md)](docs/tr/WORKFLOWS.md)

## ⚙️ Kurulum
```bash
python3 scripts/build_cursor_rules.py
```
