#!/usr/bin/env bash
set -euo pipefail

# File purpose: make local edits immediately visible to agent harnesses.
# Dev-only helper for maintainers: link this checkout into local agent skill dirs.
# Users should install Moneta Skills through skills.sh instead of running this.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

# Collect bundled skills once, then link the same set into every destination.
names=()
srcs=()
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  names+=("$(basename "$src")")
  srcs+=("$src")
done < <(find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -print0)

for DEST in "${DESTS[@]}"; do
  # Refuse a destination symlink that points back into this repo.
  if [ -L "$DEST" ]; then
    resolved="$(readlink -f "$DEST")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $DEST is a symlink into this repo ($resolved)." >&2
        echo "Remove it and re-run; this script will recreate per-skill links." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$DEST"
  for i in "${!names[@]}"; do
    name="${names[$i]}"
    src="${srcs[$i]}"
    target="$DEST/$name"

    # Replace stale local copies so the symlink becomes the single editable path.
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi

    ln -sfn "$src" "$target"
    echo "linked $name -> $src ($DEST)"
  done
done
