#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"
FAIL=0

echo "== 02-headlines-hooks eval =="

echo "-- contract check --"
if python3 "$DIR/contract_check.py"; then
  echo "PASS: contract_check.py"
else
  echo "FAIL: contract_check.py"
  FAIL=1
fi

echo "-- fixtures structural check --"
set +e
python3 - "$FIXTURES" <<'PY'
import json
import sys

path = sys.argv[1]

try:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
except (OSError, json.JSONDecodeError) as exc:
    print(f"FAIL: could not parse {path} as JSON: {exc}")
    sys.exit(1)

problems = []

if not isinstance(data, list):
    problems.append("top-level JSON value must be an array")
    data = []

if len(data) < 10:
    problems.append(f"expected at least 10 fixture entries, found {len(data)}")

follow_count = sum(1 for item in data if isinstance(item, dict) and item.get("expected") == "follow")
violates_count = sum(1 for item in data if isinstance(item, dict) and item.get("expected") == "violates")

if follow_count < 5:
    problems.append(f"expected at least 5 entries with expected=follow, found {follow_count}")
if violates_count < 5:
    problems.append(f"expected at least 5 entries with expected=violates, found {violates_count}")

for i, item in enumerate(data):
    if not isinstance(item, dict):
        problems.append(f"entry {i} is not an object")
        continue
    for field in ("id", "scenario", "expected"):
        if field not in item:
            problems.append(f"entry {i} ({item.get('id', '?')}) missing required field {field!r}")
    if item.get("expected") == "violates" and "violates_gate" not in item:
        problems.append(f"entry {i} ({item.get('id', '?')}) has expected=violates but no violates_gate")

if problems:
    print("FAIL: fixtures structural check")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)

print(f"PASS: fixtures structural check ({len(data)} entries, {follow_count} follow / {violates_count} violates)")
PY
FIXTURES_STATUS=$?
set -e

if [ "$FIXTURES_STATUS" -ne 0 ]; then
  FAIL=1
fi

echo "== summary =="
if [ "$FAIL" -ne 0 ]; then
  echo "RESULT: FAIL"
  exit 1
fi

echo "RESULT: PASS"
