# M-series Operator Panel, VCP, and Keyboard Interface

Hardware jog panel controls (§2.1-2.24), Virtual Control Panel (§2.25), keyboard jog panel
(§2.26-2.27), and keyboard shortcut keys (§2.28). Source: Router Manual Ch 2 (Operator Panel).

> Note: control-system behavior for the functions below depends on optional software settings,
> the PLC program, machine parameters, and hardware wiring; the described behavior may not apply
> to every control, or may differ in some respects (Router Manual §2.24, p.21).

The M-series Operator Panel is a sealed membrane keyboard of momentary membrane switches that
controls machine operations and functions; key placement is customizable, and the panel shown
in the manual's figure is representative of a default configuration (Router Manual §2, p.17).

---

## 2.1 Axis Jog Buttons

`X+` `X-` `Y+` `Y-` `Z+` `Z-` `4th+` `4th-` — momentary switches for jogging each of the four
axes, two buttons per axis; only one axis jogs at a time (Router Manual §2.1, p.18).

> Note: the jog buttons do not operate if the M-series CNC software is not running, or while a
> job is running.

## 2.2 Slow/Fast

Labeled with a turtle/rabbit icon in the center of the Axis Motion Controls section (Router
Manual §2.2, p.18). Turtle = slow jog mode; when SLOW is selected (LED on) a jog press moves the
axis at the slow jog rate, otherwise at the fast jog rate. See Ch 15 for setting the fast and
slow jog rates per axis.

## 2.3 Inc/Cont

Toggles between incremental and continuous jogging; LED lit = INC selected (Router Manual §2.3,
p.18). In CONT mode, an axis jog button held down moves the axis continuously until released.

## 2.4 x1, x10, x100

Sets the jog increment amount for incremental jogs and for each MPG handwheel click; only one
increment is active at a time, for all axes together (Router Manual §2.4, p.18):

| Key | Increment |
|---|---|
| x1 | 0.0001" |
| x10 | 0.0010" |
| x100 | 0.0100" |

## 2.5 MPG

Housed in a separate hand-held unit (Router Manual §2.5, p.18). Press `MPG` to make jogging
respond to the MPG handwheel (LED on); select the jog increment and axis, then turn the wheel
slowly. When the LED is off, the MPG is disabled and the jog panel is active.

## 2.6 Single Block

Toggles between auto and single block mode (LED on = single block) (Router Manual §2.6, p.18).
In single block mode, the program runs one line at a time, pressing `CYCLE START` after each
block. Auto mode (the default, LED off) runs the loaded program continuously after `CYCLE
START`; auto mode can be selected at any time while in single block mode, but single block mode
cannot be selected while auto mode is running a program.

## 2.7 Cycle Start

Begins processing the current program at the beginning, then prompts for a second `CYCLE
START` press to begin execution (Router Manual §2.7, p.19). After an M0, M1, M2, or M6, the
message "Press CYCLE START to continue" appears and the control waits for another press.

> **WARNING** Pressing CYCLE START will cause the M-series Control to start moving the axes
> immediately without further warning. Be certain that you are ready to start the program when
> you press this button. Pressing FEED HOLD, E-STOP, or CYCLE CANCEL stops movement if CYCLE
> START is pressed accidentally.

## 2.8 Feed Rate Override

Controls the percentage (0-200%) of the programmed feed rate used during feed-rate cutting moves
— lines, arcs, canned cycles, etc. (Router Manual §2.8, p.19).

> **CAUTION** The Feed Rate Override knob will not work during tapping cycles (G74 and G84).

## 2.9 Feed Hold

Decelerates the current movement to a stop, pausing the running job; `CYCLE START` resumes
motion from the stopped location (Router Manual §2.9, p.19).

> **CAUTION** Feed Hold is temporarily disabled during tapping cycles (G74 and G84) and
> automatic tool changes (M6).

## 2.10 Tool Check

While no program is running, moves the Z-axis to its home/G28 position (Router Manual §2.10,
p.19). While a program is running, aborts it: the control stops normal movement, pulls Z to home,
clears all M-functions, and displays the Resume Job Screen, where tool settings (height/diameter
offsets, etc.) can be changed before resuming with the new tool settings.

