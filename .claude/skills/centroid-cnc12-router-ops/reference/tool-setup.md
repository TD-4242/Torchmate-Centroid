# CNC12 Tool Setup: Offset Library, Tool Library, Tool Life, and Laser Setup

Configure tool height and diameter offsets, tool descriptions, tool life tracking, and PWM laser output. Source:
Router Manual Ch 5 (Tool Setup).

Navigation path (Router Manual Ch 5 intro, p.65): press `F5 – Tool/ATC` from the Main Screen to reach the Offset
Library, `F8 – Tool Library` from there for tool descriptions, `F3 – Tool Life` from the Tool Library for Tool Life
Management.

---

## 5.1 Offset Library (p.65-69)

The Offset Library holds the values for Height Offset (H) and Diameter (D) numbers. For example, if `H01` is
`-.25`, that height offset is applied whenever `H01` is referenced; if `D01` is `1.5`, diameter offset `01` is `1.5`
(p.65).

You can inspect and change any of the 200 `H` or 200 `D` values. Automatic tool length measurement typically sets
`H`-values; `D`-values are entered manually from known or measured tool diameters. `H01`/`D01`, `H02`/`D02`, etc.
are shown together on the same line for convenience only — the Height and Diameter Offset numbers are otherwise
independent; associations between them are made only in the Tool Library (§5.2) (p.66).

Offset Library softkeys (screen, p.65):

| Softkey | Label | Description |
|---|---|---|
| `F1` | Z Ref | Select the Z-reference setting function. |
| `F2` | Manual Measure | Manually measure the current tool's height offset. |
| `F3` | Auto Measure | Automatically measure tool lengths (requires the TT1 option). |
| `F4` | Batch | Measure multiple tools in one process (requires TT1 and an Automatic Tool Changer). |
| `F5` | +.001 | Increase the highlighted offset by `0.001"` (`0.02mm` metric). |
| `F6` | -.001 | Decrease the highlighted offset by `0.001"` (`0.02mm` metric). |
| `F7` | Change Tool | Change tools via the Automatic Tool Changer (if installed). |
| `F8` | Tool Library | Opens the Tool Library (§5.2). |
| `F9` | TT Setup | Not described in the surrounding text; shown on the Offset Library softkey bar (Router Manual §5.1, p.65). |
| `F10` | Save | Save changes and exit; `ESC` exits without saving. |

> Note: `F1 – Z-Ref` is only visible if `Parameter 3` is not set to fixed Home Z-Ref (change via the CNC12
> Wizard, `Touch Devices > Tool Touch Off > Tool Measurement Reference Method`). `F4 – Batch` only appears with an
> ATC configured (Wizard `ATC > ATC Setup`) and a fixed Tool Touch Off device installed (p.65).

### Height Offset (p.66)

The distance the control adjusts Z-axis positions when tool length compensation (`G43` or `G44`) is used with a
given `H`-value. For example, if `H001` is `-1.0` and the job contains `G43 H1`, the CNC software shifts all Z-axis
positions down `1.0` to compensate for the shorter tool.

Height Offsets are measured from the Z-reference position: the Z-axis position when the tip of the reference
tool touches the work surface. The reference tool should always be the longest tool (p.66).

The Height Offset for end mills and drills is the difference between the Z-axis position with the tool tip touching
the work surface and the Z-reference position. For ball nose and bull nose cutters it is the difference between the
Z-axis position with the tool's center at the work surface and the Z-reference position; since the tool cannot be
positioned that way directly, move the tip to the work surface instead, then manually subtract the tool nose radius
from the measured value (p.66).

#### Manual Height Offset Measurement Procedure

Establishing the Z-reference position (p.66):

> Note: On a fresh CNC12 Router install, Z-ref is set to Fixed Home. Change this in the CNC12 Wizard under
> `Touch Devices > Tool Touch Off`, toggling `Tool Measurement Reference Method` from `Z Home = Z Ref` to
> `Reference Tool`, then write the settings to the CNC Control Configuration; `F1 – Z-ref` then appears.

1. Press `F1 – Z-ref` to select the Z-reference setting function.
2. Insert the longest tool into the tool holder (`Jog` or `TOOL CHECK` keys can assist).
3. Jog the tip of the tool to the top of the work surface.
4. Press `F10 – Save` to set the Z-ref to the current Z position.

