# Centroid PLC Resource Types Reference

Source: `docs/official/centroid_plc_programming_manual.pdf` (PLC Manual, rev8 07/24/26) and
`docs/official/centroid-cnc12-router-operator-manual.pdf` (Router Manual). The PLC Manual prints
no page numbers; citations below are PDF page numbers, verified with
`pdftotext -layout -f N -l N docs/official/centroid_plc_programming_manual.pdf -`. Router Manual
citations are printed page (PDF page = printed + 1).

This file covers **what resource types exist**, their address ranges, Acorn's physical I/O, and
how macros and M-codes read or trigger PLC resources. It does not duplicate operator or
statement syntax — see [syntax.md](syntax.md) — or message encoding — see
[messages.md](messages.md).

---

## Resource Types

The `IS` keyword in the definition section binds a symbolic name to a hardware or internal
resource, given by its resource type and instance number. Every type has a fixed range
(PLC Manual, PDF p.13):

| Keyword | Type | Instance range | Notes |
|---------|------|----------------|-------|
| `INP` | Physical input bit | `INP1`-`INP1312` | Buffered at the start of each scan; the same value reads throughout the pass. |
| `OUT` | Physical output bit | `OUT1`-`OUT1312` | The in-program image updates immediately; a later line in the same pass sees the value an earlier line wrote. |
| `MEM` | Internal memory bit | `MEM1`-`MEM1024` | Not wired to hardware; updates immediately, like Outputs. |
| `STG` | Stage bit | `STG1`-`STG256` | `STG1` is SET at startup. Logic inside a Stage is skipped entirely while that Stage is RST (PLC Manual, PDF p.16). |
| `FSTG` | Fast stage bit | `FSTG1`-`FSTG256` | Behaves like `STG` but runs up to 1000 scans/s instead of the standard 50 scans/s, provided the rest of the program finishes under 1ms (PLC Manual, PDF p.16). |
| `T` | Timer | `T1`-`T128` | `T1`-`T64` before CNC12 v4.22, `T1`-`T128` from v4.22. Counts up in milliseconds to the stored value, then evaluates true until RST (PLC Manual, PDF p.15). Buffered at the start of the scan like Inputs. |
| `PD` | One-shot (positive differential) | `PD1`-`PD256` | SET on the coil line's rising edge; the same line's condition must go false to RST it before it can trigger again — holding a button down will not retrigger it (PLC Manual, PDF p.15). |
| `W` | 32-bit signed integer word | `W1`-`W128` | `W1`-`W88` "available for PLC Detective and G-code variables" (PLC Manual, PDF p.13). |
| `DW` | 64-bit signed integer | `DW1`-`DW128` | `DW1`-`DW22` "available for PLC Detective and G-code variables" (PLC Manual, PDF p.13). |
| `FW` | 32-bit floating-point word | `FW1`-`FW128` | `FW1`-`FW44` "available for PLC Detective and G-code variables" (PLC Manual, PDF p.13)[^fw-typo]. |
| `DFW` | 64-bit floating-point word | `DFW1`-`DFW128` | `DFW1`-`DFW22` "available for PLC Detective and G-code variables" (PLC Manual, PDF p.13). |

[^fw-typo]: PDF p.13 prints this range as `FW1-FDW44`, an evident typo; the Router Manual's
    independent macro-variable table (§11.2.16, p.205, `98001-98044 FW1-FW44`) confirms the
    intended range is `FW1`-`FW44`.

### Addressing form

