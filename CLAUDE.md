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
