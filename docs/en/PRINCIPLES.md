# 🧠 Core Principles

## 1. Evolutionary Architecture & YAGNI
Generic `BaseService` is strictly for simple CRUD. As business logic evolves, agents proactively refactor logic into dedicated Use-Case services.

## 2. Defensive Programming & IoC
Inputs are validated instantly (Fail-Fast). Dependencies like `DateTime.Now` are abstracted behind `IDateTimeProvider` for 100% testability.

## 3. Database Segregation
Database tables must be separated into logical schemas (e.g., `audit`, `identity`, `sales`) right after the business plan is approved, preventing public schema bloat.
