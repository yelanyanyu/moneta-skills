#!/usr/bin/env bash
set -euo pipefail

# File purpose: report the skill files that belong to the publishable package.
# List every bundled Moneta skill that will be discovered by package tooling.
REPO="$(cd "$(dirname "$0")/.." && pwd)"

# Keep the scan rooted at skills/ so examples and docs never look installable.
cd "$REPO"
find skills -name SKILL.md -not -path '*/node_modules/*' | sort
