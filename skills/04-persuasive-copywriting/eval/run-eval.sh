#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_FILE="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

FAIL=0

echo "== 04-persuasive-copywriting eval =="

echo "-- contract check --"
if python3 "$SCRIPT_DIR/contract_check.py"; then
  echo "PASS: contract_check.py"
else
  echo "FAIL: contract_check.py"
  FAIL=1
fi

echo "-- fixtures structural check --"
if [ ! -f "$FIXTURES_FILE" ]; then
  echo "FAIL: fixtures file not found: $FIXTURES_FILE"
  FAIL=1
else
  RESULT="$(python3 - "$FIXTURES_FILE" <<'PY'
import json
import sys

path = sys.argv[1]

try:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
except (json.JSONDecodeError, OSError) as exc:
    print(f"INVALID:{exc}")
    sys.exit(0)

if not isinstance(data, list):
    print("INVALID:fixtures root is not a JSON array")
    sys.exit(0)

total = len(data)
follow = sum(1 for item in data if isinstance(item, dict) and item.get("expected") == "follow")
violates = sum(1 for item in data if isinstance(item, dict) and item.get("expected") == "violates")

missing_fields = []
for item in data:
    if not isinstance(item, dict):
        missing_fields.append("entry is not an object")
        continue
    for field in ("id", "scenario", "expected"):
        if field not in item:
            missing_fields.append(f"entry {item.get('id', '?')} missing field {field!r}")
    if item.get("expected") == "violates" and "violates_gate" not in item:
        missing_fields.append(f"entry {item.get('id', '?')} missing field 'violates_gate'")

print(f"OK:{total}:{follow}:{violates}:{'|'.join(missing_fields)}")
PY
)"

  STATUS="${RESULT%%:*}"
  if [ "$STATUS" = "INVALID" ]; then
    echo "FAIL: ${RESULT#INVALID:}"
    FAIL=1
  else
    IFS=':' read -r _ total follow violates missing <<< "$RESULT"
    echo "total=$total follow=$follow violates=$violates"

    if [ "$total" -lt 10 ]; then
      echo "FAIL: expected at least 10 fixture entries, found $total"
      FAIL=1
    fi
    if [ "$follow" -lt 5 ]; then
      echo "FAIL: expected at least 5 'follow' entries, found $follow"
      FAIL=1
    fi
    if [ "$violates" -lt 5 ]; then
      echo "FAIL: expected at least 5 'violates' entries, found $violates"
      FAIL=1
    fi
    if [ -n "$missing" ]; then
      echo "FAIL: fixture entries missing required fields:"
      IFS='|' read -ra ITEMS <<< "$missing"
      for item in "${ITEMS[@]}"; do
        echo "  - $item"
      done
      FAIL=1
    fi

    if [ "$FAIL" -eq 0 ]; then
      echo "PASS: fixtures structural check"
    fi
  fi
fi

echo "== summary =="
if [ "$FAIL" -eq 0 ]; then
  echo "ALL CHECKS PASSED"
  exit 0
else
  echo "EVAL FAILED"
  exit 1
fi