## 2.11 Cycle Cancel

Aborts the running program immediately — stops movement, clears all M-functions, and returns to
the Main Screen (Router Manual §2.11, p.19). Press `FEED HOLD` first if possible. After
`CYCLE CANCEL`, resuming requires rerunning the entire program or using the search function
(see Ch 3 or Ch 6).

## 2.12 Emergency Stop

Releases power to all axes and cancels the current job immediately; also resets certain faults
once the fault condition is fixed or cleared (Router Manual §2.12, p.20).

> **WARNING** On some machines, vertical axes (such as Z and/or W) may start to move due to
> gravity pulling them down when motor power is cut due to EMERGENCY STOP being pressed.

## 2.13 Spindle CW/CCW

Sets the direction the spindle turns when started manually; ignored (program controls direction)
when the spindle starts automatically. Default direction is CW (Router Manual §2.13, p.20).

## 2.14 Spindle Speed +

In Auto Spindle mode, increases speed by 10% of the commanded speed, capped at the lesser of the
maximum speed or 200% of commanded speed (Router Manual §2.14, p.20). In Manual Spindle mode,
increases speed by 5% of maximum speed, up to the maximum. The key's LED lights when speed is
above the 100% point.

## 2.15 Spindle Speed 100%

Sets spindle speed to the 100% point — the commanded speed in Auto mode, or half the maximum
speed in Manual mode; the LED lights at that point (Router Manual §2.15, p.20).

## 2.16 Spindle Speed -

In Auto Spindle mode, decreases speed by 10% of commanded speed, floored at 10% of commanded
speed (Router Manual §2.16, p.20). In Manual mode, decreases by 5% of maximum speed, down to 5%
of maximum. The LED lights when speed is below the 100% point.

## 2.17 Spindle Auto/Man

Toggles the spindle between program control (Automatic, LED lit) and operator control (Manual,
LED off); default is Auto mode (Router Manual §2.17, p.20).

## 2.18 Spin Start

In manual spindle mode, starts the spindle rotating; in automatic mode, restarts the spindle if
it was paused with Spin Stop (Router Manual §2.18, p.21).

## 2.19 Spin Stop

In manual spindle mode, stops the spindle; in automatic mode, pauses spindle rotation, which
Spin Start can then resume (Router Manual §2.19, p.21).

> NOTICE: The SPIN STOP key should only be pressed during FEED HOLD or when a program is NOT
> running.

## 2.20 Coolant Auto/Manual

Toggles automatic and manual coolant control (Router Manual §2.20, p.21). In automatic mode, M7
(Mist) and M8 (Flood) select coolant from the G-code program. In manual mode, flood and mist are
controlled by their own keys.

> Note: switching from automatic to manual mode turns both flood and mist coolant off
> automatically.

## 2.21 Coolant Flood

In manual coolant mode, toggles flood coolant on/off; the LED lights when flood is selected in
either mode (Router Manual §2.21, p.21).

## 2.22 Coolant Mist

In manual coolant mode, toggles mist coolant on/off; the LED lights when mist is selected in
either mode (Router Manual §2.22, p.21).

## 2.23 Auxiliary Function Keys (AUX1-AUX12)

The jog panel has 12 Auxiliary keys (9 labeled); some may be defined by customized systems
(Router Manual §2.23, p.21).

## 2.24 Notes About Operator Panels

See the callout at the top of this file (Router Manual §2.24, p.21).

---

## 2.25 VCP Introduction

The Virtual Control Panel (VCP) lets the operator use a mouse and/or touch screen to activate
the CNC Control Operator Interface Panel (Router Manual §2.25, p.22). CNC12 installs the default
Centroid VCP skin automatically; it can be used as-is, or modified per the VCP Manual.

The VCP legend below covers this router build's default skin (Router Manual §2.25, p.22-28):

