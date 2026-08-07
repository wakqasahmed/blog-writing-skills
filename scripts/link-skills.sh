#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
target="${1:?Usage: scripts/link-skills.sh /path/to/skills-directory}"

mkdir -p "$target"
shopt -s nullglob
for skill in "$repo"/skills/*; do
  [ -d "$skill" ] && ln -sfn "$skill" "$target/$(basename "$skill")"
done
