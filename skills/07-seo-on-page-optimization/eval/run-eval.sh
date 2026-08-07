#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "== Contract check =="
python3 "$SCRIPT_DIR/contract_check.py"

echo
echo "== Fixture structural check =="
python3 - "$FIXTURES" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    data = json.load(f)

errors = []

if not isinstance(data, list):
    sys.exit("Fixtures file must contain a JSON array")

if len(data) < 10:
    errors.append(f"expected >=10 scenarios, found {len(data)}")

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
        if not entry.get("violates_gate"):
            errors.append(f"entry {i} (id={entry.get('id')}) is 'violates' but missing 'violates_gate'")

if follow_count < 5:
    errors.append(f"expected >=5 'follow' scenarios, found {follow_count}")
if violates_count < 5:
    errors.append(f"expected >=5 'violates' scenarios, found {violates_count}")

if errors:
    print("Fixture structural check FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"Fixture structural check PASSED: {len(data)} scenarios ({follow_count} follow, {violates_count} violates).")
PY

echo
echo "All eval checks passed."