| Function | Description |
|---|---|
| 4th+ Jog | Jogs the 4th-axis positively |
| 4th- Jog | Jogs the 4th-axis negatively |
| Toggle Spindle Auto/Manual | Toggles between automatic and manual spindle operation mode |
| Cycle Start | Same as Cycle Start |
| Cycle Cancel | Same as Cycle Cancel |
| Spindle Override Percentage | Displays the percentage of the default spindle speed the spindle is currently operating at |
| Spindle Override +1% | Increase the spindle override by 1% while held |
| Spindle Override -1% | Decrease the spindle override by 1% while held |
| Feed Hold | Temporarily pauses the feed rate |
| Single Block | Selects Single Block Mode |
| Tool Check | Performs a tool check |
| VCP Options | Allows the user to edit VCP settings |
| Push to Free | Unpins the VCP window so it can be moved around the screen |
| Push to Pin | Pins the VCP, preventing it from being moved from its pinned location |
| Emergency Stop | Same as Emergency Stop |
| Increase/Decrease Feed Rate Override | Increase/decrease feed rate override by 1% while held |
| Incremental/Continuous Jog Selection | Toggles incremental or continuous jog mode |
| Toggle Work Light | Toggles the work light between ON and OFF |
| Limit Switch Defeat | Overrides the limit switches when active |
| Selects CW Spin | Selects CW spin direction in manual mode |
| Selects CCW Spin | Selects CCW spin direction in manual mode |
| Toggle MPG | Toggles between the MPG and jog panel |
| Park | Parks the machine in its current position |
| Reset Home | Resets the home values that are currently set |
| Slow/Fast | Toggles between slow and fast jogging modes |
| Spin Start | Starts the spindle in the selected direction if in manual mode |
| Spin Stop | Stops the spindle regardless of auto or manual mode |
| Decrease/Increase Jog Increment | Decreases/increases the current jog increment to the next available increment |
| X+/X- Jog | Jogs the X-axis positively/negatively |
| Y+/Y- Jog | Jogs the Y-axis positively/negatively |
| Z+/Z- Jog | Jogs the Z-axis positively/negatively |
| Spindle warm up | Runs the spindle warm-up macro |
| Set WCS XY0 | Sets the current Work Coordinate System X and Y to zero |
| Set Rotary WCS | Sets the current WCS Z0 to a rotary axis parallel to X or Y, based on operator input |
| M58 Macro | Runs the M58 macro |
| Set WCS Z0 | Sets the current Work Coordinate System Z to zero |
| Re-pair Axes | Runs the axis re-pairing macro (M55) |
| Laser Set XY | Sets Parameter 560 to the current X and Parameter 561 to the current Y position |
| Auto Z to Plate | Runs the touch-plate auto Z zero macro, using a touch plate and tool to determine Z |
| Goto WCS XY0 | Moves the tool to the current WCS X and Y zero |
| Laser On/Off | Toggles the laser output |
| Air Blow | Toggles the Air Blow output |
| Dust Collector | Toggles the Dust Collector output |
| Hold Down VAC | Toggles the Hold Down VAC output |
| Set Tool Number | Sets the currently-selected tool to the entered tool number |
| Utilities | Opens the Router Utilities menu (by default: calibrate commanded vs. actual axis movement, run a communications stress test, teach in the laser offset distance from the spindle centerline) |
| Diagonal Jogging | Lets the operator jog diagonally, if enabled (CNC12 Wizard > Preferences > VCP Preferences > VCP Skin, set to `acorn_router_vcp_diagonal_rapid_skin.vcp` or `acorn_router_vcp_diagonal_skin.vcp`) |

---

## 2.26 Keyboard Jog Panel

The PC keyboard can serve as a jog panel; press `ALT+J` to display and enable it (Router
Manual §2.26, p.28-30). Coolant on/off, spindle on/off, feed rate, and spindle override work
without the panel displayed; full functionality, including jogging, needs the panel displayed
on screen, which requires Parameter 170 set to `1`.

- The status window (upper-right) shows jogging mode (continuous/incremental), incremental step
  size, and jog speed (fast/slow).
- Continuous mode: jog keys move while held, stop on release. Incremental mode: each press moves
  the set increment.
