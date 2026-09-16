# Acorn Wizard PLC Reference

Source: `docs/official/centroid_plc_programming_manual.pdf` (PLC Manual, rev8 07/24/26), PDF
p.6-11; `docs/official/centroid_acorn_install_manual.pdf` (Acorn Install), §6.19;
`docs/official/centroid-cnc12-router-operator-manual.pdf` (Router Manual), §1.8. The PLC Manual
prints no page numbers; citations below are PDF page numbers, verified with
`pdftotext -layout -f N -l N docs/official/centroid_plc_programming_manual.pdf -`. Router Manual
citations are printed page (PDF page = printed + 1).

---

## Same language, Wizard-generated program

Centroid's PLC programming language is the same across all current platforms — Oak, Allin1DC,
MPU11, Acorn, AcornSix and Hickory — with differences between them coming only from the board's
hardware feature set, not the language itself (PLC Manual, PDF p.11).

Acorn and AcornSix CNC12 use a control-configuration Wizard that creates the PLC program for the
control based on the Input/Output selections made in the Wizard's input and output menus. The
Wizard builds a "custom" PLC program by drag-and-drop assigning a list of canned PLC functions to
inputs and outputs, using the user's selections (PLC Manual, PDF p.6-8).

## Files

The Acorn Wizard uses a Universal Template PLC source program to build the custom Acorn PLC
program. The manual gives the template's path as:

```
cncm\resources\wizard\default\plc\acorn_universal_template.src
```

(PLC Manual, PDF p.8)

Source code for the Wizard-generated PLC program appears in the CNC12 installation's root
directory, for example `acorn_mill_plc.src` (PLC Manual, PDF p.8). The manual shows only the mill
example, with the mill's `cncm` directory prefix; it does not show a router example. CNC12
Router's install directory is `c:\cncr` (Router Manual §1.8, p.13), not `c:\cncm` — no manual page
gives the router-specific generated-PLC filename, so none is stated here.

## Hand-editing safely

Before hand-editing an Acorn PLC program, turn off the Wizard's automatic PLC program generation
so the Wizard does not overwrite the edit. The "Custom PLC" in-use setting is in the Wizard
Preferences menu (PLC Manual, PDF p.8) — see
[Custom PLC preference](../../centroid-acorn-install/reference/wizard.md#custom-plc-preference)
(Acorn Install §6.19, p.98).

## Tools

- **PLC Diagnostic screen** (virtual input/output LEDs):
  `https://www.centroidcnc.com/centroid_diy/downloads/acorn_documentation/cnc12_PLC_diagnostic_screen.pdf`
  (PLC Manual, PDF p.9-10)
- **PLC Detective** (real-time logic analyzer):
  `https://www.centroidcnc.com/downloads/centroid_PLC_detective_quickstart.pdf`
  (PLC Manual, PDF p.9-10)

## Board identification

`SV_DRIVE_TYPE_x (1-8)` reports the type of drive connected to each axis. Its values include
`13 = ACORN` and `24 = ACORNSIX` (PLC Manual, PDF p.110).
