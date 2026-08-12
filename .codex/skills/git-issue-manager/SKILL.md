---
name: Git Issue Manager
description: "GitHub/GitLab issue management best practices, bug report templates, feature requests, and triage labeling. / TR: GitHub/GitLab issue yönetimi için en iyi uygulamalar. Etkili hata raporları, özellik istekleri yazma ve etiketleme."
alwaysApply: false
---

# Git Issue Management Guide

This skill outlines the best practices for managing issues, writing effective bug reports and feature requests, and streamlining the triage process.

## Writing Effective Bug Reports

A good bug report helps developers reproduce and fix the issue quickly.

### Essential Components
1. **Title**: Clear and concise summary of the issue.
2. **Environment**: OS, Browser, App Version, etc.
3. **Reproduction Steps**: Step-by-step instructions to reproduce the bug.
4. **Expected Behavior**: What should happen.
5. **Actual Behavior**: What actually happens.
6. **Visual Proof**: Screenshots, videos, or logs (if applicable).

### Example
**Title**: Search bar returns 500 error when special characters are used
**Steps to Reproduce**:
1. Go to the homepage.
2. Enter `%$#@` in the search bar.
3. Click "Search".
**Expected**: A "No results found" message or input validation error.
**Actual**: The page crashes and displays a 500 Internal Server Error.

## Writing Feature Requests

Feature requests should clearly state the problem and the proposed solution.

### Essential Components
1. **Problem Statement**: What is the problem or limitation?
2. **Proposed Solution**: How should the feature work?
3. **Alternatives Considered**: What other options were evaluated?
4. **Additional Context**: Any other information, like mockups or use cases.

## Labeling Strategy

Use a consistent labeling strategy to categorize and prioritize issues.

### Common Label Categories
- **Type**: `bug`, `enhancement`, `documentation`, `question`
- **Priority**: `high`, `medium`, `low`, `critical`
- **Status**: `triage`, `in-progress`, `blocked`, `needs-review`
- **Scope/Component**: `frontend`, `backend`, `database`, `ui`

## Triage Process

1. **Review New Issues**: Read through incoming issues regularly.
2. **Reproduce**: Verify if bugs are reproducible.
3. **Labeling**: Apply appropriate type, priority, and scope labels.
4. **Assignment**: Assign the issue to a team member or milestone.
5. **Link to PRs**: Ensure developers link pull requests to the issue using keywords (e.g., `Fixes #123`).

## Checklist for Issue Creators
- [ ] Did I search for existing issues to avoid duplicates?
- [ ] Is the title descriptive?
- [ ] Are the reproduction steps clear?
- [ ] Did I provide environment details?
