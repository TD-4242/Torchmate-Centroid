---
name: centroid-plc-programming
description: "Use when writing, reading, or debugging Centroid CNC12 PLC stage-language source (.src) or M-code macro-to-PLC interaction on an Acorn - stage/scan execution, IF/THEN/SET/RST syntax, resource types and Acorn I/O addressing, the SV_* system-variable catalog, operator-message encoding and plcmsg.txt, and the Acorn Wizard-generated PLC (universal template, Custom PLC before hand-editing). Source: CNC12 PLC Programming Manual rev8 07/24/26."
---

# Centroid PLC Programming

## When to use / when not

Use this skill for PLC stage-language (`.src`) programming and macro-to-PLC interaction on a
Centroid **Acorn**: stage/scan execution and syntax, resource types and Acorn I/O addressing,
the `SV_*` system-variable catalog, operator-message encoding, and the Acorn Wizard-generated
PLC program.

**Do not use this skill** for Acorn hardware wiring or Wizard configuration-page fields -- use
`centroid-acorn-install` ([SKILL.md](../centroid-acorn-install/SKILL.md)).

## Language essentials

The PLC source file has two parts. The **definition section** (top) uses `Name IS Resource` to
bind a symbolic name to a hardware or internal resource; any definition after the first
`IF`/`THEN` is a compile-time error (PLC Manual, PDF p.17):

```
EStopOk_I IS INP11   ; PLC Manual, PDF p.17
Lube_O    IS OUT2    ; PLC Manual, PDF p.17
```

The rest of the program is a flat, sequential list of `IF`/`THEN` statements that runs top to
bottom every pass; logic inside a Stage (`STG`/`FSTG`) is skipped entirely while that Stage is
RST (PLC Manual, PDF p.30, p.16). Regular Stages run 50 times per second; Fast Stages or code
outside any Stage run up to 1000 times per second, provided the rest of the program finishes in
under 1ms (PLC Manual, PDF p.13, p.16). `STG1` is SET automatically at startup (PLC Manual, PDF
p.13).

Inputs and Timers are buffered for the whole pass; physical Output state is buffered too, but the
in-program image of the Outputs updates immediately, along with Memory Bits, Words, One-Shots,
Stages and System Variables, so a later line in the same pass sees an earlier line's write
(PLC Manual, PDF p.13).

Every action follows `THEN`, comma-separated: `SET`/`RST` turn a bit-type variable
unconditionally on or off, `(<bit-var>)` coils it to the condition, `<word> = <expr>` assigns a
Word or Timer, and `JMP <stage>` RSTs the current Stage and SETs another (PLC Manual, PDF
p.21-22). There is no `ELSE` keyword; the manual's stated workaround is a second line with the
condition negated by `!` (PLC Manual, PDF p.17). See [syntax.md](reference/syntax.md) for the
statement-form, operator and comment-style reference.

A macro reads PLC resource state through fixed variable ranges (for example `OUT` n at
`#(60000+n)`), and `M94`/`M95` set/reset `SV_M94_M95_1`-`128` for the PLC program to read -- see
[resources.md](reference/resources.md#macro---plc-access).

## Reference router

| Reference file | Look here when... |
| --- | --- |
| `reference/syntax.md` | You need statement syntax: `IF`/`THEN`, `SET`/`RST`/`JMP`, the output-coil `()` form, Logical/Relational/Arithmetic operators, comment style, or the manual's naming and layout conventions |
| `reference/resources.md` | You need a resource type (`INP`/`OUT`/`MEM`/`STG`/`FSTG`/`T`/`PD`/`W`/`DW`/`FW`/`DFW`), its address range, Acorn's physical I/O, the naming-suffix convention, or macro<->PLC access (`#(60000+n)`, `M94`/`M95`) |
| `reference/system-variables.md` | You need to look up or verify an `SV_*` system-variable name, its type, direction (CNC->PLC vs. PLC->CNC), or an Appendix H-K bit table |
| `reference/messages.md` | You need to encode or decode an operator-message constant (`value = type + 256 x msgNumber`), the `plcmsg.txt` format, or the manual's worked message example |
| `reference/acorn-plc.md` | You need the Acorn Wizard's universal-template path, where the Wizard-generated `.src` lands, how to turn on Custom PLC before hand-editing, or the PLC Diagnostic/PLC Detective tools |

Example PLC projects are not indexed here; the Acorn Wizard's own generated template is
described in [acorn-plc.md](reference/acorn-plc.md).

## Not covered here

- Compiler Errors (PLC Manual, PDF p.52-59).
- Keywords beyond the basic statement forms above: Indexes, Range `..`, DUMP, BTW/WTB, BCD/BIN,
  BITSET/BITRST/BITTST, LSHIFT/RSHIFT, and the math functions (PLC Manual, PDF p.20-28).
- SV and data-type names cannot be used as constant or variable labels (PLC Manual, PDF p.20).
- There are no bitwise operators (PLC Manual, PDF p.21).
- Standard PLC Program Layout, the manual's full worked example program (PLC Manual, PDF
  p.30-51).

## Useful resources

- PLC Diagnostic screen (virtual input/output LEDs):
  https://www.centroidcnc.com/centroid_diy/downloads/acorn_documentation/cnc12_PLC_diagnostic_screen.pdf
  (PLC Manual, PDF p.9-10)
- PLC Detective (real-time logic analyzer):
  https://www.centroidcnc.com/downloads/centroid_PLC_detective_quickstart.pdf
  (PLC Manual, PDF p.9-10)
