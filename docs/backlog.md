# Torchmate Router — Backlog

Work waiting on a precondition. Legend: `[ ]` todo, `[~]` in progress, `[x]` done.

## After the PLC goes custom

These need hand edits to `acorn_router_plc.src`, so they wait until the Wizard configuration
is settled and the Wizard's **Custom PLC** preference is set (otherwise a Wizard save
overwrites the edits; see `centroid-plc-programming`, [acorn-plc.md](../.claude/skills/centroid-plc-programming/reference/acorn-plc.md)).

### Precondition

- [ ] **Home switches wired and configured.** Home-only switches (no limits): assign the home
  inputs in the Wizard, switch homing from Simple to switch-based (`cncm.hom`), and update the
  "No home or limit switches" note in `CLAUDE.md`.
- [ ] **Final Wizard pass, then set Custom PLC.** Leave the `Bench Test` preset, save the
  Wizard once more, commit the regenerated PLC as the custom baseline, then set Custom PLC.
  From then on a Wizard I/O change means regenerating and re-applying the items below by hand.

### Items

- [ ] **VCP run lamp.** The `cycle_start_pb` button lights its amber lens on `OUT1100`
  (`UnusedR9C4LED`), which the PLC declares but never drives. Add
  `IF SV_PROGRAM_RUNNING THEN (UnusedR9C4LED)`. Check on the machine whether the lamp should
  stay lit during Feed Hold.
- [ ] **VCP tool-number display.** Get the current tool number into a PLC word the VCP can show:
  call `M107` in the tool-change macro so the number reaches `SV_TOOL_NUMBER` (Router Manual
  §13.38, p.294), copy it into a free `W` word in the PLC, and add a `<plc_word>` display with a
  `TOOL` label to `torchmate_router_skin.vcp`. First test whether M6 alone sets
  `SV_TOOL_NUMBER` on this machine. The tool description cannot be shown: `<plc_word>` is
  numeric and `<text>` is static (VCP Manual pp.45-50).

For every PLC edit: run `./compile.sh`, review the change, then load it on the machine.