Measuring each tool height (p.66-67):

1. Insert the desired tool into the tool holder.
2. Jog the tip of the tool to the top of the work surface.
3. For a drill or end mill, press `F2 – Manual Measure` to measure the height.
4. For a bull or ball nose cutter, press `F2 – Manual Measure`, then subtract the tool nose radius from the value.
5. After a tool height is measured, the next Height Offset entry is automatically selected.
6. Press `F10 – Save` to save the Offset Library and exit.

Height offset examples assuming Z-reference = `-1.5` (p.67):

| Tool position | Nose radius | Tool height |
|---|---|---|
| -1.75 | — | -0.25 |
| -1.75 | 0.25 | -0.50 |
| -2.25 | — | -0.75 |
| -2.75 | 0.125 | -1.375 |

### Diameter (p.67)

Tells the control the distance to adjust when cutter diameter compensation (`G41` or `G42`) is used with a given
`D`-value. For example, if `D001` is `0.5` and the job contains `G41 D1`, the CNC software adjusts all X-Y
positions `0.25` (half the tool diameter) to the left of the programmed tool path.

To edit, navigate to the desired diameter offset number with `Arrow`, `Page Up`, `Page Down`, `HOME`, `END`, type
the value, and press `ENTER`. Small adjustments to either Height Offsets or Diameters can be made with
`F5 – +.001` and `F6 – -.001`: use `F5` if cut parts are undersized (cut less material), `F6` if oversized (cut
more material) (p.67).

---

### 5.1.1 Automatic Tool Measurement (p.67-68)

Z-minus single-surface probing using the TT-1 tool touch-off post is available in the Tool Offset Library (p.67).

First Time Setup: confirm the parameters in Ch 9 and Ch 15 are set (`Parameter 18`, `244`, `257`, `281`,
`282`, `283`, `367`), and that the detector is plugged in at the correct table location. When first testing the
TT-1, hold it in hand and manually touch it to the tool to confirm correct electrical connection and parameter
setup (p.67).

> **WARNING** Incorrect setup may cause damage to the machine, tool, and/or cause injury to the Operator (p.67).

> **NOTICE** Before manually jogging any probe to a position, make sure that the machine feed rate is turned down
> (less than ten in/min) or damage to the probe may result (p.68).

Setting the Z-reference (p.68): using the longest tool (or designated reference tool), press `F1 – Z-ref`,
then `F3`, then `CYCLE START`. The Z-axis moves down until tool touch-off is detected, and the Z-reference is set
at that position. `Parameter 3` bit 1 sets Z-reference to the Z-home position (see Ch 15).

Setting the Tool Height Offsets (p.68): pressing `F3 – Auto Measure` then `CYCLE START` moves the Z-axis down
until touch-off is detected; the resulting tool length is entered into the table (same as `F2 – Manual`), then the
Z-axis returns to its home position. If `Parameter 17` is set to a valid return point (`1` or `2`), `F3 – Auto
Measure` moves X and Y to that return point first — return point 1 is the `G28` position, return point 2 the `G30`
position, both from the WCS Configuration screen (Ch 4). If `Parameter 17` is `0`, X and Y do not move first; jog
the machine directly over the detector before pressing `F3 – Auto Measure`. See `Parameter` `18`, `244`, `257`,
`281`, `282`, `283`, `367` (Ch 15) for full setup.

> Note: `SHIFT+F3` overrides any return-point movement when `Parameter 17` is set to use it — useful when the
> height measurement is not taken from the tool's center point (p.68).

Batch Tool Height Offset Measurement (p.68): with both TT1 and an Automatic Tool Changer installed, press
`F4 – Batch` to measure multiple tools in one process; a dialog prompts `Enter the list of tools to measure.
Example: 1-4, 6, 15`. Press `CYCLE START` to run the batch measurement.

---

### 5.1.2 Setting Up Tool Height Offsets (p.68-69)

#### Using a Probe as the Reference Tool (p.69)

Before setting the Z-reference, confirm the probe's Tool Number is entered into `Parameter 12` on the Machine
Parameters screen, and that `Parameter 17` contains `0`.

