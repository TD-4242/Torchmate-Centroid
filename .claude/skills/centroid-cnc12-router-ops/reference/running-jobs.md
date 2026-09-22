# CNC12 Running Jobs: Run Screens, Cancel/Resume, Run Menu, Power Feed, and the Utility Menu

Start, monitor, cancel, and resume a job; move axes manually with Power Feed; run the
communications stress test; and use the Utility Menu. Source: Router Manual Ch 6 (Running a
Job), Ch 7 (The Utility Menu).

---

## 6.1 Active Job Run Screen with G-code Display (p.82-83)

To start the currently-loaded job, go to the Main Screen and press `CYCLE START` on the jog
panel, or `ALT+S` on the keyboard if no jog panel is fitted (Router Manual §6.1, p.82). See
[operator-panel.md](operator-panel.md) §2.7 for `CYCLE START`.

If the Run-time Graphics option is off, this screen is displayed while a job runs, with the
following F-keys available (Router Manual §6.1, p.82):

| Softkey | Label | Description |
|---|---|---|
| `F3` | Repeat On/Off | Toggle the repeat feature for part counting; see §6.5 F3 |
| `F4` | Skips On/Off | Enable/disable block skips; see §6.5 F4 |
| `F5` | Auto | Single Block mode only: turns on Auto mode and disables Single Block. Single Block cannot be re-enabled until the job is stopped; see §6.5 F5 |
| `F6` | Stops off | Appears only if Optional Stops is on; turns Optional Stops off. Cannot be re-enabled until the job is stopped; see §6.5 F6 |
| `F8` | Graph | Switch to the Run-time Graphics screen (§6.2); appears only if the job was started with Run-time Graphics on |
| `F9` | Rapid On/Off | Toggle rapid override |

For other keys available while a job is running, see [operator-panel.md](operator-panel.md) Ch 2
(Router Manual §6.1, p.83).

## 6.2 Run-time Graphics Screen (p.83)

When a job runs with Run-time Graphics set to on, a screen showing a live tool-path display is
shown instead of §6.1's G-code display (Router Manual §6.2, p.83). Available keys:

| Softkey | Label | Description |
|---|---|---|
| `F7` | Clear | Clear the trail up to the tool's current position |
| `F8` | G-code | Switch to the §6.1 Job Run Screen with G-code display |
| `F9` | Trail On/Off | Turn the tool trail display on/off |

## 6.3 Canceling a Job in Progress (p.83)

There are three ways to cancel a running job; each records the job's progress so it can be
resumed with Resume Job (§6.4) or Search and Run (§6.5, `F2 – Search`) (Router Manual §6.3,
p.83). See [operator-panel.md](operator-panel.md) §2.10-2.12 for the `TOOL CHECK`,
`CYCLE CANCEL`, and `EMERGENCY STOP` button behavior — all three abort the running job, and
`TOOL CHECK` additionally pulls Z to home and opens the Resume Job screen automatically.

## 6.4 Resuming a Canceled Job (p.84)

A job canceled by one of the §6.3 methods can be resumed three ways (Router Manual §6.4, p.84):

- `CYCLE START` — restarts the job at the beginning of the part program.
- `F1 – Resume Job` (in the `F4 – Run` menu) — restarts at or near the point of interruption;
  see §6.5.
- `F2 – Search` (in the `F4 – Run` menu) — restarts at a specified point; see §6.5.

> **Note:** before `F1 – Resume Job` or `F2 – Search`, the tool may need to be repositioned in X
> and Z for cycles that start down inside an ID or behind a shoulder (Router Manual §6.4, p.84).

## 6.5 Run Menu (p.84-86)

Press `F4 – Run` from the Main Screen to reach the Run menu (Router Manual §6.5, p.84); see
[interface.md](interface.md) §F4 – Run Job Options for the top-level softkey path. From here the
operator restarts a canceled job or changes how a job runs.

| Softkey | Label | Description |
|---|---|---|
| `F1` | Resume Job | Access the resume job screen; see §6.4 |
| `F2` | Search | Open the Search and Run menu |
| `F3` | Repeat On/Off | Toggle the repeat feature for part counting |
| `F4` | Skips On/Off | Toggle the block skip feature |
| `F5` | Block Mode | Toggle Single Block mode |
| `F6` | Optional Stops | Toggle optional stops |
| `F8` | Graph | Graph the part |
| `F9` | Rapid On/Off | Toggle Rapid Override |
| `F10` | RTG On/Off | Toggle the Run-time Graphics option |

