---
name: Client-Side Security Best Practices
description: "Frontend güvenliği; XSS, CSRF, Content Security Policy (CSP) header'ları ve DOM tabanlı zafiyetlerin engellenmesi."
alwaysApply: false
---

# Client-Side Security Best Practices

## Overview
This skill outlines how to build secure frontend applications by preventing Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), configuring robust Content Security Policy (CSP) headers, ensuring secure cookie usage, and mitigating DOM-based vulnerabilities.

## Core Principles

### 1. Cross-Site Scripting (XSS) Prevention
Never trust data rendered to the DOM.
- **Context-aware encoding:** Always encode data based on where it will be rendered (HTML body, attributes, JavaScript variables).
- **Use modern frameworks:** Leverage frameworks like React, Angular, or Vue which automatically escape content by default.
- **Avoid dangerous APIs:** Avoid using APIs like `innerHTML`, `document.write()`, or `v-html`/`dangerouslySetInnerHTML` unless absolutely necessary and the input is strictly sanitized (e.g., using DOMPurify).

### 2. Cross-Site Request Forgery (CSRF) Mitigation
Protect state-changing requests from being forged.
- **Anti-CSRF Tokens:** Implement synchronizer token pattern where every state-changing request (POST, PUT, DELETE) includes a unique, session-tied token.
- **SameSite Cookies:** Use the `SameSite=Lax` or `SameSite=Strict` flag on all sensitive cookies (e.g., session cookies) to prevent the browser from sending them in cross-site requests.

### 3. Secure Cookie Flags
Ensure cookies are handled securely by the browser.
- **HttpOnly:** Prevent client-side scripts from accessing the cookie, mitigating the impact of XSS.
- **Secure:** Ensure the cookie is only transmitted over HTTPS.
- **SameSite:** Mitigate CSRF by controlling cross-site cookie sending.

### 4. Content Security Policy (CSP)
Use CSP to restrict the sources from which resources can be loaded.
- **Strict Policies:** Implement a strict CSP that relies on nonces or hashes rather than `unsafe-inline` or `unsafe-eval`.
- **Report-Only Mode:** Deploy CSP in report-only mode first to monitor violations before enforcing.

### 5. DOM-Based Vulnerabilities
Prevent attacks where the payload is executed as a result of modifying the DOM environment in the victim's browser.
- **Avoid sinks:** Be cautious with DOM sinks like `location.href`, `setTimeout`, `eval()`.
- **Validate sources:** Validate data from sources like `location.hash`, `document.referrer`, `window.name`.

## Code Examples

### Setting Secure Cookies (Node.js/Express)
```javascript
res.cookie('session_id', 'value', {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'strict',
  maxAge: 3600000 // 1 hour
});
```

### Implementing a Strict CSP (Express with Helmet)
```javascript
const helmet = require('helmet');

app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", (req, res) => `'nonce-${res.locals.nonce}'`],
    objectSrc: ["'none'"],
    upgradeInsecureRequests: [],
  }
}));
```

## Checklist for Client Security Review
- [ ] Is input sanitized before being injected into the DOM?
- [ ] Are dangerous APIs like `innerHTML` avoided or carefully reviewed?
- [ ] Are Anti-CSRF tokens implemented for all state-changing requests?
- [ ] Do sensitive cookies have `HttpOnly`, `Secure`, and `SameSite` flags?
- [ ] Is a robust CSP implemented without `unsafe-inline`?
- [ ] Are user inputs from URL fragments or referrers validated before use?
