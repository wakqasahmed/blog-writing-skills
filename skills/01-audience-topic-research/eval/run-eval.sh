#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "== Contract check =="
python3 "$DIR/contract_check.py"

echo
echo "== Fixtures structural check =="
python3 - "$FIXTURES" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    data = json.load(f)

errors = []

if not isinstance(data, list):
    print("Fixtures file must contain a JSON array.")
    sys.exit(1)

if len(data) < 10:
    errors.append(f"Expected at least 10 scenarios, found {len(data)}.")

follow_count = 0
violates_count = 0

for i, entry in enumerate(data):
    for field in ("id", "scenario", "expected"):
        if field not in entry:
            errors.append(f"Entry {i} missing required field '{field}'.")

    expected = entry.get("expected")
    if expected == "follow":
        follow_count += 1
    elif expected == "violates":
        violates_count += 1
        if "violates_gate" not in entry:
            errors.append(f"Entry {i} ({entry.get('id')}) has expected='violates' but no 'violates_gate'.")
    else:
        errors.append(f"Entry {i} ({entry.get('id')}) has invalid expected value: {expected!r}")

if follow_count < 5:
    errors.append(f"Expected at least 5 'follow' scenarios, found {follow_count}.")
if violates_count < 5:
    errors.append(f"Expected at least 5 'violates' scenarios, found {violates_count}.")

if errors:
    print("Fixtures structural check FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"Fixtures structural check PASSED: {len(data)} scenarios ({follow_count} follow, {violates_count} violates).")
PY

echo
echo "All eval checks passed."
