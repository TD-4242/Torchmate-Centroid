# Design: Acorn skill set and repo foundation

**Date:** 2026-09-14
**Status:** Approved (design phase)

## Purpose

Torchmate-Centroid is the controller source for a Torchmate CNC router retrofitted with a
Centroid **Acorn**, modeled on `../Acroloc-Centroid` (an ALLIN1DC mill). The machine is
partly installed and its CNC12 files are not yet available, so this first sub-project builds
the repo foundation and a set of **generic Centroid knowledge skills for Acorn**, the
counterpart of Acroloc's ALLIN1DC skills.

Sub-project sequence for the whole effort (each gets its own spec):

1. **Repo foundation + Acorn skill set** (this spec).
2. Router baseline: capture the Wizard-generated PLC, macros and config from the control PC.
3. Router customizations (VCP, homing/squaring, spindle relay, anything the Wizard cannot do).
4. Plasma: torch, THC and head switching, after the router is fully functional.

## Decisions (from brainstorming)

| Topic | Decision |
| --- | --- |
| Controller | Acorn (step/dir), CNC12 Router |
| Approach | **Fork and re-source**: start from Acroloc's skill structure, strip ALLIN1DC/Acroloc content, re-verify every retained fact against the Acorn/router sources |
| Skills | `centroid-acorn-install`, `centroid-plc-programming`, `centroid-cnc12-router-ops`, `centroid-vcp` |
| Router-ops depth | Full depth for daily operation (manual Ch 1-7); complete one-line indexes for G-codes, M-codes, machine parameters and messages |
| Sources | Current public manuals downloaded from centroidcnc.com |
| Git | `git init` on `main`; public GitHub repo `TD-4242/Torchmate-Centroid`, like Acroloc |
| Scope boundary | Skills are generic: no Torchmate machine content |

## Sources

Stored in `docs/official/`. Page citations use the **printed page number** in the manual's
footer, not the PDF page index. The PLC manual prints no page numbers, so its citations use
the PDF page index, written `PDF p.N`.

| File | Document | Revision | Pages | Tracked |
| --- | --- | --- | --- | --- |
| `centroid_acorn_install_manual.pdf` | Acorn CNC Installation Manual | rev6 11-9-23, CNC12 v5.0+ | 138 | yes (16 MB) |
| `paired_axes_acorn_user_guide.pdf` | Acorn CNC12 Axis Pairing and Squaring | rev19 10-27-25, CNC12 v5.2x+ | 41 | yes (21 MB) |
| `centroid_plc_programming_manual.pdf` | CNC12 PLC Programming Manual | rev8 07/24/26, CNC12 v5.x+ | 132 | yes (3 MB) |
| `centroid_vcp_users_manual.pdf` | VCP 2.0 Users Manual | rev28 5-14-26, CNC12 v5.22+ | 64 | yes (12 MB) |
| `centroid-cnc12-router-operator-manual.pdf` | CNC12 Router Operators Manual | CNC12 v5.42+, created 2026-07-06 | 511 | **no** (63 MB, gitignored) |

Download URLs (centroidcnc.com returns HTTP 406 to curl's default headers; send a browser
`User-Agent`):

- `https://www.centroidcnc.com/centroid_diy/downloads/acorn_documentation/centroid_acorn_install_manual.pdf`
- `https://www.centroidcnc.com/centroid_diy/downloads/acorn_documentation/paired_axes_acorn_user_guide.pdf`
- `https://www.centroidcnc.com/centroid_diy/downloads/centroid_plc_programming_manual.pdf`
- `https://www.centroidcnc.com/centroid_diy/downloads/centroid_vcp_users_manual.pdf`
- `https://www.centroidcnc.com/centroid_diy/downloads/operator_manuals/centroid-cnc12-router-operator-manual.pdf`

The router manual is represented in git by `docs/official/centroid-cnc12-router-operator-manual.md`,
a stub giving its URL, revision and page count, matching how Acroloc handles its 57 MB mill
manual. Acroloc's PLC manual copy (rev7, 7-18-23) is **not** reused; the current download
supersedes it.

## Repo foundation

- **`.gitignore`**: Acroloc's ignore-everything allowlist, because the repo root will double as
  the CNC12 install directory. Un-ignore `.claude/`, `docs/`, `tools/` (minus `__pycache__/`),
  `.gitignore`, `.gitattributes`, `CLAUDE.md`, `README.md`, `LICENSE.md`. Explicitly ignore
  the router manual PDF and `.superpowers/`. PLC/macro/control-PC files are added to the
  allowlist in sub-project 2.
