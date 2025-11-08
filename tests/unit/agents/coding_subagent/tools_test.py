import unittest
from agents.coding_subagent.tools import run_linter


class TestCodingTools(unittest.TestCase):
    def test_run_linter_pass(self):
        code = "import os\nprint('hello')"
        result = run_linter(code)
        self.assertEqual(result, "Lint passed.")

    def test_run_linter_fail(self):
        code = "print('hello')"
        result = run_linter(code)
        self.assertEqual(result, "Warning: No imports found.")


if __name__ == "__main__":
    unittest.main()
