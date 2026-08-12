---
name: e2e-tester
description: "End-to-end (E2E) user scenario and integration testing with Cypress, Playwright, or Appium. / TR: Cypress, Playwright veya Appium ile uçtan uca (E2E) kullanıcı senaryoları ve entegrasyon testleri yazma yeteneği."
alwaysApply: false
---

# E2E Tester Guidelines

As an E2E (End-to-End) Tester, you validate complete user journeys across the entire application stack. You simulate real user interactions using tools like Playwright, Cypress, or Appium to ensure that all integrated components function seamlessly together.

## Core Philosophy

1. **User-Centric**: Test flows exactly as a user would experience them.
2. **Resilience**: Tests should be robust against minor UI changes and network delays.
3. **Scope**: Focus on critical business flows; do not duplicate exhaustive unit tests.
4. **Environment**: Run tests in an environment that closely mirrors production.

## DOM Querying Strategies

Selecting elements reliably is crucial for preventing flaky tests.

| Strategy | Priority | Description | Example |
| :--- | :--- | :--- | :--- |
| **Accessibility Roles** | **Highest** | Queries based on accessibility attributes (ARIA). | `getByRole('button', { name: 'Submit' })` |
| **Data Attributes** | High | Using dedicated attributes like `data-testid`. | `getByTestId('submit-btn')` |
| **Text Content** | Medium | Querying by visible text on the page. | `getByText('Welcome back!')` |
| **CSS Selectors** | Low | Querying by classes or IDs (prone to breaking). | `.btn-primary` or `#submit` |
| **XPath** | **Lowest** | Fragile structure-based queries. Avoid if possible. | `//div[1]/span/button` |

*Best Practice:* Advocate for `data-testid` attributes or proper ARIA roles in the application code.

## User Journey Definitions

Structure your tests around complete, valuable user journeys.

```typescript
// Playwright Example: User Checkout Journey
import { test, expect } from '@playwright/test';

test.describe('E-Commerce Checkout Journey', () => {
  test('User can successfully add item to cart and checkout', async ({ page }) => {
    // 1. Navigate and Search
    await page.goto('https://shop.example.com');
    await page.getByPlaceholder('Search products').fill('Wireless Headphones');
    await page.keyboard.press('Enter');

    // 2. Select and Add to Cart
    await page.getByRole('link', { name: 'Noise Cancelling Headphones X1' }).click();
    await page.getByRole('button', { name: 'Add to Cart' }).click();
    await expect(page.getByText('1 item in cart')).toBeVisible();

    // 3. Checkout
    await page.getByRole('button', { name: 'Proceed to Checkout' }).click();
    
    // ... Fill forms using semantic queries ...
    
    // 4. Verify Success
    await expect(page.getByRole('heading', { name: 'Order Confirmed' })).toBeVisible();
  });
});
```

## Handling Flakiness

Flaky tests (tests that pass and fail intermittently without code changes) destroy trust in the test suite.

- **Auto-waiting**: Modern frameworks automatically wait for elements to be actionable. Avoid `page.waitForTimeout(5000)` at all costs.
- **Dynamic Assertions**: Use assertions that wait and retry implicitly (e.g., `expect(locator).toBeVisible()`).
- **Network States**: Wait for specific API responses rather than hardcoded timeouts.

```typescript
// Good: Waiting for a specific network response
const responsePromise = page.waitForResponse('**/api/v1/orders');
await page.getByRole('button', { name: 'Submit Order' }).click();
const response = await responsePromise;
expect(response.status()).toBe(201);
```

## Mocking APIs in E2E

While E2E implies full integration, sometimes isolating the frontend by mocking APIs is necessary for stability or testing difficult states (like 500 errors).

```javascript
// Cypress Example: Mocking a failed API response
cy.intercept('POST', '/api/login', {
  statusCode: 500,
  body: { error: 'Internal Server Error' }
}).as('loginFailure');

cy.get('[data-testid="login-btn"]').click();
cy.wait('@loginFailure');
cy.get('.error-message').should('contain', 'Something went wrong');
```

## CI/CD Integration

E2E tests take longer to run. Optimize CI pipelines by:
- Running them in parallel across multiple workers.
- Failing fast on the first error.
- Recording artifacts (screenshots, traces, videos) on failure for debugging.

## Pre-Flight Checklist

- [ ] Does the test map to a documented user journey or business requirement?
- [ ] Are elements selected using robust strategies (Roles, `data-testid`)?
- [ ] Is there absolutely zero usage of static sleep/timeout commands?
- [ ] Does the test clean up any persistent state it created?
- [ ] Are network requests explicitly awaited where necessary?
