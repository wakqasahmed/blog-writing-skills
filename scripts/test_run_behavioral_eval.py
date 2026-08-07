#!/usr/bin/env python3
"""Unit tests for run-behavioral-eval.py. No network access, no credentials."""
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT_PATH = Path(__file__).resolve().parent / "run-behavioral-eval.py"
spec = importlib.util.spec_from_file_location("run_behavioral_eval", SCRIPT_PATH)
run_behavioral_eval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run_behavioral_eval)


def _fixture(id_, expected, gate=None, scenario="scenario text"):
    entry = {"id": id_, "scenario": scenario, "expected": expected}
    if gate is not None:
        entry["violates_gate"] = gate
    return entry


class EvaluateFixtureTests(unittest.TestCase):
    def _run(self, fixture, canned_response):
        with mock.patch.object(run_behavioral_eval, "call_model", return_value=canned_response):
            return run_behavioral_eval.evaluate_fixture(
                fixture, "SKILL.md contents", "http://fake", "fake-model", "fake-token"
            )

    def test_correct_follow_classification(self):
        fixture = _fixture("f-01", "follow")
        passed, message = self._run(fixture, '{"classification": "follow", "gate": null}')
        self.assertTrue(passed)
        self.assertIn("PASS", message)

    def test_correct_violates_classification_matching_gate(self):
        fixture = _fixture("v-01", "violates", gate="Case-study structure gate")
        passed, message = self._run(
            fixture, '{"classification": "violates", "gate": "Case-study structure gate"}'
        )
        self.assertTrue(passed)
        self.assertIn("PASS", message)
        self.assertNotIn("warning", message)

    def test_correct_violates_classification_differently_worded_gate(self):
        fixture = _fixture("v-02", "violates", gate="Case-study structure and verifiable-specifics gate")
        passed, message = self._run(
            fixture, '{"classification": "violates", "gate": "verifiable specifics"}'
        )
        self.assertTrue(passed, "lenient gate matching should still pass classification")

    def test_wrong_classification_fails(self):
        fixture = _fixture("f-02", "follow")
        passed, message = self._run(fixture, '{"classification": "violates", "gate": "some gate"}')
        self.assertFalse(passed)
        self.assertIn("FAIL", message)

    def test_malformed_json_response_is_failure_not_crash(self):
        fixture = _fixture("f-03", "follow")
        passed, message = self._run(fixture, "not valid json at all")
        self.assertFalse(passed)
        self.assertIn("FAIL", message)

    def test_code_fenced_json_response_is_parsed(self):
        fixture = _fixture("f-04", "follow")
        passed, message = self._run(
            fixture, '```json\n{"classification": "follow", "gate": null}\n```'
        )
        self.assertTrue(passed)

    def test_model_call_exception_is_failure_not_crash(self):
        fixture = _fixture("f-05", "follow")
        with mock.patch.object(run_behavioral_eval, "call_model", side_effect=RuntimeError("boom")):
            passed, message = run_behavioral_eval.evaluate_fixture(
                fixture, "SKILL.md contents", "http://fake", "fake-model", "fake-token"
            )
        self.assertFalse(passed)
        self.assertIn("FAIL", message)


class GateMatchesTests(unittest.TestCase):
    def test_substring_either_direction_matches(self):
        self.assertTrue(run_behavioral_eval.gate_matches("verifiable specifics gate", "Case-study structure and verifiable specifics gate".lower()))
        self.assertTrue(run_behavioral_eval.gate_matches("Case-study structure gate", "structure"))

    def test_no_match(self):
        self.assertFalse(run_behavioral_eval.gate_matches("unrelated gate", "self-containment"))

    def test_none_values_do_not_match(self):
        self.assertFalse(run_behavioral_eval.gate_matches(None, "self-containment"))
        self.assertFalse(run_behavioral_eval.gate_matches("some gate", None))


class MainSkipTests(unittest.TestCase):
    def test_main_skips_without_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "eval" / "fixtures").mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("guidance")
            (skill_dir / "eval" / "fixtures" / "held-out-scenarios.json").write_text("[]")

            env = dict(os.environ)
            env.pop("OCR_LLM_AUTH_TOKEN", None)
            sys_argv_backup = sys.argv
            with mock.patch.dict(os.environ, env, clear=True):
                try:
                    sys.argv = ["run-behavioral-eval.py", str(skill_dir)]
                    exit_code = run_behavioral_eval.main()
                finally:
                    sys.argv = sys_argv_backup
            self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
