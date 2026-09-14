# Acorn Skill Set and Repo Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the Torchmate-Centroid repo foundation and four generic, page-cited Centroid knowledge skills for the Acorn controller.

**Architecture:** One small stdlib Python tool (a link checker, built test-first) plus documentation-extraction work. Each reference file is built by extracting a fixed page range from a vendor PDF with `pdftotext` and writing it up as Markdown with a citation on every fact. Three skills are forks of Acroloc-Centroid skills: keep their structure, re-source every retained fact. The work ships as five PRs (foundation, then one per skill). A skill may only name skills that already exist, so each later stage adds the cross-links back into the skills merged before it.

**Tech Stack:** Markdown; Python 3 stdlib (`unittest`, `re`, `pathlib`); `pdftotext`/`pdfinfo` (poppler-utils); `curl`; `git`; `gh`.

**Spec:** `docs/superpowers/specs/2026-09-14-acorn-skill-set-design.md`

## Global Constraints

- **Repo:** `/home/bwarner/github/Torchmate-Centroid`, remote `origin` = `git@github.com:TD-4242/Torchmate-Centroid.git` (public, blank until Task 1).
- **Fork sources (read-only, never modify):** `/home/bwarner/github/Acroloc-Centroid/.claude/skills/`.
- **Generic only:** no Torchmate or Acroloc content in `.claude/skills/`. `ALLIN1DC`/`MPU11` may appear only where a cited manual covers multiple boards.
- **Every fact cited.** A fact that cannot be cited is dropped. Exception: a board-agnostic lesson carried from an Acroloc skill that no manual states is kept with the label `Field-verified (CNC12, <YYYY-MM from the Acroloc skill>)`.
- **No dangling pointers:** name only skills that exist in `.claude/skills/` at that commit. Topics without a skill point to a manual chapter and page instead.
- **Current state only:** no tombstones ("removed", "used to").
- **CNC12 Router install directory is `c:\cncr`** (Router Manual §1.8, p.13). Never write `c:\cncm` except when quoting a manual about mill.
- **Shape:** `SKILL.md` = frontmatter (`name`, `description`), when to use / when not, essentials, reference router table, useful resources. Reference files are roughly 100-250 lines; index files are exempt.
- **Python:** stdlib only, no pytest. Code comments are 1-2 lines and only where the code is confusing; rationale goes in commit messages.
- **Commits** end with these two lines, after a blank line:
  ```
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
  ```
- **PR bodies** end with:
  ```
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
  ```
- **Stage stop points:** each stage ends by opening a PR. Stop and wait for the user to merge it. The next stage starts from an updated `main` (`git switch main && git pull --ff-only`).

### Sources, page mapping and citation forms

All under `docs/official/`. Extract text with `pdftotext -layout -f <PDF first> -l <PDF last> docs/official/<file> -`. Use the Read tool with `pages` (max 20 per call) only to look at a figure. Cite the printed page; the PLC manual prints none, so cite its PDF page.

| File | Printed -> PDF page | Citation form |
| --- | --- | --- |
| `centroid_acorn_install_manual.pdf` | PDF = printed + 1 | `(Acorn Install §5.5, p.46)`, `(Acorn Install App D, p.123)` |
| `paired_axes_acorn_user_guide.pdf` | PDF = printed | `(Pairing Guide p.3)` |
| `centroid_plc_programming_manual.pdf` | no printed numbers | `(PLC Manual, PDF p.8)` |
| `centroid_vcp_users_manual.pdf` | PDF = printed | `(VCP Manual p.44)` |
| `centroid-cnc12-router-operator-manual.pdf` | PDF = printed + 1 | `(Router Manual §13.64, p.304)` |

The router manual PDF is gitignored. If working in a fresh worktree or clone, re-download it with the command in `docs/official/centroid-cnc12-router-operator-manual.md` before any router-ops task.

### Standard checks

Run from the repo root. "Run the standard checks" in a task means all five.

- **S1 generic:** `grep -rniE 'acroloc|torchmate' .claude/skills` -> no output.
- **S2 links:** `python3 tools/check_skill_links.py` -> exit 0, prints `OK:`.
- **S3 frontmatter:**
  ```bash
  python3 - <<'EOF'
  import pathlib, re, sys
  bad = 0
  for p in sorted(pathlib.Path('.claude/skills').glob('*/SKILL.md')):
      m = re.match(r'---\nname: (.+)\ndescription: (.+)\n---\n', p.read_text(encoding='utf-8'))
      if not m or m.group(1) != p.parent.name:
          print('bad frontmatter:', p); bad = 1
  print('frontmatter OK' if not bad else 'frontmatter FAILED'); sys.exit(bad)
  EOF
  ```
- **S4 board names:** `grep -rnE 'ALLIN1DC|MPU11' .claude/skills` -> every hit is either in a sentence citing a multi-board manual (PLC Manual, VCP Manual or Router Manual), or a verbatim manual quote marked `[sic]` with its citation. Rewrite any other hit.
- **S5 tracked tree:** `git ls-files docs/official` -> does not list `centroid-cnc12-router-operator-manual.pdf`.

---

## Stage 1: Foundation (branch `foundation`)

### Task 1: Link checker

**Files:**
- Create: `tools/check_skill_links.py`
- Test: `tools/test_check_skill_links.py`

**Interfaces:**
- Produces: `check_tree(root: pathlib.Path) -> list[str]`, which returns misses formatted `<path relative to root>:<line>: <reason>`, where reason is `broken link <target>` or `unknown skill <name>`. Also `main(argv: list[str]) -> int`: `argv[0]` is an optional repo root (default: the parent of `tools/`), it prints misses or `OK: <n> files checked`, and returns 1 or 0. CLI: `python3 tools/check_skill_links.py [root]`.

- [ ] **Step 1: Publish `main` and branch**

`main` holds the spec and this plan. The remote is blank, so this creates its base branch.

```bash
cd /home/bwarner/github/Torchmate-Centroid
git push -u origin main
git switch -c foundation
```
Expected: push succeeds; `git branch --show-current` prints `foundation`.

- [ ] **Step 2: Write the failing tests**

Create `tools/test_check_skill_links.py`:

```python
#!/usr/bin/env python3
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
        self.assertEqual(csl.main([str(self.root)]), 0)
        self.write(".claude/skills/centroid-alpha/SKILL.md", "[x](gone.md)\n")
        self.assertEqual(csl.main([str(self.root)]), 1)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python3 tools/test_check_skill_links.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'check_skill_links'`.

- [ ] **Step 4: Write the implementation**

Create `tools/check_skill_links.py`:

```python
#!/usr/bin/env python3
"""Report broken relative links and unknown skill names in skill docs, CLAUDE.md and README.md."""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKILL_RE = re.compile(r"`(centroid-[a-z0-9-]+)`")
EXTERNAL = ("http://", "https://", "mailto:")


def _doc_files(root):
    files = sorted((root / ".claude" / "skills").glob("**/*.md"))
    files += [p for p in (root / "CLAUDE.md", root / "README.md") if p.is_file()]
    return files


def check_tree(root):
    root = Path(root)
    skills_dir = root / ".claude" / "skills"
    known = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
    misses = []
    for path in _doc_files(root):
        rel_path = path.relative_to(root).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for target in LINK_RE.findall(line):
                if target.startswith(EXTERNAL):
                    continue
                file_part = target.split("#", 1)[0]
                if file_part and not (path.parent / file_part).exists():
                    misses.append(f"{rel_path}:{lineno}: broken link {target}")
            for name in SKILL_RE.findall(line):
                if name not in known:
                    misses.append(f"{rel_path}:{lineno}: unknown skill {name}")
    return misses


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    misses = check_tree(root)
    for miss in misses:
        print(miss)
    if misses:
        return 1
    print(f"OK: {len(_doc_files(root))} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 tools/test_check_skill_links.py -v`
Expected: `Ran 9 tests` ... `OK`.

- [ ] **Step 6: Commit**

