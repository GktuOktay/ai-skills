---
name: Git PR Reviewer
description: "Pull Request (PR) oluşturma ve kod inceleme (code review) süreçleri için standartlar ve yapıcı geri bildirim."
alwaysApply: false
---

# Pull Request and Code Review Guide

This skill provides guidelines for creating excellent pull requests and conducting effective, constructive code reviews.

## Writing Good PR Descriptions

A PR description should answer the "What, Why, and How" to give reviewers context.

### Essential Components
1. **What**: Briefly summarize the changes introduced.
2. **Why**: Explain the motivation (link to issue/ticket).
3. **How**: Highlight key implementation details or architectural decisions.
4. **Testing**: How can the reviewer test these changes?

### Example PR Description
```markdown
## What
Added email verification step during user registration.

## Why
Fixes #456. We need to ensure users provide valid email addresses before granting access.

## How
- Integrated SendGrid API for sending verification emails.
- Added `is_verified` flag to `users` table.
- Created `/verify-email` endpoint.

## Testing Steps
1. Register a new account.
2. Check your email for the verification link.
3. Click the link and verify the account activates successfully.
```

## Conducting Constructive Code Reviews

Code reviews should improve code quality and facilitate knowledge sharing, not criticize the author.

### Principles
- **Be Respectful**: Critique the code, not the author. Use "we" instead of "you".
- **Be Specific**: Point exactly to the line and suggest an alternative.
- **Explain Why**: Don't just say "change this"; explain the benefit (e.g., performance, readability).
- **Praise Good Code**: Acknowledge elegant solutions.

## Merge Strategies

Choose the right merge strategy based on project conventions.

### 1. Squash and Merge
- **Best for**: Feature branches with many messy, WIP commits.
- **Result**: Combines all commits into a single, clean commit on the main branch.

### 2. Rebase and Merge
- **Best for**: Branches with clean, logical, and atomic commits.
- **Result**: Appends all commits to the main branch history linearly (no merge commit).

### 3. Merge Commit
- **Best for**: Large feature branches where keeping the branch history intact is valuable.
- **Result**: Creates a dedicated merge commit showing when the branch was merged.

## Handling Merge Conflicts

1. Update your main branch: `git pull origin main`
2. Checkout your feature branch: `git checkout feature-branch`
3. Merge or Rebase main: `git merge main` or `git rebase main`
4. Resolve conflicts manually in the editor.
5. Complete the merge/rebase and push to origin.

## PR Checklist
- [ ] Code follows style guidelines.
- [ ] Tests have been added or updated.
- [ ] Documentation has been updated.
- [ ] Commit history is clean and descriptive.