1. Load the probe into the machine.
2. Jog the probe over the desired reference surface and press `F1 – Z-ref`.
3. Press `F3` and then `CYCLE START`; the probe finds the Z-reference.

The Z-reference is then entered into the Offset Library as the reference height for all other tools. Remove the
probe and measure other tool offsets manually as described above.

#### Measuring Each Tool Offset Using a Fixed Detector (p.69)

Before measuring any tool height, enter a reference point number (`1` or `2`) into `Parameter 17` and enter the
detector position as the corresponding Reference Return Point on the WCS Configuration screen (Ch 4). Confirm
`Parameter 44` is set correctly — this is the TT1's input number.

1. Load a reference tool (preferably the longest) and highlight its Height Offset Number with `UP`/`DOWN` arrow.
2. Press `F1 – Z Ref`, `F3 – Auto Measure`, then `CYCLE START` to set the Z-reference; X and Y traverse to the
   preset location, then Z moves down until the tool is detected.
3. Load the next tool.
4. Highlight the desired Height Offset Number with `UP ARROW`/`DOWN ARROW`.
5. Press `F3 – Auto Measure` then `CYCLE START`; a negative offset means the tool is shorter than the reference
   tool.

Press `F10 – Save` once all tool offsets are measured, or `ESC` to cancel changes.

---

## 5.2 Tool Library (p.70-71)

The Tool Library associates tool (T) numbers with Height Offset (H) values, Diameter (D) values, and text
descriptions; the on-screen columns are `Tool`, `Bin`, `Ht.`, `Dia.`, `Description` (Router Manual §5.2, p.70).
Intercon (Ch 10) uses this to provide defaults at each tool change. For enhanced ATC features, `T` numbers are
also associated with bin numbers (see `Parameter 160`, Ch 15) (p.70).

To edit, navigate to the desired tool number with `Arrow`, `Page Up`, `Page Down`, `HOME`, `END`; type new
Height Offset, Diameter, or description values and press `ENTER`; press `F10 – Save` to save and exit (p.70).

### Bin (p.70)

Specifies the bin location, or ATC position, the tool occupies. Valid values are `-1` (shown as `—`) through the
maximum tool count set by `Parameter 161`. `0` indicates the tool is currently in the spindle. `F1`/`F2` work only
when the cursor is in the Bin column:

| Softkey | Label | Description |
|---|---|---|
| `F1` | Clear Bin | Places `—` into the bin field (same as entering `-1`). |
| `F2` | Clear All | Places `—` into every bin field. |

> Note: If enhanced ATC features are not on, the cursor cannot move into the Bin column and `Bin fields are
> locked` appears where the tool-in-spindle display is located; `F1 – Clear Bin` and `F2 – Clear All` only appear
> with enhanced ATC on (p.70).

> Note: For enhanced ATC applications, bin numbers update when tool changes complete. For random or arm-type
> tool changers, tools in the spindle are placed into the same bin the next tool is picked up from, not
> necessarily the bin they were originally taken from (p.70).

### Height (p.71)

Specifies a default Height Offset (`H`) number (`1` to `200`) for the tool; Intercon uses it to provide a default
`H`-value at each tool change.

> The manual's own cross-reference for this field reads "The CNC software also uses this information to correct
> for the length of the tool that is used to establish the Z-axis position of the Part Setup (see Chapter 5)"
> (Router Manual §5.2, p.71) — Chapter 5 is this same Tool Setup chapter; the Z-axis Part Setup procedure it
> describes is in Ch 4 (see [part-setup.md](part-setup.md) §4.1.2). Quoted as printed, not corrected.

### Diameter (p.71)

Specifies a default Diameter (`D`) number (`1` to `200`); Intercon uses it to provide a default `D`-value at each
tool change. Type a new number and press `ENTER` to change it.

### Description (p.71)

Text description of the tool, shown in a prompt message when the CNC software reaches a tool change (`M6`).

### F5 – Export Lib (p.71)

The tool library can be exported in `txt` (space-separated, aligned columns) or `csv` (comma-separated columns)
format by pressing `F5`; choose `txt` or `csv` for the desired format.

> Note: the Tool Library screenshot (Router Manual §5.2, p.70) labels this key `Export Lib...` at `F4`; the body
> text on p.71 calls it `F5 – Export Lib`. Both are quoted as printed; the softkey table above follows the
> screenshot, this heading follows the body text's own label.

