# CNC12 Screen Layout and Main-Screen Menu Map

Screen windows, keystroke conventions, startup homing procedure, and the F1-F10 main-screen
menu map. Source: Router Manual Ch 1 (Introduction), Ch 3 (CNC Software Main Screen).

---

## 1.1 DRO Display

The DRO display shows the digital read-out of the tool's current position (Router Manual §1.1,
p.10). It is configurable for number of axes and desired display units of measure (see Ch 15).
The bars under each axis are load meters, representing the amount of power supplied to the
drive for that axis; their display is controlled by Parameter 143.

## 1.2 Distance-to-Go DRO

Located below the main DRO, this display shows the distance to go to complete the current
movement (Router Manual §1.2, p.10). It is controlled by Parameter 143 and can be turned on
with `Ctrl+D` — see [operator-panel.md](operator-panel.md) §2.28 for the full hot-key list.

> The manual disagrees with itself here: p.10 says `Ctrl+D` turns this display on, while
> §2.28.16 (p.38) says `CTRL+D` swaps the positions of the DRO and the Distance-to-Go DRO.

## 1.3 Status Window

The first line of the status window shows the name of the currently-loaded job file (Router
Manual §1.3, p.11). Below the job name:

| Indicator | Description |
|---|---|
| Tool Number | Currently-active tool |
| Program Number | See G65 (Ch 12) or M98 (Ch 13) |
| Feed Rate Override | Current override percentage set on the Jog Panel; label turns RED if the rapid override is off |
| Spindle Speed | Current spindle speed (requires a variable-frequency spindle drive/inverter) |
| Feed Hold | Current on/off status of FEED HOLD |

See [operator-panel.md](operator-panel.md) for the Feed Hold Button, Feed Rate Override Knob,
and Spindle controls.

When `CYCLE START` is pressed and a job is running, the Part Cnt and Elapsed Time indicators
also appear. Part Cnt increments by one on each completed run and does not increment if a job
is canceled early; Part # shows how many parts have run, with an arrow indicating count
direction (Router Manual §1.3, p.11).

> Note: the same paragraph names this timer both "Elapsed Time" and, two sentences later, "Part
> Time" (Router Manual §1.3, p.11). It counts elapsed time since CYCLE START and keeps running
> through optional stops, tool changes, and FEED HOLD, until the job is canceled.

The Indicator Board, added in CNC12 v5.42, sits under the Rapid override and above the message
window; it displays graphics for conditions such as active keyboard jogging or feed hold
(Router Manual §1.3, p.11).

## 1.4 Message Window

Divided into a message section (upper lines) and a prompt section (lowest line) (Router Manual
§1.4, p.11):

- The prompt line shows control prompts, e.g. `Press CYCLE START to start job` after power-up.
- The message section shows warnings, errors, and status messages; newest lines appear at the
  bottom and older lines scroll upward off the top.
- When messages have scrolled out of view a scroll bar appears on the right; use `UP ARROW`
  and `DOWN ARROW` to view older messages.

See Ch 16 for the CNC software error and status message list.

## 1.5 Options Window

Options are selected by pressing the function key shown in the box (Router Manual §1.5, p.11).
For example, on the main screen pressing `F7 – Utility` selects the Utility Menu.

## 1.6 User Window

Content depends on the operation the operator is performing; the window is empty when no action
is being taken (Router Manual §1.6, p.11). When `CYCLE START` is pressed and a job processes
correctly, up to 11 lines of G-code are shown here as the part runs. Part zeros, tool library
setup, and Digitizing/Probing entries are also entered by the operator in this window.

## 1.7 Conventions

Keystroke and softkey notation used throughout the manual (Router Manual §1.7, p.12):

| Convention | Meaning |
|---|---|
| `A` | Bold, capitalized letter = a keystroke, e.g. the A key |
| `ENTER` | Bold, capitalized word = a named key; the Escape key is written `ESC` |
| `ALT-D` | Hold the first key, then press the second |
| `F10 – Save` | All data entry screens use F10 – Save to save changes |
| `ESC` | Exits any menu, returning to the previous menu; usually discards changes made in that menu |

