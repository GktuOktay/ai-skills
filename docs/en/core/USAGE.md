# 🧠 Agentic Prompting & Usage Guide

[🇹🇷 Türkçe Dokümantasyon (Turkish)](../../tr/core/USAGE.md)

**Autonomous Agency** is not an ordinary Q&A assistant. To get the most out of this factory consisting of 109 experts and 5 departments, you must issue your commands (Prompts) like a **Project Manager**.

## 1. Golden Rule: Speak to the Orchestrators
You wouldn't go to a company and directly tell the database expert, *"Make this button red."* The same rule applies here.
Do not forward your requests to specific experts (e.g., .NET Architect). Forward them to the **Master Orchestrator** or **Code Orchestrator**. It will wake up the right experts on your behalf.

### ❌ Command to Avoid (Amateur Usage)
> *"Build me an e-commerce cart. Frontend in React, Backend in C#, connect the database with Entity Framework. Oh, and don't forget to write the tests."*
**Result:** The IDE will crash or hallucinate. The AI cannot hold all this burden in a single context.

### ✅ Perfect Usage (Agentic Workflow)
> *"Your role: Master Orchestrator. We are going to build an e-commerce cart infrastructure. Please wake up the Business Analyst and Database Architect agents first to map out the database schema for me. Once I approve, hand it over to the Code Orchestrator."*
**Result:** The system first draws the business analysis and SQL tables. You approve. Then the Backend is coded, passes the TDD gate, you approve, and it moves to the Frontend.

---

## 2. Dealing with Quality Gates
In our system, codes pass through Quality Gates before reaching you. If the code is rejected (e.g., because a test wasn't written), the agent might pause.

**In such a case, guide the agent:**
> *"The TDD Quality Gate rejected your code. Please read the error (Feedback Loop) and write the missing xUnit tests to request permission to pass the gate again."*

---

## 3. Cross-Team API Handoff
Synchronization of Backend and Frontend teams is always a problem in projects. Use the `API_HANDOFF.md` workflow to solve this.

**When the Backend is finished:**
> *"Backend operations are complete. Code Orchestrator, please contact the Workflow agent and generate the API_HANDOFF.md file (with JSON diffs) for the Frontend team."*

**When starting the Frontend:**
> *"Mobile Architect, please read the API_HANDOFF.md file and update the Riverpod/Redux state architecture according to the new JSON contract."*

---

## 4. Exceptions: Bypassing Rules (Override)
Very rarely, when prototyping, you might feel that the Quality Gates (mandatory Swagger writing, mandatory Tests) are slowing you down.
If you want to temporarily bypass a rule, add the following command to the end of your prompt:
> *"I am temporarily using the `[TDD_GATE_BYPASS]` authority for this operation. Give me the prototype code directly without writing tests."*
*(Note: This operation is only for emergencies; it weakens the enterprise architecture.)*
