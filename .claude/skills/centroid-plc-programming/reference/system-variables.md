# Centroid CNC12 SV_* System Variable Catalog

This catalog lists every system variable in the PLC Manual's Appendix D tables (PLC Manual,
PDF p.104-120), grouped by function, plus the status-bit breakdowns of Appendices H-K (PDF
p.128-132). Appendix D also prints two names without the `SV_` prefix, `ENCODER_DIFF_BITS` and
`ENCODER_QUAD_BITS` (PDF p.111); they are listed under their printed names. Types: `M` memory bit, `I32`/`I64` signed integer,
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

Rows below are drawn from PLC Manual, PDF p.102-120 (see the Page column for each fact's exact
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
| `SV_PLC_SPINDLE_KNOB` | I32 | PLC→CNC | "Spindle Speed override percentage sent to the PLC" [sic]: the manual lists it in the PLC → CNC table. | p.117 |
| `SV_PLC_FUNCTION_37` | M | PLC→CNC | Spindle Start. | p.114 |
| `SV_PLC_FUNCTION_38` | M | PLC→CNC | Spindle Stop. | p.114 |
| `SV_PLC_FUNCTION_98` | M | PLC→CNC | Select Spindle CCW. | p.114 |
| `SV_PLC_FUNCTION_99` | M | PLC→CNC | Select Spindle CW. | p.114 |
| `SV_PLC_FUNCTION_106` | M | PLC→CNC | Spindle Override +. | p.114 |
| `SV_PLC_FUNCTION_107` | M | PLC→CNC | Spindle Override -. | p.115 |
| `SV_PLC_FUNCTION_108` | M | PLC→CNC | Select Spindle Override / 100%. | p.115 |
| `SV_PC_SPINDLE_OVERRIDE` | I32 | CNC→PLC | Not currently used. | p.107 |
| `SV_MEASURED_SPINDLE_SPEED` | F32 | CNC→PLC | Measured spindle speed in RPM, taking into account the `SV_SPINDLE_MID_RANGE` and `SV_SPINDLE_LOW_RANGE` settings. | p.112 |
| `SV_PC_MAX_SPINDLE_SPEED_FOR_TOOL` | F32 | CNC→PLC | Maximum allowed spindle speed for the tool in the spindle. | p.112 |
| `SV_PC_MAXIMUM_CSS_SPEED` | F32 | CNC→PLC | Lathe: the maximum constant surface speed set by a G50 command. | p.112 |
| `SV_SPINDLE_RPM_MODE` | M | PLC→CNC | C axis lathe: when set, the MPU11 sends the current value of `SV_SPINDLE_DAC` as the PID output to the drive for the last axis configured as a "C axis"; while active, full power without motion and position errors are disabled for that axis. Write only once per PLC pass. | p.102, p.116 |
| `SV_SPINDLE_DAC` | I32 | PLC→CNC | C axis lathe: the value the MPU sends as the PID output while `SV_SPINDLE_RPM_MODE` is set. p.118 prints the bit's own description ("When this bit is set…") under this I32 word. | p.116, p.118 |

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
| `SV_DOING_AUTO_TOOL_MEASURE` | M | CNC→PLC | Set by CNC software while performing an automatic tool measure with the TT1. | p.105 |
| `SV_FORCE_PROBE_DETECTION_ON` | M | CNC→PLC | Set by CNC software when detection of a probe is forced, typically when the probe tool number is called and in the spindle; the PLC should enable any probe protections it has while this is set. | p.106 |

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

Rows below are drawn from PLC Manual, PDF p.104-106, p.111, p.117-118.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_JOG_LINK_ONLINE` | M | CNC→PLC | 1 = valid jog panel detected as Jogboard. | p.104 |
| `SV_JOG_PANEL_REQUIRED` | M | CNC→PLC | Reflects the "Jog Panel Required" setting in CNC software's Control Configuration menu. | p.105 |
| `SV_PC_VIRTUAL_JOGPANEL_ACTIVE` | M | CNC→PLC | Indicates the user has activated the keyboard (virtual) jog panel with ALT-J; most functions besides jogging are allowed without the screen up by default. | p.105 |
| `SV_PLC_DEBOUNCE_x` (1-64) | I32 | PLC→CNC | Debounce configuration word for the first 240 PLC inputs. | p.117 |
| `SV_JOG_LINK_DEBOUNCE_x` (1-32) | I32 | PLC→CNC | Jog Panel input debounce configuration words. | p.117 |
| `SV_LOCAL_DEBOUNCE_x` (1-13) | I32 | PLC→CNC | MPU11 onboard/local inputs debounce configuration. | p.118 |
| `SV_LEGACY_JOG_PANEL_ONLINE` | M | CNC→PLC | 1 = legacy jog panel detected, e.g. Uniconsole-2. | p.104 |
| `SV_PC_EXT_USB_PANEL_ONLINE_BITS` | I32 | CNC→PLC | SET by CNC software when an external USB panel is connected. | p.111 |
| `SV_PC_EXT_USB_PANEL_INP_x` (1-64) | M | CNC→PLC | SET by CNC software for an external USB panel, to indicate a press of a button. | p.106 |
| `SV_PC_EXT_USB_PANEL_OUT_x` (1-64) | M | CNC→PLC | "SET by PLC to activate outputs for an external USB Panel to activate indication LEDs" — see the note below. | p.106 |
| `SV_PC_EXT_USB_PANEL_W_x` (1-16) | I32 | CNC→PLC | SET by CNC software "to typically indicate a ration [sic] of a knob for Feed/Rapid/Spindle for an external USB Panel". | p.111 |

> `SV_PC_EXT_USB_PANEL_OUT_x` is printed in the CNC → PLC table, but its description says the PLC
> SETs it (PLC Manual, PDF p.106). The Dir column follows the table, as everywhere in this catalog.

### Axis absolute position

Rows below are drawn from PLC Manual, PDF p.103-104, p.107, p.111-112.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_MPU11_ABS_POS_x` (0-7) | I64 | CNC→PLC | Absolute position of the axis in encoder counts, same value CNC reports and shows in the PID screen as AbsPos; index is zero-based (0-7 for 8 axes), unlike most other `_1-8` families. Should be read once per PLC pass — written externally. | p.103, p.111 |
| `SV_MPU11_EXPECTED_POS_x` (0-7) | I64 | CNC→PLC | Expected position of the axis in encoder counts — the current commanded position. Read only once per PLC pass — written externally. | p.104, p.112 |
| `SV_MPU11_LASH_OFFSET_0-7` | I32 | CNC→PLC | The current lash offset. Read only once per PLC pass — written externally. | p.103, p.107 |
| `SV_ENCODER_POSITION_x` (1-32) | I64 | CNC→PLC | Current encoder position. | p.112 |
| `SV_MACHINE_POSITION_AXIS_x` (1-8) / `SV_?_AXIS_MACHINE_POSITION` | F32 | CNC→PLC | Current machine position of each axis (1-8, or A, B, C, U, V, W, X, Y, Z) in machine units. | p.112 |

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

Machine parameter meanings: `centroid-cnc12-router-ops` [parameter-index.md](../../centroid-cnc12-router-ops/reference/parameter-index.md) (Router Manual §15.7, p.320).

### Control configuration

Rows below are drawn from PLC Manual, PDF p.112.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PC_CONFIG_MIN_SPINDLE_SPEED` | F32 | CNC→PLC | Minimum spindle speed from the control configuration. | p.112 |
| `SV_PC_CONFIG_MAX_SPINDLE_SPEED` | F32 | CNC→PLC | Maximum spindle speed from the control configuration. | p.112 |

---

## System state, faults, and program control

Rows below are drawn from PLC Manual, PDF p.102-120.

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
| `SV_ESTOP_PRESSED` | M | PLC→CNC | SET by the PLC to tell CNC software that E-Stop was pressed. | p.117 |
| `SV_RESET_PRESSED` | M | PLC→CNC | SET by the PLC to tell CNC software that Reset was pressed. | p.117 |
| `SV_STOP_REASON` | I32 | PLC→CNC | When motion stops, the reason is stored here. "Do not use at this time." | p.117 |
| `SV_M_FUNCTION` | I32 | CNC→PLC | Set as part of M-code execution. Read only once per PLC pass — written externally; p.103 notes it is "Not used in any program." | p.103, p.107 |
| `SV_PC_CURRENT_WCS` | I32 | CNC→PLC | The work coordinate system (1-18) currently in effect in CNC software. | p.110 |
| `SV_STARTUP_TIME` | I64 | CNC→PLC | 12-digit integer holding the date and time CNC software was started, format `YYMMDDHHmmSS`. | p.112 |
| `SV_PC_DEFEAT_TRAVEL_LIMITS` | M | CNC→PLC | CNC software SETs this when software travel limits are defeated by M297. | p.107 |
| `SV_PLC_DISABLE_TRAVEL_LIMITS` | M | PLC→CNC | When SET by the PLC, CNC no longer stops at or errors at software travel limits when jogging and/or with the MPG. It does not prevent software travel limits during normal job processing. | p.117 |
| `SV_PLC_RESTART_FORWARD` | M | PLC→CNC | SET by the PLC to instruct Traverse.exe to move forward in the job. | p.117 |
| `SV_PLC_RESTART_REVERSE` | M | PLC→CNC | SET by the PLC to instruct Traverse.exe to move in reverse in the job. | p.117 |
| `SV_SYS_COMMAND` | I32 | PLC→CNC | A non-zero positive value makes CNC software launch a process that tries to run the Windows batch file `plc_system_command_n.bat`, where n is the value set. | p.118 |
| `SV_RESET_PLC_STATS_MIN_MAX` | M | PLC→CNC | Resets the current Minimum/Maximum PLC executor statistics shown on the PLC diagnostic screen (ALT-I). | p.116 |
| `SV_RESET_PLC_STATS_AVG` | M | PLC→CNC | Resets the current Average PLC executor statistics shown on the PLC diagnostic screen (ALT-I). | p.116 |
| `SV_SMSG_D_ARG_x` (1-9) | I32 | PLC→CNC | Reserved for future use. Do not use. | p.117 |
| `SV_SMSG_F_ARG_x` (1-9) | F32 | PLC→CNC | Reserved for future use. Do not use. | p.120 |
| `SV_PLC_FAULT`, `SV_LUBRICANT_LOW`, `SV_DRIVE_FAULT` | M | PLC→CNC | Obsolete. Do not use. | p.113 |
| `SV_PLC_OP_IN_PROGRESS` | M | PLC→CNC | Obsolete. Do not use. p.103 names it in the Externally Read list only "for completeness". | p.103, p.113 |

> `SV_STALL_ERROR` is printed in the PLC → CNC table (p.115), but p.103's "Externally Written
> System Variables" list also names it — meaning it is actually written by the MPU outside the
> PLC program's control flow, and the PLC should read it once per pass and only RST it under the
> stated condition (PLC Manual, PDF p.103, p.115).

---

## Axis validity, drive status, and power

Rows below are drawn from PLC Manual, PDF p.103-111, p.115-116.

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
| `SV_DRIVE_VERSION_x` (1-8) | I32 | CNC→PLC | The drive firmware version. | p.110 |
| `SV_AXIS_LABEL_x` (1-8) | I32 | CNC→PLC | Uppercase ASCII character value of the axis label, e.g. A = 65, N = 78, X = 88, Y = 89, Z = 90. | p.110 |
| `SV_?_AXIS_DRIVE_NUMBER` | I32 | CNC→PLC | Mapped to machine parameters 300 (Axis 1 Drive Number) through 307 (Axis 8 Drive Number), by axis label A, B, C, U, V, W, X, Y, Z; a convenience for PLC programs that handle axis changes. | p.110 |
| `SV_HOME_SET_AXIS_1-8` | M | CNC→PLC | Set after initial homing; stays set even if CNC software resets the homing state. | p.106 |
| `SV_ENCODER_INDEX_PULSE_1-21` | M | CNC→PLC | Current state of the encoder index pulses. | p.106 |
| `SV_LATCHED_ENCODER_INDEX_PULSE_1-21` | M | CNC→PLC | Latched state of the encoder index pulses; they remain set until read. | p.106 |
| `SV_SCALE_ENABLED_AXIS_1-8` | M | CNC→PLC | Set if the scale is enabled in CNC software's Scale Menu. | p.106 |
| `SV_SCALE_INITIALIZED_AXIS_1-8` | M | CNC→PLC | Set when a scale is initialized (axis homed); turns off once an axis homing command is issued. | p.106 |
| `SV_SCALE_INHIBIT_AXIS_x` (1-8) | M | PLC→CNC | When set, scale compensation for the axis is disabled until the bit is reset, undoing previous corrections; the DRO then shows the motor encoder's absolute position. | p.116 |
| `SV_POSITION_MODE_ERROR_AXIS_x` (1-8) | I32 | CNC→PLC | Same as in CNC software's PID Encoder menu. | p.111 |
| `SV_DISABLE_STALL_DETECTION` | M | PLC→CNC | When SET, disables detection of some stall errors, such as position errors and full power without motion errors. | p.116 |
| `ENCODER_DIFF_BITS` | I32 | CNC→PLC | Bitmap of encoder differential errors. Printed without the `SV_` prefix. | p.111 |
| `ENCODER_QUAD_BITS` | I32 | CNC→PLC | Bitmap of encoder quadrature errors. Printed without the `SV_` prefix. | p.111 |
| `SV_HSC_DRIVE_x_STATUS_y` | I32 | CNC→PLC | Every bit of the status packets AC1 drives send back: 64 variables, eight for each of eight drives. Only `SV_HSC_DRIVE_x_STATUS_4` is documented. Its bit00 FatalError should be monitored on all AC1 drives and treated as an emergency stop; if it is still on about a second after `SV_MASTER_ENABLE` is turned back on, throw the fault again. Full bit list on p.108-109. | p.108-109 |
| `SV_SD_DRIVE_x_STATUS` (1-5) | I32 | CNC→PLC | Status of legacy SD drives. bit00 FatalErrorDetected should be monitored for all drives and treated as an emergency stop; the manual recommends echoing the variable to W1-W44 for viewing in PLC diagnostics. Full bit list on p.109. | p.109 |

`SV_PLC_BUS_ONLINE` and `SV_PLC_IO2_ONLINE` are CNC-written despite the `SV_PLC_` prefix — see
[resources.md](resources.md#system-variables-sv).

---

### RPM mode (AC1 drives)

Rows below are drawn from PLC Manual, PDF p.105-120.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_RPM_MODE_ACTIVE_1-8` | M | CNC→PLC | 1 = the AC1 drive axis is in RPM mode. | p.105 |
| `SV_RPM_MODE_ZERO_SPEED_x` (1-8) | M | CNC→PLC | 1 = the AC1 drive axis is at zero speed in RPM mode. | p.105 |
| `SV_RPM_MODE_ENABLE_x` (1-8) | M | PLC→CNC | Enables RPM mode on an AC1 drive. | p.116 |
| `SV_RPM_MODE_AXIS_ENABLE_x` (1-8) | M | PLC→CNC | Enables the axis in RPM mode on an AC1 drive. | p.116 |
| `SV_RPM_MODE_DIRECTION_x` (1-8) | M | PLC→CNC | Sets the RPM-mode direction on an AC1 drive. | p.116 |
| `SV_RPM_MODE_SPEED_REQUEST_1-8` | F32 | PLC→CNC | The requested RPM speed, for AC1 drives. | p.120 |

---

## Override and feedrate

Rows below are drawn from PLC Manual, PDF p.102-107, p.115, p.117, p.120.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PLC_FEEDRATE_KNOB` | I32 | PLC→CNC | Feedrate knob as the PLC would have CNC11 see it. Write only once per PLC pass. | p.102, p.117 |
| `SV_PLC_FEEDRATE_OVERRIDE` | F32 | PLC→CNC | Feedrate factor for MPU11 motion control, 0-2.0; 1.0 = no change to the programmed or jog-rate value. The MPU caps the feedrate to the Machine Setup maximum. Never apply a negative value. Write only once per PLC pass. | p.102, p.120 |
| `SV_PLC_RAPID_FEEDRATE_OVERRIDE` | F32 | PLC→CNC | Rapid-rate factor for MPU motion control, 0 (exclusive) to 1.0; 1.0 = no change to the programmed rapid rate. When set to 0, the MPU reverts to using `SV_PLC_FEEDRATE_OVERRIDE` for rapid rates. The MPU caps the rapid rate to the machine-configuration maximum. | p.120 |
| `SV_PC_TOGGLE_RAPID_OVERRIDE` | M | CNC→PLC | CNC software SETs this bit when the state of Rapid Override needs to change; the PLC should RST it after toggling Rapid Override. Named by `SV_PLC_FUNCTION_34` as its replacement (see [PLC function commands](#plc-function-commands-jog-panel--cycle-control)). | p.105 |
| `SV_PC_FEEDRATE_PERCENTAGE` | I32 | CNC→PLC | 0-200% adjustment for axis motion control, sent for machine parameter 78 bit 1 checking and on-screen display; not needed if `SV_PC_OVERRIDE_CONTROL_FEEDRATE_OVERRIDE` is not SET. Read only once per PLC pass — written externally. | p.103, p.107 |
| `SV_PC_OVERRIDE_CONTROL_FEEDRATE_OVERRIDE` | M | CNC→PLC | 1 = the Feedrate Override Knob is allowed to change the feedrate on axis motion. | p.104 |
| `SV_PC_OVERRIDE_CONTROL_FEEDHOLD` | M | CNC→PLC | 1 = Feedhold pauses the G-code program. | p.104 |
| `SV_PC_OVERRIDE_CONTROL_SPINDLE_OVERRIDE` | M | CNC→PLC | 1 = the Spindle Override keys or knob change the commanded spindle speed. | p.104 |
| `SV_PLC_OVERRIDE_CONTROL_FEEDRATE_OVERRIDE` | M | PLC→CNC | 1 = the feedrate can be changed from the commanded value by Feedrate Override. | p.115 |
| `SV_PLC_OVERRIDE_CONTROL_SPINDLE_OVERRIDE` | M | PLC→CNC | 1 = the spindle speed can be changed from the commanded value by Spindle Override. | p.115 |
| `SV_PLC_OVERRIDE_CONTROL_FEEDHOLD` | M | PLC→CNC | 1 = Feedhold is allowed. | p.115 |
| `SV_PC_TOGGLE_RAPID_FEED_LINK` | M | CNC→PLC | CNC software SETs this bit when the state of Feed/Rapid Link needs to change; the PLC should RST it after toggling Feed/Rapid Link. | p.106 |

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

Rows below are drawn from PLC Manual, PDF p.103, p.106-107, p.111, p.116, p.118-120.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_METER_x` (1-16) / `SV_?_AXIS_METER` | F32 | PLC→CNC | Set by the PLC program to -100.0 to 100.0, for CNC software to display as a meter in the DRO. Only the first eight are used; meters 9-16 are reserved for future use. | p.120 |
| `SV_NV_Wx` (1-10) | I32 | PLC→CNC | Nonvolatile memory: used like any other I32 variable, but the value is retained when power is off; changes are written to non-volatile memory within 2ms. | p.118 |
| `SV_NV_Fwx` (1-10) | F32 | PLC→CNC | Nonvolatile memory: used like any other F32 variable, but the value is retained when power is off; changes are written to non-volatile memory within 2ms. | p.120 |
| `SV_PC_LASER_ON` | M | CNC→PLC | Crosshair laser status. CNC software SETs it when the laser is requested on; the PLC should SET it when the laser is on and RST it when off. | p.106-107 |
| `SV_DAC_OUTPUT_ENABLE_x` (1-8) | M | PLC→CNC | When set, enables control of the analog voltage on the OpticDirect through `SV_DAC_OUTPUT_VALUE_1-8`. | p.116 |
| `SV_DAC_OUTPUT_VALUE_1-8` | I32 | PLC→CNC | Controls the analog output on an OpticDirect, provided the corresponding `SV_DAC_OUTPUT_ENABLE_1-8` is set. | p.119 |
| `SV_ETHER1616_ONLINE_BITS` | I32 | CNC→PLC | Online status of the Ether1616 devices; used with `SV_MACHINE_PARAMETER_415` (Ether1616 Configured Bits) to detect changes. | p.111 |
| `SV_FSIO_1-32` | I32 | CNC→PLC | Fast Synchronous IO (see the M300 commands in the Operator Manual). Read only once per PLC pass — written externally. | p.103, p.107 |

---

## Plasma torch height control (THC)

Rows below are drawn from PLC Manual, PDF p.106-119. The torch-height board is the Centroid
THC_TXRX; P516 and P517 set the dive detection (PLC Manual, PDF p.106).

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_THC_CONTROL_ENABLE` | M | PLC→CNC | SET by the PLC to instruct CNC12 to turn on height control movement for the Z axis. | p.117 |
| `SV_THC_RESET_REQUEST` | M | PLC→CNC | SET by the PLC to instruct CNC12 to reset position after height control movement for the Z axis. | p.117 |
| `SV_THC_TARGET_VOLTAGE` | I32 | PLC→CNC | Sets the target voltage, in the range 0-4095, when `SV_THC_CONTROL_ENABLE` is SET. | p.119 |
| `SV_THC_VOLTAGE` | I32 | CNC→PLC | Current voltage reading from the THC_TXRX board. | p.111 |
| `SV_THC_TORCH_TOUCH` | M | CNC→PLC | The MPU SETs this when torch touch is detected, i.e. when the "Tin" input on a connected Centroid THC_TXRX board is triggered; the information reaches the MPU through the Encoder Index Pulse channel. | p.106 |
| `SV_THC_DIVE_DETECTED` | M | CNC→PLC | The MPU sets this when a voltage spike is detected, based on P516 and P517; the PLC should react and turn off `SV_THC_CONTROL_ENABLE` where that is valid. | p.106 |
| `SV_THC_ENCODER_STATUS` | I32 | CNC→PLC | Height-control encoder status from the THC_TXRX board. Bit 0 General Error is typically the only one used, as it reports all error types; bit 1 Negative Delta Error, bit 2 No B6/B7 Detected Error, bit 3 B6/B7 Both Detected Error, bit 4 Zero Delta Error. | p.111 |
| `SV_VELOCITY_RATIO` | F32 | CNC→PLC | Current ratio, 0 to 1, between actual velocity and requested feedrate velocity. Reliable for both smoothed and non-smoothed motion since V5.22.00; from V5.00.00 to V5.20.00, only for non-smoothing moves. | p.112 |
| `SV_THC_VELOCITY_XY` | F32 | CNC→PLC | Current XY velocity in encoder counts. The manual marks it Deprecated: it was used for the smoothing-ratio calculation and is no longer needed since V5.22.00. | p.112 |

---

## PC keyboard key state

Row below is drawn from PLC Manual, PDF p.100, p.105.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_PC_KEYBOARD_KEY_x` (1-104) | M | CNC→PLC | 1 = keyboard key pressed, 0 = not pressed. See PLC Manual App C for the key-number to physical-key map. | p.100, p.105 |

---

## Skin events (CNC skinning API)

Rows below are drawn from PLC Manual, PDF p.106, p.110, p.112.

| SV_ name | Type | Dir | Meaning | Page |
|---|---|---|---|---|
| `SV_SKIN_EVENT_1-255` | M | CNC→PLC | Generic events SET/RST by skinning applications via the CNC Skinning API — e.g. the Centroid Virtual Control Panel (VCP), which uses them for virtual jog-panel button states. Convention: `SV_SKIN_EVENT_1` through `SV_SKIN_EVENT_50` map to the fifty keys on a real hardware jog panel, left to right and top to bottom, with `SV_SKIN_EVENT_1` = Spindle+ and `SV_SKIN_EVENT_50` = CYCLE_START. | p.106 |
| `SV_SKINNING_DATA_W_x` (1-12) | I32 | CNC→PLC | Generic 32-bit integer data set by CNC Skinning API functions and read by the PLC. | p.110 |
| `SV_SKINNING_DATA_FW_1-11` | F32 | CNC→PLC | Generic 32-bit floating-point data set by CNC Skinning API functions and read by the PLC. | p.112 |
| `SV_SKINNING_DATA_DFW_1-11` | F64 | CNC→PLC | Generic 64-bit floating-point data set by CNC Skinning API functions and read by the PLC. | p.112 |

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
