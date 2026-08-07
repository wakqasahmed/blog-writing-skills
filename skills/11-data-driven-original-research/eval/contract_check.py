#!/usr/bin/env python3
"""Assert SKILL.md still contains its gate headers and load-bearing phrases."""
import pathlib
import sys

SKILL_PATH = pathlib.Path(__file__).resolve().parent.parent / "SKILL.md"

GATES = {
    "1. Methodology-transparency gate": [
        "the survey mode, the population studied, how the sample was recruited or selected, and the exact question wording",
        "do not present a non-probability sample's results with the same confidence language used for a probability sample",
        "not only the headline number",
    ],
    "2. Sample-size and margin-of-error disclosure gate": [
        "a subgroup number with an unstated (and likely small) base is not publication-ready",
        "disclose the estimated margin of sampling error alongside the headline statistic",
        "describe the model that produced it rather than presenting it as a standard margin of error",
    ],
    "3. Anti-p-hacking and anti-cherry-picking gate": [
        "do not report only the one cut that reached significance while silently dropping the others",
        "revise the thesis rather than the presented slice of data",
    ],
    "4. Correlation-versus-causation gate": [
        "Label an association found in observational or correlational data as a correlation, not a cause",
        "do not let a headline, chart title, or pull quote imply causation that the body copy does not substantiate",
    ],
    "5. Honest chart-design gate": [
        "do not choose a truncated, non-zero, or otherwise distorting axis, scale, or visual proportion",
        "the chart's visual proportions must match the substantiated claim behind it",
    ],
    "6. Pre-publish QA addendum": [
        "confirm the post discloses sample size, margin of error (or its non-probability equivalent), survey mode, and question wording",
        "every chart's axis and scale were reviewed for distortion",
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
