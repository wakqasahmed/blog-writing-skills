#!/usr/bin/env python3
import json
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "held-out-scenarios.json"

REQUIRED_HEADERS = [
    "## 0. Evidence-quality caveat",
    "## 1. Passage self-containment gate",
    "## 2. Statistic and citation density gate",
    "## 3. Structured, quotable claims gate",
    "## 4. Answer-engine traffic-impact disclosure gate",
    "## 5. Pre-publish GEO QA gate",
]

REQUIRED_PHRASES = [
    "../00-blog-writing-guardrails/SKILL.md",
    "heterogeneous",
    "generalize poorly",
    "not a guaranteed",
    "[ARXIV-GEOSURVEY-01]",
    "[ARXIV-GEOCITE-01]",
    "[AHREFS-AIOCTR-01]",
]

REQUIRED_SOURCE_IDS = {
    "ARXIV-GEOSURVEY-01",
    "ARXIV-GEOCITE-01",
    "AHREFS-AIOCTR-01",
}


def fail(errors: list[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    errors = []

    if not SKILL_MD.is_file():
        fail([f"missing {SKILL_MD}"])

    text = SKILL_MD.read_text()

    for header in REQUIRED_HEADERS:
        if header not in text:
            errors.append(f"SKILL.md missing required gate header: {header!r}")

    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            errors.append(f"SKILL.md missing required phrase: {phrase!r}")

    for source_id in REQUIRED_SOURCE_IDS:
        if f"[{source_id}]" not in text:
            errors.append(f"SKILL.md never cites required source [{source_id}]")

    if not FIXTURES.is_file():
        errors.append(f"missing {FIXTURES}")
    else:
        scenarios = json.loads(FIXTURES.read_text())
        if not isinstance(scenarios, list) or not scenarios:
            errors.append("fixtures file must be a non-empty JSON array")
        else:
            should_follow = [s for s in scenarios if s.get("expected") == "follow"]
            would_violate = [s for s in scenarios if s.get("expected") == "violates"]
            if len(should_follow) < 5:
                errors.append(f"expected >=5 should_follow scenarios, found {len(should_follow)}")
            if len(would_violate) < 5:
                errors.append(f"expected >=5 would_violate scenarios, found {len(would_violate)}")
            required_keys = {"id", "expected", "scenario", "expected_guidance"}
            for scenario in scenarios:
                missing_keys = required_keys - scenario.keys()
                if missing_keys:
                    errors.append(f"scenario {scenario.get('id', '?')} missing keys: {sorted(missing_keys)}")
                if scenario.get("expected") == "violates" and "violates_gate" not in scenario:
                    errors.append(f"scenario {scenario.get('id', '?')} missing 'violates_gate'")

    if errors:
        fail(errors)

    print(f"contract check passed: {len(REQUIRED_HEADERS)} gate headers, "
          f"{len(REQUIRED_PHRASES)} required phrases, fixtures validated")


if __name__ == "__main__":
    main()
