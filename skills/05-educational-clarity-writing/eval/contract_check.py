#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases.

Fails loudly (exit 1, printed list of what's missing) if a future edit
silently drops or waters down a gate. Run via run-eval.sh or CI.
"""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parents[1] / "SKILL.md"

GATES = [
    {
        "header": "## 1. Plain-language foundation",
        "phrases": [
            "Organize the explanation around the reader's task",
            "define it the first time it appears",
            "simplify wording, not the substance of the claim",
        ],
    },
    {
        "header": "## 2. Readability-formula mechanics and limits",
        "phrases": [
            "treat a grade-level score as an approximation of decoding difficulty, not a certificate of comprehension",
            "do not treat a target score (e.g. \"grade 8\") as sufficient proof a specific audience will understand the post",
            "re-verify long or restructured sentences by reading them aloud, not by chasing a numeric target alone",
        ],
    },
    {
        "header": "## 3. Cognitive load gate",
        "phrases": [
            "learning fails even though every individual fact was stated correctly",
            "do not force the reader to hold an undefined term, an unresolved forward reference, or a separated diagram-and-caption pair in memory",
            "adding one new element at a time rather than introducing several interdependent concepts in the same paragraph",
        ],
    },
    {
        "header": "## 4. Worked examples and analogies",
        "phrases": [
            "Prefer showing a fully worked example of a procedure over stating the abstract rule alone",
            "state explicitly where the analogy holds and where it breaks down",
            "Pair each worked example with a smaller, near-transfer practice case",
        ],
    },
    {
        "header": "## 5. Pre-publish clarity QA",
        "phrases": [
            "Confirm a first-time reader in the target audience can restate the core concept in their own words",
            "if a technical reviewer is the only person who can do this, the draft is not yet reader-ready",
            "every analogy's stated limits still appear in the published draft",
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
                missing.append(f"phrase (under {gate['header']}): {phrase!r}")

    if missing:
        print("Contract check FAILED. Missing from SKILL.md:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Contract check passed: {len(GATES)} gates, all headers and phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