The current state of each toggle above is shown in the Run menu's user window (Router Manual
§6.5, p.85-86).

### F1 – Resume Job (p.84-85)

If the job was canceled by `TOOL CHECK`, the control goes to the resume job screen
automatically; otherwise reach it via `F4 – Run` then `F1 – Resume Job`. From this screen the
operator can modify tool offsets, modify the tool library, toggle block mode or optional stops,
graph the partially-completed job, or start it from the point of interruption (Router Manual
§6.5, p.84). The resume option is unavailable after loading a new job, running a job to
completion, a parse error in the job, editing or reposting the job file, or a loss of power
while a job is running (Router Manual §6.5, p.84-85).

### F2 – Search (p.85)

Opens the "Search and Run" menu, which specifies the program line, block number (prefix `N`),
or tool number (prefix `T`) at which to begin execution; program lines are numbered from 1 at
the top of the file. Press `CYCLE START` to start at the specified point (Router Manual §6.5,
p.85). `F1 – Tool Change` toggles whether the control performs a tool change so the loaded tool
matches the one specified at that line or block (`YES`) or keeps the currently-loaded tool
regardless (`NO`). Previous searches are recalled with `UP ARROW` / `DOWN ARROW` in the search
text box.

> **Note:** you cannot search within a subroutine (Router Manual §6.5, p.85).

### F3 – Repeat On/Off and Part Count (p.85)

Toggles the repeat feature for part counting; while Repeat is on and part counting is in
effect, the job re-runs automatically until the specified part count is reached. The `Part
Count` prompt sets that count: a positive value counts up from `Part #` zero to the entered
`Part Cnt`, incrementing on each completed run; a negative value counts down from the entered
count to zero, decrementing on each completed run (Router Manual §6.5, p.85).

### F4-F10 (p.85-86)

`F4 – Skips On/Off` skips G-code lines starting with `/`; because jobs run pre-processed and
buffered, toggling it during a run may take effect with a delay. `F5 – Block Mode` toggles
Single Block mode (equivalent to the `AUTO/BLOCK` key); Auto mode is the default and is
re-instated when a job run ends. `F6 – Optional Stops` makes M1 codes wait for `CYCLE START`
like M0 when on, and be ignored when off (see Router Manual Ch 13 for M-code definitions).
Optional Stops defaults to off; the manual prints, under this same key, "If you use this key to
turn on Single Block mode and then run a job, Optional Stops will be set to off" (Router Manual
§6.5, p.86). `F8 – Graph` graphs the
part; from the Search or Resume Job screens it shows dotted lines for the portion that will be
skipped and solid lines for the portion that will be machined. `F9 – Rapid On/Off` toggles
Rapid Override; when on, the Feed Rate Override knob adjusts rapid-move (`G0`) speed (see
Router Manual Ch 12 for G-code definitions), and when off rapids run at full speed. `F10 – RTG
On/Off` must be on for Run-time Graphics (§6.2) to start with `CYCLE START`, and off prevents
starting it mid-run (Router Manual §6.5, p.85-86).

> Note: that sentence, printed under the `F6 – Optional Stops` key, names Single Block mode, not
> Optional Stops, as the thing "this key" turns on (Router Manual §6.5, p.86).

Machine Parameter 400 controls whether `CYCLE START` is enabled on the Run menu: zero disables
it there, any other value enables it. This does not apply to the Resume and Search sub-menus,
where `CYCLE START` is always enabled (Router Manual §6.5, p.86).

## 6.6 Power Feed (p.86)

