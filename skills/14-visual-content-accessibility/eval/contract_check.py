#!/usr/bin/env python3
"""Asserts SKILL.md still contains its gate headers and load-bearing phrases.

Run directly: python3 contract_check.py
Exits 0 if every header and phrase is present, exits 1 and prints what's
missing otherwise. This guards against silent edits that gut a gate while
leaving the section heading in place, or that remove a heading entirely.
"""
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Does the visual earn its place?",
        "phrases": [
            "conveys meaning the surrounding text cannot as efficiently",
            "do not add stock imagery purely for visual break-up",
            "also state that information in the surrounding text or a caption",
        ],
    },
    {
        "header": "## 2. Alt text quality gate (not just presence)",
        "phrases": [
            "informative (the image conveys a message",
            "decorative (the image adds no information",
            "functional (the image is inside a link or button",
            "never leave the underlying data reachable only through the image",
        ],
    },
    {
        "header": "## 3. Color and contrast gate",
        "phrases": [
            "contrast ratio of at least 4.5:1 against its background",
            "contrast ratio of at least 3:1 against adjacent colors",
            "Do not use color as the only way to distinguish data series",
        ],
    },
    {
        "header": "## 4. Embedded video and audio gate",
        "phrases": [
            "Provide a synchronized text caption for every prerecorded video",
            "Provide a transcript for every embedded audio-only or video piece",
            "provide audio description",
        ],
    },
    {
        "header": "## 5. Pre-publish checklist for this skill",
        "phrases": [
            "or is explicitly marked decorative",
            "No information is conveyed by color alone",
            "video with unnarrated meaningful visuals has audio description",
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
            missing.append(f"header: {gate['header']}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(f"phrase (under '{gate['header']}'): {phrase!r}")

    if missing:
        print("Contract check FAILED. Missing from SKILL.md:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Contract check passed: all {len(GATES)} gate headers and phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
