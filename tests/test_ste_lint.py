from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ste-lint.py"


def write_tmp(text: str) -> Path:
    handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False)
    handle.write(text)
    handle.close()
    return Path(handle.name)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        capture_output=True,
        check=False,
    )


class LintTests(unittest.TestCase):
    def test_procedure_sentence_limit(self):
        path = write_tmp("Install the component after you carefully inspect the complete mounting surface and make sure that all four retaining bolts are fully removed from the housing.")
        result = run("lint", "--type", "procedure", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("sentence-length", result.stdout)

    def test_description_sentence_limit(self):
        path = write_tmp("The controller reads the measured value and compares it with the target value before it calculates the correction that the actuator applies to the process during normal operation.")
        result = run("lint", "--type", "description", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("sentence-length", result.stdout)

    def test_paragraph_limit(self):
        path = write_tmp("One. Two. Three. Four. Five. Six. Seven.")
        result = run("lint", "--type", "description", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("paragraph-length", result.stdout)

    def test_contraction_and_semicolon(self):
        path = write_tmp("Don't open the cover; the unit is energized.")
        result = run("lint", "--type", "procedure", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("contraction", result.stdout)
        self.assertIn("semicolon", result.stdout)

    def test_valid_vertical_list(self):
        path = write_tmp("Make sure that these conditions are true:\n- The guard is installed.\n- The panel is closed.\n- The control is OFF.\n")
        result = run("lint", "--type", "procedure", str(path))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "0 violations")

    def test_invalid_vertical_list(self):
        path = write_tmp("Make sure that these conditions are true\n- the guard is installed;\n- The panel is closed\n")
        result = run("lint", "--type", "procedure", str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("vertical-list-lead", result.stdout)
        self.assertIn("vertical-list-capitalization", result.stdout)
        self.assertIn("vertical-list-punctuation", result.stdout)
        self.assertIn("vertical-list-final-period", result.stdout)

    def test_fenced_code_is_not_linted(self):
        path = write_tmp("```text\nDon't; don't; don't;\n```\nThe unit operates.")
        result = run("lint", "--type", "description", str(path))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_json_output(self):
        path = write_tmp("The unit operates.")
        result = run("--json", "lint", "--type", "description", str(path))
        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["mode"], "lint")


class FidelityTests(unittest.TestCase):
    def test_preserved_details_pass(self):
        original = write_tmp("CPU module ABC-123 must not exceed 5% load between 10 and 15 mmHg. Use `limit_value`.")
        rewritten = write_tmp("The CPU module ABC-123 must not exceed 5% load from 10 to 15 mmHg. Use `limit_value`.")
        result = run("details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_missing_detail_fails(self):
        original = write_tmp("Keep pressure between 10 and 15 mmHg. CPU limit is 5%.")
        rewritten = write_tmp("Keep the pressure at 10 mmHg. Keep the CPU limit low.")
        result = run("details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL", result.stdout)
        self.assertIn("numbers", result.stdout)
        self.assertIn("ranges", result.stdout)
        self.assertIn("percentages", result.stdout)

    def test_added_detail_fails(self):
        original = write_tmp("The limit is 10 mm.")
        rewritten = write_tmp("The limit is 10 mm for 5 seconds.")
        result = run("details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 1)
        self.assertIn("added", result.stdout)

    def test_negation_change_fails(self):
        original = write_tmp("Do not open the cover.")
        rewritten = write_tmp("Open the cover.")
        result = run("details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 1)
        self.assertIn("negations", result.stdout)

    def test_code_block_change_fails(self):
        original = write_tmp("```sh\necho 10\n```\nThe limit is 10 mm.")
        rewritten = write_tmp("```sh\necho 11\n```\nThe limit is 10 mm.")
        result = run("details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 1)
        self.assertIn("code_blocks", result.stdout)

    def test_details_json(self):
        original = write_tmp("Use ABC-123 at 10 mm.")
        rewritten = write_tmp("Use ABC-123 at 10 mm.")
        result = run("--json", "details", str(original), str(rewritten))
        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["preserved"])
        self.assertEqual(payload["mode"], "details")


if __name__ == "__main__":
    unittest.main()
