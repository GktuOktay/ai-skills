# 🔄 Autonomous Workflows

## 1. Backend-to-Frontend API Handoff
When a backend API changes, the agent autonomously generates `API_HANDOFF.md` detailing the Old vs. New JSON diff and specific instructions for the Frontend team.

## 2. Project Bootstrapping
The `project-bootstrap-orchestrator` autonomously runs CLI commands (`dotnet new`) to scaffold Clean Architecture folder structures.

## ⏱️ API Devir-Teslim (Handoff) Akış Şeması
Backend'in kodu bitirmesinden Frontend'e devrine kadar geçen otonom süre.

```mermaid
sequenceDiagram
    actor User as User
    participant CTO as Code Orchestrator
    participant BE as .NET Architect
    participant Tracker as Changelog Workflow
    participant FE as Swift/Flutter Architect
    
    User->>CTO: Create new cart API.
    CTO->>BE: Delegate Task
    
    Note over BE: Code is written, tested,<br/>Swagger docs generated.
    
    BE-->>Tracker: Endpoint updated!
    Tracker->>Tracker: CHANGELOG.md updated.
    Tracker->>Tracker: API_HANDOFF.md generated (Old JSON vs New JSON)
    
    Tracker->>FE: Review API_HANDOFF specs!
    
    Note over FE: Frontend State updated<br/>based on new JSON spec.
    
    FE-->>User: Cart integration complete (Turkish output)
```
