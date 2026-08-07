#!/usr/bin/env python3
"""Contract check for skills/10-eeat-credibility-signals/SKILL.md.

Asserts the skill file still contains each gate header and the load-bearing
phrases that make that gate enforceable. Exits 0 if all present, exits 1
with a printed list of what is missing otherwise.
"""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Author bio and credentials",
        "phrases": [
            "visible author bio",
            "author` structured data pointing to a `Person`",
            "About us",
        ],
    },
    {
        "header": "## 2. Disclosing methodology and first-hand experience",
        "phrases": [
            "state how it was done",
            "first-hand experience",
            "Disclose any conflict of interest",
        ],
    },
    {
        "header": "## 3. Linking to primary sources",
        "phrases": [
            "Link every statistic, quote, or factual claim to the primary source",
            "close enough to the claim that a reader or an AI system can verify it",
        ],
    },
    {
        "header": "## 4. Original-data callouts",
        "phrases": [
            "call it out explicitly as original",
            "at least one original data point",
        ],
    },
    {
        "header": "## 5. Trust signals: last-updated dates and correction policy",
        "phrases": [
            "last updated",
            "Maintain a corrections policy and follow it",
            "correct it quickly, clearly, and prominently",
        ],
    },
    {
        "header": "## 6. Pre-publish checklist",
        "phrases": [
            "Author bio present, accurate, and linked to a profile/About page",
            "Every claim traces to a primary source link",
            "a corrections path exists for future errors",
        ],
    },
]


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"MISSING FILE: {SKILL_PATH}")
        return 1

    text = SKILL_PATH.read_text()
    missing = []

    for gate in GATES:
        if gate["header"] not in text:
            missing.append(f"header: {gate['header']}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(f"phrase (under {gate['header']}): {phrase}")

    if missing:
        print("Contract check FAILED. Missing:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Contract check passed: all gate headers and load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
