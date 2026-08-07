#!/usr/bin/env python3
"""Send a skill's held-out scenarios to an LLM and check its classifications.

Usage: python3 scripts/run-behavioral-eval.py <skill-dir>
"""
import json
import os
import re
import sys
import urllib.request

CODE_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def call_model(prompt: str, url: str, model: str, token: str) -> str:
    body = json.dumps(
        {
            "model": model,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You classify whether a scenario follows or violates a skill's "
                        "written guidance. Respond with strict JSON only, no prose, no "
                        "markdown code fences: "
                        '{"classification": "follow" or "violates", "gate": "<gate name or null>"}. '
                        "Set gate to the name of the violated gate when classification is "
                        "'violates', otherwise null."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }
    )
    req = urllib.request.Request(
        f"{url.rstrip('/')}/chat/completions",
        data=body.encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return payload["choices"][0]["message"]["content"]


def parse_response(raw: str):
    cleaned = CODE_FENCE_RE.sub("", raw.strip()).strip()
    parsed = json.loads(cleaned)
    return parsed["classification"], parsed.get("gate")


def gate_matches(actual_gate, expected_gate) -> bool:
    if not actual_gate or not expected_gate:
        return False
    actual = str(actual_gate).lower()
    expected = str(expected_gate).lower()
    return actual in expected or expected in actual


def evaluate_fixture(fixture: dict, skill_md: str, url: str, model: str, token: str):
    """Returns (passed: bool, message: str)."""
    prompt = (
        f"Skill guidance (SKILL.md):\n---\n{skill_md}\n---\n\n"
        f"Scenario:\n{fixture['scenario']}\n\n"
        "Does this scenario follow or violate the skill's guidance?"
    )

    try:
        raw = call_model(prompt, url, model, token)
    except Exception as exc:
        return False, f"FAIL {fixture['id']}: model call errored: {exc}"

    try:
        classification, gate = parse_response(raw)
    except Exception as exc:
        return False, f"FAIL {fixture['id']}: could not parse model response as JSON ({exc}): {raw!r}"

    expected = fixture["expected"]
    if classification != expected:
        return False, f"FAIL {fixture['id']}: expected classification {expected!r}, got {classification!r}"

    warning = ""
    if expected == "violates":
        expected_gate = fixture.get("violates_gate")
        if expected_gate and not gate_matches(gate, expected_gate):
            warning = f" (warning: gate {gate!r} does not match expected {expected_gate!r})"

    return True, f"PASS {fixture['id']}: classification={classification}{warning}"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: run-behavioral-eval.py <skill-dir>")
        return 1

    skill_dir = sys.argv[1]
    url = os.environ.get("OCR_LLM_URL", "")
    model = os.environ.get("OCR_LLM_MODEL", "")
    token = os.environ.get("OCR_LLM_AUTH_TOKEN", "")

    if not token:
        print("SKIP: no LLM credentials available, behavioral eval not run")
        return 0

    with open(os.path.join(skill_dir, "SKILL.md"), encoding="utf-8") as f:
        skill_md = f.read()

    fixtures_path = os.path.join(skill_dir, "eval", "fixtures", "held-out-scenarios.json")
    with open(fixtures_path, encoding="utf-8") as f:
        fixtures = json.load(f)

    correct = 0
    total = len(fixtures)
    for fixture in fixtures:
        passed, message = evaluate_fixture(fixture, skill_md, url, model, token)
        print(message)
        if passed:
            correct += 1

    print(f"{correct}/{total} classifications correct")
    return 0 if correct == total else 1


if __name__ == "__main__":
    sys.exit(main())
