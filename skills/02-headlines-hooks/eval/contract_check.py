#!/usr/bin/env python3
"""Assert that skills/02-headlines-hooks/SKILL.md still contains its gate
headers and the load-bearing phrases each gate depends on.

Run directly or via run-eval.sh. Exits 0 if everything required is present,
exits 1 and prints exactly what's missing otherwise.
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Title-length gate",
        "phrases": [
            "between roughly 40 and 60 characters",
            "front-load the words that carry the meaning",
        ],
    },
    {
        "header": "## 2. Sentiment and honesty gate",
        "phrases": [
            "Do not force positive framing onto content that is genuinely a warning, failure, or critique",
            "Never publish a headline whose implied claim",
        ],
    },
    {
        "header": "## 3. Question-headline gate",
        "phrases": [
            "Do not default to a question-format headline as a CTR tactic",
            "answer it in the opening paragraph rather than deferring the answer to build suspense",
        ],
    },
    {
        "header": "## 4. Scan-first structure gate",
        "phrases": [
            "the headline and the first two paragraphs are the only text most visitors will read",
            "do not bury the point under throat-clearing, anecdotes, or scene-setting",
        ],
    },
    {
        "header": "## 5. Hook-substance gate",
        "phrases": [
            "rather than a generic curiosity tease with no informational content",
            "a headline promising a unique insight must be backed by content that actually delivers one",
        ],
    },
    {
        "header": "## 6. Test-before-you-trust-your-instinct gate",
        "phrases": [
            "test more than one headline variant against real readers before finalizing",
            "apply the length, sentiment, and question gates above as the default heuristic",
        ],
    },
    {
        "header": "## 7. Pre-publish QA gate",
        "phrases": [
            "Confirm the final title is between 40 and 60 characters",
            "would still make sense as a standalone extract, independent of the headline",
        ],
    },
]


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"FAIL: SKILL.md not found at {SKILL_PATH}")
        return 1

    text = SKILL_PATH.read_text(encoding="utf-8")
    missing = []

    for gate in GATES:
        if gate["header"] not in text:
            missing.append(f"header missing: {gate['header']}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(f"phrase missing under {gate['header']!r}: {phrase!r}")

    if missing:
        print("Contract check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Contract check PASSED: all {len(GATES)} gate headers and phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
