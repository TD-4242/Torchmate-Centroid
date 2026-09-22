# M-code index

Source: Router Manual Ch 13 (§13.1-§13.69, p.280-306).

§13.1 gives a summary of every M-function, pointing to Ch 12-13 for detail (Router Manual
§13.1, p.280-281). §13.2 covers customizing **Most** M-functions 0-90 with an `mfuncXX.mac`
file in `c:\cncr`; M2, M6, and M25 can be customized but always move the Z-axis home before
the macro's commands run, and M0-M9 filenames must use a single digit (`mfunc3.mac`, not
`mfunc03.mac`); no M-function above 90 can be customized with a macro (Router Manual §13.2,
p.281).

| Code | Name | Summary | Ref |
|---|---|---|---|
| M00 | Stop for Operator | Stops motion and prompts the operator to press `CYCLE START` to continue. | §13.3, p.282 |
| M01 | Optional Stop for Operator | Pauses the job for `CYCLE START` only when optional stops are turned on; otherwise has no effect. | §13.4, p.282 |
| M02 | Restart Program | Moves Z home, performs any requested movement, and restarts the program from the first line after `CYCLE START`. | §13.5, p.283 |
| M03 | Spindle On Clockwise | Requests the PLC to start the spindle clockwise. | §13.6, p.283 |
| M04 | Spindle On Counter-clockwise | Requests the PLC to start the spindle counter-clockwise. | §13.7, p.283 |
| M05 | Spindle Stop | Requests the PLC to stop the spindle. | §13.8, p.283 |
| M06 | Tool Change | Moves Z home, stops spindle and coolant, then commands an automatic tool changer or prompts the operator to insert the tool. | §13.9, p.283 |
| M07 | Mist Coolant On | Requests the PLC to start the mist coolant system. | §13.10, p.284 |
| M08 | Flood Coolant On | Requests the PLC to start the flood coolant system. | §13.11, p.284 |
| M09 | Coolant Off | Requests the PLC to stop the coolant system. | §13.12, p.284 |
| M10 | Clamp On | Requests the PLC to activate the clamp (chuck). | §13.13, p.284 |
| M11 | Clamp Off | Requests the PLC to release the clamp (chuck). | §13.14, p.285 |
| M17 | Prepare for Tool Change (Macro) | Has no default action; a custom macro turns off spindle/coolant and starts spindle orientation ahead of M6. | §13.15, p.285 |
| M19 | Spindle Orient (Macro) | Has no default action; a custom macro requests the PLC to rotate the spindle to its preset orient position. | §13.16, p.285 |
| M25 | Move to Z-home | Moves the Z-axis to its Return #1 home position; optional axis arguments move other axes to their Return #1 positions instead. | §13.17, p.285 |
| M26 | Set Axis Home | Sets the home position for the specified axis (default Z) to the current position after the line's movement. | §13.18, p.285 |
| M30 | Custom M-code | Posted at the end of every G-code program; performs no operation by default, but can be customized. | §13.19, p.286 |
| M37 | Laser ON | Requests the PLC to power on a PWM-connected laser. | §13.20, p.286 |
| M38 | Laser OFF | Requests the PLC to power off a PWM-connected laser. | §13.21, p.286 |
| M39 | Air Drill | Runs a default air-drill activation sequence with a 2-second timeout. | §13.22, p.287 |
| M41 | Select Spindle Gear Range (Low) | Has no default action; a custom macro notifies the PLC to select the low gear range. | §13.23, p.287 |
| M42 | Select Spindle Gear Range (Medium-Low) | Has no default action; a custom macro notifies the PLC to select the medium-low gear range. | §13.23, p.287 |
| M43 | Select Spindle Gear Range (High) | Has no default action; a custom macro notifies the PLC to select the high gear range. | §13.23, p.287 |
| M60 | 5-axis Digitizing Macro | Moves a probe from a start to a finish position, set via user variables, for 5-axis digitizing on the Tilt Table system. | §13.24, p.287 |
| M91 | Move to Minus Home | Moves the specified axis to its minus home switch at the slow jog rate, then reverses to clear it and find the index pulse. | §13.25, p.288 |
| M92 | Move to Plus Home | Moves the specified axis to its plus home switch at the slow jog rate, then reverses to clear it and find the index pulse. | §13.26, p.289 |
| M93 | Release/Restore Motor Power | Releases (or, with `P1`, restores) motor power for the specified axis, or all axes if none is given. | §13.27, p.289 |
| M94 | Output On | Turns on one of 128 user-definable system-variable bits (`SV_M94_M95_n`) the PLC reads; see `centroid-plc-programming` [resources.md](../../centroid-plc-programming/reference/resources.md#triggering-plc-actions-with-m94m95). | §13.28, p.290 |
| M95 | Output Off | Turns off one of the same 128 system-variable bits set by M94; see `centroid-plc-programming` [resources.md](../../centroid-plc-programming/reference/resources.md#triggering-plc-actions-with-m94m95). | §13.28, p.290 |
| M98 | Call Subprogram | Calls a numbered or named subprogram file, with an optional repeat count; the subprogram ends with M99. | §13.29, p.290 |
| M99 | Return from Macro or Subprogram | Ends a subprogram or macro and returns control to the calling program; assumed at the end of the file if omitted. | §13.30, p.292 |
| M100 | Wait for PLC Bit (Open, Off, Reset) | Waits for an `INP`/`OUT`/`MEM`/`T`/`STG`/`FSTG` bit to reach its open/off/reset state; see `centroid-plc-programming` [resources.md](../../centroid-plc-programming/reference/resources.md). | §13.31, p.292 |
| M101 | Wait for PLC Bit (Closed, On, Set) | Waits for the same bit types to reach their closed/on/set state; see `centroid-plc-programming` [resources.md](../../centroid-plc-programming/reference/resources.md). | §13.32, p.292 |
| M102 | Restart Program | Performs any requested movement and restarts the program from the first line, without homing Z or prompting the operator. | §13.33, p.293 |
| M103 | Programmed Action Timer | Starts a time limit for a timed operation; the job cancels if the timer is not stopped (usually by M104) before it expires. | §13.34, p.293 |
| M104 | Cancel Programmed Action Timer | Stops the timer started by the last M103. | §13.35, p.293 |
| M105 | Move Minus to Switch | Moves the requested axis minus at the current feed rate until a specified switch opens or closes. | §13.36, p.293 |
| M106 | Move Plus to Switch | Moves the requested axis plus at the current feed rate until a specified switch opens or closes. | §13.37, p.294 |
| M107 | Output Tool Number | Sends the current tool number to the automatic tool changer via the PLC, without setting the strobe or checking for acknowledgement. | §13.38, p.294 |
| M108 | Enable Override Controls | Re-enables the feed rate and/or spindle speed override controls disabled by M109. | §13.39, p.294 |
| M109 | Disable Override Controls | Disables the feed rate and/or spindle speed override controls; not usable in MDI mode. | §13.40, p.294 |
| M115 | Protected Move Probing | Moves the specified axis until a PLC bit reaches the tripped state (or, with a negative bit number, the clear state); defaults to the negative direction if no position is given. | §13.41, p.295 |
| M116 | Protected Move Probing | Behaves like M115, but defaults to the positive direction when no position is given. | §13.41, p.295 |
| M125 | Protected Move Probing | Behaves like M115, for moves where no contact is expected. | §13.41, p.295 |
| M126 | Protected Move Probing | Behaves like M116, for moves where no contact is expected. | §13.41, p.295 |
| M115/M116/M125/M126 | DSP Probe Specific Information | With a DSP-type probe configured, these commands add window-check retries and `L1`/`L2`/`Q1` options, and store position in system variables `#24301`-`#24305`. | §13.42, p.295 |
| M120 | Open Data File (Overwrite Existing File) | Opens the named data file for writing, closing any file already open; errors and cancels the job if it cannot open. | §13.43, p.296 |
| M121 | Open Data File (Append to Existing File) | Opens the named data file for writing at the end, creating it if needed; closes any file already open. | §13.44, p.297 |
| M122 | Record Local Position(s) and Optional Comment in Data File | Writes the current position(s), in local coordinates, and any line comment to the open data file. | §13.45, p.297 |
| M123 | Record Value and/or Comment in Data File | Writes a specified value and/or a line comment to the open data file. | §13.46, p.297 |
| M124 | Record Machine Position(s) and Optional Comment in Data File | Like M122, but reports machine position instead of local WCS position. | §13.47, p.298 |
| M127 | Record Date and Time in a Data File | Writes the date, time, and year to the open data file. | §13.48, p.298 |
| M128 | Move Axis by Encoder Counts | Moves the requested axis by an `L`-specified encoder count position or quantity, per the current G90/G91 mode. | §13.49, p.298 |
| M129 | Record Current Job File Path to Data File | Writes the current job's file path to the open data file. | §13.50, p.298 |
| M130 | Run System Command | Runs a shell command given as a string argument; an `L1` parameter waits for it to finish. | §13.51, p.298 |
| M150 | Set Spindle Encoder to Zero at Next Index Pulse | Resets the spindle encoder position to 0 at the next index pulse; the spindle must be commanded to move for this to occur. | §13.52, p.299 |
| M151 | Unwind Rotary Axis | Resets the specified rotary axis's machine position to less than one revolution. | §13.53, p.299 |
| M200/M223/M224/M225/M290 | Formatted String Commands (syntax) | Defines the shared printf-style `%c`/`%s`/`%f` formatted-string syntax these M-codes use for custom screen and file I/O. | §13.54, p.299 |
| M200 | Stop for Operator, Prompt for Action | Pauses the job and prompts the operator with a formatted string; jogging is enabled only if M0 jogging is unlocked or the control is in DEMO mode. | §13.55, p.301 |
| M201 | Stop for Operator, Prompt for Action (job-status bits off) | Behaves like M200, but also turns off the `SV_PROGRAM_RUNNING`, `SV_MDI_MODE`, and `SV_JOB_IN_PROGRESS` bits while the prompt is displayed. | §13.55, p.301 |
| M221 | Display Formatted String Non-Modal | Outputs a formatted string without halting the job; also supports the HTML `<a>` link tag. | §13.56, p.302 |
| M222 | Prompt for Operator Keycode Input | Prompts the operator with a message and returns the first keycode pressed into a variable. | §13.57, p.302 |
| M223 | Write Formatted String to File | Writes a formatted string to a file already opened with M120 or M121. | §13.58, p.302 |
| M224 | Prompt for Operator Input Using Formatted String | Displays a formatted-string prompt and assigns the operator's input to a specified variable. | §13.59, p.302 |
| M225 | Display Formatted String for a Period of Time | Displays a formatted string for a specified number of seconds, or indefinitely if 0; `CYCLE START` skips the wait. | §13.60, p.303 |
| M290 | Digitize Profile (Optional) | Performs a two-axis digitize, probing along one axis while stepping over on a perpendicular travel axis. | §13.61, p.303 |
| M291 | Reset MPG Offset | Resets the MPG offset for all axes; requires an Ultimate license. | §13.62, p.304 |
| M294 | Un-pair Master Axis | Un-pairs a master axis from its slaved axes, which then reappear on the DRO if labeled; requires a Pro license. | §13.63, p.304 |
| M295 | Re-pair Master Axis | Re-pairs a master axis with its slaved axes, optionally re-syncing first (`P1`) or not (`P2`); requires a Pro license. | §13.64, p.304 |
| M297 | Disable Software Travel Limits | Makes CNC12 ignore software travel limits (Limit and Home switches are still respected) until M298, MDI closes, or the job ends. | §13.65, p.305 |
| M298 | Enable Software Travel Limits | Restores adherence to software travel limits; active by default and reapplied after each job or MDI close. | §13.66, p.305 |
| M300 | Fast Synchronous I/O Update | Sets one of 32 fast system-integer variables (`SV_FSIO1`-`SV_FSIO32`) for the PLC, without decelerating motion to a stop (unlike M94/M95). | §13.67, p.305 |
| M333 | Axis Role Re-assignment | Experimental: re-assigns X, Y, and Z axis behavior to other axes; not recommended for normal use. | §13.68, p.305 |
| M1000-M1015 | Graphing Color for Feed Rate Movement | Sets the toolpath-graph color for feed-rate moves from a 16-color chart; does not affect the program's actual run, and cannot share a line with another M-code. | §13.69, p.305 |

> The manual names two of these codes differently in its §1.9 summary than in Ch 13: M30 is
> "M-code for End of Program" there but "Custom M-code" in Ch 13 (Router Manual §1.9, p.15;
> §13.1, p.280; §13.19, p.286). M107 is "Output Binary Coded Decimal Tool Number" there but
> "Output Tool Number" in Ch 13, which does not mention a BCD encoding (Router Manual §1.9,
> p.15; §13.1, p.280; §13.38, p.294).