```bash
git add tools/check_skill_links.py tools/test_check_skill_links.py
git commit -F - <<'EOF'
Add skill link checker

Fails on relative links that do not resolve and on backticked
centroid-* skill names with no directory under .claude/skills, so
skill docs cannot point at skills that were never built.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 2: Repo files, vendor sources, foundation PR

**Files:**
- Create: `.gitignore`, `.gitattributes`, `LICENSE.md`, `README.md`, `CLAUDE.md`
- Create: `docs/official/centroid_acorn_install_manual.pdf`, `docs/official/paired_axes_acorn_user_guide.pdf`, `docs/official/centroid_plc_programming_manual.pdf`, `docs/official/centroid_vcp_users_manual.pdf` (tracked)
- Create: `docs/official/centroid-cnc12-router-operator-manual.pdf` (gitignored), `docs/official/centroid-cnc12-router-operator-manual.md` (stub)

**Interfaces:**
- Consumes: `tools/check_skill_links.py` (Task 1).
- Produces: the five PDFs at the paths above (every later task reads them); the `.gitignore` allowlist; the README "Reference skills" table that Tasks 8, 12, 19 and 22 add rows to.

- [ ] **Step 1: Write `.gitignore`**

```gitignore
# Repo root doubles as the CNC12 install directory (c:\cncr): track only allowlisted paths.
/*

!/.claude/
/.claude/settings.local.json
!/docs/
!/tools/
/tools/__pycache__/
!/.gitattributes
!/.gitignore
!/CLAUDE.md
!/LICENSE.md
!/README.md

# 63 MB vendor manual kept local-only; its .md stub is tracked.
/docs/official/centroid-cnc12-router-operator-manual.pdf
.superpowers/
```

- [ ] **Step 2: Write `.gitattributes`**

```gitattributes
*.pdf binary
*.exe binary
```

- [ ] **Step 3: Download the vendor manuals**

centroidcnc.com returns HTTP 406 to curl's default headers, so send a browser User-Agent.

```bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
B=https://www.centroidcnc.com/centroid_diy/downloads
dl() { curl -fL -A "$UA" -H 'Accept: application/pdf,*/*' -o "docs/official/$1" "$2"; }
mkdir -p docs/official
dl centroid_acorn_install_manual.pdf          $B/acorn_documentation/centroid_acorn_install_manual.pdf
dl paired_axes_acorn_user_guide.pdf           $B/acorn_documentation/paired_axes_acorn_user_guide.pdf
dl centroid_plc_programming_manual.pdf        $B/centroid_plc_programming_manual.pdf
dl centroid_vcp_users_manual.pdf              $B/centroid_vcp_users_manual.pdf
dl centroid-cnc12-router-operator-manual.pdf  $B/operator_manuals/centroid-cnc12-router-operator-manual.pdf
```

- [ ] **Step 4: Verify the revisions match the spec**

```bash
for f in docs/official/*.pdf; do printf '%s pages=%s\n' "$f" "$(pdfinfo "$f" | awk '/^Pages/{print $2}')"; done
pdftotext -layout -l 1 docs/official/centroid_acorn_install_manual.pdf - | grep -o 'rev6 11-9-23'
pdftotext -layout -l 1 docs/official/paired_axes_acorn_user_guide.pdf - | grep -o 'rev19 10-27-25'
pdftotext -layout -f 13 -l 13 docs/official/centroid_plc_programming_manual.pdf - | grep -o 'rev8.odt 07/24/26'
pdftotext -layout -l 2 docs/official/centroid_vcp_users_manual.pdf - | grep -o 'rev 28 5-14-26'
pdftotext -layout -l 1 docs/official/centroid-cnc12-router-operator-manual.pdf - | grep -o 'CNC12 V.5.42+'
```
Expected pages: acorn 138, paired 41, plc 132, vcp 64, router 511; each grep prints its match. **If any page count or revision differs, stop and report it to the user.** The spec pins these revisions, and page citations depend on them.

- [ ] **Step 5: Write the router manual stub**

Create `docs/official/centroid-cnc12-router-operator-manual.md`:

````markdown
# CNC12 Router Operators Manual (local-only PDF)

The PDF is 63 MB, so it is gitignored. Skills cite it as `Router Manual`.

- Title: Centroid CNC12 Router Operators Manual
- Version: CNC12 V.5.42+ (PDF created 2026-07-06), 511 pages
- Models: Acorn, AcornSix, Hickory
- Page mapping: PDF page = printed page + 1

Download into this directory:

```bash
curl -fL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' \
  -H 'Accept: application/pdf,*/*' \
  -o docs/official/centroid-cnc12-router-operator-manual.pdf \
  https://www.centroidcnc.com/centroid_diy/downloads/operator_manuals/centroid-cnc12-router-operator-manual.pdf
```

Centroid serves only the latest revision. If the downloaded version or page count differs from
the above, page citations in the skills may be off.
````

- [ ] **Step 6: Write `LICENSE.md`**

```markdown
# License

This repository holds Centroid CNC12 reference skills, tooling and documentation for a
Torchmate CNC router retrofitted with a Centroid Acorn controller. It mixes original work with
third-party documentation that has different owners. This file states what covers what.

## Original contributions -- MIT License

Copyright (c) 2026 Bill Warner

The original contributions in this repository -- the reference skills under `.claude/`, the
tooling under `tools/`, and the project documentation authored here (`README.md`, `CLAUDE.md`,
and everything under `docs/` except `docs/official/`) -- are licensed under the MIT License:

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## Third-party material -- not covered by the MIT grant above

The MIT license applies only to the original contributions described above. It does not, and
cannot, relicense material owned by others.

- **`docs/official/`.** Everything under this directory is third-party documentation retained
  for reference: the Centroid Acorn installation manual, the Acorn axis pairing and squaring
  guide, the CNC12 PLC programming manual, the VCP users manual, and the CNC12 router operator
  manual -- Copyright (c) Centroid Corp. Centroid publishes these free of charge but grants no
  redistribution or relicensing rights, so they remain under Centroid's own terms. They are
  included for documentation purposes only and are not relicensed.

## Trademarks

"Centroid", "Acorn", "AcornSix", "CNC12", and "Torchmate" are the trademarks of their
respective owners. Use of these names is for identification and reference only and does not
imply endorsement.
```

- [ ] **Step 7: Write `README.md`**

Do not put unbuilt skill names in backticks; the link checker rejects them.

```markdown
# Torchmate-Centroid

