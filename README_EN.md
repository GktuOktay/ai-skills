# 🚀 AI-Skills v2.0: The Autonomous Digital Agency

[Türkçe Dokümantasyon (README.md)](README.md)

This repository is a fully autonomous agent ecosystem that rejects standard, passive LLM prompt libraries. Instead, it features **decision-making agents, automated testing, sub-agent delegation, and deterministic quality gates.**

## 📊 Agent Topology & Deep Data Flow
```mermaid
flowchart TB
    %% User Request
    User((User)) -->|Task Request| MO[01: Master Orchestrator]

    %% Phase 1: Analysis & Architecture
    subgraph Phase1 [Phase 1: Architecture Lock-in]
        direction TB
        MO --> BA[02: Business Analyst & Architect]
        BA -->|1. Schema Design| DB_Gate{DB Schema Segregation}
        DB_Gate -->|identity, audit, business schemas| DB[(Database)]
        BA -->|2. Acceptance Criteria| Spec[Project & API Specs]
    end

    %% Phase 2: Execution
    subgraph Phase2 [Phase 2: Vertical Execution]
        direction TB
        Spec --> CO[01: Code Orchestrator]
        CO --> Backend[02: .NET Enterprise Architect]
        CO --> Frontend[02: Mobile Swift/Flutter Architect]
        CO --> Migrator[02: Legacy Code Migrator]
        
        Backend --> Logic[Business Logic - CQRS/MediatR]
        Migrator --> Logic
        Frontend --> UI[UI & State Management]
    end

    %% Phase 3: Quality Gates
    subgraph Phase3 [Phase 3: Deterministic Quality Gates]
        direction LR
        Logic --> TDD{03: Test-Driven Gate}
        TDD -->|Unit Test Failed| Backend
        TDD -->|Unit Test Passed| Sec{03: Security & Logging Gate}
        
        Sec -->|Failed: Plaintext Log| Backend
        Sec -->|Passed: Structured Log| Swagger{03: Swagger & XML Gate}
    end

    %% Phase 4: Delivery
    subgraph Phase4 [Phase 4: Handoff & Delivery]
        direction TB
        Swagger -->|Approved| Handoff[04: API Handoff Workflow]
        Handoff -->|Old/New API Diff| UIDocs[Frontend Integration Docs]
        
        UIDocs --> LangGate{03: Turkish Language Enforcer}
        UI --> LangGate
        LangGate -->|Strictly Turkish Output| User
    end

    %% Styles
    classDef orchestrator fill:#2b1b3d,stroke:#9d5bdf,stroke-width:2px,color:#fff
    classDef specialist fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    classDef gate fill:#5c1a1b,stroke:#e74c3c,stroke-width:2px,color:#fff
    classDef database fill:#2d4a22,stroke:#5c9e42,stroke-width:2px,color:#fff
    
    class MO,CO orchestrator
    class BA,Backend,Frontend,Migrator specialist
    class DB_Gate,TDD,Sec,Swagger,LangGate gate
    class DB database
```

## 📚 Comprehensive Documentation (English)
* 🏗️ [Architecture Anatomy (ARCHITECTURE.md)](docs/en/ARCHITECTURE.md)
* 🧠 [Core Principles (PRINCIPLES.md)](docs/en/PRINCIPLES.md)
* 🔄 [Autonomous Workflows (WORKFLOWS.md)](docs/en/WORKFLOWS.md)

## ⚙️ Installation
```bash
python3 scripts/build_cursor_rules.py
```
