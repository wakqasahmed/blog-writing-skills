#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run: python3 skills/15-distribution-repurposing/eval/contract_check.py
"""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = {
    "## 1. Internal-linking cluster-strategy gate": [
        "one comprehensive pillar page",
        "at least one crawlable internal link from another page on the site",
        "descriptive, reasonably concise, and relevant",
    ],
    "## 2. Cross-channel repurposing gate": [
        "is not a duplicate-content risk under Google's indexing rules",
        "apply the guardrails' duplicate-content and canonicalization gate to that page",
        "does not exempt it from the accuracy gate",
    ],
    "## 3. Syndication canonicalization gate": [
        'mark every non-canonical copy with a `rel="canonical"` link',
        "Keep the original, canonical URL self-referencing",
        "request a direct link back to the original URL",
    ],
    "## 4. Pre-distribution QA gate": [
        "Verify every new or updated internal link resolves",
        "Confirm the canonical tag on every syndicated or cross-posted copy",
    ],
}


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"MISSING FILE: {SKILL_PATH}")
        return 1

    text = SKILL_PATH.read_text(encoding="utf-8")
    missing = []

    for header, phrases in GATES.items():
        if header not in text:
            missing.append(f"header not found: {header!r}")
            continue
        for phrase in phrases:
            if phrase not in text:
                missing.append(f"phrase missing under {header!r}: {phrase!r}")

    if missing:
        print("Contract check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Contract check PASSED: all gate headers and load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
