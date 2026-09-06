---
name: Software Composition and Dependency Auditing
description: "Proje bağımlılıklarındaki (npm, pip vb.) CVE zafiyetlerinin taranması, supply chain güvenliği ve versiyon güncellemeleri."
alwaysApply: false
---

# Software Composition & Dependency Auditing

## Overview
This skill focuses on managing the security of third-party libraries and tools used in your project. It covers Software Composition Analysis (SCA), auditing dependencies, handling Common Vulnerabilities and Exposures (CVEs), preventing lockfile poisoning, and establishing automated update strategies.

## Core Principles

### 1. Software Composition Analysis (SCA)
Understand what comprises your application.
- **Inventory:** Maintain an accurate inventory of all direct and transitive dependencies (e.g., SBOM - Software Bill of Materials).
- **Continuous Monitoring:** Regularly scan your dependency tree for known vulnerabilities.

### 2. Auditing Dependencies
Ensure that libraries pulled from package managers (npm, pip, Maven, etc.) are safe.
- **Run audits regularly:** Use built-in tools like `npm audit`, `pip-audit`, or third-party tools like Snyk or OWASP Dependency-Check in your CI/CD pipeline.
- **Assess risk:** Evaluate the severity of CVEs. A high-severity vulnerability in a dev dependency might pose a lower risk than a medium-severity one in production code, but both should be addressed.

### 3. Supply Chain Security and Lockfile Poisoning
Prevent malicious packages from entering your build process.
- **Lock files:** Always commit your lock files (`package-lock.json`, `yarn.lock`, `Pipfile.lock`, `requirements.txt` with hashes) to ensure deterministic builds.
- **Verify integrity:** Ensure package managers are configured to check integrity hashes. Watch out for unauthorized changes to lock files during PR reviews (lockfile poisoning).
- **Typosquatting:** Double-check package names before installation to avoid typosquatting attacks (e.g., `electro` instead of `electron`).

### 4. Automated Dependency Updates
Keep dependencies up-to-date to patch vulnerabilities proactively.
- **Automation tools:** Use tools like Dependabot or Renovate to automatically create PRs for dependency updates.
- **Testing:** Ensure you have a robust automated test suite so you can confidently merge dependency updates.

## Code Examples

### GitHub Actions: Run npm audit
```yaml
name: Dependency Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: npm ci
      - name: Run audit
        run: npm audit --audit-level=high
```

### Python: Requirements with Hashes
Generate requirements with hashes to ensure integrity:
```bash
pip-compile --generate-hashes requirements.in
```

## Checklist for Dependency Security
- [ ] Is an SCA tool integrated into the CI/CD pipeline?
- [ ] Are lock files committed to the repository?
- [ ] Are lock file changes reviewed carefully during PRs?
- [ ] Is an automated dependency update tool (Dependabot/Renovate) configured?
- [ ] Are package integrity hashes verified during installation?
- [ ] Is there a process to evaluate and remediate reported CVEs promptly?
