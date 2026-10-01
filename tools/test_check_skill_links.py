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

    def test_anchor_to_existing_heading_passes(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md", "# A\n## Section\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "# Top\n[a](reference/a.md#section) [top](#top)\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_missing_anchor_is_reported(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md", "# A\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "# Top\n[a](reference/a.md#nope) [b](#gone)\n")
        self.assertEqual(
            csl.check_tree(self.root),
            [".claude/skills/centroid-alpha/SKILL.md:2: broken anchor reference/a.md#nope",
             ".claude/skills/centroid-alpha/SKILL.md:2: broken anchor #gone"])

    def test_anchor_slugs_follow_github_rules(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md",
                   "## Axis Configuration (§6.5)\n"
                   "## Appendix H: Cyclone & MCU Status\n"
                   "## 1. Definition — `Name IS Resource`\n"
                   "## Symptom -> fix (App B)\n"
                   "## Dup\n## Dup\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "[a](reference/a.md#axis-configuration-65) "
                   "[b](reference/a.md#appendix-h-cyclone--mcu-status) "
                   "[c](reference/a.md#1-definition--name-is-resource) "
                   "[d](reference/a.md#symptom---fix-app-b) "
                   "[e](reference/a.md#dup) [f](reference/a.md#dup-1)\n")
        self.assertEqual(csl.check_tree(self.root), [])

    def test_headings_in_code_fences_are_not_anchors(self):
        self.write(".claude/skills/centroid-alpha/reference/a.md",
                   "# A\n```\n# not a heading\n```\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md",
                   "[a](reference/a.md#not-a-heading)\n")
        self.assertEqual(
            csl.check_tree(self.root),
            [".claude/skills/centroid-alpha/SKILL.md:1: broken anchor reference/a.md#not-a-heading"])

    def test_anchors_into_non_markdown_files_are_not_checked(self):
        self.write(".claude/skills/centroid-alpha/reference/t.py", "x = 1\n")
        self.write(".claude/skills/centroid-alpha/SKILL.md", "[t](reference/t.py#L1)\n")
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

    def test_main_rejects_missing_root(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(csl.main([str(self.root / "no-such-dir")]), 2)
        self.assertIn("has no Markdown files to check", err.getvalue())

    def test_main_rejects_root_with_nothing_to_check(self):
        empty = self.root / "empty"
        empty.mkdir()
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(csl.main([str(empty)]), 2)
        self.assertIn("error:", err.getvalue())

    def test_main_rejects_empty_skills_dir(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(csl.main([str(self.root)]), 2)
        self.assertIn("has no Markdown files to check", err.getvalue())


if __name__ == "__main__":
    unittest.main()
