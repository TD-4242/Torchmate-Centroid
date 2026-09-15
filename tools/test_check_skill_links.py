#!/usr/bin/env python3
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_skill_links as csl


class CheckTreeTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / ".claude" / "skills" / "centroid-alpha" / "reference").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_clean_tree_has_no_misses(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md", "# A\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "See [a](reference/a.md) and `centroid-alpha`.\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_broken_relative_link_is_reported_with_line(self):
        self.write(".claude/skills/centroid-alpha/SKILL.md", "ok\n[b](reference/missing.md)\n")
        self.assertEqual(
            csl.check_tree(self.root),
            [".claude/skills/centroid-alpha/SKILL.md:2: broken link reference/missing.md"])

    def test_anchor_is_stripped_before_resolving(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md", "# A\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "[a](reference/a.md#section) [top](#top)\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_external_links_are_skipped(self):
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "[w](https://x.invalid/a) [h](http://x.invalid) [m](mailto:a@b.invalid)\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_unknown_backticked_skill_is_reported(self):
        self.write(".claude/skills/centroid-alpha/SKILL.md", "Use `centroid-beta` for that.\n")
        self.assertEqual(
            csl.check_tree(self.root),
            [".claude/skills/centroid-alpha/SKILL.md:1: unknown skill centroid-beta"])

    def test_backticked_token_must_be_whole_skill_name(self):
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "Path `centroid-beta/SKILL.md` and `x centroid-beta`.\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_root_claude_and_readme_are_scanned(self):
        self.write("CLAUDE.md", "[s](docs/spec.md)\n")
        self.write("README.md", "`centroid-gamma`\n")
        self.assertEqual(
            csl.check_tree(self.root),
            ["CLAUDE.md:1: broken link docs/spec.md",
             "README.md:1: unknown skill centroid-gamma"])

    def test_files_outside_scope_are_ignored(self):
        self.write("docs/notes.md", "[x](nowhere.md) `centroid-zeta`\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_main_exit_codes(self):
        self.write(".claude/skills/centroid-alpha/SKILL.md", "fine\n")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(csl.main([str(self.root)]), 0)
        self.write(".claude/skills/centroid-alpha/SKILL.md", "[x](gone.md)\n")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(csl.main([str(self.root)]), 1)


if __name__ == "__main__":
    unittest.main()
