# 🤝 Contributing to AI Skills Library

First off, thank you for considering contributing to the **AI Skills & Rules Library**! It's contributions like yours that make open source such an amazing community to learn, inspire, and build together.

---

## 🚀 How Can I Contribute?

### 1. Adding a New Skill
1. Create a new folder under `skills/<your-skill-name>/`.
2. Add a `SKILL.md` file using standard YAML frontmatter:
   ```markdown
   ---
   name: your-skill-name
   description: A concise description of what this skill does and when to use it.
   alwaysApply: false
   ---

   # Skill Title

   Detailed instructions for the AI agent...
   ```
3. Run `python setup.py` to compile Cursor rules and universal agent formats.
4. Test your skill locally across Cursor, Antigravity, or Claude Code.
5. Submit a Pull Request!

### 2. Improving Existing Skills
- Refine existing prompt instructions, add edge-case guards, or enhance anti-sycophancy rules.

---

## 📜 Pull Request Process

1. Fork the repo and create your branch from `main`.
2. Ensure `python setup.py` completes cleanly with no errors.
3. Keep commit messages clear (use [Conventional Commits](https://www.conventionalcommits.org/)).
4. Open a Pull Request with a clear description of the changes and motivation.

---

## ⚖️ Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
