#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "== Running contract check =="
python3 "$DIR/contract_check.py"

echo "== Validating fixtures structure =="
python3 "$DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo "== Eval harness passed =="
