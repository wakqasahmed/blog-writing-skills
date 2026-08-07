#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run: python3 skills/03-structure-scannability/eval/contract_check.py
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Inverted-pyramid gate",
        "phrases": [
            "core answer, conclusion, or most important point in the first two paragraphs",
            "do not make the reader scroll past setup to reach the point",
            "Order the remaining sections from most to least important",
        ],
    },
    {
        "header": "## 2. Heading and layer-cake structure gate",
        "phrases": [
            "visually distinct, descriptive subheading that leads with its most important words",
            "do not use bold paragraph text as a substitute for a real heading",
            "Break each section into short paragraphs or lists rather than dense blocks of text",
        ],
    },
    {
        "header": "## 3. TL;DR and summary-box gate",
        "phrases": [
            "short, self-contained direct-answer statement near the top",
            "not a teaser that withholds the answer to keep the reader scrolling",
        ],
    },
    {
        "header": "## 4. Bold, list, and table gate",
        "phrases": [
            "Bold the specific key phrase or number a scanning reader needs",
            "over-bolding defeats the purpose of drawing the eye",
            "use a table when comparing the same attributes across three or more items",
        ],
    },
    {
        "header": "## 5. Pre-publish scannability check",
        "phrases": [
            "Read only the headings, the TL;DR, and any bolded phrases in the draft",
            "restructure before publishing rather than adding more prose",
        ],
    },
]


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"MISSING FILE: {SKILL_PATH}")
        return 1

    text = SKILL_PATH.read_text(encoding="utf-8")
    missing = []

    for gate in GATES:
        if gate["header"] not in text:
            missing.append(f"header not found: {gate['header']!r}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(
                    f"phrase not found for {gate['header']!r}: {phrase!r}"
                )

    if missing:
        print("contract_check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"contract_check PASSED: all {len(GATES)} gates and their load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