Coordinate and motion conventions (Router Manual §1.7, p.12):

- Facing the router, X is positive to the right, Y is positive to the rear, and Z is positive
  upward, perpendicular to the XY plane.
- Direction of motion is defined by the cutter's motion, not the table's motion.
- CW = clockwise, CCW = counter-clockwise.

## 1.8 Machine Home

On startup, before any job can run, machine home must be set (Router Manual §1.8, p.13).

If the machine has home/limit switches, reference marks, or safe hard stops, the control can
home itself automatically. If it has reference marks, jog until they line up, then press
`CYCLE START` to begin the automatic homing sequence. The control executes the G-codes in
`cncm.hom` in the `c:\cncr` directory; by default this file homes Z in the plus direction, then
X in the minus direction, and Y in the plus direction (Router Manual §1.8, p.13).

If the machine has no home/limit switches or safe hard stops, a message says so instead; the
operator must move each axis to its home position with the jog keys or handwheels, then press
`CYCLE START` to set machine home (Router Manual §1.8, p.14).

## 1.9 Router M- and G-codes

Ch 1 gives a summary table of M- and G-codes, pointing to Ch 12-13 for full detail (Router
Manual §1.9, p.14-15). The full, cited M-code and G-code catalogs for this manual are in
[m-code-index.md](m-code-index.md) and [g-code-index.md](g-code-index.md).

## 1.10 How to Unlock Software Features or Unlock Your Control

To unlock software features (Router Manual §1.10, p.15-16):

1. Go to the Main screen of the Control software.
2. Press `F7 – Utility`, then `F8 – Import License`.
3. Select the license file from the file browser.
4. Repeat steps 1-3 for each new unlock.

## 1.11 Centroid API

CNC12 exposes a C# programming API so users can write software that communicates with CNC12 —
moving the machine, setting parameters, and similar tasks (Router Manual §1.11, p.16). See the
`CentroidAPIDocumentation` folder in the CNC12 installation directory, or the API forum at
`https://centroidcncforum.com/viewforum.php?f=72`.

## 1.12 CNC12 with Multiple Displays

