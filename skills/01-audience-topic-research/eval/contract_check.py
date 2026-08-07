#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Run: python3 contract_check.py
Exits 0 if every gate header and phrase is present, 1 otherwise (with a
printed list of what is missing).
"""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = {
    "## 1. Reader-intent and ICP gate": [
        "Identify who the post is for and what task or question brings them to it",
        "different segments of the target reader describe the same need in different words",
        "State the reader's starting knowledge level and desired outcome",
    ],
    "## 2. Query-understanding and keyword-research gate": [
        "Treat a keyword list as a stand-in for real reader queries, not an exercise in stuffing exact phrases",
        "Build the keyword set from multiple primary inputs",
        "Do not select a topic on search-volume estimates alone",
    ],
    "## 3. Competitive SERP and AI-answer gap analysis gate": [
        "read the pages currently ranking or being cited for the target query",
        "Identify a concrete gap the existing top results or AI answers leave open",
        "plan a concise, self-contained answer near the top of the post under its own heading",
    ],
    "## 4. Research-to-outline handoff gate": [
        "Carry the confirmed reader, primary query, classified intent, and identified content gap into the outline stage as fixed constraints",
        "Record the keyword/topic research and its date alongside the draft",
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
            missing.append(f"HEADER: {header}")
        for phrase in phrases:
            if phrase not in text:
                missing.append(f"PHRASE (under {header}): {phrase}")

    if missing:
        print("Contract check FAILED. Missing from SKILL.md:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Contract check PASSED: all gate headers and load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
