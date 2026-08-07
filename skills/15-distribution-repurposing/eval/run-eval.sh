#!/usr/bin/env bash
set -euo pipefail

EVAL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$EVAL_DIR/fixtures/held-out-scenarios.json"

echo "== Running contract check =="
python3 "$EVAL_DIR/contract_check.py"

echo
echo "== Validating fixtures structure =="
python3 "$EVAL_DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo
echo "All eval checks passed."
