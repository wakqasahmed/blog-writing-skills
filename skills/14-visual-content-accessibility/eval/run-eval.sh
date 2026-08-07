#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "== Contract check =="
python3 "$SCRIPT_DIR/contract_check.py"

echo
echo "== Fixture structural check =="

if [ ! -f "$FIXTURES" ]; then
  echo "MISSING FIXTURES FILE: $FIXTURES"
  exit 1
fi

python3 - "$FIXTURES" <<'PYEOF'
import json
import sys

path = sys.argv[1]

with open(path, encoding="utf-8") as f:
    data = json.load(f)

errors = []

if not isinstance(data, list):
    errors.append("fixtures file must contain a JSON array")
    data = []

if len(data) < 10:
    errors.append(f"expected at least 10 fixture entries, found {len(data)}")

follow_count = 0
violates_count = 0

for i, entry in enumerate(data):
    if not isinstance(entry, dict):
        errors.append(f"entry {i} is not an object")
        continue
    for field in ("id", "scenario", "expected"):
        if field not in entry:
            errors.append(f"entry {i} missing required field '{field}'")
    expected = entry.get("expected")
    if expected == "follow":
        follow_count += 1
    elif expected == "violates":
        violates_count += 1
        if "violates_gate" not in entry:
            errors.append(f"entry {i} (id={entry.get('id')}) has expected='violates' but no 'violates_gate'")
    else:
        errors.append(f"entry {i} (id={entry.get('id')}) has invalid expected value: {expected!r}")

if follow_count < 5:
    errors.append(f"expected at least 5 entries with expected='follow', found {follow_count}")
if violates_count < 5:
    errors.append(f"expected at least 5 entries with expected='violates', found {violates_count}")

if errors:
    print("Fixture structural check FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"Fixture structural check passed: {len(data)} entries ({follow_count} follow, {violates_count} violates).")
PYEOF

echo
echo "All eval checks passed."
