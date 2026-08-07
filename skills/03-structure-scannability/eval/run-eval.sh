#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_FILE="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "== 03-structure-scannability eval =="

echo "-- contract check --"
python3 "$SCRIPT_DIR/contract_check.py"

echo "-- fixtures structural check --"
python3 "$SCRIPT_DIR/../../../scripts/validate-fixtures.py" "$FIXTURES_FILE"

echo "== summary =="
echo "ALL CHECKS PASSED"
