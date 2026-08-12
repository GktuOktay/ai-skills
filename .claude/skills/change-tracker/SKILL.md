---
name: change-tracker
description: "Automated Markdown changelog and version history maintenance during development. / TR: Kod yazıldıkça yapılan değişiklikleri (changelog) ve versiyon geçmişini standart Markdown dosyasında tutma kuralı."
alwaysApply: true
---

# Change Tracker & Versioning Standard

This skill mandates that every meaningful code change (feature, bugfix, refactor) in the project is immediately documented and that the version history (changelog) is kept in a standard format.

## 📌 Core Rules

1. **Continuous Tracking:** When a task or module is completed in the code, immediately add the changes to `CHANGELOG.md` (or the relevant Markdown document in the project structure) rather than keeping them in mind.
2. **Standard Format:** Log changes in accordance with the "Keep a Changelog" (keepachangelog.com) standard.
3. **Versioning:** Adhere to Semantic Versioning (SemVer) rules (MAJOR.MINOR.PATCH).
4. **Unreleased Management:** Always group in-development changes under the `[Unreleased]` (or current sprint/target version) heading.

## 📝 Format Template

Use the following structure in the `CHANGELOG.md` file (or similar version tracking file):

```markdown
# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- New UI components for the user login screen.
- New indexing structure for database optimization.

### Changed
- Authentication service updated to use OAuth2.

### Fixed
- Fixed the horizontal scrolling issue on mobile view.

## [1.0.2] - 2026-08-10
### Fixed
- Fixed the 500 error returned when the API rate limit is exceeded (changed to 429).
```

## 🔄 Workflow

1. **Code Development:** Write or modify the code as requested.
2. **Log Update:** Add a clean bullet point summarizing the work done under the `[Unreleased]` heading (or appropriate version) in the relevant category (Added, Changed, Fixed, Removed, etc.) in the `CHANGELOG.md` file.
3. **Pre-Commit Check:** Right before committing changes with `git-conventional-commits`, ensure that the `CHANGELOG.md` file is saved.

## 🛠 Categories to Use
- **Added:** for new features.
- **Changed:** for changes in existing functionality.
- **Deprecated:** for soon-to-be removed features.
- **Removed:** for now removed features.
- **Fixed:** for any bug fixes.
- **Security:** in case of vulnerabilities.

**IMPORTANT:** When the user activates the "track version/md as code is written" rule, you (the AI assistant) must automatically edit the project's change history file after every code block modification.
