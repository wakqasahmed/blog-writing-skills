#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$DIR/fixtures/held-out-scenarios.json"

echo "== Contract check =="
python3 "$DIR/contract_check.py"

echo "== Fixture structural check =="
python3 "$DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo "== All eval checks passed =="
