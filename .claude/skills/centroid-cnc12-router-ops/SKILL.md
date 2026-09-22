---
name: centroid-cnc12-router-ops
description: "Use when operating Centroid CNC12 Router software on Acorn, AcornSix, or Hickory - main screen and F1-F10 menus, machine home, jog panel/MPG/VCP/keyboard shortcuts, setting part zeros and WCS, offset and tool libraries, running, canceling and resuming jobs, the Utility menu - and for looking up any router G-code, M-code, machine parameter, or CNC12 message by number. Source: CNC12 Router Operators Manual v5.42+."
---

# Centroid CNC12 Router Operation

## When to use / when not

Use this skill for **operating** Centroid CNC12 Router software on **Acorn, AcornSix, or
Hickory**: the main screen and F1-F10 menus, machine home, the hardware jog panel / MPG / VCP /
keyboard interface, setting part zeros and Work Coordinate Systems, the offset and tool
libraries, running/canceling/resuming jobs, and the Utility menu -- plus looking up any router
G-code, M-code, machine parameter, or CNC12 message by number. It is a faithful, generic capture
of the official **CNC12 Router Operators Manual** (v5.42+) -- not specific to any one machine.

**Do not use this skill** for Acorn hardware installation, wiring, or Wizard configuration -- use
`centroid-acorn-install` ([SKILL.md](../centroid-acorn-install/SKILL.md)).

**Do not use this skill** for PLC stage-language (`.src`) programming or macro-to-PLC interaction
-- use `centroid-plc-programming` ([SKILL.md](../centroid-plc-programming/SKILL.md)).

## Essentials

CNC12 Router installs to `c:\cncr` (Router Manual §1.8, p.13). On startup, before any job can
run, machine home must be set: if the machine has home/limit switches, reference marks, or safe
hard stops, `CYCLE START` runs the homing G-codes in `cncm.hom` from `c:\cncr`; by default that
file homes Z plus, then X minus, then Y plus (Router Manual §1.8, p.13). The Acorn Wizard
generates `cncm.hom` from its homing settings; see
[axis-pairing.md](../centroid-acorn-install/reference/axis-pairing.md).

The Options Window offers ten F1-F10 menus from the main screen (Router Manual §1.5, p.11):

| F-key | Menu |
| --- | --- |
| `F1` | Set Part Zeros |
| `F2` | Load Job |
| `F3` | MDI |
| `F4` | Run Job Options |
| `F5` | Tool/ATC |
| `F6` | Edit G-Code |
| `F7` | Utility |
| `F8` | Graph |
| `F9` | Smoothing |
| `F10` | Shut Down |

See [interface.md](reference/interface.md) for each menu's own sub-keys and full detail.

## Reference router

| Reference file | Look here when... |
| --- | --- |
| `reference/interface.md` | You need the DRO/message/status window layout, the machine-home procedure, or the F1-F10 main-screen menu map and each menu's sub-keys |
| `reference/operator-panel.md` | You need the hardware jog panel button functions, the default VCP button legend, or the keyboard jog panel and keyboard shortcut keys |
| `reference/part-setup.md` | You're setting part zeros (manually, by laser, by probe, or by touch plate), configuring Work Coordinate Systems, Coordinate System Rotation (CSR), or Transformed WCS |
| `reference/tool-setup.md` | You're working with the Offset Library (H/D values), the Tool Library, Tool Life Management, or PWM laser/spindle output setup |
| `reference/running-jobs.md` | You're starting, canceling, or resuming a job; using the Run menu, Power Feed, or the communications stress test; or navigating the Utility menu |
| `reference/g-code-index.md` | You need to look up a router G-code by number |
| `reference/m-code-index.md` | You need to look up a router M-code by number |
| `reference/parameter-index.md` | You need to look up a machine parameter by number |
| `reference/messages-index.md` | You need to look up a CNC12 status or error message by number |

The G-code, M-code, machine parameter, and CNC12 message indexes above are complete for the
chapters they cover -- G-codes (Router Manual Ch 12), M-codes (Ch 13), machine parameters (§15.7),
and CNC12 messages (Ch 16) -- not for the whole manual.

## Topics without a reference file

| Topic | Manual pointer |
| --- | --- |
| Digitizing | Router Manual Ch 8, p.92 |
| Probing | Router Manual Ch 9, p.104 |
| Intercon (conversational part programming) | Router Manual Ch 10, p.114 |
| Macro programming | Router Manual Ch 11, p.196 |
| ATC operation | Router Manual Ch 14, p.307 |
| Configuration menus (machine parameters are indexed in [parameter-index.md](reference/parameter-index.md)) | Router Manual Ch 15, p.310 |
| Plasma CNC12 parameters | Router Manual §15.23, p.434 |
| Additional resources | Router Manual Ch 17, p.451 |
| File and input glossaries | Router Manual Ch 18, p.454 |

## Useful resources

- Centroid manuals index (includes the CNC12 PLC Programming Manual):
  https://www.centroidcnc.com/centroid_diy/centroid_manuals.html (Router Manual §11.3.7, p.214)
- Centroid support forum, API discussion section: https://centroidcncforum.com/viewforum.php?f=72
  (Router Manual §1.11, p.16)
