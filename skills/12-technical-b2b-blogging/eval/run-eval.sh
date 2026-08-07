#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "== Contract check =="
python3 "$SCRIPT_DIR/contract_check.py"

echo
echo "== Fixture structural check =="
python3 "$SCRIPT_DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo
echo "All eval checks passed."
