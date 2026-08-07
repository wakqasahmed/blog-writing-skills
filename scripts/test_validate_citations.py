#!/usr/bin/env python3
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "validate_citations", Path(__file__).resolve().parent / "validate-citations.py"
)
vc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vc)


class ClassifyStatusTests(unittest.TestCase):
    def test_2xx_is_ok(self):
        self.assertEqual(vc.classify_status(200)[0], "ok")
        self.assertEqual(vc.classify_status(204)[0], "ok")

    def test_3xx_redirect_is_ok(self):
        self.assertEqual(vc.classify_status(301)[0], "ok")
        self.assertEqual(vc.classify_status(302)[0], "ok")

    def test_bot_blocking_statuses_are_warnings(self):
        for status in (401, 403, 405, 429):
            level, message = vc.classify_status(status)
            self.assertEqual(level, "warning", f"status {status} should be a warning")
            self.assertIn(str(status), message)

    def test_dead_link_statuses_are_errors(self):
        for status in (404, 410, 500, 502, 503):
            level, message = vc.classify_status(status)
            self.assertEqual(level, "error", f"status {status} should be an error")
            self.assertIn(str(status), message)


class ClassifyStalenessTests(unittest.TestCase):
    def test_fresh_is_ok(self):
        self.assertEqual(vc.classify_staleness(0), "ok")
        self.assertEqual(vc.classify_staleness(180), "ok")

    def test_just_over_warn_threshold_is_warning(self):
        self.assertEqual(vc.classify_staleness(181), "warning")
        self.assertEqual(vc.classify_staleness(365), "warning")

    def test_just_over_error_threshold_is_error(self):
        self.assertEqual(vc.classify_staleness(366), "error")
        self.assertEqual(vc.classify_staleness(1000), "error")


if __name__ == "__main__":
    unittest.main()
