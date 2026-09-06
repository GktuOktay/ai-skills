---
name: Smart Codebase Exploration
description: "Büyük ve karmaşık kod tabanlarında akıllı gezinme, giriş noktalarını bulma ve kod yapısını anlama taktikleri."
---

# Intelligent Codebase Exploration and Navigation

Navigating a large, unfamiliar codebase can be overwhelming. Relying solely on manual file browsing is inefficient. This guide covers strategies for rapidly understanding code architecture and finding specific logic.

## 1. Grep/Ripgrep Patterns for Finding Code

Ripgrep (`rg`) is the fastest tool for text-based searching.
- **Find Function Definitions**: To find where a function is defined, search for keywords like `def`, `class`, or `function`.
  - `rg "function processOrder"` or `rg "const processOrder ="`
- **Find Class Definitions**:
  - `rg "class PaymentGateway"`
- **Filter by File Type**:
  - `rg "TODO" -t py` (Only search Python files)
- **Exclude Directories**:
  - `rg "password" --glob "!tests/*" --glob "!node_modules/*"`
- **Case Insensitive**:
  - `rg -i "user_id"`

## 2. AST-Based Exploration

While `rg` is fast, it lacks context. AST (Abstract Syntax Tree) tools understand code structure.
- **LSP (Language Server Protocol)**: Use IDE features (Go to Definition, Find All References). These are vastly superior to text search.
- **Tree-sitter**: Used in modern editors (Neovim, Zed) for precise syntax highlighting and structural navigation.
- **AST Grep (`sg`)**: Allows searching code by structure rather than exact text matches (e.g., finding all try/catch blocks that silently ignore errors).

## 3. Finding Entry Points and Hot Paths

When starting in a new repository, find where execution begins.
- **Web Apps**: Look for `index.js`, `main.ts`, `App.tsx`, `wsgi.py`, or `main.go`.
- **Routing**: Search for router definitions (e.g., `rg "react-router"`, `rg "@app.route"`, `rg "router.get"`). This maps URLs to specific controllers.
- **Package Manifests**: Check `package.json`, `Cargo.toml`, or `Makefile` for start commands (e.g., `npm run start`). The script defined there points to the entry point.

## 4. Tracing Function Call Chains

To understand a feature, trace its execution path.
1. **Identify the Trigger**: Find the UI button click, API endpoint, or cron job schedule.
2. **Follow the Data**: Look at the arguments passed to the controller.
3. **Drill Down**: Use "Go to Definition" to jump through the service layer, repositories, and finally to the database queries.
4. **Take Notes**: Maintain a scratchpad documenting the call stack (e.g., `Route -> UserController -> AuthService -> DB`).

## 5. Understanding Module Boundaries

Large systems are organized into modules.
- **Look at Imports**: High-level modules should orchestrate lower-level modules. If you see cyclical imports or UI components importing database drivers directly, the boundaries are poorly defined.
- **Folder Structure**: Common patterns include:
  - By Feature (e.g., `/auth`, `/billing`, `/users`) - Usually easier to navigate.
  - By Type (e.g., `/controllers`, `/models`, `/views`) - Often requires jumping across many folders to understand one feature.

## 6. Identifying Dead Code

Dead code adds noise and confusion.
- **Unused Exports**: Use IDE features or linters (like ESLint) to highlight exported functions with zero references.
- **Feature Flags**: Search for feature flag evaluations. If a flag is permanently on or off, the conditional logic can be removed.
- **Logs**: If you suspect a function is dead, check production logs or APM tools. If it hasn't been executed in 30 days, it might be safe to remove.

## 7. Reading Test Files as Documentation

Tests are often the most accurate and up-to-date documentation.
- **Unit Tests**: Reveal the expected inputs, outputs, and edge cases of individual functions.
- **Integration Tests**: Show how different modules wire together.
- **E2E Tests**: Document critical user flows and the exact steps required to complete a business process.

## 8. Using Git Blame/Log for Evolution Context

Code rarely explains *why* it was written, only *what* it does.
- **`git blame <file>`**: Shows who last modified each line and in which commit.
- **`git log -S "string"` (Pickaxe)**: Finds commits that added or removed a specific string. Useful for finding when a bug was introduced or a feature was removed.
- **Reading Commit Messages**: A good commit message explains the context behind a confusing block of code.
