#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "== 02-headlines-hooks eval =="

echo "-- contract check --"
python3 "$DIR/contract_check.py"

echo "-- fixtures structural check --"
python3 "$DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo "== summary =="
echo "RESULT: PASS"
