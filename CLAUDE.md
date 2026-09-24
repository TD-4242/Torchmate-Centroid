# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Centroid CNC12 source and reference skills for a Torchmate CNC router on a Centroid **Acorn**
(step/direction, CNC12 Router, install directory `c:\cncr`). The repo holds the machine's CNC12
files as checked out on the control PC, generic Acorn knowledge skills, the vendor manuals they
cite, and a link checker. Plasma comes after the router works. See [README.md](README.md) for
status.

## Layout

- `acorn_router_plc.src` -- the Acorn Wizard-generated PLC source. The Wizard overwrites it unless
  its Custom PLC preference is set; see `centroid-plc-programming` before hand-editing.
- `cncm.hom`, `mfunc*.mac`, `plcmsg.txt`, `language.msg`, `mpucomp.exe` -- home program, M-code
  macros, PLC messages and the PLC compiler, from `c:\cncr`.
- `resources/vcp/`, `resources/colors/` -- the VCP (skins, buttons, images, `options.xml`) and
  color themes.
- `.claude/skills/` -- generic Centroid skills: `SKILL.md` plus `reference/*.md`.
- `docs/official/` -- vendor manuals the skills cite. The router manual PDF is gitignored; its
  `.md` stub holds the download command.
- `docs/superpowers/specs/`, `docs/superpowers/plans/` -- design specs and implementation
  plans. They are the historical record and may be annotated.
- `tools/check_skill_links.py` -- link checker (`python3 tools/test_check_skill_links.py`).
- `compile.sh` -- compile-checks `acorn_router_plc.src` with `mpucomp.exe`, natively or via Wine.
  Run it after any PLC edit, before loading the program on the machine.

## Skill conventions

1. **Generic.** No machine content in `.claude/skills/`; a machine skill will link to them.
2. **Sourced.** Every fact cites document and section/page. Uncitable facts are dropped.
3. **Field-verified exception.** A board-agnostic lesson no manual states is kept only when
   labeled `Field-verified (CNC12, YYYY-MM)`.
4. **Advisory exception.** Electrical-safety guidance that no manual states is allowed only as a
   line labeled `**Advisory (not in the manual):**`. Security and software advice stays as the
   manual gives it.
5. **No dangling pointers.** Name only skills that exist in `.claude/skills/`; otherwise cite
   the manual chapter and page. `python3 tools/check_skill_links.py` must exit 0.
6. **Current state.** Describe what the software does now; no tombstones.
7. **Shape.** `SKILL.md` (frontmatter, when to use / when not, essentials, reference router,
   useful resources) plus `reference/*.md` at roughly 100-250 lines; index files are exempt.
8. **Paths.** CNC12 Router lives in `c:\cncr`, not the mill's `c:\cncm`.

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
