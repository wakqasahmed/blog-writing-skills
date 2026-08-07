#!/usr/bin/env bash
set -euo pipefail

eval_dir="$(cd "$(dirname "$0")" && pwd)"

python3 "$eval_dir/contract_check.py"

python3 "$eval_dir/../../../scripts/validate-fixtures.py" "$eval_dir/fixtures/held-out-scenarios.json"

echo "00-blog-writing-guardrails eval: ALL CHECKS PASSED"
