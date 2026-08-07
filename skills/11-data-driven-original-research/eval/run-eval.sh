#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "Running contract check..."
python3 "$DIR/contract_check.py"

echo "Running fixtures structural check..."
python3 - "$FIXTURES" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    data = json.load(f)

if not isinstance(data, list) or len(data) < 10:
    print(f"FAILED: expected at least 10 fixture entries, found {len(data) if isinstance(data, list) else 'invalid'}")
    sys.exit(1)

required_fields = {"id", "scenario", "expected"}
follow_count = 0
violates_count = 0

for entry in data:
    missing = required_fields - entry.keys()
    if missing:
        print(f"FAILED: entry {entry.get('id', '?')} missing fields: {missing}")
        sys.exit(1)
    if entry["expected"] == "follow":
        follow_count += 1
    elif entry["expected"] == "violates":
        violates_count += 1
        if "violates_gate" not in entry:
            print(f"FAILED: entry {entry['id']} has expected=violates but no violates_gate")
            sys.exit(1)
    else:
        print(f"FAILED: entry {entry['id']} has invalid expected value: {entry['expected']}")
        sys.exit(1)

if follow_count < 5:
    print(f"FAILED: expected at least 5 'follow' entries, found {follow_count}")
    sys.exit(1)

if violates_count < 5:
    print(f"FAILED: expected at least 5 'violates' entries, found {violates_count}")
    sys.exit(1)

print(f"Fixtures structural check PASSED: {len(data)} entries, {follow_count} follow, {violates_count} violates.")
PY

echo "All eval checks passed."