---

## 5.3 Tool Life Management Menu (Router Manual §5.3, p.71-75)

Sets up each tool's pre-determined life and tracks its usage toward an end-of-life condition. Off by default;
enabled per tool. Screen columns: `Tool#`, `Type`, `Total Life`, `Used`, `Remaining`, `Units`, `Mode`,
`Description` (p.71-72).

Softkeys (p.71-72):

| Softkey | Label | Description |
|---|---|---|
| `F1` | Show/Hide Unmanaged | Toggles including/excluding tools whose `Total Life` is `0` (Off). |
| `F2` | Sort Recent | Sorts by tools whose `Total Life`/`Used` were most recently modified. |
| `F3` | Sort Tool # | Sorts by Tool Number. |
| `F4` | Sort Remaining | Sorts by Life Remaining. |
| `F10` | Save | Saves changes. |

Automatic Management (Mode = `Auto` and `Total Life` > `0`) (p.72):

| Type | Units | Tool Activity Monitored | Effect on `Used` field |
|---|---|---|---|
| Drill | Cycles | Downward Z-plunge at feed rate at a unique XY location | Incremented by one cycle |
| Drill | Inch/mm | Downward Z-plunge at feed rate at a unique XY location | Total downward Z-distance (minus overlaps) added |
| EM (End Mill) | Cycles | Tool Change | Incremented by 1 cycle |
| EM (End Mill) | Inch/mm | Sideways XY feed rate moves (non-rapid) | XY distance accumulated |

Field definitions (p.72-73):

- `Type` — Drill or EM (End Mill); when `Mode` is `Auto`, determines the tracked activity type. Select `Drill` for
  a Bore or Tap.
- `Total Life` — total tool life; `>0` enables management, `0` (Off) makes it "Unmanaged" (hide/show with `F1`).
  Units per the `Units` field.
- `Used` — consumed tool life; initialize to `0` for a new tool. In `Auto` mode, updated automatically during a
  job run.
- `Remaining` — non-editable display of remaining tool life.
- `Units` — `Cycles` or distance (`mm`/`Inches`, per the Control Configuration menu, Ch 15) for `Total Life`,
  `Used`, `Remaining`.
- `Mode` — `Auto` (tool activity monitored and accumulated automatically) or `Manual` (updates depend on
  user-variable modifications programmed into the running G-code; see §5.3.2).
- `Description` — text description shown in the tool-change (`M6`) prompt during a job run.

### 5.3.1 Effect on Job Run and Backplot (p.73-74)

At Start of Job (p.73-74): tool life expiration is checked at job start. If any managed tool is expired, a
dialog appears:

```
Tool life expired:
T1

F1 = Go to the Tool Life Management menu
F2 = Continue to run job   F3 = Cancel job
```

> Note: at job start the CNC software does not yet know which tools will be used, so the listed tools are all
> expired tools, whether or not the job actually uses them (p.74).

At Job Restart (p.74): expirations are also checked on job restart (`M2` or `M102`). The dialog is similar,
but lists only tools used since the previous restart.

At End of Job (p.74): expiration during a job does not cancel it. On successful completion:

```
Tool life expired during job:
T1

Go to the Tool Life Management menu?
F1 = Yes   F2 = No
```

This dialog lists only expired tools that were used in the job.

Using Backplot Graphics to Predict Tool Expirations (p.74): press `F8 – Graph` at the Main Screen or Load menu.
If the graphed job would expire a tool, the message `Tool life will expire on this job:` appears with the tool
number.

### 5.3.2 Using G-code User Variables (p.74-75)

If a tool's `Mode` is `Manual`, the `Used` field is not updated during a job run unless the G-code is programmed
to modify it (p.74).

User variable for a tool's Used Life field (p.75):

```
#[19000+[#4120-1]*5+2]
```

Example: with tool T23's `Mode` set to `Manual` and `Units` `Cycles`, the following increments T23's Used Life
field by one after `examplecycle.cnc` completes:

