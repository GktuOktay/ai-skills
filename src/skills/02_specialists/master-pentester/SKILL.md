---
name: testing-master
description: "Test stratejileri, birim testleri (unit test) ve e2e testler yazmak için yetenek."
metadata:
  version: 1.0.0
---

# Testing Master (QA & Automated Testing)

This skill designs and implements automated testing suites to guarantee code stability, reliability, and regression prevention.

## 🧪 Testing Pyramid & Strategies

### 1. Unit Testing
- **Tools:** Vitest, Jest.
- **Scope:** Pure functions, utilities, custom hooks, isolated components.
- **Principles:** AAA pattern (Arrange - Act - Assert), dependency mocking (`vi.fn()` / `jest.fn()`).

### 2. Integration & Component Testing
- **Tools:** React Testing Library, User Event, MSW (Mock Service Worker).
- **Scope:** User interactions (clicks, form inputs, modal reveals) and API mocking.
- **Principles:** Query accessible DOM elements (`getByRole`, `getByText`) rather than implementation details.

### 3. End-to-End (E2E) Testing
- **Tools:** Playwright, Cypress.
- **Scope:** Critical user journeys (Signup, Checkout, Content creation).
- **Principles:** Avoid flaky tests using dynamic waits (`waitForSelector`) and isolated test fixtures.

## Output Template

1. 🎯 **Testing Strategy Summary**
2. 📝 **Production Test Code:** Complete, executable test suite files.
3. 🛠️ **Mocking & Execution Setup:** Fixtures and execution commands (`npm run test`).
