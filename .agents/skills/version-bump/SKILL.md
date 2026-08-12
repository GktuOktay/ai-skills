---
name: Version Bumping and Release Management
description: "Semantic versioning rules, automated release notes generation, and release management. / TR: Semantik versiyonlama kuralları, otomatik sürüm notu oluşturma ve sürüm yönetimi süreçleri."
---

# Semantic Versioning and Release Management

Proper versioning and release management ensure predictable deployments, clear communication with users, and safe rollback mechanisms.

## 1. Semantic Versioning (SemVer) Rules

Semantic Versioning follows the format: `MAJOR.MINOR.PATCH` (e.g., `2.14.3`).

- **MAJOR (Incompatible Changes)**: Increment when you make incompatible API changes. Existing clients will break if they upgrade without code changes. (e.g., removing a deprecated endpoint, changing a function signature).
- **MINOR (New Features)**: Increment when you add functionality in a backward-compatible manner. Existing clients can upgrade safely. (e.g., adding a new API endpoint, adding a non-breaking optional parameter).
- **PATCH (Bug Fixes)**: Increment when you make backward-compatible bug fixes. No new features are added. (e.g., fixing a memory leak, resolving a crash).

*Note: Version `0.y.z` is for initial development. Anything MAY change at any time. The public API should not be considered stable.*

## 2. Pre-release Versions

Used for testing and stabilization before a major/minor release. Appended to the version number with a hyphen.
- **Alpha** (`v2.0.0-alpha.1`): Internal testing, highly unstable, features may be incomplete.
- **Beta** (`v2.0.0-beta.2`): Feature complete, public testing, bugs are expected.
- **RC (Release Candidate)** (`v2.0.0-rc.1`): Potential final release, testing for critical regressions only.

## 3. Conventional Commits and Changelog Generation

Manual changelogs are error-prone and tedious. Use **Conventional Commits** to automate them.
Format: `<type>[optional scope]: <description>`

Common Types:
- `feat:` (New feature) -> Triggers a MINOR bump.
- `fix:` (Bug fix) -> Triggers a PATCH bump.
- `docs:`, `style:`, `refactor:`, `test:`, `chore:` -> Usually do not trigger a release or changelog entry.
- `BREAKING CHANGE:` (In the footer) -> Triggers a MAJOR bump, regardless of the type.

By strictly formatting commit messages, tools can automatically calculate the next version number and generate a `CHANGELOG.md`.

## 4. Git Tagging Strategies

Git tags create immutable snapshots of releases.
- Always tag releases using the version number (e.g., `v1.2.3`).
- **Annotated Tags** (`git tag -a v1.2.3 -m "Release v1.2.3"`) are preferred over lightweight tags because they contain the tagger name, email, and date, and can be cryptographically signed.
- Push tags to the remote repository (`git push origin --tags`).

## 5. CI/CD Release Pipelines

A modern release pipeline should be fully automated.
1. **Trigger**: Developer merges a PR into the `main` branch.
2. **Test**: CI runs unit, integration, and E2E tests.
3. **Build**: Code is compiled and assets are minified.
4. **Version**: A tool analyzes commits, bumps the version in package manifests (`package.json`), generates the changelog, and creates a git tag.
5. **Publish**: Artifacts (Docker images, NPM packages, binaries) are built and published to a registry.
6. **Deploy**: The new version is deployed to staging or production environments.

## 6. Automation Tools

- **standard-version**: A utility for versioning using semver and CHANGELOG generation powered by Conventional Commits. (Note: currently in maintenance mode).
- **changesets**: Excellent for monorepos. Developers declare intents to release in PRs, and changesets aggregates them to bump versions across dependent packages simultaneously.
- **release-please (Google)**: Automates releases by analyzing commits, creating Release PRs, and maintaining changelogs. Great for GitHub Actions integration.

## 7. Monorepo Versioning

Versioning multiple packages in a single repository requires a strategy:
- **Fixed/Lockstep Versioning**: All packages in the monorepo share the exact same version number (e.g., Babel, React). Easier to manage, but forces bumps on untouched packages.
- **Independent Versioning**: Each package maintains its own version number (e.g., AWS SDK). More accurate, but dependency management between internal packages becomes complex. Tools like `changesets` or `Lerna` are essential here.
