#!/usr/bin/env python3
"""Contract check for skills/13-editing-style-voice/SKILL.md.

Asserts the skill file still contains its gate headers and the load-bearing
phrases each gate's guidance depends on. Exits 0 if everything is present,
exits 1 and prints what's missing otherwise.
"""

import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Plain-language self-edit gate",
        "phrases": [
            "Write for the reader's task, not the writer's expertise",
            "Define or cut jargon a general reader",
        ],
    },
    {
        "header": "## 2. Cutting filler, hedging, and wordiness gate",
        "phrases": [
            "Interrogate every word in a sentence",
            'Cut hedging qualifiers ("somewhat," "fairly," "it seems," "in some cases")',
            "nominalizations (verbs turned into nouns",
        ],
    },
    {
        "header": "## 3. Active-voice preference gate",
        "phrases": [
            "Default to active voice",
            "Reserve passive voice for cases where the agent performing the action is genuinely obvious, unimportant, or unknown",
        ],
    },
    {
        "header": "## 4. Consistent voice gate",
        "phrases": [
            "Keep person (first, second, or third), tense, and level of formality consistent",
            "Keep terminology consistent for the same concept throughout a post",
        ],
    },
    {
        "header": "## 5. Removing AI-tell phrasing gate",
        "phrases": [
            'Cut generic transitional filler that adds no reader value ("in conclusion," "it is important to note," "delve into,"',
            "Replace vague, inflated phrasing with specific, concrete claims and numbers",
        ],
    },
    {
        "header": "## 6. Pre-publish editing checklist",
        "phrases": [
            "Read the draft aloud (or have it read aloud) once for flow",
            "Confirm every paragraph passes the filler, hedging, active-voice, consistent-voice, and AI-tell checks above",
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
            missing.append(f"header not found: {gate['header']}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(f"phrase not found (gate {gate['header']!r}): {phrase}")

    if missing:
        print("Contract check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Contract check PASSED: all gate headers and load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
