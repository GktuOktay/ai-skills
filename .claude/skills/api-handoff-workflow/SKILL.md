---
name: api-handoff-workflow
description: "Backend'de bir değişiklik yapıldığında otomatik Changelog çıkaran ve Frontend takımı için eski/yeni API karşılaştırma (Devir-Teslim) dokümanı üreten iş akışı."
---

# Backend-to-Frontend API Handoff Workflow

Whenever a change is made to the Backend APIs, you MUST execute this workflow:

1. **Update Changelog:** Automatically update the project's changelog/tracker with the backend modifications.
2. **Generate API_HANDOFF.md:** Create or update a document specifically for the Frontend/Mobile team.
   - Show the **OLD** Request/Response JSON structure vs the **NEW** structure (Diff).
   - Explain exactly what the Frontend developer needs to do to integrate this change (e.g., "Change the `userId` field to `userGuid` in the Redux store").
   - Highlight any breaking changes in bold.
