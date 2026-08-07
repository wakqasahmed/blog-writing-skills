#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases."""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parent.parent / "SKILL.md"

GATES = {
    "1. Direct-answer gate": [
        "typically 40-60 words",
        "no markup or declaration that forces a page to become a featured snippet",
        "a passage that requires reading prior paragraphs to make sense is a worse extraction candidate",
    ],
    "2. Question-based header gate": [
        "so the heading itself functions as the query match",
        "a bolded question in body text is not a substitute for a real heading",
        "Group related questions a reader is likely to ask next under their own headings",
    ],
    "3. FAQPage schema deprecation gate": [
        "stopped appearing in Google Search as of May 7, 2026",
        "restricted FAQ rich results to well-known, authoritative government and health sites",
        "do not write new FAQ sections on the assumption that adding the schema will win a rich result",
    ],
    "4. QAPage schema boundary gate": [
        "excludes site-authored content with only one answer per question and no user-submission mechanism",
        "Reserve `QAPage` for genuine forum- or support-style pages",
    ],
    "5. Evidence-maturity caveat": [
        "actively developing, heterogeneous evidence base rather than settled, guaranteed-outcome techniques",
        "independent surveys of this literature report inconsistent methodologies and effect sizes",
        "Validate any such tactic against the target answer engine's own current documentation",
    ],
    "6. Pre-publish AEO check": [
        "stands alone as a complete answer if read with no other context on the page",
        "Confirm no `FAQPage` markup was added on the assumption of a rich-result payoff",
    ],
}


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"MISSING FILE: {SKILL_PATH}")
        return 1

    content = SKILL_PATH.read_text(encoding="utf-8")
    missing = []

    for gate, phrases in GATES.items():
        if gate not in content:
            missing.append(f"gate header: {gate}")
        for phrase in phrases:
            if phrase not in content:
                missing.append(f"phrase for '{gate}': {phrase}")

    if missing:
        print("Contract check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Contract check PASSED: all gate headers and load-bearing phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
