# Torchmate Router — Backlog

Work waiting on a precondition. Legend: `[ ]` todo, `[~]` in progress, `[x]` done.

## After the PLC goes custom

These need hand edits to `acorn_router_plc.src`, so they wait until the Wizard configuration
is settled and the Wizard's **Custom PLC** preference is set (otherwise a Wizard save
overwrites the edits; see `centroid-plc-programming`, [acorn-plc.md](../.claude/skills/centroid-plc-programming/reference/acorn-plc.md)).

### Precondition

- [x] **Home switches configured.** `HomeAll` on `IN1` with automatic homing and no limit switches
  (`9e27b11`, PR 17).
- [ ] **Confirm homing on the machine.** Run a full home, set the software travel limits, and
  confirm the touch probe's `IN7` polarity (`P911` no longer inverts it).
- [ ] **Final Wizard pass, then set Custom PLC.** Leave the `Bench Test` preset, save the
  Wizard once more, commit the regenerated PLC as the custom baseline, then set Custom PLC.
  From then on a Wizard I/O change means regenerating and re-applying the items below by hand.

### Items

- [ ] **VCP run lamp.** The `cycle_start_pb` button swaps the lit and unlit pushbutton housing
  on `MEM1020`, which the Wizard PLC leaves unused. Declare it (for example
  `RunLamp_M IS MEM1020`) and add `IF SV_PROGRAM_RUNNING THEN (RunLamp_M)`. Check on the
  machine whether the lamp should stay lit during Feed Hold.
- [ ] **VCP tool-number display.** Get the current tool number into a PLC word the VCP can show:
  call `M107` in the tool-change macro so the number reaches `SV_TOOL_NUMBER` (Router Manual
  §13.38, p.294), copy it into a free `W` word in the PLC, and add a `<plc_word>` display with a
  `TOOL` label to `torchmate_router_skin.vcp`. First test whether M6 alone sets
  `SV_TOOL_NUMBER` on this machine. The tool description cannot be shown: `<plc_word>` is
  numeric and `<text>` is static (VCP Manual pp.45-50).

For every PLC edit: run `./compile.sh`, review the change, then load it on the machine.
