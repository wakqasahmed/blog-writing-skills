#!/usr/bin/env python3
"""Shared held-out-scenarios.json shape validator, used by every skill's run-eval.sh."""
import json
import sys

REQUIRED_FIELDS = ("id", "scenario", "expected")
ALLOWED_FIELDS = {
    "id",
    "scenario",
    "expected",
    "violates_gate",
    "reasoning",
    "expected_gate",
    "expected_guidance",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate-fixtures.py <path-to-held-out-scenarios.json>")
        return 1

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    if not isinstance(data, list) or len(data) < 10:
        print(f"FAIL: fixtures must be a JSON array with >=10 entries, got {len(data) if isinstance(data, list) else 'non-list'}")
        return 1

    for d in data:
        if not isinstance(d, dict):
            print(f"FAIL: entry is not a JSON object: {d!r}")
            return 1

    follow = [d for d in data if d.get("expected") == "follow"]
    violates = [d for d in data if d.get("expected") == "violates"]

    if len(follow) < 5:
        print(f"FAIL: need >=5 'follow' entries, got {len(follow)}")
        return 1
    if len(violates) < 5:
        print(f"FAIL: need >=5 'violates' entries, got {len(violates)}")
        return 1

    for d in data:
        for field in REQUIRED_FIELDS:
            if field not in d:
                print(f"FAIL: entry missing required field {field!r}: {d}")
                return 1
        if d["expected"] == "violates" and "violates_gate" not in d:
            print(f"FAIL: violates entry missing 'violates_gate': {d}")
            return 1
        unexpected = set(d.keys()) - ALLOWED_FIELDS
        if unexpected:
            print(f"FAIL: entry has unexpected field(s) {sorted(unexpected)!r}: {d}")
            return 1

    print(f"PASS: {len(data)} fixtures ({len(follow)} follow, {len(violates)} violates)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