With multiple displays, CNC12 defaults to the display farthest to the right (Router Manual
§1.12, p.16). To override this, add `–displayX` (X = the target display's ID number) to the
`Target` field of the CNC12 desktop shortcut's Properties. An error message may appear on
startup, but the desired display is still used.

> The manual prints the switch with an en dash (`–`, U+2013), quoted here as printed, so copying
> it from this page copies the en dash.

---

## F1-F10 main-screen menu map

The Options Window shows ten softkey menus from the main screen (Router Manual §1.5, p.11).

| F-key | Menu name | One-line purpose |
|---|---|---|
| `F1` | Set Part Zeros | Set part zeros and adjust Coordinate System Rotation (CSR), manually, by laser, by probe, or by touch plate |
| `F2` | Load Job | Load a job file |
| `F3` | MDI | Run a single-line command, e.g. `G1`, `X2`, `Y3`, or `F20` |
| `F4` | Run Job Options | Search and run a job from a specific line, resume a canceled job, or change how a job runs |
| `F5` | Tool/ATC | Set or change tool offsets |
| `F6` | Edit G-Code | Open a G-code text editor on the currently-loaded job |
| `F7` | Utility | View software options, back up part/config files, create directories, import/export files |
| `F8` | Graph | Graph the toolpath of the currently-loaded part program |
| `F9` | Smoothing | Enable and configure smoothing mode |
| `F10` | Shut Down | Shut down the machine properly |

### F1 – Set Part Zeros

Sets the part position or coordinate system origin (Router Manual §3.1, p.42):

| Sub-key | Menu | Description |
|---|---|---|
| `F1` | Manual | Default screen; manually set X/Y/Z position, edge finder diameter, approach. Set XY with `F8`; set all with `Shift+F10` |
| `F2` | Laser | Toggle the crosshair laser; jog to the crosshairs, enter X/Y, `F10` to set. Set X and Y with `Shift+F10` |
| `F3` | Probe | Configure probe diameter or select a probing cycle to determine part zero |
| `F4` | Plate | Use a tool and touch plate to determine X, Y, and/or Z part zero |
| `F5` | CSR | Adjust Coordinate System Rotation via probe, touch plate, laser, or manually |
| `F6` | Rotary | Set Rotary Part X Axis Zero Position, or access other rotary tools |
| `F7` | Auto Zero | Determine zero automatically with an attached probe |
| `F8` | Set XY | Set X and Y from manual entry |
| `F9` | WCS Table | View and modify Work Coordinate System coordinates |
| `F10` | Set | Set the highlighted value as Part Zero for that axis |

### F2 – Load Job

Opens a file browser to load a job file (Router Manual §3.2, p.43).

### F3 – MDI

Runs M- and G-codes one line at a time (Router Manual §3.3, p.43). Enter a command, then press
`CYCLE START` to execute; the control then prompts for another line. Press `ESC` when
finished. Navigate previous commands with `UP ARROW` / `DOWN ARROW`; edit with `LEFT` /
`RIGHT` arrow. Press `ENTER` or `CYCLE START` to execute.

```
Block ? G92X0Y0   ; Set the current XY position to 0,0
Block ? M92 /Z    ; Move the Z to the positive limit.
Block ? M26 /Z    ; Set the current Z position as Z home.
```

### F4 – Run Job Options

Search, run, resume, and control job execution (Router Manual §3.4, p.44):

| Sub-key | Label | Description |
|---|---|---|
| `F2` | Search | Resume a job by searching for a line, tool, or block number |
| `F3` | Repeat On/Off | Toggles Job Repeat — repeats the current program when a job finishes |
| `F4` | Skips On/Off | Toggles block skips in part programs |
| `F5` | Single Block | Runs in single block mode when on |
| `F6` | Stops | Toggles optional stops (M01) in part programs |
| `F8` | Graph Job | Graphs the toolpath of the currently-loaded program |
| `F9` | Rapid | Toggles the rapid override function |
| `F10` | RTG On/Off | Toggles Run Time Graphics |

See Ch 6 for more on these options.

> §3.4 (p.44) lists no `F1` key. §6.4 (p.84) documents `F1 – Resume Job` in this menu; see
> [running-jobs.md](running-jobs.md) §6.4.

### F5 – Tool/ATC

Edit the tool library — height offset and tool diameter — and command tool changes (Router
Manual §3.5, p.44-45).

### F6 – Edit G-Code

Loads the current job into a text editor for viewing or editing (Router Manual §3.6, p.45).

> **WARNING** Editing a file (modifying and saving) while the machine is moving can cause
> personal injury or machine damage.

> **WARNING** Do not edit configuration data located in the `C:\cncr` directory. Doing so can
> cause personal injury or machine damage.

Save and exit the text editor before running the file; the `C:\cncr` directory also holds
configuration files and binary data that must not be edited, or data loss and malfunctions can
result (Router Manual §3.6, p.45).

### F7 – Utility

Design parts with Intercon, view the CNC12 manual, open Advanced Configuration, control Power
Feed, open the Color Picker, run User Maint, create a system report, import license files,
launch digitizing (if licensed), and open the CNC12 Wizard (Router Manual §3.7, p.45; see Ch 7).

| Sub-key | Label | Description |
|---|---|---|
| `F1` | Intercon/CAM Menu | Program parts with Intercon by default (see Ch 10); can become a menu — see §15.12 |
| `F2` | Manual | Open the CNC12 manual |
| `F3` | Advanced Config | Edit Control Configuration, Machine Configuration, Machine Parameters, PID; run the system test (see Ch 15) |
| `F4` | Power Feed | Set Power Feed to Absolute or Incremental; free the axes or power them |
| `F5` | Color Picker | Change from the default Centroid Classic color scheme |
| `F6` | User Maint | Perform user maintenance |
| `F7` | Create Report | Generate a `report.zip` backup of system configuration files |
| `F8` | Import License | Import a license file into CNC12 |
| `F9` | Digitizing | Open the digitizing menu: Gird [sic], Radial, Contour, Probe, Wall Following (see Ch 8) |
| `F10` | Acorn Wizard | Open the CNC12 Wizard |

### F8 – Graph

Graphs the toolpath of the currently-loaded part program (Router Manual §3.8, p.46); also
reachable from the Load Job screen and Run Job menus. Pressing `CYCLE START` in this screen
animates the toolpath as it draws.

Accelerated Graphics Backplot (default):

| Sub-key | Label | Description |
|---|---|---|
| `F1` | Pan/Rotate | Toggles arrow keys between pan and rotation; an axis indicator marks the rotation center |
| `F2` | View | Change planar view (TOP / RIGHT / FRONT) |
| `F3` | Set Range | Select which G-code lines are displayed |
| `F4` | Dimension Menu | Sub-menu: F1 Prev Line, F2 Next Line, F3 Go To Line, F4 Measure |
| `F5` | Redraw | Redraw slowly; feed rate override knob (or `+`/`−`) sets draw speed; press `F5` again to cancel |
| `F6` | Hide Rapids | Toggle hiding rapid movements |
| `F7` | Zoom In | Zoom toward part center |
| `F8` | Zoom Out | Zoom away from part center |
| `F9` | Zoom All | Fit entire part on screen |
| `F10` | Show Tools | Toggle the tools highlight menu (Tool XXX, Rapid, Origin, Travel, Spindle Center Line, Work Envelope) |
| `Spacebar` | Measure | Measure between two snapped points (2D or 3D per view) |

(Router Manual §3.8, p.46-47.) Mouse/touch: left-drag pans, right-drag rotates, wheel (or both
buttons) zooms; double-click a feed move to center on it and show its length; `F1` toggles
Pan/Rotate on touch screens.

Legacy Graphics Backplot — enabled by setting Parameter 260 to -1, or temporarily with
`Shift+F1` while in F8 – Graph; press `ESC` then `F8` to return to Accelerated (Router
Manual §3.8, p.47-48):

| Sub-key | Label | Description |
|---|---|---|
| `F1` | 2D/3D | Toggle isometric 3D view |
| `F2` | View/Rotate | Change planar view; in 3D, rotate with the arrow keys |
| `F3` | Range | Set the line/block range to graph |
| `F4` | Time | Estimate machining time (accounts for accel/decel; ignores tool-change time) |
| `F5` | Redraw | Redraw the part |
| `F6` | Pan | Move the part on screen; pick a location, then press `F6` again to continue |
| `F7` | Zoom In | Zoom in |
| `F8` | Zoom Out | Zoom out |
| `F9` | Zoom All | Fit entire part on screen |

Legacy color scheme: canned drilling cycles gray, rapid traverse red, feed rate moves yellow,
cutter-compensated moves gray.

> Note: use the FEED RATE OVERRIDE knob to control graphing speed — counter-clockwise pauses,
> clockwise resumes. On the offline demo software, use `Ctrl+` or `Ctrl−` (Router Manual
> §3.8, p.48).

### F9 – Smoothing

Enable/disable smoothing, configure smoothing options, load preconfigured setups, and configure
up to 99 custom presets (including the 7 defaults) (Router Manual §3.9, p.48). See §15.16
"G-code AD2 Smoothing" for detail.

### F10 – Shutdown

Park the machine, power off the control, open a command window, or exit the CNC software
(Router Manual §3.10, p.49):

| Sub-key | Label | Description |
|---|---|---|
| `F1` | Park | Park the machine at end of day for quicker homing at next startup; homes each axis at maximum rate to 1/4 motor revolution from home; press `CYCLE START` to start the move |
| `F2` | Poweroff | Properly shut down the control (turns off the control only — the machine itself still needs manual power-off) |
| `F6` | System Prompt | Opens a command-line interface; type `exit` to close it |
| `F9` | Exit CNC12 | Exits the CNC control software |