Centroid CNC12 controller source and reference skills for a **Torchmate** CNC router
retrofitted with a Centroid **Acorn** controller. Plasma support follows once the router is
fully working. Modeled on [Acroloc-Centroid](https://github.com/TD-4242/Acroloc-Centroid).

## Status

| Sub-project | State |
| --- | --- |
| 1. Repo foundation + Acorn skill set | In progress: [spec](docs/superpowers/specs/2026-09-14-acorn-skill-set-design.md), [plan](docs/superpowers/plans/2026-09-14-acorn-skill-set.md) |
| 2. Router baseline (Wizard PLC, macros, config from the control PC) | Waiting on control-PC files |
| 3. Router customizations | Not started |
| 4. Plasma | Not started |

## Reference skills

Generic Centroid knowledge for Acorn under `.claude/skills/`. Every fact cites the official
manual section and page. Skills land one per PR, and each adds its row here.

| Skill | Covers |
| --- | --- |

## Official documentation

| File | Document |
| --- | --- |
| `docs/official/centroid_acorn_install_manual.pdf` | Acorn CNC Installation Manual, rev6 11-9-23 |
| `docs/official/paired_axes_acorn_user_guide.pdf` | Acorn CNC12 Axis Pairing and Squaring, rev19 10-27-25 |
| `docs/official/centroid_plc_programming_manual.pdf` | CNC12 PLC Programming Manual, rev8 07/24/26 |
| `docs/official/centroid_vcp_users_manual.pdf` | VCP 2.0 Users Manual, rev28 5-14-26 |
| [`docs/official/centroid-cnc12-router-operator-manual.md`](docs/official/centroid-cnc12-router-operator-manual.md) | CNC12 Router Operators Manual v5.42+ (PDF is local-only; stub has the download) |

## Tools

    python3 tools/check_skill_links.py        # broken links / unknown skill names in skill docs
    python3 tools/test_check_skill_links.py   # its tests
```

- [ ] **Step 8: Write `CLAUDE.md`**

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Centroid CNC12 source and reference skills for a Torchmate CNC router on a Centroid **Acorn**
(step/direction, CNC12 Router, install directory `c:\cncr`). Today the repo holds generic Acorn
knowledge skills, the vendor manuals they cite, and a link checker. The machine's
Wizard-generated PLC, macros and config arrive in a later sub-project, and plasma comes after
the router works. See [README.md](README.md) for status.

## Layout

- `.claude/skills/` -- generic Centroid skills: `SKILL.md` plus `reference/*.md`.
- `docs/official/` -- vendor manuals the skills cite. The router manual PDF is gitignored; its
  `.md` stub holds the download command.
- `docs/superpowers/specs/`, `docs/superpowers/plans/` -- design specs and implementation
  plans. They are the historical record and may be annotated.
- `tools/check_skill_links.py` -- link checker (`python3 tools/test_check_skill_links.py`).

## Skill conventions

1. **Generic.** No machine content in `.claude/skills/`; a machine skill will link to them.
2. **Sourced.** Every fact cites document and section/page. Uncitable facts are dropped.
3. **Field-verified exception.** A board-agnostic lesson no manual states is kept only when
   labeled `Field-verified (CNC12, YYYY-MM)`.
4. **No dangling pointers.** Name only skills that exist in `.claude/skills/`; otherwise cite
   the manual chapter and page. `python3 tools/check_skill_links.py` must exit 0.
5. **Current state.** Describe what the software does now; no tombstones.
6. **Shape.** `SKILL.md` (frontmatter, when to use / when not, essentials, reference router,
   useful resources) plus `reference/*.md` at roughly 100-250 lines; index files are exempt.
7. **Paths.** CNC12 Router lives in `c:\cncr`, not the mill's `c:\cncm`.

## Page citations

| Document | Cite as | PDF page |
| --- | --- | --- |
| Acorn Installation Manual | `(Acorn Install §6.7, p.81)` | printed + 1 |
| Acorn Axis Pairing and Squaring | `(Pairing Guide p.3)` | printed |
| CNC12 PLC Programming Manual | `(PLC Manual, PDF p.8)` | no printed numbers |
| VCP 2.0 Users Manual | `(VCP Manual p.44)` | printed |
| CNC12 Router Operators Manual | `(Router Manual §13.64, p.304)` | printed + 1 |

Extract text with `pdftotext -layout -f <pdf page> -l <pdf page> docs/official/<file> -`.

## Git

The repo root will double as the CNC12 install directory, so `.gitignore` ignores everything
and allowlists tracked paths. A new top-level tracked path needs its own `!/path` line.
```

- [ ] **Step 9: Verify**

```bash
python3 tools/test_check_skill_links.py
python3 tools/check_skill_links.py
git check-ignore -v docs/official/centroid-cnc12-router-operator-manual.pdf
git check-ignore -v some_job.nc
git add -A && git status --short
```
Expected: tests `OK`; checker prints `OK: 2 files checked`; both `check-ignore` calls print a matching `.gitignore` rule. `git status --short` lists exactly `.gitattributes`, `.gitignore`, `CLAUDE.md`, `LICENSE.md`, `README.md`, the four tracked PDFs and the router `.md` stub. The router PDF must not appear.

- [ ] **Step 10: Commit, push, open the PR**

```bash
git commit -F - <<'EOF'
Repo foundation: allowlist gitignore, license, docs, vendor manuals

Adds the Acorn, pairing-guide, PLC and VCP manuals at the revisions the
spec pins. The 63 MB router manual stays local with a download stub.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
git push -u origin foundation
gh pr create --base main --head foundation --title "Repo foundation: link checker, docs, vendor manuals" --body "$(cat <<'EOF'
## Summary
- `tools/check_skill_links.py` + unittest: fails on broken relative links and unknown `centroid-*` skill names.
- Allowlist `.gitignore` (repo root will double as `c:\cncr`), `.gitattributes`, `LICENSE.md`, `README.md`, `CLAUDE.md`.
- Vendor manuals in `docs/official/` at the spec's pinned revisions; router manual gitignored with a download stub.

## Verification
- `python3 tools/test_check_skill_links.py`: 9 tests OK
- `python3 tools/check_skill_links.py`: OK
- Router PDF confirmed ignored; tracked file list checked.

Spec: docs/superpowers/specs/2026-09-14-acorn-skill-set-design.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
)"
```
**Stop point:** wait for the user to merge.

---

## Stage 2: `centroid-acorn-install` (branch `skill/centroid-acorn-install`)

Model skill for shape and tone (not content): `/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-allin1dc-install/`. Page ranges below are printed pages, with PDF pages in brackets.

### Task 3: `hardware.md` and `software-setup.md`

**Files:**
- Create: `.claude/skills/centroid-acorn-install/reference/hardware.md`
- Create: `.claude/skills/centroid-acorn-install/reference/software-setup.md`

**Interfaces:**
- Produces: the canonical Acorn board I/O counts (8 inputs, 8 outputs, 4 axes, per App D). `wiring.md` (Task 4) and `centroid-plc-programming/reference/resources.md` (Task 10) cite them.

- [ ] **Step 1: Start the branch**

```bash
git switch main && git pull --ff-only && git switch -c skill/centroid-acorn-install
```

- [ ] **Step 2: Extract sources**

```bash
M=docs/official/centroid_acorn_install_manual.pdf
pdftotext -layout -f 8 -l 12 $M -      # Ch 1-2, p.7-11
pdftotext -layout -f 124 -l 138 $M -   # App D Acorn Specifications, p.123-137
pdftotext -layout -f 13 -l 34 $M -     # Ch 3-4, p.12-33
pdftotext -layout -f 115 -l 115 $M -   # App A, p.114
```

- [ ] **Step 3: Write `hardware.md`**

Open with a one-line purpose and `Source: Acorn Install Ch 1, Ch 2, App D; printed pages cited inline.` Sections:
- `## Kit contents`: part numbers from Ch 1 (Acorn 14756, relay board 14734, RD-35B supply 8903, cords 14459/14460, Ethernet cable 7269; kit 14455), cited p.7.
- `## Board specifications`: table from App D (axes, pulse rate, Ethernet, drive type, digital inputs, digital outputs, analog output resolution, dimensions), plus the connector and pin tables App D gives, each cited to its App D page.
- `## Relay board and power`: from Ch 2 and App D.
- `## LEDs`: power LED and BeagleBone Green heartbeat meanings (§2.2, p.10-11), with the forum LED-explainer URL.
- `## Bench test hardware setup`: the §2.2 numbered steps, verbatim in substance, including the shielded-cable requirement (TB270) and "do not plug anything into the BBG USB port".

- [ ] **Step 4: Write `software-setup.md`**

`Source: Acorn Install Ch 3, Ch 4, App A.` Sections follow §3.1 Windows 10/11 configuration, §3.2 CNC12 install, §3.3 license file, §3.4 communications stress test, §3.5 configuration reports, §4.1 CNC12 software configuration, §4.2 spindle bench test, and App A. Keep numbered procedures as numbered lists, and put every setting name and value in backticks with its page.

- [ ] **Step 5: Verify**

Run the standard checks. Then:
```bash
wc -l .claude/skills/centroid-acorn-install/reference/{hardware,software-setup}.md
grep -c 'Acorn Install' .claude/skills/centroid-acorn-install/reference/hardware.md
```
Expected: citations on every section (count at least the number of `##` sections); lengths roughly 100-250. Confirm that the App D input and output counts match `Digital PLC Inputs: 8` and `Digital PLC Outputs: 8`.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/centroid-acorn-install/reference/hardware.md .claude/skills/centroid-acorn-install/reference/software-setup.md
git commit -F - <<'EOF'
acorn-install skill: hardware and software-setup references

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 4: `wiring.md`

**Files:**
- Create: `.claude/skills/centroid-acorn-install/reference/wiring.md`

**Interfaces:**
- Consumes: board I/O counts from `hardware.md` (Task 3). Link to it rather than repeating the spec table.
- Produces: the input/output and home/limit wiring facts that `wizard.md` (Task 5) and `axis-pairing.md` (Task 6) link to.

- [ ] **Step 1: Extract sources**

```bash
pdftotext -layout -f 35 -l 71 docs/official/centroid_acorn_install_manual.pdf -   # Ch 5, p.34-70
```
The source is 37 pages. Work section by section: §5.1 p.34-43, §5.2 p.44, §5.3 p.45, §5.4 p.45, §5.5 p.46-51, §5.6 p.52-55, §5.7 p.56-65, §5.8 p.66-68, §5.9 p.69-70.

- [ ] **Step 2: Write `wiring.md`**

`Source: Acorn Install Ch 5.` One `##` per §5.1-§5.9. Required content:
- §5.1 drive-type connection guidance and cabinet layout; describe figures and cite their page, and do not reproduce diagrams.
- §5.2/§5.3: an input table and an output table (terminal, signal, notes) exactly as the manual gives them.
- §5.4 +24VDC jumper; §5.5 E-stop circuit, with every DANGER/WARNING as a `>` callout.
- §5.6 axis drive wiring (step/direction/enable, common).
- §5.7 home and limit switches, including every switch-type and wiring option the manual shows.
- §5.8 spindle motor (relay and VFD options as given); §5.9 spindle encoder requirements.

Note: the §5.9 text in this manual says "The +5V is an output provided by the ALLIN1DC". If you include it, quote it verbatim, mark it `[sic]` and cite it; do not "correct" it.

- [ ] **Step 3: Verify**

Run the standard checks. If S4 flags the ALLIN1DC quote, confirm it is marked `[sic]` and carries its `(Acorn Install §5.9, p.69)` citation. Then:
```bash
grep -c '^## ' .claude/skills/centroid-acorn-install/reference/wiring.md   # expect >= 9
```

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-acorn-install/reference/wiring.md
git commit -F - <<'EOF'
acorn-install skill: wiring reference

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 5: `wizard.md`

**Files:**
- Create: `.claude/skills/centroid-acorn-install/reference/wizard.md`

**Interfaces:**
- Consumes: `wiring.md` (Task 4) for I/O links.
- Produces: the `## Custom PLC preference` section anchor (`#custom-plc-preference`), which `SKILL.md` (Task 8) and `centroid-plc-programming/reference/acorn-plc.md` (Task 10) link to.

- [ ] **Step 1: Extract sources**

```bash
pdftotext -layout -f 72 -l 101 docs/official/centroid_acorn_install_manual.pdf -   # Ch 6, p.71-100
```
Section starts (printed): 6.1 p.71, 6.2 p.72, 6.3 p.74, 6.4 p.75, 6.5 p.76, 6.6 p.79, 6.7 p.81 (skip; Task 6), 6.8 p.83, 6.9 p.84, 6.10 p.85, 6.11 p.86, 6.12 p.87, 6.13 p.89, 6.14 p.91, 6.15 p.92, 6.16 p.93, 6.17 p.94, 6.18 p.96, 6.19 p.98, 6.20 p.99, 6.21 p.100.

- [ ] **Step 2: Write `wizard.md`**

`Source: Acorn Install Ch 6 (§6.7 is in axis-pairing.md).` One `##` per section, for every section except §6.7, which becomes a one-line pointer: `See [axis-pairing.md](axis-pairing.md)`. For each Wizard page, list every field as `**Field name**: meaning (values)`, with the page cited once per section. The §6.19 Wizard Preferences section must contain a sub-heading exactly `## Custom PLC preference`. It records that selecting Custom PLC tells the Wizard not to overwrite a custom PLC program (Acorn Install §6.19, p.98).

- [ ] **Step 3: Verify**

Run the standard checks. Then:
```bash
F=.claude/skills/centroid-acorn-install/reference/wizard.md
grep -n '^## Custom PLC preference$' $F
for s in 1 2 3 4 5 6 8 9 10 11 12 13 14 15 16 17 18 19 20 21; do grep -q "§6\.$s[,)]" $F || echo "missing §6.$s"; done
```
Expected: the heading line prints, and no `missing` lines.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-acorn-install/reference/wizard.md
git commit -F - <<'EOF'
acorn-install skill: Wizard reference

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 6: `axis-pairing.md`

**Files:**
- Create: `.claude/skills/centroid-acorn-install/reference/axis-pairing.md`

**Interfaces:**
- Consumes: `wizard.md` (Task 5); link back to its homing section.
- Produces: pairing facts that `SKILL.md` (Task 8) summarizes, including M294/M295. Task 16's `m-code-index.md` cites the Router Manual for those codes independently.

- [ ] **Step 1: Extract sources**

```bash
pdftotext -layout -f 82 -l 83 docs/official/centroid_acorn_install_manual.pdf -   # §6.7, p.81-82
pdftotext -layout -f 1 -l 41 docs/official/paired_axes_acorn_user_guide.pdf -     # whole guide
```
Guide sections (printed = PDF): v5.4+ notice p.2, Hardware vs Software Pairing p.3-4, Hardware Pairing and Axis Squaring p.5-21, Software Pairing and Axis Squaring p.22-41.

- [ ] **Step 2: Write `axis-pairing.md`**

`Source: Acorn Install §6.7; Pairing Guide rev19.` Sections:
- `## Software vs hardware pairing`: definitions, requirements (same steps/rev and turns ratio), and "Acorn effectively becomes a 3-axis controller" (Pairing Guide p.3).
- `## License requirement`: software axis pairing needs a Pro license (Acorn Install §6.7, p.81).
- `## Wizard fields`: every §6.7 field (axis to pair with 4th, reverse direction, squaring mode, master squaring distance, homing feedrate, home switch deadband, master/slave home inputs).
- `## Homing and squaring methods`: auto home + auto square, auto home + manual square, manual home + manual square (Pairing Guide p.3), then the hardware-pairing procedure (p.5-21) and the software-pairing procedure (p.22-41).
- `## CNC12 v5.4+ changes`: M294/M295 unpair/re-pair and faster auto-squaring (Pairing Guide p.2), and the release-notes URL.

- [ ] **Step 3: Verify**

Run the standard checks. Then:
```bash
F=.claude/skills/centroid-acorn-install/reference/axis-pairing.md
grep -c 'Pairing Guide p\.' $F; grep -c 'Acorn Install §6\.7' $F; grep -n 'M294\|M295\|Pro license' $F
```
Expected: both counts at least 3, and the grep shows M294, M295 and Pro license lines.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-acorn-install/reference/axis-pairing.md
git commit -F - <<'EOF'
acorn-install skill: axis pairing and squaring reference

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 7: `commissioning.md` and `troubleshooting.md`

**Files:**
- Create: `.claude/skills/centroid-acorn-install/reference/commissioning.md`
- Create: `.claude/skills/centroid-acorn-install/reference/troubleshooting.md`

**Interfaces:**
- Consumes: `wizard.md` (Task 5) links for the axis fields that tuning adjusts.
- Produces: the two remaining router-table rows for `SKILL.md` (Task 8).

- [ ] **Step 1: Extract sources**

```bash
M=docs/official/centroid_acorn_install_manual.pdf
pdftotext -layout -f 102 -l 114 $M -   # Ch 7, p.101-113
pdftotext -layout -f 116 -l 123 $M -   # App B p.115-117, App C p.118-122
```

- [ ] **Step 2: Write `commissioning.md`**

`Source: Acorn Install Ch 7.` One `##` each for §7.1 motor testing and configuration (p.101), §7.2 coarse commanded-vs-actual (p.104), §7.3 fine turns-ratio adjustment (p.105), §7.4 backlash compensation (p.108) and §7.5 software travel limits (p.112). Keep formulas and worked numbers exactly as printed.

- [ ] **Step 3: Write `troubleshooting.md`**

`Source: Acorn Install App B, App C.` Start with a `## Symptom -> fix` table from App B, then `## Support and knowledge base` with every URL from App C and the manual's "Useful Technical Resources" (p.5).

- [ ] **Step 4: Verify**

Run the standard checks. Then:
```bash
for s in 1 2 3 4 5; do grep -q "§7\.$s[,)]" .claude/skills/centroid-acorn-install/reference/commissioning.md || echo "missing §7.$s"; done
grep -c 'App B' .claude/skills/centroid-acorn-install/reference/troubleshooting.md
```
Expected: no `missing` lines; the App B count is at least 1.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-acorn-install/reference/commissioning.md .claude/skills/centroid-acorn-install/reference/troubleshooting.md
git commit -F - <<'EOF'
acorn-install skill: commissioning and troubleshooting references

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 8: `SKILL.md`, stage verification, PR

**Files:**
- Create: `.claude/skills/centroid-acorn-install/SKILL.md`
- Modify: `README.md` (add a row to the Reference skills table)

**Interfaces:**
- Consumes: all seven reference files (Tasks 3-7).
- Produces: skill `centroid-acorn-install`, which Tasks 12, 19 and 22 link to.

- [ ] **Step 1: Write `SKILL.md`**

Frontmatter:
```yaml
---
name: centroid-acorn-install
description: Use when installing, wiring, configuring, commissioning, or troubleshooting a Centroid Acorn CNC controller - kit and board I/O, LEDs, bench test, Windows/CNC12 install and license, cabinet wiring (inputs/outputs, E-stop, step/dir drives, home/limit switches, spindle), every Acorn Wizard page including Custom PLC, software/hardware axis pairing and auto-squaring, motion tuning, backlash, travel limits, and symptom-to-fix troubleshooting. Generic to any Acorn machine. Source: Acorn Installation Manual rev6 and Acorn Axis Pairing and Squaring guide rev19.
---
```
Body, in the shape of Acroloc's `centroid-allin1dc-install/SKILL.md`:
- **When to use / when not.** Not for PLC stage language or macros: cite `PLC Manual` (no skill name yet; the PLC skill PR adds the link).
- **Essentials:** Acorn is step/direction, 4 axes, 8 in / 8 out, Ethernet to PC (App D). The Wizard generates the PLC program. Install order: bench test -> CNC12 + license + stress test -> wiring -> Wizard -> motion tuning. Cautions: shielded Ethernet only (§2.2); set Custom PLC before hand-editing a PLC ([wizard.md](reference/wizard.md#custom-plc-preference)); software pairing needs Pro (§6.7).
- **Reference router table:** one row per reference file.
- **Useful resources:** URLs from p.5 and App C.

- [ ] **Step 2: Add the README row**

In `README.md`, under the Reference skills table header, add:
```markdown
| [`centroid-acorn-install`](.claude/skills/centroid-acorn-install/SKILL.md) | Acorn hardware, wiring, Wizard, axis pairing, motion tuning, troubleshooting |
```

- [ ] **Step 3: Stage verification**

Run the standard checks. Then spot-check 5 citations:
```bash
grep -rhoE '\((Acorn Install|Pairing Guide)[^)]*\)' .claude/skills/centroid-acorn-install | sort -u | shuf -n 5 --random-source=<(yes)
```
For each of the 5, extract its page (`pdftotext -layout -f <printed+1> -l <printed+1> ...` for Acorn Install, `-f <p> -l <p>` for the guide) and confirm the sentence citing it matches the page. Fix any mismatch, and record the 5 citations with a pass/fix note for the PR body.

- [ ] **Step 4: Commit, push, PR**

```bash
git add .claude/skills/centroid-acorn-install/SKILL.md README.md
git commit -F - <<'EOF'
acorn-install skill: SKILL.md router

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
git push -u origin skill/centroid-acorn-install
gh pr create --base main --title "Skill: centroid-acorn-install" --body "$(cat <<'EOF'
## Summary
- New generic `centroid-acorn-install` skill: hardware, software-setup, wiring, wizard, axis-pairing, commissioning, troubleshooting.
- Sources: Acorn Installation Manual rev6 11-9-23; Acorn Axis Pairing and Squaring rev19 10-27-25. Every fact page-cited.

## Verification
- Standard checks S1-S5 pass.
- Spot-checked citations: <paste the 5 citations with pass/fix notes>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
)"
```
Replace the `<paste ...>` line with the real Step 3 results before running. **Stop point:** wait for merge.

---

## Stage 3: `centroid-plc-programming` (branch `skill/centroid-plc-programming`)

Fork source: `/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-plc-programming/`. Source manual: `docs/official/centroid_plc_programming_manual.pdf`, cited by PDF page. PDF section starts: Introduction 4, Acorn/Wizard 6-8, platform note 11, Language 13-29, Standard PLC Program Layout and Optional Sections 30-51, Compiler Errors 52-59, Application Examples / Custom M-Codes / Troubleshooting 60-63, App A 64-98, App B 99, App C 100-101, App D System Variables 102-120, App E I/O Location 121-123, App F 124-125, App G 126-127, App H 128, App I 129-130, App J 131, App K 132.

**Fork procedure (every Stage 3 file):** copy the Acroloc file, then walk it top to bottom. For each factual statement, find it in the current manual and add `(PLC Manual, PDF p.N)`. Rewrite anything the manual now states differently. Delete anything not found in the manual, and anything Acroloc-specific (its `.src` names, its I/O, its message numbers, "this repo" phrasing).

### Task 9: `syntax.md` and `messages.md`

**Files:**
- Create: `.claude/skills/centroid-plc-programming/reference/syntax.md` (fork)
- Create: `.claude/skills/centroid-plc-programming/reference/messages.md` (fork)

**Interfaces:**
- Produces: statement and message facts that `SKILL.md` (Task 12) summarizes.

- [ ] **Step 1: Branch and copy**

```bash
git switch main && git pull --ff-only && git switch -c skill/centroid-plc-programming
mkdir -p .claude/skills/centroid-plc-programming/reference
A=/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-plc-programming/reference
cp $A/syntax.md $A/messages.md .claude/skills/centroid-plc-programming/reference/
```

- [ ] **Step 2: Extract sources**

```bash
P=docs/official/centroid_plc_programming_manual.pdf
pdftotext -layout -f 11 -l 29 $P -   # conventions, Language
pdftotext -layout -f 52 -l 63 $P -   # compiler errors, examples, custom M-codes, troubleshooting
grep -n -i 'message' <(pdftotext -layout $P -) | head -40   # locate message-encoding pages
```

- [ ] **Step 3: Re-source `syntax.md`**

Apply the fork procedure. Keep its sections (Execution Model, Statement Forms 1-5, Operators, Conditions vs Actions, Comments). Replace the stage-header, section-header and definition-alignment conventions (Acroloc's house style) with the manual's Programming Conventions (Language section), or delete them.

- [ ] **Step 4: Re-source `messages.md`**

Apply the fork procedure. Delete `### Note on CLAUDE.md variable names`, the Acroloc worked example, and the `ATC_Lock_Released_C` gotcha. Rebuild `## Worked example` from an example the manual itself prints, with its PDF page. Keep `plcmsg.txt` format facts only where cited.

- [ ] **Step 5: Verify**

Run the standard checks. Then:
```bash
D=.claude/skills/centroid-plc-programming/reference
grep -c 'PLC Manual, PDF p\.' $D/syntax.md $D/messages.md
grep -niE 'this repo|W7[0-9]|INP2[4-9]|ATC|carousel' $D/syntax.md $D/messages.md
```
Expected: counts at least the number of `##` sections in each file; the second grep prints nothing.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/centroid-plc-programming/reference/syntax.md .claude/skills/centroid-plc-programming/reference/messages.md
git commit -F - <<'EOF'
plc-programming skill: re-sourced syntax and messages references

Forked from Acroloc-Centroid and re-verified against PLC Manual rev8
07/24/26; uncited and machine-specific material dropped.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 10: `resources.md` and `acorn-plc.md`

**Files:**
- Create: `.claude/skills/centroid-plc-programming/reference/resources.md` (fork)
- Create: `.claude/skills/centroid-plc-programming/reference/acorn-plc.md` (new)

**Interfaces:**
- Consumes: `centroid-acorn-install` reference files `hardware.md`, `wiring.md` and `wizard.md#custom-plc-preference` (Stage 2, merged).
- Produces: Acorn I/O addressing and Wizard-PLC facts, routed from `SKILL.md` (Task 12).

- [ ] **Step 1: Copy and extract**

```bash
cp /home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-plc-programming/reference/resources.md .claude/skills/centroid-plc-programming/reference/
P=docs/official/centroid_plc_programming_manual.pdf
pdftotext -layout -f 4 -l 12 $P -     # intro, Acorn Wizard PLC (6-8), resources/tools, platform note (11)
pdftotext -layout -f 13 -l 22 $P -    # Defining Variables, Data Types
pdftotext -layout -f 60 -l 61 $P -    # Custom M-Codes (M94/M95)
pdftotext -layout -f 121 -l 123 $P -  # App E PLC I/O Location
pdftotext -layout -f 45 -l 46 docs/official/centroid_acorn_install_manual.pdf -   # §5.2-5.4, p.44-45
```

- [ ] **Step 2: Re-source `resources.md`**

Apply the fork procedure. Resource types and address ranges come from Data Types (cite pages). Replace every ALLIN1DC I/O range with an `## Acorn I/O` section: the 8 inputs and 8 outputs and their terminal naming from Acorn Install §5.2/§5.3, linked to [wiring.md](../../centroid-acorn-install/reference/wiring.md). State that App E of the PLC manual lists ALLIN1DC, DC3IOB, GPIO4D and PLC expansion but not Acorn (PLC Manual, PDF p.121-123). Keep macro<->PLC access (`#(60000+n)`, `M94`/`M95`) only with PLC Manual or Router Manual citations; §13.28 M94/M95 is Router Manual p.290. Keep the naming-suffix convention only if the manual states it; otherwise delete it.

- [ ] **Step 3: Write `acorn-plc.md`**

`Source: PLC Manual PDF p.6-11; Acorn Install §6.19.` Sections:
- `## Same language, Wizard-generated program`: the PLC language is the same across Oak, Allin1DC, MPU11, Acorn, AcornSix and Hickory, with differences only in board hardware (PDF p.11). The Acorn Wizard builds a custom PLC from canned functions chosen in its input/output menus (PDF p.6-8).
- `## Files`: the universal template `acorn_universal_template.src` at `resources\wizard\default\plc\` under the CNC12 directory. The generated program is written to the CNC12 root, for example `acorn_mill_plc.src` (PDF p.8). Record that the manual shows only the mill name and path (`cncm`), and state the router directory as `c:\cncr` (Router Manual §1.8, p.13). Do **not** invent a router PLC filename.
- `## Hand-editing safely`: turn off automatic generation with Custom PLC before editing (PDF p.8), linked to [Custom PLC preference](../../centroid-acorn-install/reference/wizard.md#custom-plc-preference).
- `## Tools`: PLC Diagnostic screen and PLC Detective URLs (PDF p.9-10).
- `## Board identification`: `SV_DRIVE_TYPE_x (1-8)` reports the board/drive type; its values include `13 = ACORN` and `24 = ACORNSIX` (PLC Manual, PDF p.110).

- [ ] **Step 4: Verify**

Run the standard checks (S2 now validates the cross-skill links). Then:
```bash
D=.claude/skills/centroid-plc-programming/reference
grep -n 'acorn_universal_template.src\|Custom PLC' $D/acorn-plc.md
grep -niE 'INP(1[0-6]|9)\b|OUT(9|1[0-9])\b' $D/resources.md
```
Expected: the first grep hits; any second-grep hit is an Acorn-cited address, with no leftover ALLIN1DC ranges.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-plc-programming/reference/resources.md .claude/skills/centroid-plc-programming/reference/acorn-plc.md
git commit -F - <<'EOF'
plc-programming skill: Acorn resources and Wizard PLC references

PLC Manual App E has no Acorn I/O section, so Acorn addressing is
sourced from the Acorn Installation Manual §5.2/5.3.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 11: `system-variables.md`

**Files:**
- Create: `.claude/skills/centroid-plc-programming/reference/system-variables.md` (fork)

**Interfaces:**
- Produces: the `SV_*` catalog routed from `SKILL.md` (Task 12).

- [ ] **Step 1: Copy and extract**

```bash
cp /home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-plc-programming/reference/system-variables.md .claude/skills/centroid-plc-programming/reference/
pdftotext -layout -f 102 -l 132 docs/official/centroid_plc_programming_manual.pdf docs_sv.txt
```
`docs_sv.txt` and the `sv_*.txt` files below are scratch in the repo root (ignored by `.gitignore`); delete them in Step 4.

- [ ] **Step 2: Verify every SV name against the manual**

```bash
F=.claude/skills/centroid-plc-programming/reference/system-variables.md
grep -oE 'SV_[A-Z0-9_]+' $F | sort -u > sv_skill.txt
grep -oE 'SV_[A-Z0-9_]+' docs_sv.txt | sort -u > sv_manual.txt
comm -23 sv_skill.txt sv_manual.txt
```
Each name printed is **not** in App D-K. Search the whole manual for it (`pdftotext -layout docs/official/centroid_plc_programming_manual.pdf - | grep -n NAME`). If it's found, cite that page; otherwise delete its row. Names containing a numeric suffix pattern (e.g. `_1` ... `_8`) may appear in the manual as `_x (1-8)`, so match on the stem before deleting.

- [ ] **Step 3: Re-source the rest**

Apply the fork procedure. Each group heading cites the App D-K page range it came from; each row keeps name, type and meaning, with its page. Delete `### Machine parameters used in source (specific numbers)`, which is Acroloc's `.src` usage. Machine parameter meanings belong to the Router Manual parameter index (Stage 4), so replace that section with one line citing `Router Manual §15.7, p.320`.

- [ ] **Step 4: Verify**

Run the standard checks, then re-run the Step 2 `comm` command. Expected: no output. Then `rm docs_sv.txt sv_skill.txt sv_manual.txt`.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-plc-programming/reference/system-variables.md
git commit -F - <<'EOF'
plc-programming skill: re-sourced system-variable catalog

Every SV_* name verified against PLC Manual App D-K; names not in the
manual and Acroloc source-usage sections dropped.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 12: `SKILL.md`, back-links, stage verification, PR

**Files:**
- Create: `.claude/skills/centroid-plc-programming/SKILL.md`
- Modify: `.claude/skills/centroid-acorn-install/SKILL.md` ("when not" now names the PLC skill)
- Modify: `README.md` (add a row)

**Interfaces:**
- Consumes: Tasks 9-11 reference files; `centroid-acorn-install`.
- Produces: skill `centroid-plc-programming`, which Tasks 19 and 22 link to.

- [ ] **Step 1: Write `SKILL.md`**

Frontmatter:
```yaml
---
name: centroid-plc-programming
description: Use when writing, reading, or debugging Centroid CNC12 PLC stage-language source (.src) or M-code macro-to-PLC interaction on an Acorn - stage/scan execution, IF/THEN/SET/RST syntax, resource types and Acorn I/O addressing, the SV_* system-variable catalog, operator-message encoding and plcmsg.txt, and the Acorn Wizard-generated PLC (universal template, Custom PLC before hand-editing). Source: CNC12 PLC Programming Manual rev8 07/24/26.
---
```
Body: adapt Acroloc's `SKILL.md`. Keep "Language essentials", with every sentence re-cited to the PLC Manual. "When not" covers wiring and Wizard fields -> `centroid-acorn-install`. Router rows: `syntax.md`, `resources.md`, `system-variables.md`, `messages.md`, `acorn-plc.md`; no examples-index row. Add a line: example PLC projects are not indexed; the Wizard's template is described in [acorn-plc.md](reference/acorn-plc.md).

- [ ] **Step 2: Back-link from acorn-install**

In `.claude/skills/centroid-acorn-install/SKILL.md`, replace the "When not" sentence that cites `PLC Manual` for PLC work with:
```markdown
**Do not use this skill** for PLC stage-language (`.src`) or macro work -- use
`centroid-plc-programming` ([SKILL.md](../centroid-plc-programming/SKILL.md)).
```

- [ ] **Step 3: Add the README row**

```markdown
| [`centroid-plc-programming`](.claude/skills/centroid-plc-programming/SKILL.md) | PLC stage language, Acorn I/O, SV_* catalog, messages, Wizard-generated PLC |
```

- [ ] **Step 4: Stage verification**

Run the standard checks. Spot-check 5 citations:
```bash
grep -rhoE '\(PLC Manual, PDF p\.[0-9]+\)' .claude/skills/centroid-plc-programming | sort -u | shuf -n 5 --random-source=<(yes)
```
For each, run `pdftotext -layout -f N -l N docs/official/centroid_plc_programming_manual.pdf -` and confirm the citing sentence. Record the results for the PR body.

- [ ] **Step 5: Commit, push, PR**

```bash
git add .claude/skills/centroid-plc-programming/SKILL.md .claude/skills/centroid-acorn-install/SKILL.md README.md
git commit -F - <<'EOF'
plc-programming skill: SKILL.md router and acorn-install back-link

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
git push -u origin skill/centroid-plc-programming
gh pr create --base main --title "Skill: centroid-plc-programming (Acorn)" --body "$(cat <<'EOF'
## Summary
- `centroid-plc-programming` forked from Acroloc-Centroid and re-sourced against PLC Manual rev8 07/24/26.
- Acorn I/O addressing (from the Acorn Installation Manual; PLC Manual App E has no Acorn section) and a new `acorn-plc.md` for the Wizard-generated PLC.
- No examples index until Acorn PLC sources are in the repo.
- `centroid-acorn-install` now links here.

## Verification
- Standard checks S1-S5 pass; every SV_* name verified against App D-K.
- Spot-checked citations: <paste the 5 citations with pass/fix notes>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
)"
```
Replace the placeholder line with real results. **Stop point:** wait for merge.

---

## Stage 4: `centroid-cnc12-router-ops` (branch `skill/centroid-cnc12-router-ops`)

Structure source: `/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-cnc12-operating/`. Content source: Router Manual only; the Acroloc files are mill-manual transcriptions, so use them for shape, not facts. Before starting, confirm `docs/official/centroid-cnc12-router-operator-manual.pdf` exists (511 pages); if not, download it using the stub's command.

Chapter pages, printed [PDF]: Ch 1 10-16 [11-17], Ch 2 17-40 [18-41], Ch 3 41-49 [42-50], Ch 4 50-64 [51-65], Ch 5 65-81 [66-82], Ch 6 82-87 [83-88], Ch 7 88-91 [89-92], Ch 8 92 [93], Ch 9 104 [105], Ch 10 114 [115], Ch 11 196 [197], Ch 12 243-279 [244-280], Ch 13 280-306 [281-307], Ch 14 307 [308], Ch 15 310 [311], §15.7 320-396 [321-397], §15.23 434 [435], Ch 16 435-450 [436-451], Ch 17 451 [452], Ch 18 454 [455].

Acroloc pointers to `centroid-cnc12-gmcodes`, `centroid-cnc12-config` and `centroid-cnc12-intercon-probing` must not survive. Point to this skill's index files or to a manual chapter instead.

### Task 13: `interface.md` and `operator-panel.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/interface.md`
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/operator-panel.md`

**Interfaces:**
- Produces: the F1-F10 menu map and key notation that Tasks 14-15 reference.

- [ ] **Step 1: Branch and extract**

```bash
git switch main && git pull --ff-only && git switch -c skill/centroid-cnc12-router-ops
R=docs/official/centroid-cnc12-router-operator-manual.pdf
test "$(pdfinfo $R | awk '/^Pages/{print $2}')" = 511 && echo router-manual-ok
pdftotext -layout -f 11 -l 17 $R -   # Ch 1
pdftotext -layout -f 42 -l 50 $R -   # Ch 3
pdftotext -layout -f 18 -l 41 $R -   # Ch 2
```

- [ ] **Step 2: Write `interface.md`**

`Source: Router Manual Ch 1, Ch 3.` `##` per §1.1-§1.12, with these rules:
- §1.8 Machine Home must state that homing runs `cncm.hom` in `c:\cncr`, and its default order: Z plus, then X minus, then Y plus (p.13).
- §1.9 is a one-paragraph pointer to [g-code-index.md](g-code-index.md) and [m-code-index.md](m-code-index.md).

Then `## F1-F10 main-screen menu map`, a table from §3.1-§3.10: F1 Set Part Zeros, F2 Load Job, F3 MDI, F4 Run, F5 Tool/ATC, F6 Edit, F7 Utility, F8 Graph, F9 Smoothing, F10 Shutdown. Note the router differs from mill (F5 Tool/ATC, F9 Smoothing).

- [ ] **Step 3: Write `operator-panel.md`**

`Source: Router Manual Ch 2.` `##` per §2.1-§2.28. Put the §2.26 keyboard jog panel and §2.28 shortcut keys in tables.

- [ ] **Step 4: Verify**

Run the standard checks. Then:
```bash
D=.claude/skills/centroid-cnc12-router-ops/reference
for s in $(seq 1 12); do grep -q "§1\.$s[,)]" $D/interface.md || echo "missing §1.$s"; done
for s in $(seq 1 10); do grep -q "§3\.$s[,)]" $D/interface.md || echo "missing §3.$s"; done
for s in $(seq 1 28); do grep -q "§2\.$s[,)]" $D/operator-panel.md || echo "missing §2.$s"; done
grep -n 'cncm' $D/interface.md $D/operator-panel.md
```
Expected: no `missing` lines. Any `cncm` hit must be `cncm.hom` or a quoted manual string. S2 passes only after Task 16 creates the index files, so run Task 13's S2 with `|| true` and note that it's expected to flag `g-code-index.md`/`m-code-index.md`; everything else must be clean.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/interface.md .claude/skills/centroid-cnc12-router-ops/reference/operator-panel.md
git commit -F - <<'EOF'
router-ops skill: interface and operator-panel references

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 14: `part-setup.md` and `tool-setup.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/part-setup.md`
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/tool-setup.md`

**Interfaces:**
- Consumes: F-key notation from `interface.md` (Task 13).

- [ ] **Step 1: Extract**

```bash
R=docs/official/centroid-cnc12-router-operator-manual.pdf
pdftotext -layout -f 51 -l 65 $R -   # Ch 4
pdftotext -layout -f 66 -l 82 $R -   # Ch 5
```

- [ ] **Step 2: Write `part-setup.md`**

`Source: Router Manual Ch 4.` `##` per §4.1-§4.10: manual, laser, probe, plate and auto zero; WCS; CSR; TWCS. §4.5 probe setup gives the operator procedure only, with a pointer to Router Manual Ch 9, p.104 for probing cycles.

- [ ] **Step 3: Write `tool-setup.md`**

`Source: Router Manual Ch 5.` `##` per §5.1-§5.4: offset library fields, tool library fields, tool life management and laser setup, with field names verbatim.

- [ ] **Step 4: Verify**

Run the standard checks (S2 may still flag only the index files from Task 13). Then:
```bash
D=.claude/skills/centroid-cnc12-router-ops/reference
for s in $(seq 1 10); do grep -q "§4\.$s[,)]" $D/part-setup.md || echo "missing §4.$s"; done
for s in 1 2 3 4; do grep -q "§5\.$s[,)]" $D/tool-setup.md || echo "missing §5.$s"; done
```
Expected: no `missing` lines.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/part-setup.md .claude/skills/centroid-cnc12-router-ops/reference/tool-setup.md
git commit -F - <<'EOF'
router-ops skill: part-setup and tool-setup references

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 15: `running-jobs.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/running-jobs.md`

**Interfaces:**
- Consumes: F4 Run and F7 Utility rows from `interface.md` (Task 13).

- [ ] **Step 1: Extract**

```bash
pdftotext -layout -f 83 -l 92 docs/official/centroid-cnc12-router-operator-manual.pdf -   # Ch 6-7
```

- [ ] **Step 2: Write `running-jobs.md`**

`Source: Router Manual Ch 6, Ch 7.` `##` per §6.1-§6.7 (run screen, run-time graphics, canceling, resuming, run menu, power feed, communications stress test), then `## Utility menu` (Ch 7, p.88-91) with every softkey in a table.

- [ ] **Step 3: Verify**

Run the standard checks (S2 may still flag only the index files). Then:
```bash
F=.claude/skills/centroid-cnc12-router-ops/reference/running-jobs.md
for s in $(seq 1 7); do grep -q "§6\.$s[,)]" $F || echo "missing §6.$s"; done
grep -c 'Ch 7' $F
```
Expected: no `missing` lines; the Ch 7 count is at least 1.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/running-jobs.md
git commit -F - <<'EOF'
router-ops skill: running-jobs reference

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 16: `g-code-index.md` and `m-code-index.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/g-code-index.md`
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/m-code-index.md`

**Interfaces:**
- Produces: link targets used by `interface.md` (Task 13). Row format: `| Code | Name | Summary | Ref |`, where Ref is exactly `§12.N, p.X` or `§13.N, p.X`.

- [ ] **Step 1: Extract**

```bash
R=docs/official/centroid-cnc12-router-operator-manual.pdf
pdftotext -layout -f 244 -l 280 $R -   # Ch 12, 48 sections
pdftotext -layout -f 281 -l 307 $R -   # Ch 13, 69 sections
```

- [ ] **Step 2: Write `g-code-index.md`**

Header: `# G-code index` then `Source: Router Manual Ch 12 (§12.1-§12.48, p.243-279). One row per code; the Ref column gives the section with full syntax.` Then the table: one row per code, so a section naming several codes (e.g. §12.3 G02 & G03, §12.28 canned cycles) yields one row per code sharing the Ref. Summary is one line in your own words, and must contain no syntax the manual does not print. After the table, add `## Modal notes` only for facts the chapter states explicitly, each cited.

- [ ] **Step 3: Write `m-code-index.md`**

Same shape from Ch 13: `Source: Router Manual Ch 13 (§13.1-§13.69, p.280-306).` §13.1 (summary) and §13.2 (macro M-functions) become a short preamble with their Refs. Rows cover every M-code from §13.3 onward, including M25/M26 (§13.17-§13.18), M91/M92, M94/M95 (§13.28, p.290), M294/M295 (§13.63-§13.64, p.304) and M297/M298. For M94/M95 and M100/M101, add "see `centroid-plc-programming` [resources.md](../../centroid-plc-programming/reference/resources.md)".

- [ ] **Step 4: Verify completeness**

```bash
D=.claude/skills/centroid-cnc12-router-ops/reference
for n in $(seq 1 48); do grep -q "| §12\.$n, p\.[0-9]* |" $D/g-code-index.md || echo "missing §12.$n"; done
for n in $(seq 3 69); do grep -q "| §13\.$n, p\.[0-9]* |" $D/m-code-index.md || echo "missing §13.$n"; done
grep -q '§13\.1,' $D/m-code-index.md && grep -q '§13\.2,' $D/m-code-index.md && echo preamble-ok
```
Expected: no `missing` lines; `preamble-ok`. Run the standard checks. S2 must now pass fully.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/g-code-index.md .claude/skills/centroid-cnc12-router-ops/reference/m-code-index.md
git commit -F - <<'EOF'
router-ops skill: complete G-code and M-code indexes

Every Ch 12 (48) and Ch 13 (69) section resolves to a row, so no code
lookup dead-ends.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 17: `parameter-index.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/parameter-index.md`

**Interfaces:**
- Produces: the machine-parameter lookup that `centroid-plc-programming/reference/system-variables.md` defers to (as a manual citation; Task 19 upgrades it to a link). Row format: `| Parameter | Name | Summary | Ref |`, where Ref is `§15.7.N, p.X`.

- [ ] **Step 1: Extract and list sections**

```bash
R=docs/official/centroid-cnc12-router-operator-manual.pdf
pdftotext -layout -f 321 -l 397 $R ch157.txt
grep -oE '^\s*15\.7\.[0-9]+ +.*' ch157.txt | sed 's/^ *//' > ch157_sections.txt
wc -l ch157_sections.txt   # expect 287 (15.7.1 bit-mapped intro + 15.7.2-15.7.287)
```
`ch157.txt` and `ch157_sections.txt` are scratch; delete them before committing.

- [ ] **Step 2: Write `parameter-index.md`**

Header: `# Machine parameter index` then `Source: Router Manual §15.7 (p.320-396). Parameters can also be set with G10 or #variable assignment, and many are set by the Acorn Wizard (§15.7, p.320).` Then `## Bit-mapped parameters`, which explains Value = 2^bit and the adding example (§15.7.1, p.320-321). Then the table: one row per §15.7.2-§15.7.287 section. A section heading a parameter range (e.g. "Parameters 11-13") gets one row with that range. Summary is one line; for bit-mapped parameters write `Bit-mapped; see manual`. The page is the printed page where the section starts.

- [ ] **Step 3: Verify completeness**

```bash
F=.claude/skills/centroid-cnc12-router-ops/reference/parameter-index.md
for n in $(seq 2 287); do grep -q "| §15\.7\.$n, p\.[0-9]* |" $F || echo "missing §15.7.$n"; done
grep -q '§15\.7\.1,' $F && echo bitmap-ok
rm -f ch157.txt ch157_sections.txt
```
Expected: no `missing` lines; `bitmap-ok`. Run the standard checks.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/parameter-index.md
git commit -F - <<'EOF'
router-ops skill: machine parameter index

All 286 parameter sections of Router Manual §15.7 indexed with page.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 18: `messages-index.md`

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/reference/messages-index.md`

**Interfaces:**
- Produces: row format `| Code | Message | Meaning | Ref |`, where Ref is `§16.N, p.X`.

- [ ] **Step 1: Extract and list codes**

```bash
R=docs/official/centroid-cnc12-router-operator-manual.pdf
pdftotext -layout -f 436 -l 451 $R ch16.txt
grep -oE '^\s*[0-9]{3,4} ' ch16.txt | tr -d ' ' | sort -u > ch16_codes.txt
wc -l ch16_codes.txt
```

- [ ] **Step 2: Write `messages-index.md`**

Header: `# CNC12 message index` then `Source: Router Manual Ch 16 (§16.1-§16.11, p.435-450).` One `##` per §16.1-§16.11 with its Ref, each holding a table of that section's messages: numeric code, message text verbatim, one-line meaning condensed from "Cause & Effect", and Ref. Keep the manual's "Action" text only when it is not "No action required."

- [ ] **Step 3: Verify completeness**

```bash
F=.claude/skills/centroid-cnc12-router-ops/reference/messages-index.md
grep -oE '^\| [0-9]{3,4} ' $F | tr -d '| ' | sort -u > idx_codes.txt
comm -23 ch16_codes.txt idx_codes.txt
for n in $(seq 1 11); do grep -q "§16\.$n," $F || echo "missing §16.$n"; done
```
Expected: no `missing` lines. `comm` prints codes in the chapter but not the index. For each one, look at its line in `ch16.txt`. If it is a real message code, add it. If it is not (e.g. a number wrapped from prose), leave it out and list it in the commit body. Then `rm ch16.txt ch16_codes.txt idx_codes.txt` and run the standard checks.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-cnc12-router-ops/reference/messages-index.md
git commit -F - <<'EOF'
router-ops skill: CNC12 message index

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```
If Step 3 excluded any numbers, list them in the body above the trailer lines as `Excluded non-message numbers from Ch 16 extraction: ...`.

---

### Task 19: `SKILL.md`, back-links, stage verification, PR

**Files:**
- Create: `.claude/skills/centroid-cnc12-router-ops/SKILL.md`
- Modify: `.claude/skills/centroid-plc-programming/reference/system-variables.md` (parameter citation becomes a link)
- Modify: `.claude/skills/centroid-acorn-install/SKILL.md` ("when not" names router-ops for operating the control)
- Modify: `README.md` (add a row)

**Interfaces:**
- Consumes: Tasks 13-18.
- Produces: skill `centroid-cnc12-router-ops`, which Task 22 links to.

- [ ] **Step 1: Write `SKILL.md`**

Frontmatter:
```yaml
---
name: centroid-cnc12-router-ops
description: Use when operating Centroid CNC12 Router software on Acorn, AcornSix, or Hickory - main screen and F1-F10 menus, machine home, jog panel/MPG/VCP/keyboard shortcuts, setting part zeros and WCS, offset and tool libraries, running, canceling and resuming jobs, the Utility menu - and for looking up any router G-code, M-code, machine parameter, or CNC12 message by number. Source: CNC12 Router Operators Manual v5.42+.
---
```
Body sections:
- **When to use / when not:** wiring and Wizard -> `centroid-acorn-install`; PLC -> `centroid-plc-programming`.
- **Essentials:** `c:\cncr`; homing via `cncm.hom`; F-key map summary.
- **Reference router:** 9 rows.
- `## Topics without a reference file`: a table with manual pointers: Digitizing Ch 8 p.92; Probing Ch 9 p.104; Intercon Ch 10 p.114; macro programming Ch 11 p.196; ATC Ch 14 p.307; configuration menus Ch 15 p.310 (parameters -> [parameter-index.md](reference/parameter-index.md)); Plasma CNC12 parameters §15.23 p.434; additional resources Ch 17 p.451; file and input glossaries Ch 18 p.454.
- **Useful resources:** manual URL and forum.

- [ ] **Step 2: Back-links**

In `.claude/skills/centroid-plc-programming/reference/system-variables.md`, replace the line citing `Router Manual §15.7, p.320` with:
```markdown
Machine parameter meanings: `centroid-cnc12-router-ops` [parameter-index.md](../../centroid-cnc12-router-ops/reference/parameter-index.md) (Router Manual §15.7, p.320).
```
In `.claude/skills/centroid-acorn-install/SKILL.md` "When not", add:
```markdown
For operating the control (menus, jogging, part zero, running jobs) and G/M-code, parameter, or message lookups, use `centroid-cnc12-router-ops` ([SKILL.md](../centroid-cnc12-router-ops/SKILL.md)).
```

- [ ] **Step 3: Add the README row**

```markdown
| [`centroid-cnc12-router-ops`](.claude/skills/centroid-cnc12-router-ops/SKILL.md) | CNC12 Router operation plus G-code, M-code, parameter and message indexes |
```

- [ ] **Step 4: Stage verification**

Run the standard checks. Confirm no Acroloc sibling-skill names survived:
```bash
grep -rn 'cnc12-gmcodes\|cnc12-config\|intercon-probing\|cnc12-operating' .claude/skills
```
Expected: no output. Spot-check 5 citations:
```bash
grep -rhoE '§[0-9]+(\.[0-9]+)*, p\.[0-9]+' .claude/skills/centroid-cnc12-router-ops | sort -u | shuf -n 5 --random-source=<(yes)
```
For each, run `pdftotext -layout -f <p+1> -l <p+1> docs/official/centroid-cnc12-router-operator-manual.pdf -` and confirm. Record results.

- [ ] **Step 5: Commit, push, PR**

```bash
git add .claude/skills/centroid-cnc12-router-ops/SKILL.md .claude/skills/centroid-plc-programming/reference/system-variables.md .claude/skills/centroid-acorn-install/SKILL.md README.md
git commit -F - <<'EOF'
router-ops skill: SKILL.md router and cross-skill links

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
git push -u origin skill/centroid-cnc12-router-ops
gh pr create --base main --title "Skill: centroid-cnc12-router-ops" --body "$(cat <<'EOF'
## Summary
- `centroid-cnc12-router-ops` from the CNC12 Router Operators Manual v5.42+: full daily-operation references (Ch 1-7).
- Complete indexes: G-codes (48 sections), M-codes (69), machine parameters (286), CNC12 messages (Ch 16).
- Topics without a reference file point to manual chapter and page; no pointers to unbuilt skills.
- acorn-install and plc-programming now link here.

## Verification
- Standard checks S1-S5 pass; index completeness loops report no missing sections.
- Spot-checked citations: <paste the 5 citations with pass/fix notes>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
)"
```
Replace the placeholder line with real results. **Stop point:** wait for merge.

---

## Stage 5: `centroid-vcp` (branch `skill/centroid-vcp`)

Fork source: `/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-vcp/`. Source manual: `docs/official/centroid_vcp_users_manual.pdf` (printed = PDF). Manual sections: Introduction 2, Button Grid Layout 6, VCP user editable files 7, Move or delete a button 8, Button graphics location and format 11, Change button graphics and VCP background 12, LED indicator color 17, Swap image when clicked 18, Swap image when function activated 20, Create a new button 21, Logos and icons 26, Border and backgrounds 30, Hover/click and touch effects 31, Run a macro / launch an app 32, BIG buttons 42, Display data with PLC words 44, Troubleshooting 54, Special cases 60, Resources 63.

**Fork procedure (every Stage 5 file):**
- Copy the Acroloc file.
- Cite each manual-backed fact as `(VCP Manual p.N)`.
- Replace `c:\cncm` paths with `c:\cncr` wherever the manual gives a CNC12-directory path. Record that the manual's path examples are mill paths if it only shows `cncm`.
- Delete references to `acroloc_retro_vcp_skin`, `tools/vcpgen.py`, `coolant_pump`, "this repo" and `acroloc-s10`.
- Board-agnostic field notes (Svg2Xaml subset, text-anchor ignored, SVG size tracks artboard, `image_on` polarity, options screen rewrites skin, ASCII+CRLF, restart to reload, bisect with minimal skins, `<type>Float</type>` reads the FW register) stay, labeled `Field-verified (CNC12, 2026-07)`, unless the manual states the same thing, in which case cite the manual instead.
- Acroloc-skin-specific measurements (retro skin cell sizes) are deleted.

### Task 20: `skin-and-grid.md`, `button-anatomy.md`, `visual-states.md`

**Files:**
- Create: `.claude/skills/centroid-vcp/reference/skin-and-grid.md` (fork)
- Create: `.claude/skills/centroid-vcp/reference/button-anatomy.md` (fork)
- Create: `.claude/skills/centroid-vcp/reference/visual-states.md` (fork)

**Interfaces:**
- Produces: the layout, button and visual-state references routed from `SKILL.md` (Task 22).

- [ ] **Step 1: Branch, copy, extract**

```bash
git switch main && git pull --ff-only && git switch -c skill/centroid-vcp
mkdir -p .claude/skills/centroid-vcp/reference
A=/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-vcp/reference
cp $A/skin-and-grid.md $A/button-anatomy.md $A/visual-states.md .claude/skills/centroid-vcp/reference/
V=docs/official/centroid_vcp_users_manual.pdf
pdftotext -layout -f 2 -l 10 $V -    # intro, grid, editable files, move/delete
pdftotext -layout -f 11 -l 25 $V -   # graphics, LED, swaps, create button
pdftotext -layout -f 26 -l 31 $V -   # logos, borders, hover/touch
```

- [ ] **Step 2: Re-source the three files**

Apply the fork procedure:
- `skin-and-grid.md` <- p.2-10 (and p.30 if it covers skin-level background).
- `button-anatomy.md` <- p.11-16 and p.21-25.
- `visual-states.md` <- p.17-20 and p.26-31.

- [ ] **Step 3: Verify**

Run the standard checks. S2 may flag links to `actions.md`, `advanced.md` or `troubleshooting.md` until Task 21; note them, but nothing else may fail. Then:
```bash
D=.claude/skills/centroid-vcp/reference
grep -c 'VCP Manual p\.' $D/skin-and-grid.md $D/button-anatomy.md $D/visual-states.md
grep -rniE 'cncm|retro|vcpgen|coolant_pump|this repo' $D/skin-and-grid.md $D/button-anatomy.md $D/visual-states.md
```
Expected: each count is at least its file's `##` count. Any second-grep hit is a quoted manual mill path with a note; otherwise fix it.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-vcp/reference/skin-and-grid.md .claude/skills/centroid-vcp/reference/button-anatomy.md .claude/skills/centroid-vcp/reference/visual-states.md
git commit -F - <<'EOF'
vcp skill: re-sourced skin, button and visual-state references

Forked from Acroloc-Centroid, re-cited against VCP Manual rev28; Acroloc
skin specifics dropped, board-agnostic field notes labeled.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 21: `actions.md`, `advanced.md`, `troubleshooting.md`

**Files:**
- Create: `.claude/skills/centroid-vcp/reference/actions.md` (fork)
- Create: `.claude/skills/centroid-vcp/reference/advanced.md` (fork)
- Create: `.claude/skills/centroid-vcp/reference/troubleshooting.md` (fork)

**Interfaces:**
- Consumes: `centroid-plc-programming` (merged) for PLC-bit and SV links.

- [ ] **Step 1: Copy and extract**

```bash
A=/home/bwarner/github/Acroloc-Centroid/.claude/skills/centroid-vcp/reference
cp $A/actions.md $A/advanced.md $A/troubleshooting.md .claude/skills/centroid-vcp/reference/
V=docs/official/centroid_vcp_users_manual.pdf
pdftotext -layout -f 32 -l 41 $V -   # macros, apps
pdftotext -layout -f 42 -l 53 $V -   # big buttons, PLC words
pdftotext -layout -f 54 -l 64 $V -   # troubleshooting, special cases, resources
```

- [ ] **Step 2: Re-source the three files**

Apply the fork procedure:
- `actions.md` <- p.32-41. Replace `acroloc-s10` pointers for "which skin events this machine uses" with the manual's method for finding event numbers. Point PLC-bit questions to `centroid-plc-programming`.
- `advanced.md` <- p.42-53 and p.60-62. Keep the "Field notes (retro-skin work, 2026-07)" facts that are board-agnostic, relabeled `Field-verified (CNC12, 2026-07)`, and drop the "retro-skin" wording.
- `troubleshooting.md` <- p.54-59.

- [ ] **Step 3: Verify**

Run the standard checks; S2 must now pass fully. Then:
```bash
D=.claude/skills/centroid-vcp/reference
grep -c 'VCP Manual p\.' $D/actions.md $D/advanced.md $D/troubleshooting.md
grep -rniE 'cncm|retro|vcpgen|coolant_pump|this repo' $D
grep -rn 'Field-verified' $D | grep -vE 'Field-verified \(CNC12, 20[0-9]{2}-[0-9]{2}\)'
```
Expected: counts as in Task 20; the second grep has only noted manual quotes; the third grep prints nothing (every label well-formed).

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/centroid-vcp/reference/actions.md .claude/skills/centroid-vcp/reference/advanced.md .claude/skills/centroid-vcp/reference/troubleshooting.md
git commit -F - <<'EOF'
vcp skill: re-sourced actions, advanced and troubleshooting references

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
```

---

### Task 22: `SKILL.md`, back-links, final verification, PR

**Files:**
- Create: `.claude/skills/centroid-vcp/SKILL.md`
- Modify: `.claude/skills/centroid-cnc12-router-ops/reference/operator-panel.md` (§2.25 VCP Introduction links to the VCP skill)
- Modify: `README.md` (add a row; mark sub-project 1 done)

**Interfaces:**
- Consumes: Tasks 20-21; all three earlier skills.

- [ ] **Step 1: Write `SKILL.md`**

Frontmatter:
```yaml
---
name: centroid-vcp
description: Use when customizing a Centroid CNC12 Virtual Control Panel (VCP) on Acorn or other CNC12 controls - moving, creating, or deleting buttons; button XML/SVG and graphics; LED colors and image swaps; logos, borders, backgrounds, hover/touch effects; wiring a button to a skin event, macro, app, or PLC bit; big buttons and live PLC-word displays; and diagnosing a VCP that will not load. Generic to the Centroid VCP. Source: VCP 2.0 Users Manual rev28 plus labeled field-verified notes.
---
```
Body: adapt Acroloc's `SKILL.md`. Keep the two-layer mental model and the button-XML table (re-cited). "When not" covers PLC -> `centroid-plc-programming` and operating -> `centroid-cnc12-router-ops`. `## Field-verified facts` lists only labeled items from Tasks 20-21. The "Navigating the VCP files" commands use `c:\cncr\resources\vcp` paths, with no machine button names. Drop the `acroloc-s10`, README and CLAUDE links.

- [ ] **Step 2: Back-link from router-ops**

In `.claude/skills/centroid-cnc12-router-ops/reference/operator-panel.md`, at the end of the §2.25 VCP Introduction section, add:
```markdown
To customize the VCP, use `centroid-vcp` ([SKILL.md](../../centroid-vcp/SKILL.md)).
```

- [ ] **Step 3: Update README**

Add the row:
```markdown
| [`centroid-vcp`](.claude/skills/centroid-vcp/SKILL.md) | VCP skins, buttons, visual states, actions, PLC-word displays, troubleshooting |
```
Change the sub-project 1 state cell to `Done: [spec](docs/superpowers/specs/2026-09-14-acorn-skill-set-design.md), [plan](docs/superpowers/plans/2026-09-14-acorn-skill-set.md)`.

- [ ] **Step 4: Final verification (whole spec)**

```bash
python3 tools/test_check_skill_links.py
python3 tools/check_skill_links.py
ls .claude/skills
```
Also run the standard checks S1-S5 across all skills. Expected: tests OK, checker OK, and exactly `centroid-acorn-install`, `centroid-cnc12-router-ops`, `centroid-plc-programming` and `centroid-vcp`. Spot-check 5 VCP citations:
```bash
grep -rhoE '\(VCP Manual p\.[0-9]+\)' .claude/skills/centroid-vcp | sort -u | shuf -n 5 --random-source=<(yes)
```
Confirm each against `pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`, and record the results.

- [ ] **Step 5: Commit, push, PR**

```bash
git add .claude/skills/centroid-vcp/SKILL.md .claude/skills/centroid-cnc12-router-ops/reference/operator-panel.md README.md
git commit -F - <<'EOF'
vcp skill: SKILL.md router; sub-project 1 complete

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
git push -u origin skill/centroid-vcp
gh pr create --base main --title "Skill: centroid-vcp" --body "$(cat <<'EOF'
## Summary
- `centroid-vcp` forked from Acroloc-Centroid and re-sourced against VCP 2.0 Users Manual rev28 5-14-26; router paths (`c:\cncr`); Acroloc skin content removed.
- Board-agnostic on-machine lessons kept as `Field-verified (CNC12, 2026-07)`.
- router-ops operator panel links here; README marks sub-project 1 done.

## Verification
- Standard checks S1-S5 pass across all four skills; link checker OK.
- Spot-checked citations: <paste the 5 citations with pass/fix notes>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_014QFNfJkDFXMYt6eVZURZmb
EOF
)"
```
Replace the placeholder line with real results. **Stop point:** wait for merge. Sub-project 1 is complete.