- The jog keys sit in the cursor-key block between the main keyboard and the numeric keypad; a
  key controlling an axis is overlaid with that axis's symbol (X, Y, etc.). They are the Arrow,
  Page Up, and Page Down keys.

| Key(s) | Function | Description | Availability |
|---|---|---|---|
| `Alt J` | Start/Exit Keyboard Jogging | Invokes or exits the keyboard jogging panel | Always, with few exceptions |
| `Alt S` | Cycle Start | Same as Cycle Start | Always, with few exceptions |
| `Esc` | Cycle Cancel | Same as Cycle Cancel | During a job; otherwise Esc exits menus |
| `Ctrl F1`-`Ctrl F12` | Aux 1-Aux 12 | Executes the function defined to that Aux key; a custom PLC program is required to act on jog panel signals | Always, with few exceptions |
| `Ctrl M` | Toggle Auto Coolant | Toggles coolant mode between auto and manual | Always, with few exceptions |
| `Ctrl N` | Turns Flood Coolant | Toggles flood coolant if in manual mode | Always, with few exceptions |
| `Ctrl K` | Toggle Mist Coolant | Toggles mist coolant if in manual mode | Always, with few exceptions |
| `Ctrl +` | Increase Feedrate Override | Increase feed rate override 1% while held | Jog panel, job run, graphing, and some other times |
| `Ctrl -` | Decrease Feedrate Override | Decrease feed rate override 1% while held | Jog panel, job run, graphing, and some other times |
| `Ctrl C` | Selects CW Spin | Selects CW spin direction in manual mode | Always, with few exceptions |
| `Ctrl W` | Selects CCW Spin | Selects CCW spin direction in manual mode | Always, with few exceptions |
| `Ctrl A` | Toggle Spindle Auto/Manual | Toggles automatic/manual spindle operation | Always, with few exceptions |
| `Ctrl S` | Spindle Start | Starts spindle in selected direction if in manual mode | Always, with few exceptions |
| `Ctrl Q` | Spindle Cancel | Stops spindle regardless of auto/manual mode | Always, with few exceptions |
| `Ctrl >` | Spindle Override +1% | Increase spindle override 1% while held | Always, with few exceptions |
| `Ctrl <` | Spindle Override -1% | Decrease spindle override 1% while held | Always, with few exceptions |
| `Ctrl T` | Tool Check | Performs a tool check | Always, with few exceptions |
| `Ctrl I` | Incremental/Continuous Jog Selection | Toggles incremental or continuous jog mode | Available most times jogging is available |
| `Ctrl B` | Selects Single Block Mode | Selects Single Block Mode | Always, with few exceptions |
| `Delete`/`Insert` | Decrease/Increase Jog Increment | Steps the jog increment to the next available value | Always, with few exceptions |
| `Ctrl Right/Left Arrow` | X +Jog/X -Jog | Jogs the X-axis positively/negatively | With on-screen jog panel displayed |
| `Ctrl Up/Down Arrow` | Y +Jog/Y -Jog | Jogs the Y-axis positively/negatively | With on-screen jog panel displayed |
| `Ctrl Page Up/Page Down` | Z +Jog/Z -Jog | Jogs the Z-axis positively/negatively | With on-screen jog panel displayed |
| `Ctrl Home`/`Ctrl End` | 4th +Jog/4th -Jog | Jogs the 4th-axis positively/negatively | With on-screen jog panel displayed |
| `Spacebar` | Feedhold | Enables Feedhold; press Cycle Start to resume | Always, with few exceptions |

> Note: keyboard jogging disables and re-enables itself when leaving and entering the main menu,
> to avoid unexpected movement; it can still be enabled in any menu with `ALT+J` (even after
> being disabled by CNC12) (Router Manual §2.26, p.34).

## 2.27 MDI and the Keyboard Jog Panel

Many keyboard jog panel keys double as MDI commands (Router Manual §2.27, p.34). To use jog
panel functions in MDI, press `ALT+J`; jog, use the handwheels, or use any other jog panel
function, then press `ALT+J` or `Esc` to return to MDI.

