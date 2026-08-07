#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "== Running contract check =="
python3 "$SCRIPT_DIR/contract_check.py"

echo
echo "== Validating held-out scenarios fixture =="

if [ ! -f "$FIXTURES" ]; then
  echo "MISSING FILE: $FIXTURES"
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
    errors.append("fixture root must be a JSON array")
    data = []

total = len(data)
if total < 10:
    errors.append(f"expected at least 10 scenarios, found {total}")

follow_count = 0
violates_count = 0

for i, entry in enumerate(data):
    for field in ("id", "scenario", "expected"):
        if field not in entry:
            errors.append(f"entry {i} missing required field '{field}'")

    expected = entry.get("expected")
    if expected not in ("follow", "violates"):
        errors.append(f"entry {i} has invalid expected value: {expected!r}")
    elif expected == "follow":
        follow_count += 1
    elif expected == "violates":
        violates_count += 1
        if "violates_gate" not in entry:
            errors.append(f"entry {i} has expected='violates' but no 'violates_gate'")

if follow_count < 5:
    errors.append(f"expected at least 5 'follow' scenarios, found {follow_count}")
if violates_count < 5:
    errors.append(f"expected at least 5 'violates' scenarios, found {violates_count}")

if errors:
    print("Fixture structural check FAILED. Issues:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(
    f"Fixture structural check PASSED: {total} scenarios "
    f"({follow_count} follow, {violates_count} violates)."
)
PYEOF

echo
echo "All eval checks passed."
