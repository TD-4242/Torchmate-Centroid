# Motion Tuning Reference

Final motion tuning after the Wizard is configured (Ch 6): axis motor testing and direction,
coarse and fine calibration of the Overall Turns Ratio, backlash compensation, and software
travel limits. Where a step adjusts a Wizard field, see [wizard.md](wizard.md) rather than
this file for the field's definition.
Source: Acorn Install Ch 7; printed pages cited inline.

## Axis Motor Testing & Configuration Setup (§7.1)

> **DANGER:** mechanically disconnect the axis motors from the machine tool before jogging
> them for the first time — an incorrectly entered parameter can make a motor oscillate
> violently or move out of control (Acorn Install §7.1, p.101).

1. Release E-stop to clear all errors and provide VM power to the axis motors; set feedrate
   to around 10%; jog each disconnected motor (VCP arrow keys) to confirm correct motion;
   disable increment mode (`Incr Cont` not lit) (Acorn Install §7.1, p.101).
2. If a motor doesn't move: confirm `DB25` wiring for +5VDC logic (stepper) drives, that the
   schematic matches the drive, no `406 Emergency Stop Detected` message, VCP `RESET` isn't
   showing `Tripped`, motor power is present, and the motor/encoder is wired correctly; try
   testing without the drive-enable signal connected, since it can inadvertently disable the
   drive under Acorn control (Acorn Install §7.1, p.101).
3. After successful movement, power down, center all axes for clearance, then mechanically
   connect the motors to the machine and power back up (Acorn Install §7.1, p.101-102).
