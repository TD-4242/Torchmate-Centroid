# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Centroid CNC12 source and reference skills for a Torchmate CNC router on a Centroid **Acorn**
(step/direction, CNC12 Router, install directory `c:\cncr`). The repo holds the machine's CNC12
files as checked out on the control PC, generic Acorn knowledge skills, the vendor manuals they
cite, a link checker and generators for the custom VCP buttons. Plasma comes after the router works. See [README.md](README.md) for
status.

## Commands

```bash
python3 tools/check_skill_links.py       # links, #anchors, skill names; must print OK: and exit 0
python3 tools/test_check_skill_links.py  # checker tests (stdlib unittest)
python3 tools/test_check_skill_links.py CheckTreeTest.test_missing_anchor_is_reported  # one test
./compile.sh [-v] [-o out.plc]           # compile-check acorn_router_plc.src (Windows, or Wine)
python3 tools/gen_toggle_switches.py     # regenerate custom VCP art; also gen_cycle_buttons, gen_jog_speed_button, gen_jog_step_switch
```

Run `compile.sh` after any PLC edit, before loading the program on the machine. A Wizard save
rewrites `acorn_router_plc.src` and reorders its lines, so a plain diff is mostly noise. This
shows only the real changes (I/O reassignments and logic):

```bash
n() { tr -d '\r' | sed 's/[[:space:]]\+/ /g; s/^ //; s/ $//' | grep -v '^;\|^$' | LC_ALL=C sort; }
diff <(git show HEAD~1:acorn_router_plc.src | n) <(n < acorn_router_plc.src)
```

## This machine

Read these before "fixing" the config; each is deliberate.

- **Bench testing.** The PLC header's Wizard Drive and PLC Preset are still `Bench Test`.
- **Home switches only, no limit switches.** All home switches share `HomeAll` on `IN1`. `cncm.hom`
  prompts (`M225`) to square the gantry by hand, then homes Z+, Y+, X- with `M91`/`M92 L1` and `M26`.
  Over-travel protection is software travel limits only, so `LimitAll` is unassigned and
  `cncmcfg.xml` has zero limit inputs.
- **Paired X.** Axis 4 is slaved to X in software (`P554 = 1` in `cncm.prm.xml`); there is no 4th
  axis to jog.
- **I/O.** `IN1` `HomeAll`, `IN5` `DriveOk` (motor alarm outputs), `IN7` `ToolTouchOffTriggered`
  (touch probe), `IN8` `EStopOk`. `P911 = 16` inverts IN5 only;
  IN7's polarity is unconfirmed since this went from 80 to 16, so test the probe before relying on it.
  `OUT1` `NoFaultOut`, `OUT2` `SpinFWD` driving the trim-router contactor (M3 only; no speed or
  reverse control).
- **Motors.** Rattm TST57/TST60 integrated closed-loop steppers at 4000 counts/turn; manuals in
  `docs/official/`, and the README notes the DIP switch SW6 the manuals omit.

## Layout

- `acorn_router_plc.src` -- the Acorn Wizard-generated PLC source. The Wizard overwrites it unless
  its Custom PLC preference is set; see `centroid-plc-programming` before hand-editing.
- `cncm.hom`, `mfunc*.mac`, `plcmsg.txt`, `language.msg`, `mpucomp.exe` -- home program, M-code
  macros, PLC messages and the PLC compiler, from `c:\cncr`.
- `cncmcfg.xml`, `cncm.prm.xml`, `wizardsettings.xml` -- axis configuration, machine parameters
  (including axis pairing) and Wizard preferences.
- `resources/vcp/`, `resources/colors/` -- the VCP (skins, buttons, images, `options.xml`) and
  color themes.
- `resources/vcp/skins/torchmate_router_skin.vcp` -- the active skin, a trimmed copy of the stock
  rapid skin. `CustomVCP` is still `False`, so a Wizard save can switch back to the stock skin.
- `tools/gen_*.py` -- generate the custom VCP buttons and images; change the generator, not the SVG.
- `.claude/skills/` -- generic Centroid skills: `SKILL.md` plus `reference/*.md`.
- `docs/official/` -- vendor manuals: the Centroid manuals the skills cite and the motor manuals.
  The router manual PDF is gitignored; its `.md` stub holds the download command.
- `docs/superpowers/specs/`, `docs/superpowers/plans/` -- design specs and implementation
  plans. They are the historical record and may be annotated.

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

The repo root is also the control PC's `c:\cncr` checkout, so `.gitignore` ignores everything and
allowlists tracked paths. A new top-level tracked path needs its own `!/path` line, and on the
control PC `git add -A --dry-run` shows exactly what the allowlist will stage.

`.gitattributes` keeps CNC12's text files (`.src`, `.mac`, `.hom`, VCP `.xml`/`.vcp`/`.svg`) CRLF,
stores the Wizard XML files byte-for-byte (`-text`), and keeps `compile.sh` LF. Give any new
tracked file a line-ending rule there too.
