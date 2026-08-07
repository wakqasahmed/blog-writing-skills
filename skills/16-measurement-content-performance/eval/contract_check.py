#!/usr/bin/env python3
"""Contract check for 16-measurement-content-performance/SKILL.md.

Asserts the skill file still contains each required gate header and its
load-bearing phrases. Exits 0 if all present, 1 with a printed list of
what's missing otherwise.
"""

import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parent.parent / "SKILL.md"

GATES = [
    {
        "header": "## 1. KPI-to-funnel-stage gate",
        "phrases": [
            "do not report a discovery-stage metric",
            "compare a page's CTR only against pages holding a similar ranking position",
            "Report engagement metrics (time-on-page, scroll depth) and conversion metrics (email signups, product clicks) as a separate KPI layer from traffic metrics",
        ],
    },
    {
        "header": "## 2. Content-decay detection and refresh-cadence gate",
        "phrases": [
            "sustained decline (not a single-week dip)",
            "do not change only the datestamp without a substantive content change",
            "Re-verify every statistic and claim carried into a refreshed post against its current primary source",
        ],
    },
    {
        "header": "## 3. Valid headline/CTA A/B-testing gate",
        "phrases": [
            "do not stop the test the first time the observed difference crosses significance",
            "Test only one variable at a time (headline alone, or CTA copy alone) per experiment arm",
            "Report a winning variant only once the test reaches its pre-committed stopping rule",
        ],
    },
    {
        "header": "## 4. Reporting-integrity gate",
        "phrases": [
            'unless the underlying test met its pre-committed stopping rule and the claim can be substantiated on request',
            "Carry forward the byline, publish date, and last-reviewed date changes from any content refresh",
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
            missing.append(f"HEADER MISSING: {gate['header']}")
        for phrase in gate["phrases"]:
            if phrase not in text:
                missing.append(f"PHRASE MISSING under '{gate['header']}': {phrase}")

    if missing:
        print("Contract check FAILED. Missing items:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"Contract check PASSED: all {len(GATES)} gate headers and phrases present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
