#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "== Running contract check =="
python3 "$DIR/contract_check.py"

echo "== Validating fixtures structure =="
python3 - "$FIXTURES" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path) as f:
    data = json.load(f)

if not isinstance(data, list):
    print("FAIL: fixtures file must contain a JSON array")
    sys.exit(1)

if len(data) < 10:
    print(f"FAIL: expected at least 10 fixture entries, found {len(data)}")
    sys.exit(1)

required_fields = {"id", "scenario", "expected"}
follow_count = 0
violates_count = 0
errors = []

for i, entry in enumerate(data):
    missing = required_fields - entry.keys()
    if missing:
        errors.append(f"entry {i} ({entry.get('id', '?')}) missing fields: {missing}")
        continue
    expected = entry["expected"]
    if expected == "follow":
        follow_count += 1
    elif expected == "violates":
        violates_count += 1
        if "violates_gate" not in entry:
            errors.append(f"entry {i} ({entry['id']}) expected=violates but missing violates_gate")
    else:
        errors.append(f"entry {i} ({entry['id']}) has invalid expected value: {expected}")

if follow_count < 5:
    errors.append(f"expected at least 5 'follow' entries, found {follow_count}")
if violates_count < 5:
    errors.append(f"expected at least 5 'violates' entries, found {violates_count}")

if errors:
    print("FAIL: fixture structural check failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"PASS: {len(data)} entries ({follow_count} follow, {violates_count} violates)")
PY

echo "== Eval harness passed =="
