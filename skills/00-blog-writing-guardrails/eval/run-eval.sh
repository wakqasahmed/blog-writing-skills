#!/usr/bin/env bash
set -euo pipefail

eval_dir="$(cd "$(dirname "$0")" && pwd)"

python3 "$eval_dir/contract_check.py"

python3 - "$eval_dir/fixtures/held-out-scenarios.json" <<'PY'
import json
import sys

path = sys.argv[1]
data = json.loads(open(path).read())

if not isinstance(data, list) or len(data) < 10:
    print(f"FAIL: fixtures must be a JSON array with >=10 entries, got {len(data) if isinstance(data, list) else 'non-list'}")
    sys.exit(1)

follow = [d for d in data if d.get("expected") == "follow"]
violates = [d for d in data if d.get("expected") == "violates"]

if len(follow) < 5:
    print(f"FAIL: need >=5 'follow' entries, got {len(follow)}")
    sys.exit(1)
if len(violates) < 5:
    print(f"FAIL: need >=5 'violates' entries, got {len(violates)}")
    sys.exit(1)

for d in data:
    for field in ("id", "scenario", "expected"):
        if field not in d:
            print(f"FAIL: entry missing required field {field!r}: {d}")
            sys.exit(1)
    if d["expected"] == "violates" and "violates_gate" not in d:
        print(f"FAIL: violates entry missing 'violates_gate': {d}")
        sys.exit(1)

print(f"PASS: {len(data)} fixtures ({len(follow)} follow, {len(violates)} violates)")
PY

echo "00-blog-writing-guardrails eval: ALL CHECKS PASSED"
