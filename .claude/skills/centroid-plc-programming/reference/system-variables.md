# Centroid CNC12 SV_* System Variable Catalog

This catalog is a re-verified subset of the `SV_*` system variables documented in the PLC
Manual's Appendix D (PLC Manual, PDF p.102-120) and Appendices H-K (PDF p.128-132), grouped by
function; Appendix D itself is the full list. Types: `M` memory bit, `I32`/`I64` signed integer,
`F32`/`F64` floating-point (PLC Manual, PDF p.102).

Appendix D splits variables into two write-direction tables, **CNC Software Write-Controlled**
(CNC → PLC, starting PDF p.104) and **PLC Write-Controlled** (PLC → CNC, starting PDF p.113).
Direction below follows the table an SV is printed in, not its name — see
[resources.md](resources.md#system-variables-sv) for the `SV_PLC_BUS_ONLINE` /
`SV_PLC_IO2_ONLINE` exception. Indexed families the manual prints as a range (e.g.
`SV_AXIS_VALID_1-8`, or the axis-letter form `SV_?_AXIS_VALID`) are listed once, using the
manual's own notation, rather than expanded per instance.

---

## Spindle

Rows below are drawn from PLC Manual, PDF p.104-120 (see the Page column for each fact's exact
page).

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_SPINDLE_LOW_RANGE` | M | PLC→CNC | Must be SET for rigid tapping and spindle-speed display to work correctly; combined with `SV_SPINDLE_MID_RANGE`, up to four gear ranges are supported. | p.113 |
| `SV_SPINDLE_MID_RANGE` | M | PLC→CNC | Must be SET for rigid tapping and spindle-speed display to work correctly; combined with `SV_SPINDLE_LOW_RANGE`, up to four gear ranges are supported. | p.113 |
| `SV_SPINDLE_FAULT` | M | PLC→CNC | Obsolete. Do not use. | p.113 |
| `SV_SPINDLE_METER` | F32 | PLC→CNC | Maps to the `SV_METER_x` (1-16, see [Meters and misc](#meters-and-misc)) slot for the spindle axis. | p.120 |
| `SV_PC_DAC_SPINDLE_SPEED` | I32 | CNC→PLC | DAC spindle speed as requested by CNC software (0-65535). | p.107 |
| `SV_PC_COMMANDED_SPINDLE_SPEED` | F32 | CNC→PLC | Commanded "S" value with Spindle Override factored in; Parameters 65-67 for spindle range must still be controlled in the PLC program. | p.112 |
| `SV_PC_RIGID_TAP_SPINDLE_OFF` | M | CNC→PLC | CNC software SETs this to signal the spindle should turn off at rigid-tap depth, needed only if Parameter 36 bit 4 is SET and turning off the spindle takes more than clearing M3/M4 (CNC clears only one of M3 or M4 during a rigid tap, not both). | p.104-105 |
| `SV_PLC_SPINDLE_SPEED` | I32 | PLC→CNC | If Parameter 78 is not set to display actual spindle speed, this is the value CNC shows on-screen. | p.117 |
| `SV_PLC_SPINDLE_KNOB` | I32 | PLC→CNC | Spindle-speed override percentage sent to the PLC (spindle knob). | p.117 |
| `SV_PLC_FUNCTION_37` | M | PLC→CNC | Spindle Start. | p.114 |
| `SV_PLC_FUNCTION_38` | M | PLC→CNC | Spindle Stop. | p.114 |
| `SV_PLC_FUNCTION_98` | M | PLC→CNC | Select Spindle CCW. | p.114 |
| `SV_PLC_FUNCTION_99` | M | PLC→CNC | Select Spindle CW. | p.114 |
| `SV_PLC_FUNCTION_106` | M | PLC→CNC | Spindle Override +. | p.114 |
| `SV_PLC_FUNCTION_107` | M | PLC→CNC | Spindle Override -. | p.115 |
| `SV_PLC_FUNCTION_108` | M | PLC→CNC | Select Spindle Override / 100%. | p.115 |

---

## Tool / tool-change

Rows below are drawn from PLC Manual, PDF p.104-119 (see the Page column for each fact's exact
page).

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_TOOL_NUMBER` | I32 | CNC→PLC | Set as part of a tool change (M107) to indicate the requested tool number; under "enhanced ATC" this is actually a request for a carousel bin location. | p.107 |
| `SV_ATC_CAROUSEL_POSITION` | I32 | CNC→PLC | Sent by CNC software at startup or as part of an "enhanced ATC" reset. | p.107 |
| `SV_ATC_TOOL_IN_SPINDLE` | I32 | CNC→PLC | Sent by CNC software at startup when the `.job` file is parsed, or as part of an "enhanced ATC" reset. | p.107 |
| `SV_PLC_CAROUSEL_POSITION` | I32 | PLC→CNC | Carousel bin position; the carousel must not be allowed to turn unless CNC software is running. When Parameter 160 = 0, CNC uses this to determine Active Tool and expects a BCD value; when Parameter 160 != 0, CNC also uses it for carousel position and tool putback, and expects normal binary. | p.117 |
| `SV_SYS_MACRO` | I32 | PLC→CNC | Setting a non-zero value while CNC software is at the main menu makes CNC software load and run the G-code program `MPGmacro#.mac` from the system directory (e.g. `\cncm\system\MPGmacro3.mac` for `SV_SYS_MACRO = 3` on a Mill system); can be set negative. | p.119 |
| `SV_M94_M95_1-128` | M | CNC→PLC | Used for M-codes needing PLC interaction (M3, M4, M6, M7, M8, M10, M11 and custom M-codes); set/reset from M/G-code programs with `M94`/`M95`. Also settable by the PLC program itself, even though the table labels them Read Only for the PLC. CNC11 has built-in default actions for some M-codes that control the first 16 of these variables, e.g. `IF !SV_PROGRAM_RUNNING THEN RST M3, RST M4, RST M7, RST M8`. See [resources.md](resources.md#triggering-plc-actions-with-m94m95) for which requests those default actions cover (Router Manual §13.28, p.290). | p.104 |

---

## Jog / MPG

This group is drawn from PLC Manual, PDF p.103-120 (see each subsection and the Page column for
exact pages).

### MPG groups

Up to nine independent MPG groups: 1-3 from V3.00.00, 4-9 added at V5.10.00 (PLC Manual, PDF
p.115, p.118).

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_MPG_x_AXIS_SELECT` (1-9) | I32 | PLC→CNC | Currently selected axis for the MPG group (1-8); change takes effect only when MPG movement is stopped. | p.103, p.118 |
| `SV_MPG_x_MULTIPLIER` (1-9) | I32 | PLC→CNC | MPG multiplier value, normally 1, 10 or 100. | p.118 |
| `SV_MPG_x_ENABLED` (1-9) | M | PLC→CNC | MPG group is enabled; switches between MPG mode and vector-controlled mode for all axes in the group. While enabled, the MPU will not process motion vectors from the PC or allow jogging. | p.115 |
| `SV_MPG_x_WINDUP_MODE` (1-9) | M | PLC→CNC | MPG moves the total distance commanded by the encoder input; typically enabled for x1/x10, disabled for x100 (disabling it while the MPG can't keep up shows "MPG moving too fast"). | p.115 |
| `SV_MPG_x_OFFSET_MODE` (1-9) | M | PLC→CNC | MPG movement is added to the current Expected Position instead of setting it; the MPG can command motion independently while vectors are being processed. | p.115-116 |
| `SV_MPG_x_PLC_MPG_MODE` (1-9) | M | PLC→CNC | MPG encoder input is read from `SV_MPG_1_PLC_OFFSET` instead of the actual encoder; the PLC program can change that offset to move the MPG axis. | p.116 |
| `SV_MPG_x_PLC_OFFSET` (1-9) | I32 | PLC→CNC | MPG offset for PLC-controlled MPG input, letting the PLC drive the MPG through an analog-to-digital input rather than an encoder; enabled when the group's `PLC_MPG_MODE` bit is set. | p.118 |

### USB wireless MPG

Rows below are drawn from PLC Manual, PDF p.106, p.110-111.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_USB_MPG_POWER` | M | CNC→PLC | Set when the USB wireless MPG is powered on; requires a state change of the MPG to be detected. | p.106 |
| `SV_USB_MPG_AXIS_SELECT` | I32 | CNC→PLC | Wireless USB MPG axis-select switch: 0 = Off, 1-6 = selected axis (X, Y, Z, 4th, 5th, 6th). | p.110 |
| `SV_USB_MPG_SCALE_SELECT` | I32 | CNC→PLC | Wireless USB MPG scale-selector knob: 1 = x1, 100 = x100, 1000 = SPIN, 10000 = FEED. | p.111 |
| `SV_USB_MPG_ENCODER_WHEEL` | I32 | CNC→PLC | Wireless MPG wheel position; counts up and down and does not roll over. | p.111 |
| `SV_USB_MPG_BUTTON_STATE` | I32 | CNC→PLC | Wireless MPG button state bits: 0 = Reset (Cycle Cancel), 1 = Feed Hold, 2 = Cycle Start, 3 = Jog Plus, 4 = Jog Minus, 5 = SPIN Auto/Man, 6 = SPIN On/Off, 7-10 = Macro 1-4, 11 = Tool Check, 12 = Set Zero. | p.111 |

> The manual's scale-selector list prints both `10 = x100` and `100 = x100` (PLC Manual, PDF
> p.111); `10 = x10` is almost certainly intended.

### Jog panel link and debounce

Rows below are drawn from PLC Manual, PDF p.104-105, p.117.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_JOG_LINK_ONLINE` | M | CNC→PLC | 1 = valid jog panel detected as Jogboard. | p.104 |
| `SV_JOG_PANEL_REQUIRED` | M | CNC→PLC | Reflects the "Jog Panel Required" setting in CNC software's Control Configuration menu. | p.105 |
| `SV_PC_VIRTUAL_JOGPANEL_ACTIVE` | M | CNC→PLC | Indicates the user has activated the keyboard (virtual) jog panel with ALT-J; most functions besides jogging are allowed without the screen up by default. | p.105 |
| `SV_PLC_DEBOUNCE_x` (1-64) | I32 | PLC→CNC | Debounce configuration word for the first 240 PLC inputs. | p.117 |
| `SV_JOG_LINK_DEBOUNCE_x` (1-32) | I32 | PLC→CNC | Jog Panel input debounce configuration words. | p.117 |

### Axis absolute position

Rows below are drawn from PLC Manual, PDF p.103, p.111.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_MPU11_ABS_POS_x` (0-7) | I64 | CNC→PLC | Absolute position of the axis in encoder counts, same value CNC reports and shows in the PID screen as AbsPos; index is zero-based (0-7 for 8 axes), unlike most other `_1-8` families. Should be read once per PLC pass — written externally. | p.103, p.111 |

### PLC function commands (jog panel / cycle control)

The PLC function bits are SET by the PLC program to send control commands to CNC software (cycle
start/cancel, jog mode selection, axis jog, feedhold, etc.); all are type M, direction PLC→CNC
(PLC Manual, PDF p.113-115).
Spindle-specific bits are in [Spindle](#spindle) and coolant-specific bits are in
[Coolant](#coolant).

| SV_ name | Meaning | Page |
|---|---|---|
| `SV_PLC_FUNCTION_0` | Invalid (do not use). | p.113 |
| `SV_PLC_FUNCTION_1` | Cycle Cancel. | p.113 |
| `SV_PLC_FUNCTION_2` | Cycle Start. | p.113 |
| `SV_PLC_FUNCTION_3` | Tool Check. | p.113 |
| `SV_PLC_FUNCTION_4` | Select Single Block. | p.113 |
| `SV_PLC_FUNCTION_5` | Select X1 Jog Mode. | p.113 |
| `SV_PLC_FUNCTION_6` | Select X10 Jog Mode. | p.113 |
| `SV_PLC_FUNCTION_7` | Select X100 Jog Mode. | p.113 |
| `SV_PLC_FUNCTION_8` | Not used (formerly User Jog Inc Mode). | p.113 |
| `SV_PLC_FUNCTION_9` | Select Inc/Cont Jog Mode. | p.113 |
| `SV_PLC_FUNCTION_10` | Select Fast/Slow Jog Mode. | p.113 |
| `SV_PLC_FUNCTION_11` | Select Mpg Mode. | p.113 |
| `SV_PLC_FUNCTION_12` | Axis 1 + Jog. | p.113 |
| `SV_PLC_FUNCTION_13` | Axis 1 - Jog. | p.113 |
| `SV_PLC_FUNCTION_14` | Axis 2 + Jog. | p.113 |
| `SV_PLC_FUNCTION_15` | Axis 2 - Jog. | p.113 |
| `SV_PLC_FUNCTION_16` | Axis 3 + Jog. | p.113 |
| `SV_PLC_FUNCTION_17` | Axis 3 - Jog. | p.114 |
| `SV_PLC_FUNCTION_18` | Axis 4 + Jog. | p.114 |
| `SV_PLC_FUNCTION_19` | Axis 4 - Jog. | p.114 |
| `SV_PLC_FUNCTION_20` | Axis 5 + Jog. | p.114 |
| `SV_PLC_FUNCTION_21` | Axis 5 - Jog. | p.114 |
| `SV_PLC_FUNCTION_22` | Axis 6 + Jog. | p.114 |
| `SV_PLC_FUNCTION_23` | Axis 6 - Jog. | p.114 |
| `SV_PLC_FUNCTION_24` | Aux1. | p.114 |
| `SV_PLC_FUNCTION_25` | Aux2. | p.114 |
| `SV_PLC_FUNCTION_26` | Aux3. | p.114 |
| `SV_PLC_FUNCTION_27` | Aux4. | p.114 |
| `SV_PLC_FUNCTION_28` | Aux5. | p.114 |
| `SV_PLC_FUNCTION_29` | Aux6. | p.114 |
| `SV_PLC_FUNCTION_30` | Aux7. | p.114 |
| `SV_PLC_FUNCTION_31` | Aux8. | p.114 |
| `SV_PLC_FUNCTION_32` | Aux9. | p.114 |
| `SV_PLC_FUNCTION_33` | Aux10. | p.114 |
| `SV_PLC_FUNCTION_34` | Select Rapid Override; deprecated in favor of `SV_PC_TOGGLE_RAPID_OVERRIDE`. | p.103, p.114 |
| `SV_PLC_FUNCTION_35` | Select Man or Auto Spindle Mode. | p.114 |
| `SV_PLC_FUNCTION_36` | Do not use. | p.114 |
| `SV_PLC_FUNCTION_39` | Aux11. | p.114 |
| `SV_PLC_FUNCTION_40` | Aux12. | p.114 |
| `SV_PLC_FUNCTION_41` | Deprecated. Do not use. | p.114 |
| `SV_PLC_FUNCTION_42` | Deprecated. Do not use. | p.114 |
| `SV_PLC_FUNCTION_45` | Feed Hold. | p.114 |
| `SV_PLC_FUNCTION_46-97` | Do not use. | p.114 |
| `SV_PLC_FUNCTION_100-103` | Do not use. | p.114 |
| `SV_PLC_FUNCTION_105` | Do not use. | p.114 |
| `SV_PLC_FUNCTION_109` | Escape Key (sent to the PC). | p.115 |
| `SV_PLC_FUNCTION_110` | Axis 7 Jog +. | p.115 |
| `SV_PLC_FUNCTION_111` | Axis 7 Jog -. | p.115 |
| `SV_PLC_FUNCTION_112` | Axis 8 Jog +. | p.115 |
| `SV_PLC_FUNCTION_113` | Axis 8 Jog -. | p.115 |
| `SV_PLC_FUNCTION_114-127` | Unused. | p.115 |

---

## Coolant

Rows below are drawn from PLC Manual, PDF p.114.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PLC_FUNCTION_43` | M | PLC→CNC | Select Coolant Flood. | p.114 |
| `SV_PLC_FUNCTION_44` | M | PLC→CNC | Select Coolant Mist. | p.114 |
| `SV_PLC_FUNCTION_104` | M | PLC→CNC | Coolant Auto / Manual Mode. | p.114 |

---

## Machine parameters

Row below is drawn from PLC Manual, PDF p.112.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_MACHINE_PARAMETER_0-999` | F32 | CNC→PLC | Machine parameter value as entered in CNC software; converted from the 64-bit float CNC software actually maintains, so there may be some precision loss. | p.112 |

Machine parameter meanings are in the Router Manual parameter index (Router Manual §15.7, p.320).

### Control configuration

Rows below are drawn from PLC Manual, PDF p.112.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PC_CONFIG_MIN_SPINDLE_SPEED` | F32 | CNC→PLC | Minimum spindle speed from the control configuration. | p.112 |
| `SV_PC_CONFIG_MAX_SPINDLE_SPEED` | F32 | CNC→PLC | Maximum spindle speed from the control configuration. | p.112 |

---

## System state, faults, and program control

Rows below are drawn from PLC Manual, PDF p.102-117.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_STOP` | M | PLC→CNC | SET by the PLC program on a critical error or E-Stop press, to signal CNC software and the MPU to prevent axis motion, spindle commands and ATC changes; RST when E-Stop is released and no other errors remain. Write only once per PLC pass. | p.102, p.113 |
| `SV_PROGRAM_RUNNING` | M | CNC→PLC | 1 = MDI mode or a job is in progress. | p.104 |
| `SV_MDI_MODE` | M | CNC→PLC | 1 = MDI mode active. | p.104 |
| `SV_PC_HOME_SET` | M | CNC→PLC | 1 = home set for all valid axes; check this to force slow jog before homing unless Parameter 148 bit 0 is set. | p.105 |
| `SV_JOB_IN_PROGRESS` | M | CNC→PLC | Set when CNC software is running a job or an MDI command, but not while waiting at the MDI prompt. | p.105 |
| `SV_LIMIT_TRIPPED` | M | CNC→PLC | 1 = any configured limit switch is tripped, 0 = none tripped; the PLC program is not required to act on this bit. | p.105 |
| `SV_PC_SOFTWARE_READY` | M | CNC→PLC | 1 = CNC software is initialized and communicating with the MPU normally; 0 = CNC software exited normally or a communication fault occurred. Intended to disable certain PLC functions when CNC software is not running (e.g. an ATC carousel should not rotate). | p.105 |
| `SV_STALL_ERROR` | M | PLC→CNC | 1 = MPU11 detected an error the PLC should handle (see `SV_STALL_REASON`, `SV_STALL_AXIS`); the PLC should turn off all enables including `SV_MASTER_ENABLE`, and RST this bit if the error occurred and E-Stop is pushed in. | p.115 |
| `SV_STALL_REASON` | I32 | CNC→PLC | Set whenever `SV_STALL_ERROR` is set: 0 No Error, 1 position error, 2 full power without motion, 3 encoder differential error, 4 spindle slave position error, 6 OpticDirect C8 error, 15 scale encoder differential error, 16 encoder quadrature error, 17 scale encoder quadrature error, 18 standoff error, 19 scale position error, 99 master enable turned off. | p.107-108 |
| `SV_STALL_AXIS` | I32 | CNC→PLC | Set whenever `SV_STALL_ERROR` is set, to the axis (1-based) associated with the stall; 255 if not applicable. | p.108 |
| `SV_PLC_FAULT_STATUS` | I32 | PLC→CNC | Bitwise PLC executor fault: `0x00000001` DIV_BY_ZERO, `0x00000002` OUT_OF_BOUNDS, `0x00000004` INVALID_OPCODE. | p.117 |
| `SV_PLC_FAULT_ADDRESS` | I32 | PLC→CNC | Address in the PLC program where the fault in `SV_PLC_FAULT_STATUS` occurred. | p.117 |
| `SV_MASTER_ENABLE` | M | PLC→CNC | PLC sets this bit to turn on the Master Enable to hardware devices (drives and PLCs). | p.115 |
| `SV_ENABLE_IO_OVERRIDE` | M | PLC→CNC | When SET by the PLC program, CNC software indirectly allows inversion and forcing of PLC bits through the live PLC display (ALT-I) by manipulating machine parameters 911-939, which the PLC program uses directly to set the forcing/inversion system variables. | p.116 |
| `SV_TRIGGER_PLOT_DUMP` | M | PLC→CNC | Internal debugging: when SET, starts a debug dump sent to CNC software, which launches `plot.exe`; without custom-built CNC software the dump has no useful data. | p.116 |

> `SV_STALL_ERROR` is printed in the PLC → CNC table (p.115), but p.103's "Externally Written
> System Variables" list also names it — meaning it is actually written by the MPU outside the
> PLC program's control flow, and the PLC should read it once per pass and only RST it under the
> stated condition (PLC Manual, PDF p.103, p.115).

---

## Axis validity, drive status, and power

Rows below are drawn from PLC Manual, PDF p.103-107, p.110, p.115.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_AXIS_VALID_1-8` / `SV_?_AXIS_VALID` | M | CNC→PLC | 1 = the Motor Parameters screen axis label allows motion; allowed labels are X, Y, Z, A, B, C, U, V, W. | p.104 |
| `SV_DRIVE_ONLINE_1-8` / `SV_?_AXIS_DRIVE_ONLINE` | M | CNC→PLC | 1 = the drive for the axis is detected. | p.104 |
| `SV_DRIVE_TYPE_x` (1-8) / `SV_?_AXIS_DRIVE_TYPE` | I32 | CNC→PLC | Type of drive connected to the axis; values include `13 = ACORN` and `24 = ACORNSIX`. | p.110 |
| `SV_ENABLE_AXIS_x` (1-8) | M | PLC→CNC | Obsolete. Do not use. | p.115 |
| `SV_PC_POWER_AXIS_x` (1-8) / `SV_?_AXIS_POWERED` | M | CNC→PLC | 1 = the axis is powered and holding position. Read only once per PLC pass — written externally. | p.103-104 |
| `SV_PC_CYCLONE_STATUS_x` (1-16) | I32 | CNC→PLC | PLC and drive status bits; bit meanings by board generation are in [Appendix H](#appendix-h-cyclone--mcu-status-sv-information). | p.107 |
| `SV_PC_MCU_STATUS_x` (1-16) | I32 | CNC→PLC | MPU13 EtherCAT-processor status bits; bit meanings are in [Appendix H](#appendix-h-cyclone--mcu-status-sv-information). | p.111 |
| `SV_PC_MINI_PLC_ONLINE` | I32 | CNC→PLC | Online bits for PLCADD1616 and other expansion PLC modules: bit 0 = miniPLC1 online, ... bit 15 = miniPLC16 online; bits 16-31 reserved. | p.107 |
| `SV_PLC_BUS_ONLINE` | M | CNC→PLC | 1 = valid MPU11 PLC detected; checked as part of the Fiber Checking PLC program section. | p.104 |
| `SV_PLC_IO2_ONLINE` | M | CNC→PLC | 1 = IO2 Legacy PLC detected. | p.104 |
| `SV_?_AXIS_FIBER_OK` | M | CNC→PLC | Nine system variables mapped to the bits in `SV_PC_CYCLONE_STATUS_2` by axis label (X, Y, Z, A, B, C, U, V, W); a convenience for PLC programs that handle axis changes. | p.105-106 |
| `SV_?_AXIS_POWERED` | M | CNC→PLC | See `SV_PC_POWER_AXIS_x` above. | p.104 |

`SV_PLC_BUS_ONLINE` and `SV_PLC_IO2_ONLINE` are CNC-written despite the `SV_PLC_` prefix — see
[resources.md](resources.md#system-variables-sv).

---

## Override and feedrate

Rows below are drawn from PLC Manual, PDF p.102-105, p.107, p.120.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PLC_FEEDRATE_KNOB` | I32 | PLC→CNC | Feedrate knob as the PLC would have CNC11 see it. Write only once per PLC pass. | p.102, p.117 |
| `SV_PLC_FEEDRATE_OVERRIDE` | F32 | PLC→CNC | Feedrate factor for MPU11 motion control, 0-2.0; 1.0 = no change to the programmed or jog-rate value. The MPU caps the feedrate to the Machine Setup maximum. Never apply a negative value. Write only once per PLC pass. | p.102, p.120 |
| `SV_PLC_RAPID_FEEDRATE_OVERRIDE` | F32 | PLC→CNC | Rapid-rate factor for MPU motion control, 0 (exclusive) to 1.0; 1.0 = no change to the programmed rapid rate. When set to 0, the MPU reverts to using `SV_PLC_FEEDRATE_OVERRIDE` for rapid rates. The MPU caps the rapid rate to the machine-configuration maximum. | p.120 |
| `SV_PC_TOGGLE_RAPID_OVERRIDE` | M | CNC→PLC | CNC software SETs this bit when the state of Rapid Override needs to change; the PLC should RST it after toggling Rapid Override. Named by `SV_PLC_FUNCTION_34` as its replacement (see [PLC function commands](#plc-function-commands-jog-panel--cycle-control)). | p.105 |
| `SV_PC_FEEDRATE_PERCENTAGE` | I32 | CNC→PLC | 0-200% adjustment for axis motion control, sent for machine parameter 78 bit 1 checking and on-screen display; not needed if `SV_PC_OVERRIDE_CONTROL_FEEDRATE_OVERRIDE` is not SET. Read only once per PLC pass — written externally. | p.103, p.107 |
| `SV_PC_OVERRIDE_CONTROL_FEEDRATE_OVERRIDE` | M | CNC→PLC | 1 = the Feedrate Override Knob is allowed to change the feedrate on axis motion. | p.104 |
| `SV_PC_OVERRIDE_CONTROL_FEEDHOLD` | M | CNC→PLC | 1 = Feedhold pauses the G-code program. | p.104 |

---

## Set axis part zero

Row below is drawn from PLC Manual, PDF p.116.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PLC_SET_AXIS_x_PART_ZERO` (1-8) | M | PLC→CNC | When SET by the PLC program while not running a job and at the main screen, requests CNC software to set Part Zero for the axis. | p.116 |

---

## I/O inversion and forcing

Used together with `SV_ENABLE_IO_OVERRIDE` and machine parameters 911-939 to allow live I/O
overrides from the PLC display (ALT-I) (PLC Manual, PDF p.116, p.118-119). Each stem is five
16-bit words spanning I/O 1-80 (`1_16`, `17_32`, `33_48`, `49_64`, `65_80`), least significant
bit mapped to the lower-numbered I/O point; only the first and last word of each family are
named below.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_INVERT_INP1_16_BITS`-`SV_INVERT_INP65_80_BITS` | I32 | PLC→CNC | Inverts the indicated inputs. | p.118 |
| `SV_FORCE_INP1_16_BITS`-`SV_FORCE_INP65_80_BITS` | I32 | PLC→CNC | Forces the indicated inputs on if the corresponding `SV_INVERT_INP` bit is clear, off if set. | p.118 |
| `SV_FORCE_ON_OUT1_16_BITS`-`SV_FORCE_ON_OUT65_80_BITS` | I32 | PLC→CNC | Forces the indicated outputs ON; the corresponding `SV_FORCE_OFF*` bit must be clear. | p.118-119 |
| `SV_FORCE_OFF_OUT1_16_BITS`-`SV_FORCE_OFF_OUT65_80_BITS` | I32 | PLC→CNC | Forces the indicated outputs OFF; the corresponding `SV_FORCE_ON*` bit must be clear. | p.119 |
| `SV_FORCE_ON_MEM1_16_BITS`-`SV_FORCE_ON_MEM65_80_BITS` (only 4 words — see note) | I32 | PLC→CNC | Forces the indicated memory bits ON; the corresponding `SV_FORCE_OFF_MEM` bit must be clear. The forced state is applied between PLC program passes — the PLC program can still change the bit during execution. | p.119 |
| `SV_FORCE_OFF_MEM1_16_BITS`-`SV_FORCE_OFF_MEM65_80_BITS` | I32 | PLC→CNC | Forces the indicated memory bits OFF; the corresponding `SV_FORCE_ON_MEM` bit must be clear. Same between-pass timing as above. | p.119 |

> The manual's `SV_FORCE_ON_MEM*` row prints `SV_FORCE_ON_MEM33_48_BITS` twice and has no
> `SV_FORCE_ON_MEM49_64_BITS` entry, unlike its four sibling families which all cover 1-16
> through 65-80 (PLC Manual, PDF p.119). This looks like a manual typo; only the four names it
> actually prints are listed above.

---

## Meters and misc

Row below is drawn from PLC Manual, PDF p.120.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_METER_x` (1-16) / `SV_?_AXIS_METER` | F32 | PLC→CNC | Set by the PLC program to -100.0 to 100.0, for CNC software to display as a meter in the DRO. Only the first eight are used; meters 9-16 are reserved for future use. | p.120 |

---

## PC keyboard key state

Row below is drawn from PLC Manual, PDF p.100, p.105.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PC_KEYBOARD_KEY_x` (1-104) | M | CNC→PLC | 1 = keyboard key pressed, 0 = not pressed. See PLC Manual App C for the key-number to physical-key map. | p.100, p.105 |

---

## Skin events (CNC skinning API)

Row below is drawn from PLC Manual, PDF p.106.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_SKIN_EVENT_1-255` | M | CNC→PLC | Generic events SET/RST by skinning applications via the CNC Skinning API — e.g. the Centroid Virtual Control Panel (VCP), which uses them for virtual jog-panel button states. Convention: `SV_SKIN_EVENT_1` through `SV_SKIN_EVENT_50` map to the fifty keys on a real hardware jog panel, left to right and top to bottom, with `SV_SKIN_EVENT_1` = Spindle+ and `SV_SKIN_EVENT_50` = CYCLE_START. | p.106 |

---

## Appendix H: Cyclone & MCU Status SV Information

`SV_PC_CYCLONE_STATUS_x` (see [Axis validity, drive status, and power](#axis-validity-drive-status-and-power))
carries the same information the cyclone processor itself uses, so each board generation may use
the bits differently, though the manual keeps them consistent where it can (PLC Manual, PDF
p.128). Board labels below are verbatim from the manual's column headers.

**`SV_PC_CYCLONE_STATUS_1`** — MPU13 (Hickory), MPU12 (AcornSix) and MPU11 (MPU11, ALLIN1DC, OAK)
share this layout:

| Bits | Meaning |
|---|---|
| 0-20 | Reserved |
| 21 | PLCbus external device enabled |
| 22 | Reserved |
| 24-31 | Reserved |

> Bit 23: `JOGlink external device enabled` on MPU13 (Hickory); the table prints no entry for
> MPU12 (AcornSix) or MPU11 (MPU11, ALLIN1DC, OAK) at bit 23 (PLC Manual, PDF p.128).

**`SV_PC_CYCLONE_STATUS_2`** — same for all three board generations:

| Bits | Meaning |
|---|---|
| 0-7 | Drive Axis 1-8 Enabled |
| 8-31 | Reserved |

**`SV_PC_CYCLONE_STATUS_3`**: bits 0-31 Reserved, all board generations.

**`SV_PC_CYCLONE_STATUS_4`**:

| Bits | MPU13 (Hickory) | MPU12 (AcornSix) | MPU11 (MPU11, ALLIN1DC, OAK) |
|---|---|---|---|
| 0-1 | Reserved | Reserved | Reserved |
| 2 | MCU Shutdown Detected | Reserved | Reserved |
| 3-31 | Reserved | Reserved | Reserved |

**`SV_PC_CYCLONE_STATUS_5-16`**: bits 0-31 Reserved, all board generations.

MPU13 systems also have `SV_PC_MCU_STATUS_x` (see [Axis validity, drive status, and power](#axis-validity-drive-status-and-power))
for the EtherCAT processor (PLC Manual, PDF p.128):

**`SV_PC_MCU_STATUS_1-3`**: bits 0-31 Reserved.

**`SV_PC_MCU_STATUS_4`**:

| Bits | Meaning |
|---|---|
| 0-15 | Reserved |
| 16 | EtherCAT is in OP Mode |
| 17-31 | Reserved |

**`SV_PC_MCU_STATUS_5-16`**: bits 0-31 Reserved.

---

## Appendix I: Drive Status SV Information

`SV_DRIVE_STATUS_x` (1-8) / `SV_?_AXIS_DRIVE_STATUS` (I32, CNC→PLC, PLC Manual, PDF p.107) is a
High Speed Drive Status word whose bit meanings are separated by drive type (PLC Manual, PDF
p.129-130):

**ALLIN1DC/DC3IOB**

| Bit | Meaning |
|---|---|
| 0 | Current Setting Low |
| 1 | Current Setting High |
| 2 | High power enable — FETs are installed to handle 15A current setting |
| 3 | Drive master/slave — 1 = communication on fibers, 0 = communication on wires |
| 4 | Aux 1 jumper state — 1 = jumper block removed, 0 = jumper block in place |
| 5 | Aux 2 jumper state — 1 = jumper block removed, 0 = jumper block in place |
| 6-15 | Reserved |

**DC1**

| Bit | Meaning |
|---|---|
| 0 | Current Setting Low |
| 1 | Current Setting High |
| 2 | High power enabled — FETs are installed to handle 15A current setting |
| 3-4 | Reserved |
| 5 | Spare jumper state — 1 = jumper block removed, 0 = jumper block in place |
| 6 | Plus Limit State |
| 7 | Minus Limit State |
| 8-15 | Reserved |

**Optic 4**

| Bit | Meaning |
|---|---|
| 0-10 | Reserved |
| 11 | Quadrature Error: incorrect encoder state transition |
| 12 | Direction Bit |
| 13 | Index Pulse |
| 14 | Differential error on encoder A or B channel |
| 15 | Drive fault from 3rd-party drive (1 = fault, or no voltage at input) |

**Optic Direct**

| Bit | Meaning |
|---|---|
| 0-1 | Reserved |
| 2 | Acceleration too high |
| 3 | Quadrature Generation Error |
| 4 | On-board test point |
| 5-7 | Alarm code bit 3, 2, 1 |
| 8 | /TGON — above speed |
| 9 | Holding Brake State |
| 10 | /S_RDY — Servo Ready |
| 11 | Quadrature error |
| 12 | Direction bit |
| 13 | Index Pulse |
| 14 | Differential error on encoder A or B channel |
| 15 | Drive fault from 3rd-party drive (1 = fault, or no voltage at input) |

---

## Appendix J: Error Counter Information

`SV_PC_ERROR_COUNTER_x` (1-40) (I32, CNC→PLC, PLC Manual, PDF p.111) breaks down as (PLC Manual,
PDF p.131):

| # | MPU11 | MPU12/MPU13 | Note |
|---|---|---|---|
| 1 | Jog external error count | Reserved | Expansion Side |
| 2 | Jog internal error count | Reserved | MPU Side |
| 3 | Jog external error count | Reserved | Expansion Side |
| 4 | Jog internal error count | Reserved | MPU Side |
| 5 | Shutdown count | Shutdown count | FPGA shutdowns |
| 6 | Drive internal errors | Reserved | MPU Side |
| 7-14 | Drive external errors 0-7 | Reserved | Expansion Side |
| 15 | PLCIO2 reception errors | Reserved | MPU side |
| 16 | SD drive errors | Reserved | Comm Errors |
| 17 | Missed interrupts | Missed interrupts | FPGA interrupts missed |
| 18 | Reserved | Homeless blocks | Data received before location assignment |
| 19-32 | Reserved | Reserved | |
| 33 | Missed interrupts | Missed interrupts | FPGA interrupts missed, counted on DSP from INT_MISS bit |
| 34 | Debug packet overflow | Debug packet overflow | |
| 35 | Raw debug buffer overflow | Raw debug buffer overflow | |
| 36 | Command buffer overflow | Command buffer overflow | |
| 37 | Rx buffer overflow | Rx buffer overflow | |
| 38 | Rx buffer full | Rx buffer full | |
| 39 | Rx wiznet buffer full | Rx wiznet buffer full | |
| 40 | Increments every pass | Increments every pass | Debug life sign |

---

## Appendix K: Drive Control SV Information

`SV_DRIVE_CONTROL_x` (1-8) / `SV_?_AXIS_DRIVE_CONTROL` (I32, PLC→CNC, PLC Manual, PDF p.118) is a
High Speed Drive Control word whose bit meanings are separated by drive type (PLC Manual, PDF
p.132):

**Allin1DC/DC3IOB/DC1**

| Bit | Meaning |
|---|---|
| 0-14 | Reserved |
| 15 | Axis Enable* |

**Optic 4**

| Bit | Meaning |
|---|---|
| 0-12 | Reserved |
| 13 | Tach. Direction Inversion** |
| 14 | Auxiliary Output |
| 15 | Axis Enable* |

**Optic Direct**

| Bit | Meaning |
|---|---|
| 0-6 | Reserved |
| 7 | Position Error Clear |
| 8 | P-OT — Drive Limit |
| 9 | N-OT — Drive Limit |
| 10 | /P-CON — Control Method Switching |
| 11 | /P-CL — Positive Torque Limit |
| 12 | /N-CL — Negative Torque Limit |
| 13 | Absolute position send (not controllable on V0x0008+) |
| 14 | Alarm Reset |
| 15 | Axis Enable* |

`*` Controlled by MPU firmware; do not attempt to change. `**` Controlled by parameters 200-207;
do not attempt to change.