---

## 2.28 Keyboard Shortcut Keys

A computer-style keyboard, supplied with most systems, doubles as a jog panel and supplies "hot
keys" usable at almost any time, with few exceptions — some menus may prohibit their use (Router
Manual §2.28, p.34).

| Keystroke | Function | Description |
|---|---|---|
| `Alt D` | WCS/Machine Coordinates | Swaps the DRO display between current WCS position and current machine position |
| `Alt E` | Generate Screenshot | If Parameter 389 > 0, saves a screenshot as `screenshot-nnn.png`; `nnn` starts at 000 and increments per screenshot, resetting on CNC12 restart |
| `Alt I` | Live PLC I/O | Opens the CNC12 PLC Diagnostic Screen, showing real-time status of all inputs/outputs |
| `Alt J` | Keyboard Jog Panel | Opens the keyboard jog panel; a window overlays keyboard keys with a VCP-like legend, and a print button prints the panel image |
| `Alt K` | ATC Bin | Displays the current ATC bin |
| `Alt L` | ATC Putback Location | Displays the current ATC putback location |
| `Alt M` | Run MDI | Runs MDI |
| `Alt P` | Live PID Display | Displays the live PID screen with current axis positioning information |
| `Alt S` | Cycle Start | Alternative to the CYCLE START button |
| `Alt T` | Temperature Display | Shows current per-axis temperatures in the message window |
| `Alt V` | Display CNC Software Version Info | Shows CNC12 version info (same as F1 from the main menu) |
| `Alt 1` ... `Alt 0` | Select WCS | Cycles through the first ten Work Coordinate Systems |
| `Alt -` | Select Previous WCS | Selects the previous WCS |
| `Alt =` | Select Next WCS | Selects the next WCS |
| `Alt F10` | Exit CNC12 | Exits CNC12 (utility menu only) |
| `Ctrl D` | Swap DRO and Distance-to-Go DRO | Swaps the positions of the DRO and the Distance-to-Go DRO |
| `Ctrl E` | Launch PLC Detective | Launches the PLC Detective application |
| `Ctrl H` | Enable G-code Display | Shows the G-code display if a job is running and it is hidden |
| `Ctrl I` | Save PLC state to file | While on the Live PLC I/O screen, prints the current PLC I/O state to `plcstate.txt` |
| `Ctrl Q` | Probing Cycles History | Shows recorded probing-cycle positions (from F9 – Digitize > F4 – Probe); enter a description, delete history, or copy positions to the clipboard; close with `CTRL+Q` again or a click outside the window |
| `Shift F1` | Switch to Old-style Graphics Backplot | While in the accelerated backplot, switches to the old-style backplot that does not use OpenGL |
| `Shift F2` | Erase Log File | From Utility > Logs > Errors (or Stats), erases the log file after a confirmation dialog |
| `Ctrl Alt X` | Go to Shutdown Screen | From the main menu, opens the CNC12 shutdown screen |
| `Ctrl C` | Copy | From a numeric field or WCS Table column, copies the selected value to the clipboard |
| `Ctrl X` | Cut | From a numeric field or WCS Table column, cuts the selected value to the clipboard; the previous value is set to 0 |
| `Ctrl V` | Paste | From a numeric field or WCS Table column, pastes the value from the clipboard |

> Note: the manual's §2.28.26 heading reads "CTRL+V – Paste," but its body text instructs
> pressing `CTRL+P` to paste (Router Manual §2.28, p.40, both in the same paragraph); this file
> follows the heading's key.

With proper PLC support, `Alt I`'s Live PLC I/O screen also accepts `Ctrl Alt I` to toggle
Inputs 1-80 and `Ctrl Alt F` to toggle outputs (Router Manual §2.28.3, p.35). For the Enhanced
PLC Diagnostics view: open `F7 – Utility`, then `F10 – Acorn Wizard`, select "CNC Control"
under Preferences, and toggle "Enable Simple PLC Diagnostic as default"; then use the Arrow,
`F11`, and `F12` keys to navigate.