4. Confirm `Homing Type` is `Simple Homing` in the Wizard before proceeding — see
   [wizard.md](wizard.md#axis-homing-and-travel-66) (Acorn Install §7.1, p.102).

> **DANGER:** home switches aren't configured correctly yet; homing to switches now could
> damage the machine (Acorn Install §7.1, p.102).

5. Feedrate to ~10%; press `Start`/`alt+s` to set home at the current position (DROs zero),
   then slow-jog each axis to confirm motion (Acorn Install §7.1, p.102).
6. **Correct axis direction:** direction is determined by tool motion relative to the part.
   On a lathe with a front-mount tool post, use the standard convention; a rear-mount tool
   post reverses X relative to a front-mount post. On a mill, table-moving axes (e.g. X/Y on
   a knee mill) move **opposite** the tool motion; tool-moving axes (e.g. the quill) move the
   **same** as the tool motion (Acorn Install §7.1, p.102-103).
7. Jog each axis and confirm the DRO counts more positive moving in the positive direction
   (more negative moving negative). To flip a wrong axis, set `Direction Reversal` to `Y` in
   the Wizard's Axis Configuration — see
   [wizard.md](wizard.md#axis-configuration-65) (Acorn Install §7.1, p.103).

## Coarse Configuration: Commanded vs. Actual Movement (§7.2)

Rough calibration of the `Overall Turns Ratio` (see
[wizard.md](wizard.md#axis-configuration-65)) by comparing a commanded MDI move against the
actual measured travel; useful when the exact pulley/gearbox tooth counts are hard to
determine. A fine adjustment against a gauge block follows in §7.3
(Acorn Install §7.2, p.104).

1. Jog the spindle to the table center; zero the DRO (`F1 Setup` -> `F1 Part` -> `F10 Set
   Zero`); lay a tape measure with 0" under the spindle center (Acorn Install §7.2, p.104).
2. Command a move of at least 1 foot via `F3 MDI`, e.g. `G1 X12 F10`, and press cycle start;
   use a slow feedrate and be ready to hit E-stop in case the axis over-travels (Acorn Install
   §7.2, p.104).
3. Measure the actual travel and, if it differs from the commanded distance, calculate a new
   `Overall Turns Ratio`:
   - **Imperial:** divide the commanded distance (DRO/MDI value) by the actual measured
     distance, then multiply by the current Overall Turns Ratio. Example: commanded 7.5",
     actual 6": `7.5 / 6 = 1.25`; current ratio `5.000 * 1.25 = 6.25`
     (Acorn Install §7.2, p.104).
   - **Metric:** divide the actual measured distance by the commanded distance (DRO/MDI
     value), then multiply by the current Overall Turns Ratio. Example: actual 150mm,
     commanded 175mm: `150 / 175 = .85714`; current ratio `5.08 * .85714 = 4.35428` (Acorn
     Install §7.2, p.105).
4. Enter the new value in the Wizard's Axis Configuration and click `Write Settings to CNC
   Control` — see [wizard.md](wizard.md#axis-configuration-65) (Acorn Install §7.2, p.105).
5. Repeat until the commanded movement matches the tape measurement, then repeat for each
   axis (Acorn Install §7.2, p.105).

## Fine Adjustment of Overall Turns Ratio (§7.3)

Precision follow-up to §7.2 using a dial indicator against a gauge block of known length,
rather than a tape measure (Acorn Install §7.3, p.105).

1. Attach a dial test indicator to the spindle; build an `L`-shaped test fixture whose long
   leg is a precision gauge block, ideally 6-12" (a longer standard gives better accuracy —
   the example uses a 12.000" block) (Acorn Install §7.3, p.105).
2. Secure the fixture parallel to the axis under test. Jog the indicator toward the block
   **only** (jogging past it and backing up introduces backlash into the measurement — restart
   the test if that happens) until it touches, then fine-jog in to remove system play (Acorn
   Install §7.3, p.105-106).
3. Zero the DRO (`F1 Setup` -> `F1 Part` -> `F10 Set Zero`); raise the indicator axis clear,
   then jog it to the base of the `L`, approaching only in one direction as before (Acorn
   Install §7.3, p.107).
4. Read the distance moved on the DRO. Example: the DRO reads `12.005` against a 12" standard
   — a ballscrew-pitch imperfection typical even on good screws (Acorn Install §7.3, p.107).
5. Calculate a new `Overall Turns Ratio`:
   - **Imperial:** divide the DRO value by the actual standard length, then multiply by the
     current ratio. Example: `12.005 / 12 = 1.000416`; current ratio
     `5.000 * 1.000416 = 5.00208` (Acorn Install §7.3, p.108).
   - **Metric:** divide the actual gauge-block length by the DRO value, then multiply by the
     current ratio. Example: actual 300mm, DRO `304.927`: `300 / 304.927 = .98384`; a 20mm
     ballscrew belted 1:1 gives current ratio `20 x .98384 = 19.6768`
     (Acorn Install §7.3, p.108).
6. Enter the new value in the Wizard's Axis Configuration (Acorn Install §7.3, p.108) — see
   [wizard.md](wizard.md#axis-configuration-65). Repeat until the DRO matches the gauge block,
   then repeat per axis (Acorn Install §7.3, p.108).

## Backlash Compensation (§7.4)

Set `Lash Comp` (see [wizard.md](wizard.md#axis-configuration-65)) **last**, once the machine
is fully configured and operational. Electronic compensation cannot cure mechanical play — the
mechanical lash should be minimized first; typical usable lash is zero-`.002"` for mills and
zero-`.005"` for routers, and lash under `.0002"` (2 tenths) is often best left uncompensated
(Acorn Install §7.4, p.108).

> The manual gives two different typical mill values: zero-`.0015"` in the Wizard's Axis
> Configuration field description (Acorn Install §6.5, p.77) and zero-`.002"` here (Acorn
> Install §7.4, p.108). Both cite zero-`.005"` for routers.

1. Reduce mechanical lash to under `.002"` before setting electronic compensation. Attach a
   plunge-type dial indicator parallel to the axis and perpendicular to the touch surface
   (Acorn Install §7.4, p.108).
2. In the Wizard's Axis Configuration, zero any previously entered `Lash Comp` value and write
   settings before measuring — measuring while the control is already compensating gives a
   false reading (Acorn Install §7.4, p.108-109).
3. Slow-jog to the touch point, then incrementally jog (`.010"`/`X10`) further in the same
   direction to a position that's easy to remember (Acorn Install §7.4, p.109).
4. Jog 10 increments further in the same direction, then 10 increments back in the opposite
   direction (Acorn Install §7.4, p.109-110).
5. Compare the indicator to the remembered position: it either returns exactly, or falls
   short by the axis's mechanical backlash. Example: the indicator fell short and landed on
   `22` instead of `21`, i.e. `.001"` of backlash (Acorn Install §7.4, p.111).
6. Enter the measured value into `Lash Comp` and rerun the test; an accurate value returns the
   indicator to the remembered position (Acorn Install §7.4, p.111). See Technical Bulletin
   #37 for more (Acorn Install §7.4, p.111).

## Software Travel Limits (§7.5)

Without software travel limits an axis runs at full speed until a limit switch trips, and may
not have time to decelerate before hitting the hard stop. Travel limits decelerate the axis
before the switch and reject G-code that would move past them (Acorn Install §7.5, p.112).

**Prerequisites:** steps/revolution and Overall Turns Ratio configured (§7.2/§7.3), limit
switches working, max feedrate and acceleration set; restart and home the machine (Acorn
Install §7.5, p.112).

1. Display machine coordinates: press `alt+D` until the DRO's top-left corner reads
   `machine` (Acorn Install §7.5, p.112).
2. From home, jog the axis to the opposite end of travel, stopping short of the hard stop by
   a safe margin (typically `.1"` to `.37"`). Note the DRO value — it may be negative
   depending on where home was set. Repeat per axis (Acorn Install §7.5, p.112-113).
3. Enter each recorded value into `Travel (-)` or `Travel (+)` in the Wizard's Axis Homing and
   Travel screen — see [wizard.md](wizard.md#axis-homing-and-travel-66). Both limits at zero
   disables travel limits for that axis; setting either one non-zero enables both (Acorn
   Install §7.5, p.113).
4. Repeat for each axis (Acorn Install §7.5, p.113).
5. Test by slow-jogging toward a limit — the axis should stop at the software limit before the
   switch trips. Confirm with MDI G-code commanding a move past the limit; CNC12 should reject
   it and report `907 # axis travel exceeded, 325 Limit: job canceled`
   (Acorn Install §7.5, p.113).