Every resource is bound to a name with `Name IS Keyword n` in the definition section, before the
first `IF`/`THEN` — see [syntax.md](syntax.md#1-definition--name-is-resource) for the statement
form. Manual examples (PLC Manual, PDF p.14, p.17):

```
EStopOk_I    IS INP11   ; PLC Manual, PDF p.17
Lube_O       IS OUT2    ; PLC Manual, PDF p.17
Error_Code_W IS W10     ; PLC Manual, PDF p.14
BigNumber_DW IS DW3     ; PLC Manual, PDF p.14
```

## Acorn I/O

The Acorn has 8 physical inputs. They are sourcing 24VDC: the Acorn supplies +24VDC at the input
pin, and an external switch or sensor must sink it to `COM` to activate it — the "contact
closure to ground (COM)" method (Acorn Install §5.2, p.44). The Acorn has 8 relay outputs; each
output toggles one SPDT relay (Acorn Install §5.3, p.45).

> App D describes the same outputs differently: 8 open-collector drivers normally drive an
> external 8-relay board over ribbon cable (Acorn Install App D, p.126). Its I/O map lists these
> as the `H10` outputs, with output type `Open Collector`, not relay (Acorn Install App D, p.129).
> See [wiring.md](../../centroid-acorn-install/reference/wiring.md#outputs-53) for the full note.

See [wiring.md](../../centroid-acorn-install/reference/wiring.md#inputs-52) and
[wiring.md](../../centroid-acorn-install/reference/wiring.md#outputs-53) for terminal wiring, and
[hardware.md](../../centroid-acorn-install/reference/hardware.md#io-map) for the per-terminal
input and output tables.

The PLC Manual's own I/O appendix (App E) documents ALLIN1DC, DC3IOB, GPIO4D and PLC-expansion
I/O ranges but has no Acorn entry (PLC Manual, PDF p.121-123). No manual page states which
`INPn`/`OUTn` a given Acorn screw terminal maps to: the Acorn Wizard assigns the PLC `INP`/`OUT`
number for each function from the choices made in its input and output menus, rather than using
a fixed table (PLC Manual, PDF p.6). See [acorn-plc.md](acorn-plc.md) for how the Wizard builds
the program.

## System Variables (SV)

System Variables are predefined `SV_` names, not numbered like `INP`/`OUT`. Appendix D splits
them into two write-direction tables:

- **CNC Software Write-Controlled, 1-bit Boolean System Variables (CNC → PLC)** — includes the
  128 bits `SV_M94_M95_1`-`SV_M94_M95_128` that `M94`/`M95` set and reset from G/M-code programs
  (PLC Manual, PDF p.104).
- **PLC Write-Controlled, 1-bit boolean system variables (PLC → CNC)** (PLC Manual, PDF p.113).

> The name does not reliably signal direction: `SV_PLC_BUS_ONLINE` and `SV_PLC_IO2_ONLINE` are
> both CNC-written despite the `SV_PLC_` prefix, and are listed in the CNC → PLC table (PLC
> Manual, PDF p.104). Direction is determined by which Appendix D table an SV is listed in, not
> by its name.

## Constants

Constants are numeric literals or expressions bound with `IS`; they have no resource type and
are compile-time substitutions. Math and parenthesized references to earlier constants are
allowed, but only for integer values (PLC Manual, PDF p.14):

```
PI_C         IS 3.1415926535897932384626433832795   ; PLC Manual, PDF p.14
MULTIPLIER_C IS 256                                  ; PLC Manual, PDF p.14
FAULT_C      IS (SYNC+5*MULTIPLIER)                  ; PLC Manual, PDF p.14 [sic]
```

> The manual's own `FAULT_C` line omits the `_C` suffix its naming convention calls for
> (`SYNC`, `MULTIPLIER` rather than `SYNC_C`, `MULTIPLIER_C`) (PLC Manual, PDF p.14).

Message-number constants and their `Word Value` encoding are covered in
[messages.md](messages.md).

## Naming-suffix convention

The manual's suggested naming table (PLC Manual, PDF p.30-31) uses `SCREAMING_SNAKE_CASE` ending
`_C` for Constants, and `PascalCase` with a type suffix for the resource types: `_I` (`INP`),
`_O` (`OUT`), `_M` (`MEM`), `_W` (`W`), `_DW` (`DW`), `_FW` (`FW`), `_DFW` (`DFW`), `_T` (`T`),
`_PD` (`PD`), `Stage` or `_STG` (`STG`), `_FSTG` (`FSTG`). The full table, including the System
Variable and Stage-naming conventions, is in
[syntax.md](syntax.md#programming-conventions). It is presented as a suggestion, not a
compiler rule: "Whether you put an underscore between the name and type... is up to you" (PLC
Manual, PDF p.30).

## Macro <-> PLC Access

### Reading PLC resource state from a macro

A macro reads PLC resource state through fixed variable ranges; all of the ranges below are
read-only from a macro (Router Manual §11.2.16, p.205):

| PLC resource | Macro variable range | Formula |
|---|---|---|
| `INP` 1-1312 | `#50001`-`#51312` | `#(50000+n)` |
| `OUT` 1-1312 | `#60001`-`#61312` | `#(60000+n)` |
| `MEM` 1-1024 | `#70001`-`#71024` | `#(70000+n)` |
| `T` 1-128 status bit | `#90001`-`#90128` | `#(90000+n)` |
| `STG` 1-256 status bit | `#93001`-`#93256` | `#(93000+n)` |
| `FSTG` 1-256 status bit | `#94001`-`#94256` | `#(94000+n)` |
| `W` 1-88 | `#96001`-`#96088` | `#(96000+n)` |
| `DW` 1-22 | `#97001`-`#97022` | `#(97000+n)` |
| `FW` 1-44 | `#98001`-`#98044` | `#(98000+n)` |
| `DFW` 1-22 | `#99001`-`#99022` | `#(99000+n)` |

(Router Manual §11.2.16, p.205)

Jog Panel outputs live at `OUT1057`-`OUT1312` (Router Manual §11.2.16, p.205). The PLC Manual's
own Custom M-Codes example reads `OUT1058` (a.k.a. Jog Panel output 2) as `#61058`
(`60000 + 1058`):

```
;if AutoSpindle i.e. OUT1058 (a.k.a. JPO2) is set, exit the Macro
IF #61058 THEN GOTO 200
```
(PLC Manual, PDF p.61)

### Triggering PLC actions with M94/M95

`M94 /n` sets, and `M95 /n` resets, one of 128 system-variable bits `SV_M94_M95_1`-
`SV_M94_M95_128` that the PLC program reads (Router Manual §13.28, p.290). Multiple bits can be
listed on one line, e.g. `M94 /5/6` (Router Manual §13.28, p.290). Requests 1-5, 15 and 16 are
controlled by the default actions of M3, M4, M5, M6, M7, M8, M9, M10, M11 and M39; overriding one
of those requires a custom M-function (Router Manual §13.28, p.290).

To add a custom M-code, pick an unused `M94`/`M95` bit, name it after the M-code, and create an
`mfuncXXX.mac` file with the matching number; the PLC program checks that bit's `SV_M94_M95_n`
name for SET/RST (PLC Manual, PDF p.61). The manual's own M3 macro shows both directions in one
example: it sets/resets spindle-direction bits with `M94`/`M95`, then reads back an Output state
to check whether Auto Spindle mode is on before proceeding (PLC Manual, PDF p.61):

```
M95 /2 ; turn off CCW spindle
M94 /1 ;turn on CW spindle

;if AutoSpindle i.e. OUT1058 (a.k.a. JPO2) is set, exit the Macro
IF #61058 THEN GOTO 200
```