- **`.gitattributes`**: `*.pdf binary`, `*.exe binary`.
- **`LICENSE.md`**: Acroloc's wording (MIT for original work; vendor manuals remain Centroid's).
- **`README.md`**: what the repo is, the sub-project sequence, the skill list.
- **`CLAUDE.md`**: repo purpose and the skill conventions below.
- **GitHub**: public `git@github.com:TD-4242/Torchmate-Centroid.git` already exists (blank) and is
  set as `origin`; the foundation step pushes `main`.
- **Not in this sub-project**: `compile.sh`, `mpucomp.exe`, `plcfmt.py`, `vcpgen.py`. They
  operate on a `.src` and arrive with sub-project 2.

### Link checker

`tools/check_skill_links.py`, stdlib only, with `tools/test_check_skill_links.py` (`unittest`).

- Scans `.claude/skills/**/*.md`, `CLAUDE.md` and `README.md`.
- Every relative Markdown link (anchor stripped; `http(s):` and `mailto:` skipped) must resolve
  to an existing file.
- Every backticked token matching `^centroid-[a-z0-9-]+$` must name a directory in
  `.claude/skills/`.
- Prints each miss as `path:line: reason`; exits 1 on any miss, 0 when clean.

## Skill conventions

Written into `CLAUDE.md` and applied to every skill:

1. **Generic.** No Torchmate machine content. A later machine skill links to these.
2. **Sourced.** Every factual statement cites its document and section/page, e.g.
   `(Acorn Install §6.7, p.81)`. A fact that cannot be cited is dropped, not carried over.
3. **Field-verified exception.** A retained Acroloc lesson not found in any manual is kept only if
   it is board-agnostic, and is labeled `Field-verified (CNC12, <date from the Acroloc skill>)`.
4. **No dangling pointers.** A skill names only skills that exist in `.claude/skills/`. Topics
   without a skill point to the manual chapter and page instead.
5. **Current state.** Describe what the software does now; no tombstones.
6. **Shape.** `SKILL.md` (frontmatter, when to use / when not, essentials, reference router
   table, useful resources) plus `reference/*.md` at roughly 100-250 lines. Index files are
   exempt from the length guide.
7. **Paths.** CNC12 Router's install directory is `c:\cncr` (Router Manual §1.8, p.13).

## Skill 1: `centroid-acorn-install`

New, in the shape of Acroloc's `centroid-allin1dc-install`. Sources: Acorn Install Manual,
Axis Pairing guide.

| File | Source | Contents |
| --- | --- | --- |
| `reference/hardware.md` | Ch 1, Ch 2, App D | Kit contents and part numbers, board I/O, relay board, power supply, power/heartbeat LEDs |
| `reference/software-setup.md` | Ch 3, Ch 4, App A | Windows 10/11 config, CNC12 install, license file, comms stress test, configuration reports, spindle bench test |
| `reference/wiring.md` | Ch 5 | Cabinet layout, inputs/outputs, +24VDC jumper, E-stop, axis drives, home/limit switches, spindle, spindle encoder |
| `reference/wizard.md` | Ch 6 (except 6.7) | Every Wizard page: drive type, input/output definitions, axis config, homing/travel, spindle, touch devices, peripherals/WMPG, DB25, preferences including **Custom PLC** (stops the Wizard overwriting a custom PLC), VCP aux keys, lube |
| `reference/axis-pairing.md` | Ch 6.7, Pairing guide | Hardware vs software pairing, manual vs automatic squaring, slaved home input, Pro license requirement, M294/M295 (v5.4+) |
| `reference/commissioning.md` | Ch 7 | Motor test, coarse and fine turns-ratio calibration, backlash compensation, software travel limits |
| `reference/troubleshooting.md` | App B, App C | Symptom -> fix, support and knowledge-base pointers |

No `parameters.md`: Acorn configuration is Wizard-driven, and the machine-parameter index lives
in `centroid-cnc12-router-ops`.

## Skill 2: `centroid-plc-programming`

Forked from Acroloc. Source: CNC12 PLC Programming Manual (2026-07-24).

