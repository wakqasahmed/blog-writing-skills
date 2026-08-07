#!/usr/bin/env python3
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill_text = (root / "SKILL.md").read_text()
fixtures = json.loads((root / "eval" / "fixtures" / "held-out-scenarios.json").read_text())

errors = []

required_headers = [
    "## 1. Narrative-transportation applicability gate",
    "## 2. Customer-as-hero framing gate",
    "## 3. Case-study structure and verifiable-specifics gate",
    "## 4. Scope limit",
]
for header in required_headers:
    if header not in skill_text:
        errors.append(f"missing required section header: {header}")

required_phrases = [
    "../00-blog-writing-guardrails/SKILL.md",
    "does not substitute for the accuracy gate",
    "do not invent a plausible substitute",
    "explicit approval",
    "reasonable, pre-existing substantiation",
    "[NLM-NARRTRANSPORT-01]",
]
for phrase in required_phrases:
    if phrase not in skill_text:
        errors.append(f"missing required non-negotiable phrase: {phrase!r}")

if not (root.parent / "00-blog-writing-guardrails" / "SKILL.md").is_file():
    errors.append("dependency skill 00-blog-writing-guardrails/SKILL.md not found")

should_follow = [f for f in fixtures if f.get("expected") == "follow"]
would_violate = [f for f in fixtures if f.get("expected") == "violates"]
if len(should_follow) < 5:
    errors.append(f"expected at least 5 should_follow fixtures, found {len(should_follow)}")
if len(would_violate) < 5:
    errors.append(f"expected at least 5 would_violate fixtures, found {len(would_violate)}")

gate_names = {h.split(". ", 1)[1] for h in required_headers}
for fixture in fixtures:
    key = "expected_gate" if fixture.get("expected") == "follow" else "violates_gate"
    gate = fixture.get(key)
    if gate not in gate_names:
        errors.append(f"fixture {fixture.get('id')} references unknown gate: {gate!r}")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)

print(f"contract check passed: {len(fixtures)} fixtures, {len(required_headers)} gate headers verified")
