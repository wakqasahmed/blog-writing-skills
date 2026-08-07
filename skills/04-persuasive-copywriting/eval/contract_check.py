#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run: python3 skills/04-persuasive-copywriting/eval/contract_check.py
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Rhetorical-foundations gate (ethos, pathos, logos)",
        "phrases": [
            "the writer's or organization's demonstrated character and credibility (ethos)",
            "Establish ethos before leaning on pathos",
            "Do not substitute pathos for logos",
        ],
    },
    {
        "header": "## 2. Influence-principles gate (Cialdini)",
        "phrases": [
            "the underlying fact must be real and verifiable, not staged",
            "Do not fabricate or imply a false countdown, false limited stock, or false authority",
            "not as a replacement for it",
        ],
    },
    {
        "header": "## 3. Framing and loss-aversion gate",
        "phrases": [
            "the framing must describe a real outcome the reader actually faces, not an invented cost",
            "loss-framed copy",
            "Do not exploit loss aversion to manufacture urgency around a loss the reader was never actually going to incur",
        ],
    },
    {
        "header": "## 4. Objection-handling gate",
        "phrases": [
            "Name the reader's most likely objection to the offer or claim in the reader's own words",
            "not a restated assertion of confidence",
            "rather than treating persuasive copy as exempt from that gate",
        ],
    },
    {
        "header": "## 5. CTA-design gate",
        "phrases": [
            "State the single action the reader should take next in plain, specific language",
            "rather than a generic urgency phrase with nothing real behind it",
            "Give every CTA that is an image or icon equivalent alternative text",
        ],
    },
    {
        "header": "## 6. Pre-publish persuasion QA gate",
        "phrases": [
            "points back to a fact the writer can substantiate on request",
            "at least one real objection has been named and answered with evidence",
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
