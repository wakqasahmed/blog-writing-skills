#!/usr/bin/env python3
import sys
from pathlib import Path

skill_dir = Path(__file__).resolve().parents[1]
skill_md = (skill_dir / "SKILL.md").read_text()

GATES = {
    "1. Originality and AI-disclosure gate": [
        "original angle, example, data point, or firsthand experience",
        "schematic rehash",
        "treated as spam",
    ],
    "2. Accuracy and claims-substantiation gate": [
        "Verify every factual claim",
        "reasonable, pre-existing basis",
        "Link claims to their source",
    ],
    "3. E-E-A-T and author-credibility gate": [
        "Attribute every post to a named author",
        "first-hand experience",
        "date-stamp material updates",
    ],
    "4. Duplicate-content and canonicalization gate": [
        "near-duplicate content already exists",
        "self-referencing canonical",
    ],
    "5. Accessibility gate": [
        "equivalent alternative text",
        "strict nesting order",
    ],
    "6. Plain-language and clarity gate": [
        "lead with what the reader needs",
        "Define or cut jargon",
    ],
    "7. Structured-data and answer-engine hygiene gate": [
        "structured data (author, `datePublished`",
        "direct, self-contained statement",
    ],
    "8. Pre-publish QA gate": [
        "every internal and external link resolves",
        "byline, publish date, canonical tag, and structured data all agree",
    ],
}

missing = []
for gate, phrases in GATES.items():
    if gate not in skill_md:
        missing.append(f"missing gate header: {gate}")
        continue
    for phrase in phrases:
        if phrase not in skill_md:
            missing.append(f"[{gate}] missing load-bearing phrase: {phrase!r}")

if missing:
    print("FAIL: 00-blog-writing-guardrails contract check found missing items:")
    for item in missing:
        print(f"  - {item}")
    sys.exit(1)

print(f"PASS: all {len(GATES)} gates and their load-bearing phrases are present.")
