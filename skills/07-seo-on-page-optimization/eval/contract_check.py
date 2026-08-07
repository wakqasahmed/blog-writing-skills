#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run standalone or via run-eval.sh. Exits 0 if every gate header and phrase
is present verbatim in SKILL.md, exits 1 and prints what's missing otherwise.
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parent.parent / "SKILL.md"

GATES = {
    "## 1. Title tag gate": [
        "unique to the page",
        "Do not repeat the same word or phrase multiple times in the title",
        "own `<h1>`",
    ],
    "## 2. Meta description gate": [
        "short, unique to that one page",
        "Do not ship a generic or duplicated meta description",
    ],
    "## 3. Header hierarchy gate": [
        "strict nesting order",
        "do not skip levels",
        "purely to stuff in extra keyword phrasing",
    ],
    "## 4. URL structure gate": [
        "descriptive URL",
        "opaque ID",
        "exactly one URL",
    ],
    "## 5. Internal-linking gate": [
        "descriptive anchor text",
        '"click here"',
        'rel="nofollow"',
    ],
    "## 6. Image optimization gate": [
        "descriptive alt text",
        "purely decorative images",
        "descriptive names rather than generic camera-generated filenames",
    ],
    "## 7. Pre-publish on-page QA gate": [
        "unique to the page and not copy-pasted",
        "resolves to a live, correctly canonical URL",
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