Press `F4 – Power Feed` from the Utility menu (see [Utility menu](#utility-menu-p88-91) below)
to reach the Power Feed screen, used to command axis movement; every Power Feed operation can
also be run in MDI with the equivalent M- and G-codes (Router Manual §6.6, p.86). See
[interface.md](interface.md) §F3 – MDI for the MDI entry method.

| Softkey | Label | Description |
|---|---|---|
| `F1` | ABS | Move an axis to an absolute position at a specified feed rate |
| `F2` | INC | Move an axis an incremental distance at a specified feed rate |
| `F3` | Free XY | Release power to the X and Y motors for manual use |
| `F4` | Power XY | Apply power to the X and Y motors for jog-panel use |
| `F6` | 3 Axis/4 Axis | Toggle between 3-axis and 4-axis configuration |

## 6.7 Communications Stress Test (p.86-87)

The example files include a communications stress test the operator can run; results report
communication errors such as packets resent, generic communication errors, packets out of
order, and NAcks packets sent/received (Router Manual §6.7, p.86).

To run the test (Router Manual §6.7, p.86-87):

1. `F2 – Load`.
2. If not already in the `ncfiles` directory of the `cncm` folder, navigate to `cncm\ncfiles`.
3. Select the `com_stress_test.cnc` file.
4. Press `CYCLE START`.
5. The test runs; a `Communications Stress Test PASSED` message reports "max. errors acceptable
   = 5" and the results: Packets Resent, Generic Communication Errors, Packets Out of Order,
   NAcks Packets Sent, and NAcks Packets Received (p.87).

> **Note:** step 2 names the folder `cncm`, as printed (Router Manual §6.7, p.87), while Ch 7's
> `F6 – User Maint` describes `F3 – Machine Notes` as opening a file "stored in the cncr
> directory" (Router Manual Ch 7, p.90) — the router's own install directory (§1.8, p.13; see
> [interface.md](interface.md)). The manual does not reconcile the two names.

---

## Utility menu (p.88-91)

Press `F7 – Utility` at the CNC Software Main Screen to reach the Utility Menu; contents vary
by M-series Control model (Router Manual Ch 7, p.88). See [interface.md](interface.md) §F7 –
Utility for the top-level F1-F10 purpose table established from Ch 3.

| Softkey | Label | Description | p. |
|---|---|---|---|
| `F1` | Intercon/CAM Menu | Opens Intercon by default, for conversational part programming | 88 |
| `F2` | Manual | Opens a PDF of the CNC12 Operator's manual | 88 |
| `F3` | Advanced Config | Edit Control Configuration, Machine Configuration, Machine Parameters, the PID Menu, and the System Test | 88 |
| `F4` | Power Feed | Move an axis absolute (`F1 – Abs`) or incremental (`F2 – Inc`); free (`F3 – Free`) or power (`F4 – Power`) the X/Y axes; on 4-axis machines, `F6 – 3 Axis` toggles 3-axis/4-axis | 88 |
| `F5` | Color Picker | Customize CNC12 colors or pick a preset color theme | 88-89 |
| `F6` | User Maint | Access file options, restore a report, machine notes, backup/restore files, view logs, and open a command line prompt | 90 |
| `F7` | Create Report | Generate a `report.zip` backup of system configuration files, for dealer servicing/troubleshooting | 90 |
| `F8` | Import License | Select a license file for use with CNC12 | 90 |
| `F9` | Digitizing | Access the digitizing features; hidden if the machine is not homed | 90-91 |
| `F10` | Acorn Wizard | Guided configuration tool for axis motors, I/O, spindle control, and homing routines | 91 |

### F5 – Color Picker (p.89)

Centroid Classic and other preset themes are selectable. Edit an individual color by clicking
its square or typing a hex code; clicking a color square opens the Pick Swatch Type screen,
where a color wheel or RGB/Hex entry sets the color — select `Accept` to confirm it. Select
`Save` to create a new Color Profile, or `Done` to return to the previous screen. To revert
saved changes to the Centroid Classic theme, select `File` then `New` (Router Manual Ch 7,
p.89).

### F6 – User Maint (p.90)

Sub-keys of `F6 – User Maint` (Router Manual Ch 7, p.90):

| Sub-key | Label | Description |
|---|---|---|
| `F1` | File Ops | Access files in a DOS format |
| `F2` | Restore Report | Pick a `report.zip` file to restore settings to the machine from |
| `F3` | Machine Notes | Opens a text file, stored in the `cncr` directory, for notes about the machine and control customizations |
| `F4` | Backup Files | Creates a backup zip file of the `ncfiles` and `intercom` folders to a specified location |
| `F5` | Restore Files | Restores a zip file to the `ncfiles` and `intercom` folders |
| `F6` | Log | Opens the Log menu — view logs and debug information about the control and installation |
| `F7` | System Prompt | Opens the Windows command line terminal |

### F9 – Digitizing (p.90-91)

Hidden if the machine is not homed (Router Manual Ch 7, p.90).

> **Note:** requires a Probe and Ultimate license for the full feature set (Router Manual Ch 7, p.91).

### F10 – Acorn Wizard (p.91)

Available only with Acorn, AcornSix, and Hickory; a guided interface for configuring axis
motors, inputs/outputs, spindle control, and homing routines, for a mill, lathe, router, or
plasma cutter (Router Manual Ch 7, p.91).