```
M6 T23                             ; Change tool to T23
M98 "examplecycle.cnc" L1         ; Run the cycle 1 time
IF #4201 || #4202 THEN GOTO 100   ; Skip to N100 if in backplot or search mode
IF #4120 < 1 || #4120 > 200 THEN GOTO 100  ; Skip to N100 if T number not valid
#[19000+[#4120-1]*5+2] = #[19000+[#4120-1]*5+2] + 1  ; Increment Used Life by 1 cycle
N100                               ; Destination of gotos
```

See Ch 11 for more on User or System Variables (p.75).

---

## 5.4 Laser Setup (Router Manual §5.4, p.75-81)

### 5.4.1 PWM Output for Spindles and Lasers (p.75)

- 5-volt PWM output signal is on DB25 pin `#14`.
- DB25 pin `#14` is `Output 2`.
- `Output 2` is also connected to `Relay 2` via the ribbon cable.
- If PWM output is used, `Relay 2` must be disabled — see schematic `S15049` to cut the ribbon cable lead to
  `Relay 2`.
- PWM is based on the `0–100` or `0–1000` S-command; the range is selected in the Acorn Wizard.
- `M37` turns ON Laser Output, `M38` turns it OFF: `M37` activates Laser Enable, Laser Reset, and PWM Select, then
  after `0.5s` turns off LaserReset, at which point the laser controller reads the PWM signal from `OUTPUT 2`.
  `M38` waits `30s` to let the JTECH laser controller cool, then performs `M95`/`37`/`38` to turn off both Laser
  Enable and PWMSelect.
- The PWM Velocity Modulation feature adjusts PWM output based on machine tool velocity to avoid overburning on
  corners and turn-arounds; `G37 ON` = PWM VM ON, `G37 OFF` = PWM VM OFF.
- Simple PWM controls are in the Acorn Wizard, alongside preset buttons for common Jtech configurations matching
  schematics `S15049`, `S15056`, `S15057`.

### 5.4.2 PWM-related I/O in the Wizard (p.75-76)

Configured under `Primary System > Output Definitions`:

| I/O Function | Description |
|---|---|
| `PWM Output` | The PWM signal itself; usable only on `Output 2` (DB25 pin `#14`). Related code is the S-command. |
| `LaserEnable` | Typically used in a safety interlock circuit (see schematic `S15049`). `M37` enables the safety interlock and resets the laser; `M38` disables it after a delay to let the component cool. |
| `LaserReset` | Momentary output that sends a reset signal to the laser controller (see schematic `S15049`). |
| `PWMSelect` | Moves the PWM signal from Spindle to Laser. Deactivated = PWM to Spindle; activated = PWM to Laser. On a Standard Layout, connect Spindle PWM to the relay's NC side and the Laser to its NO side. See schematic `S15057` (BLDC Spindle Control). |

Wiring schematics (p.77-79):

| Schematic | Title | Page |
|---|---|---|
| `S15049` | J-TECH PHOTONICS LASER | p.77 |
| `S15056` | J-TECH PHOTONICS LASER, GENERIC VFD ENABLE-DIRECTION | p.77 |
| `S15057` | J-TECH PHOTONICS LASER, BLDC SPINDLE CONTROL | p.78 |
| `S15061` | OBT LASER | p.78 |
| `S15062` | NEJE LASER | p.79 |
| `S15063` | COMCROW D-B500F LASER | p.79 |

### 5.4.3 ZigZagSyncTest Instruction (p.80)

Requirements: Acorn CNC12 v4.6+ Mill or Router.

Test programs included with the installation:

```
ZigZagLaserSyncTest-X_Axis.cnc
ZigZagLaserSyncTest-Y_Axis.cnc
```

### 5.4.4 Purpose (p.80-81)

These two programs test for and adjust backlash in laser table axes, by creating four lines in either the X- or
Y-direction, moving back and forth in that axis while firing the laser in short `0.006` inch pulses at specific
points in each direction (p.80).

- Good alignment: four separate vertical lines, straight and aligned.
- Backlash present: lines appear as clusters of "dots" offset when direction changes; each dot is `0.006`
  inches long, giving a reference for estimating the needed backlash compensation (p.80-81).

Procedure:
1. Run the ZigZagSyncTest program and observe the result.
2. Use the Acorn Wizard to adjust the backlash compensation for the affected axis.
3. Run the program again to determine if more or less compensation is needed (p.81).
