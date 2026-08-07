#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run standalone or via run-eval.sh. Exits 0 if every gate header and phrase
is present verbatim in SKILL.md, exits 1 and prints what's missing otherwise.
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parent.parent / "SKILL.md"

GATES = {
    "## 1. Code-sample verification gate": [
        "Run every code sample against the real tool, library, or API before publishing",
        "passing test or an equivalent verification run",
        "the shown output was actually produced by running the sample",
    ],
    "## 2. Version-pinning gate": [
        "State the specific tool, library, framework, or API version",
        '"new," "currently," "latest," or "now supports"',
        "Note the date the post's compatibility claims were last verified",
    ],
    "## 3. Multi-stakeholder B2B buying-committee gate": [
        "a B2B technical purchase is decided by a multi-person buying group",
        "the technical evaluator",
        "the economic buyer",
        "Do not assume one stakeholder will relay the full technical argument",
    ],
    "## 4. Vendor-superiority substantiation gate": [
        "a reasonable, pre-existing basis the author can produce on request",
        "versions compared, hardware/environment, date run",
        "Do not restate a competitor's own marketing claim about itself as a bare fact",
    ],
    "## 5. Pre-publish QA gate": [
        "every code sample was executed against the stated tool/library version",
        "every superiority claim has a documented basis",
    ],
}


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"MISSING FILE: {SKILL_PATH}")
        return 1

    content = SKILL_PATH.read_text(encoding="utf-8")
    missing = []

    for header, phrases in GATES.items():
        if header not in content:
            missing.append(f"header: {header}")
        for phrase in phrases:
            if phrase not in content:
                missing.append(f"phrase (under {header}): {phrase}")

    if missing:
        print("Contract check FAILED. Missing:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Contract check PASSED: {len(GATES)} gates, all phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
