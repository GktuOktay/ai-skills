#!/bin/bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILLS_SRC="$SCRIPT_DIR/skills"
RULES_SRC="$SCRIPT_DIR/rules"

echo "🚀 AI Skills & Rules Symlink Kurulumu..."

create_symlink() {
    local target="$1"
    local source="$2"
    local name="$3"

    echo "⚙️ [$name] $target -> $source"
    mkdir -p "$(dirname "$target")"

    if [ -L "$target" ]; then
        rm "$target"
    elif [ -d "$target" ]; then
        rm -rf "$target"
    elif [ -f "$target" ]; then
        rm "$target"
    fi

    ln -s "$source" "$target"
    echo "   ✅ Bağlantı kuruldu."
}

create_symlink "$HOME/.gemini/config/skills" "$SKILLS_SRC" "Antigravity (Gemini)"
create_symlink "$HOME/.claude/skills" "$SKILLS_SRC" "Claude Code"
create_symlink "$HOME/.cursor/rules" "$RULES_SRC" "Cursor Rules"

echo "✨ Tüm araçlar başarıyla bağlandı!"
