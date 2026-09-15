# Acorn Wizard Reference

Every CNC12 Wizard configuration page (Ch 6): axis drive type, I/O definitions, axis motion,
spindle, touch devices, peripherals, DB25 mapping, and control preferences. Axis pairing
(§6.7) is covered separately; see below. See [hardware.md](hardware.md#io-map) and
[wiring.md](wiring.md) for the physical I/O behind the input/output pages.
Source: Acorn Install Ch 6; printed pages cited inline.

## Introduction (§6.1)

The Wizard sets AXIS motor drive type, inputs/outputs, overall turns ratio, axis direction
reversal, motor steps/revolution, travel limits, homing, axis pairing, step rate, spindle
config, touch devices, input devices (wireless MPG, keyboard emulators), DB25 signal mapping,
and CNC control/Wizard preferences (Acorn Install §6.1, p.71). Open it from the main screen:
`F7 Utility` -> `F10 Wizard` (Acorn Install §6.1, p.71).

## Primary System Axis Drive Type (§6.2)

**Drive type**: pre-set configuration matching a specific axis motor drive make/model;
selecting one and clicking `Load Drive` pre-populates the I/O map and other Wizard screens to
match that drive's schematic (Acorn Install §6.2, p.72). Default on a new install is
`Bench Test 'Screw Terminal'`, for communication bench testing with no axis drives connected
(Acorn Install §6.2, p.72).
**Create new…**: builds a `Custom` drive type from the Wizard's current settings; custom
drive types can be exported/imported (Acorn Install §6.2, p.72).

> **IMPORTANT:** Click `Write Settings to CNC Control Configuration` after any Wizard page
> change for it to take effect, then follow any on-screen prompts (Acorn Install §6.2, p.73).

## Primary Input Definitions (§6.3)

Drag an input name from the sort/type drop-down onto the desired input number to assign it;
click an assigned input number to toggle Normally Open (red) / Normally Closed (green); drag
an assignment back to the input box to remove it (Acorn Install §6.3, p.74). The input number
corresponds to the input terminal number on the Acorn; inputs are on `H1` and `H4` (Acorn
Install §6.3, p.74). See [hardware.md](hardware.md#io-map) for the terminal map and
[wiring.md](wiring.md#inputs-52) for input wiring.

## Primary System Output Definitions (§6.4)

Drag an output name from the sort/type drop-down onto the desired output number to assign it;
drag an assignment back to the output box to remove it (Acorn Install §6.4, p.75). The output
number corresponds to a relay on the Acorn relay board (Acorn Install §6.4, p.75). See
[hardware.md](hardware.md#io-map) for the terminal map and [wiring.md](wiring.md#outputs-53)
for output wiring.

## Axis Configuration (§6.5)

4th-axis simultaneous interpolated motion requires a Pro license; the free version limits
4th-axis moves to single-axis (Acorn Install §6.5, p.76).

**Linear**: axis moves in a straight line, e.g. left/right or up/down (Acorn Install §6.5,
p.76).
**Rotary**: axis rotates instead of translating, e.g. a rotary table (Acorn Install §6.5,
p.76).
**Label**: axis label shown on the main-screen DRO (Acorn Install §6.5, p.76).
**Steps/Revolution**: number of motor steps (or microsteps) per one full motor-shaft
revolution; must match the drive's own setting, not be used to tune commanded distance — e.g.
`2000` for a 10x-microstepping drive (200 x 10), or encoder line count x 4 for a closed-loop
drive, e.g. `4000` for a 1000-line encoder (Acorn Install §6.5, p.76).
**Overall Turns Ratio**: physical constant — motor turns per unit of linear travel, set by
ballscrew/rack pitch and motor-to-ballscrew pulley reduction; see §7.11 for fine-tuning by
measurement (Acorn Install §6.5, p.77).
**Lash Comp**: backlash compensation, set last, once the machine is fully configured; typical
values zero-`.0015"` for mills, zero-`.005"` for routers; see §7.4 (Acorn Install §6.5, p.77).
**Max Rate**: maximum rapid (`G0`) rate for the axis; rough estimate via
`(max motor RPM / overall turns ratio) x 0.85` (Acorn Install §6.5, p.77).
**Fast Jog**: axis speed in RAPID (Hare) continuous jog on the VCP (Acorn Install §6.5, p.77).
**Slow Jog**: axis speed in SLOW (Tortoise) continuous jog on the VCP; also the homing speed
(Acorn Install §6.5, p.77).
**Accel/Decel**: time to reach maximum velocity; `0.1`s is very fast, `1.0`s very slow;
default `0.5` for both accel and decel (Acorn Install §6.5, p.77).
**Direction Reversal**: set `Yes` to reverse the axis motor direction so the machine moves
the correct way; see Chapter 7 axis conventions (Acorn Install §6.5, p.78).
**Drive Enable Delay**: time the control waits for the drive to come online before checking
the DRIVE FAULT input, if mapped; generally left at default (Acorn Install §6.5, p.78).

## Axis Homing and Travel (§6.6)

**Home Program**: `Wizard Generated` (default, an auto-generated `.hom` file) or
`Custom User Defined` (Acorn Install §6.6, p.79).
**Homing Type**: `Simple Homing` (no home switches — operator jogs to home, presses cycle
start), `Home to Switch` (machine has home switches), or `Automatic Homing` (adds further
automatic-homing options) (Acorn Install §6.6, p.79).
**Homing Direction**: `+` (`M92`) if the axis must move positive to find its home switch, `-`
(`M91`) if negative; set per axis (Acorn Install §6.6, p.79).
**Homing Sequence**: order axes home in; default 3rd, 2nd, 1st, then 4th axis (typically Z,
then Y, then X, with a homed rotary axis last) (Acorn Install §6.6, p.80).
**Software Travel Limits — Travel Limit (+)**: used when the home switch is on the axis's
negative end; a positive value, the distance from the home switch to the far end of travel
(Acorn Install §6.6, p.80).
**Software Travel Limits — Travel Limit (-)**: used when the home switch is on the axis's
positive end; a negative value, e.g. `-12.2` for 12.2" of travel from a positive-end home
switch (Acorn Install §6.6, p.80). See §7.5 for more.
**Machine Parking**: sends all axes to a preset position on shutdown, close to (not tripping)
each home switch, to speed the next homing cycle; reached via `F10 Shutdown` -> `F1 Park` or
the VCP `Park` button; `Edit` opens the default `park.mac` (Acorn Install §6.6, p.80).

See [wiring.md](wiring.md#home-and-limit-switches-57) for home/limit switch wiring and the
Wizard input-name tables (`HomeAll`, `FirstAxishomeOk` … `FourthAxishomeOk`, etc).

**Axis Pairing (§6.7).** See [axis-pairing.md](axis-pairing.md).

## Advanced Axis Configuration (§6.8)

Changes here are usually not required except when advised (Acorn Install §6.8, p.83).

**Axis Signal Inversion**: inverts the Step, Direction or Enable signal per axis, sometimes
needed depending on drive type; do not use this to change axis movement direction — use Axis
Configuration's Direction Reversal instead (Acorn Install §6.8, p.83).
**Step Rate**: maximum steps/second Acorn sends to the drive; check the drive's maximum step
frequency rating first — too high a value causes unpredictable movement. Start at `100,000`
if unsure; AC drives typically tolerate faster (Acorn Install §6.8, p.83).
**Axis Motor Drive Fault**: fault delay while waiting for the drive's `DriveOK` signal (Acorn
Install §6.8, p.83).
**Charge Pump**: legacy support for older drives requiring a charge-pump signal (Acorn
Install §6.8, p.83).

## Spindle Setup — Mill (§6.9)

**Spindle Encoder**: whether a spindle encoder is connected to the Acorn (values: `Yes`/`No`)
(Acorn Install §6.9, p.84).
**Spindle Encoder Counts**: encoder counts per spindle revolution — line count x 4, e.g.
`4000` for a 1000-line encoder (Acorn Install §6.9, p.84).
**Spindle max speed in high range**: maximum RPM in high-gear range (Acorn Install §6.9,
p.84).
**Spindle min speed in high range**: minimum RPM in high-gear range (Acorn Install §6.9,
p.84).
**Medium range spindle speed ratio**: medium-max-RPM / high-max-RPM, e.g. `.5` for 1500/3000;
negative if the gear range reverses spindle direction, e.g. `-.5` (Acorn Install §6.9, p.84).
**Low range spindle speed ratio**: low-max-RPM / high-max-RPM, e.g. `.166` for 500/3000;
negative if the gear range reverses direction, e.g. `-.166` (Acorn Install §6.9, p.85).

See [wiring.md](wiring.md#spindle-motor-58) for spindle wiring and
[wiring.md](wiring.md#spindle-encoder-59) for encoder wiring.

## Spindle Setup — Lathe (§6.10)

**Lathe Orientation**: `Horizontal` (most lathes) or `Vertical` (Acorn Install §6.10, p.85).
A CNC12 reboot is required after any spindle-setup change (Acorn Install §6.10, p.85).
**Tool orientation**: `Front` or `Rear`; reverses the X axis direction to match how the tool
is presented to the work (Acorn Install §6.10, p.85).
**Spindle Encoder**: whether a spindle encoder is connected (values: `Yes`/`No`) (Acorn
Install §6.10, p.85).
**Spindle Encoder Counts**: encoder counts per spindle revolution — line count x 4, e.g.
`4000` for a 1000-line encoder (Acorn Install §6.10, p.86).
**Spindle max speed in high range** / **Spindle min speed in high range**: maximum/minimum
RPM in high-gear range (Acorn Install §6.10, p.86).
**Medium range spindle speed ratio** / **Low range spindle speed ratio**: same definitions
and sign convention as §6.9 (Acorn Install §6.10, p.86).

## Spindle Rigid Tapping (§6.11)

Complete Acorn spindle-speed calibration (VFD Hz adjustment) before rigid tapping setup, per
Centroid Tech Bulletin #304 (Acorn Install §6.11, p.86). See
[wiring.md](wiring.md#spindle-encoder-59) for encoder wiring (Acorn Install §6.11, p.87).
Rigid tapping requires a Pro license; do not enable/test it until the machine is fully
configured and tested (Acorn Install §6.11, p.87).

## Spindle PWM Setup (§6.12)

The Acorn's PWM output drives a laser and/or PWM spindle drive via the G-code `S` word; it is
distinct from the 0-10V analog output used for VFD-controlled 3-phase spindles (Acorn Install
§6.12, p.87).

**PWM enable**: turns PWM output on (Acorn Install §6.12, p.87).
**Base Frequency (Hz)**: PWM base frequency (Acorn Install §6.12, p.87).
**PWM Command Range**: `0-100` or `0-1000`, dividing laser power/spindle RPM into that many
increments, e.g. `S1000` = max power at the `0-1000` setting (Acorn Install §6.12, p.87).
**PWM Minimum S command power level to start Laser**: minimum `S` value before the laser
turns on (Acorn Install §6.12, p.87).
**Inverse Output**: inverts the PWM output signal (Acorn Install §6.12, p.87).
**Jtech Laser Presets**: preset PWM configurations matching Acorn-to-Jtech-laser schematics
(Acorn Install §6.12, p.87).

> PWM output is on DB25 `Output 2`, pin 14; enabling PWM takes over `Output 2`, which then
> can't be used for anything else, and the output ribbon cable to the relay board must be cut
> at `Output 2` (Acorn Install §6.12, p.88).

## Touch Devices: Probe Configuration (§6.13)

**Probe PLC Input**: the Acorn input assigned as `ProbeTripped` in Primary Input Definitions
(§6.3) (Acorn Install §6.13, p.89).
**Probe type**: `Centroid DP-4`, `Centroid KP-3`, or 3rd-party Mechanical/Conductive (Acorn
Install §6.13, p.89).
**Input state when tripped**: input state when the probe trips (Acorn Install §6.13, p.89).
**Probe tool number**: tool number the probe is registered as, for looking up its length
offset/tip diameter in the tool library (Acorn Install §6.13, p.89).
**Fast probe rate**: positioning/initial-surface-detection rate; default `10` ipm (Acorn
Install §6.13, p.89).
**Slow Probe rate**: final measuring-move rate for accuracy; default `3` ipm — too slow risks
double triggers (Acorn Install §6.13, p.90).
**Recovery Distance**: distance the probe backs off a broken surface contact before
traversing parallel to it (Acorn Install §6.13, p.90).
**Maximum Probing Distance**: maximum distance a probing cycle searches for a surface (Acorn
Install §6.13, p.90).
**Probe Protection when using VCP Jog Buttons**: `Yes` stops all motion immediately on an
unexpected probe contact during VCP jogging, until the operator slow-jogs clear; `No`
disables that protection (Acorn Install §6.13, p.90).
**Inhibit the Spindle from moving when probing**: requires a probe detect signal mapped to
`Probe Detect` in Input Definitions; default `Yes` on mills, `No` on lathes (Acorn Install
§6.13, p.90).
**Display Warning to Verify that the Probe or TT is functioning properly**: toggles the
pre-probing-cycle verification prompt (Acorn Install §6.13, p.90).

## Touch Devices: Tool Touch Off Configuration (§6.14)

**Tool Touch Off PLC Input**: the Acorn input assigned as `ToolTouchOffTriggered` in Input
Definitions (Acorn Install §6.14, p.91).
**Tool Touch Off Type**: `Centroid TT-1`, `TT-2`, or 3rd-party Mechanical/Conductive; Centroid
TT devices are closed when tripped (Acorn Install §6.14, p.91).
**Input state when triggered**: input state when the TT device trips (Acorn Install §6.14,
p.91).
**Subtract height of tool touch off device**: subtracts the TT device's height when setting Z
part-zero via Auto Part Z Zero, for a TT sitting on top of the material (Acorn Install §6.14,
p.91).
**Tool Touch off device height**: TT device's top-to-bottom height, used by the Auto Part Z
Zero probing cycle (Acorn Install §6.14, p.91).
**Use Tool Touch Off device to set Z reference**: uses the top of the TT device as the tool
height measurement origin; common on routers/bed mills, not used for knee mills (Acorn
Install §6.14, p.92).
**Inhibit the Spindle from moving when probing with ToolTouch**: requires
`ToolTouchOffDetect` mapped in Input Definitions; default `No` on mills, `Yes` on lathes
(Acorn Install §6.14, p.92).

## Control Peripheral Input Devices Setup (§6.15)

**Touchscreen**: enables touchscreen input (values: `Yes`/`No`) (Acorn Install §6.15, p.92).
**USB Operator Control Pad**: enables a USB keyboard-emulator control pad, e.g. X-Keys (Acorn
Install §6.15, p.92).
**Virtual Control Panel**: shows the VCP on the display (values: `On`/`Off`) (Acorn Install
§6.15, p.92).

## Control Peripheral Wireless MPG Configuration (§6.16)

**Centroid Wireless MPG**: select the connected MPG model (Acorn Install §6.16, p.93).
**MPG Performance**: adjusts the MPG's reaction speed (Acorn Install §6.16, p.93).
**Macro Button Configuration**: assigns custom macros to MPG buttons 1-4 via each button's
`Edit` (Acorn Install §6.16, p.93).

## DB25 Connector Selection and Optional Mapping (§6.17)

**Step and direction output**: `Screw Terminal` (default; for AC servo drives accepting 24V
open-collector signals, pins fixed per the Acorn schematics) or `DB25 Port` (for stepper
drives using 5V step/direction signals — used in most cases) (Acorn Install §6.17, p.94).
**DB25 pin mapping**: `Enable DB25 use default pin mapping` (the long-standing Gecko
G540/Mach3 standard, used by most installs) or create a custom DB25 pin map for non-standard
drives/breakout boards, avoiding a custom cable (Acorn Install §6.17, p.95).
**DB25 port — Enabled**: turns on the DB25 port (Acorn Install §6.17, p.95).
**DB25 port — Use default Pin assignments**: keeps default pins, or re-maps them; `Charge
Pump` cannot be re-mapped off pin 16 (`Output 3`) — it's only physically present there (Acorn
Install §6.17, p.95).

See [hardware.md](hardware.md#db25-h6-connector-pinout) for the DB25 pinout.

## CNC Control Preferences (§6.18)

**CNC12 Configuration Menu password**: password gating the CNC12 configuration menus, to
prevent accidental operator edits; default `137` (Acorn Install §6.18, p.96).
**Display Distance To Go**: shows a Distance-to-Go readout on the main screen (Acorn Install
§6.18, p.96).
**Display Machine Coordinates**: shows a Machine Coordinates readout on the main screen
(Acorn Install §6.18, p.96).
**Display Active G&M Codes**: shows active G/M codes, `While in MDI` or `Always` (Acorn
Install §6.18, p.96).
**Feedrate Override — Maximum percentage**: caps feedrate override, up to `200%`; `100%` is
advised for most open-loop systems (Acorn Install §6.18, p.96).
**Minimum percentage to invoke Feed Hold**: feed hold engages once feedrate override drops
below this value (useful with a Wireless MPG); typical `1-2%` for mills, `2-3%` for routers;
`0` disables (Acorn Install §6.18, p.97).
**Clean Filter Reminder Message**: `0` disables it, otherwise days between reminders (Acorn
Install §6.18, p.97).
**Run Time Graphics on Start Up**: forces run-time graphics on for every job (requires a
CNC12 restart); `No` still allows selecting it per job (Acorn Install §6.18, p.97).
**Remember Last G Code Program after restart**: reloads the last G-code program on startup
(Acorn Install §6.18, p.97).
**Allow CYCLE START in Run Menu**: lets the operator start a program from the Run Menu
without returning to the main menu first (Acorn Install §6.18, p.97).
**Display Keyboard Jogging Legend on Alt+J press**: shows the keyboard-jogging shortcut
legend when `Alt+J` is pressed (Acorn Install §6.18, p.97).
**VCP jogging state on Acorn power up**: startup Fast/Slow and Continuous/Incremental
default; typical `Slow Incremental` or `Slow Continuous` for mill/lathe, `Slow Continuous` or
`Fast Continuous` for router (Acorn Install §6.18, p.97).
**Custom VCP Skin**: when set, stops the Wizard from overwriting a custom VCP; see the VCP
manual (Acorn Install §6.18, p.97).
**Part G Code Preview on Job Load**: shows the start of the loaded G-code program without
opening an editor (Acorn Install §6.18, p.97).
**Pop Up Pins Deactivate on Cycle Start**: auto-retracts pop-up pins on cycle start, guarding
against a forgotten retract in the program (Acorn Install §6.18, p.97).
**Disable Worklight on Startup**: keeps the worklight off at power-on instead of the default
on; the VCP worklight button still always works (Acorn Install §6.18, p.98).
**Keyboard Jogging: Enter Key = Cycle Start**: makes the PC keyboard Enter key act as cycle
start (Acorn Install §6.18, p.98).
**USB/Keyboard Jogging active on CNC12 Startup**: activates USB/keyboard jogging at boot
instead of requiring `Alt+J` first (a safety default) (Acorn Install §6.18, p.98).

## Wizard Preferences (§6.19)

**Start Up Size**: Wizard dialog window size; default `Normal` (Acorn Install §6.19, p.98).
**Start Up Location**: Wizard dialog's desktop position; default `Top Left` (Acorn Install
§6.19, p.98).
**Always on Top**: keeps the Wizard above other windows (values: `Yes`/`No`) (Acorn Install
§6.19, p.98).
**Ask for password when opening Wizard**: locks the Wizard behind the Configuration Menu
password (Acorn Install §6.19, p.99).

## Custom PLC preference

**Custom PLC**: when a custom PLC program is in use, this setting tells the Wizard not to
overwrite it (Acorn Install §6.19, p.98).

## Preferences: VCP Aux Keys Macro Assignments (§6.20)

**Virtual Control Panel Macro Assignments**: lists the macros pre-assigned to VCP buttons;
see the VCP Users manual for details (Acorn Install §6.20, p.99).

## Lube Pump Preferences (§6.21)

**Lube Pump Type**: `Mechanical` (output on continuously while CNC12 runs a job/MDI, for
pumps with their own timer), `Direct Controlled` (output pulses on 15s after every 30min of
job/MDI running, for pumps that dispense while powered), `Electronic` (for `Lube First` /
`Lube Last` pumps), or `Custom` (user-defined timer) (Acorn Install §6.21, p.100). See Lube
Pump Tech Bulletin #171 for more.
