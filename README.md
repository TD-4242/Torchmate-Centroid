# Torchmate-Centroid

Centroid CNC12 controller source and reference skills for a **Torchmate** CNC router
retrofitted with a Centroid **Acorn** controller. Plasma support follows once the router is
fully working. Modeled on [Acroloc-Centroid](https://github.com/TD-4242/Acroloc-Centroid).

## Status

| Sub-project | State |
| --- | --- |
| 1. Repo foundation + Acorn skill set | Done: [spec](docs/superpowers/specs/2026-09-14-acorn-skill-set-design.md), [plan](docs/superpowers/plans/2026-09-14-acorn-skill-set.md) |
| 2. Router baseline (Wizard PLC, macros, config from the control PC) | In progress: control-PC files committed |
| 3. Router customizations | Not started |
| 4. Plasma | Not started |

## Machine files

The repo root is also the control PC's `c:\cncr` checkout. `.gitignore` allowlists the machine
files; CNC12's binaries, parameters, jobs, logs and compiler output stay untracked.

| Path | Contents |
| --- | --- |
| `acorn_router_plc.src` | Acorn Wizard-generated PLC source |
| `cncm.hom`, `mfunc*.mac` | Home program and M-code macros |
| `plcmsg.txt`, `language.msg`, `mpucomp.exe` | PLC messages, message strings, PLC compiler |
| `resources/vcp/`, `resources/colors/` | VCP skins, buttons, images and `options.xml`; color themes |

## Reference skills

Generic Centroid knowledge for Acorn under `.claude/skills/`. Every fact cites the official
manual section and page. Skills land one per PR, and each adds its row here.

| Skill | Covers |
| --- | --- |
| [`centroid-acorn-install`](.claude/skills/centroid-acorn-install/SKILL.md) | Acorn hardware, wiring, Wizard, axis pairing, motion tuning, troubleshooting |
| [`centroid-plc-programming`](.claude/skills/centroid-plc-programming/SKILL.md) | PLC stage language, Acorn I/O, SV_* catalog, messages, Wizard-generated PLC |
| [`centroid-cnc12-router-ops`](.claude/skills/centroid-cnc12-router-ops/SKILL.md) | CNC12 Router operation plus G-code, M-code, parameter and message indexes |
| [`centroid-vcp`](.claude/skills/centroid-vcp/SKILL.md) | VCP skins, buttons, visual states, actions, PLC-word displays, troubleshooting |

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
    ./compile.sh [-v] [-o out.plc]            # compile-check acorn_router_plc.src (Windows, or Wine)