| File | Change |
| --- | --- |
| `reference/syntax.md` | Re-verify against the current manual |
| `reference/resources.md` | Replace ALLIN1DC I/O ranges with Acorn I/O addressing; keep macro<->PLC access (`#(60000+n)`, `M94`/`M95`) after re-verifying |
| `reference/system-variables.md` | Re-verify each `SV_*` entry against the current manual; drop uncited entries |
| `reference/messages.md` | Re-verify encoding and `plcmsg.txt` format; drop Acroloc worked examples in favor of manual examples |
| `reference/acorn-plc.md` | **New.** The Wizard-generated PLC, the Custom PLC preference, and the Acorn-specific statements in the PLC manual |
| `reference/examples-index.md` | **Omitted.** Acroloc's index lists ALLIN1DC projects only; an Acorn index waits for sub-project 2, which provides Acorn PLC sources to index |

## Skill 3: `centroid-cnc12-router-ops`

Structure forked from Acroloc's `centroid-cnc12-operating`, content from the Router Manual.

| File | Source | Depth |
| --- | --- | --- |
| `reference/interface.md` | Ch 1, Ch 3 | Full: main screen, conventions, machine home, F1-F10 menus |
| `reference/operator-panel.md` | Ch 2 | Full: jog panel, overrides, spindle/coolant keys, VCP intro, keyboard jog and shortcuts |
| `reference/part-setup.md` | Ch 4 | Full: part zeros (manual, laser, probe, plate, auto zero), WCS, CSR, TWCS |
| `reference/tool-setup.md` | Ch 5 | Full: offset library, tool library, tool life, laser setup |
| `reference/running-jobs.md` | Ch 6, Ch 7 | Full: run screen, graphics, cancel/resume, run menu, power feed, stress test, utility menu |
| `reference/g-code-index.md` | Ch 12 | Every G-code: code, name, one line, section and page |
| `reference/m-code-index.md` | Ch 13 | Every M-function, same shape (includes M25/M26, M91/M92, M294/M295, M297/M298) |
| `reference/parameter-index.md` | Ch 15.7 | Every machine parameter: number, name, one line, page |
| `reference/messages-index.md` | Ch 16 | Every startup, fault, syntax and configuration message: text, one-line meaning, page |

`SKILL.md` gives chapter and page pointers, with no reference file, for: Digitizing (Ch 8),
Probing (Ch 9), Intercon (Ch 10), macro programming (Ch 11), ATC (Ch 14), configuration menus
other than parameters (Ch 15), and Plasma CNC12 parameters (§15.23).

## Skill 4: `centroid-vcp`

Forked from Acroloc. Source: VCP 2.0 Users Manual rev28.

- Keep the six reference files (`actions`, `advanced`, `button-anatomy`, `skin-and-grid`,
  `troubleshooting`, `visual-states`); re-verify each against rev28.
- Replace mill paths (`c:\cncm`) with `c:\cncr`; remove Acroloc skin and retro-theme references.
- Keep board-agnostic hands-on lessons under convention 3; drop any tied to Acroloc's skin.

## Build sequence

One PR per step, each passing verification before the next starts:

1. Foundation: `.gitignore`, `.gitattributes`, `LICENSE.md`, `README.md`, `CLAUDE.md`, sources
   and router-manual stub, link checker plus tests, first push of `main` to `origin`.
2. `centroid-acorn-install`
3. `centroid-plc-programming`
4. `centroid-cnc12-router-ops`
5. `centroid-vcp`

## Verification

No executable code beyond the link checker, so verification is structural:

1. `python3 tools/test_check_skill_links.py` passes.
2. `python3 tools/check_skill_links.py` exits 0.
3. Each `SKILL.md` has valid frontmatter (`name` matching its directory, and `description`).
4. At least 5 facts per skill spot-checked against the cited page.
5. `grep -rniE 'acroloc|torchmate' .claude/skills` returns nothing. `ALLIN1DC`/`MPU11` appear
   only where a cited manual covers multiple boards.
6. Router-ops indexes are complete: entry counts match the manual's Ch 12 and Ch 13 section lists.
7. The tracked tree contains no router manual PDF (`git ls-files docs/official`).

## Non-goals

- Plasma (THC, torch, head switching) and the plasma operator manual.
- A Torchmate machine skill; it follows sub-project 2.
- An Acorn PLC examples index; it follows sub-project 2.
- PLC compile and format tooling.
- Separate G/M-code, configuration or Intercon/probing skills; router-ops indexes cover lookups.
- Changes to Acroloc-Centroid.
