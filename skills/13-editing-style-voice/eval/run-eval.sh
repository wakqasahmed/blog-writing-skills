#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures/held-out-scenarios.json"

echo "Running contract check..."
python3 "$SCRIPT_DIR/contract_check.py"

echo "Running fixtures structural check..."
python3 "$SCRIPT_DIR/../../../scripts/validate-fixtures.py" "$FIXTURES"

echo "All eval checks passed."
