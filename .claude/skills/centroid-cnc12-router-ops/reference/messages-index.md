# CNC12 message index

Source: Router Manual Ch 16 (§16.1-§16.11, p.435-450). Meaning condenses the manual's
"Cause & Effect" column; the manual's "Action" text is kept only when it is not "No action
required." Placeholders (`__`, `#__`, `NNNNN`) are printed exactly as the manual shows them.

## §16.1 CNC Software Startup Errors and Messages (§16.1, p.435)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 102 | Error initializing CPU. . . cannot continue | Error sending a hex file program to the motion control card. Action: inspect MPU11 connection or fix missing/corrupted hex file; contact dealer. | §16.1, p.435 |
| 103 | Error sending setup | Error sending the current setup parameters to the motion control card. Action: inspect MPU11 connection or fix missing/corrupted hex file; contact dealer. | §16.1, p.435 |
| 104 | Error sending PID setup | Error sending the current PID setup parameters to the motion control card. Action: inspect MPU11 connection or fix missing/corrupted hex file; contact dealer. | §16.1, p.435 |
| 105 | mpu.plc file read error. . . cannot continue | Error sending the current PLC program to the motion control card. Action: install or recompile the PLC program; contact dealer. | §16.1, p.435 |
| 106 | The PC clock appears to be wrong | Error while reading the temperature file; the PC's internal clock is earlier than the time recorded in a previously-stored file. Action: set the PC internal clock to the correct time. | §16.1, p.435 |
| 199 | CNC started | The CNC control software has started. | §16.1, p.435 |

## §16.2 Messages Issued Upon Exit from the CNC Software (§16.2, p.435)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 201 | Exiting CNC due to a known error (ACORN only) | MPU11 is not responding, or the mpu11.hex/mpu.plc files are missing or damaged. Action: check for possible software corruption; contact dealer. | §16.2, p.435 |
| 202 | Exiting CNC due to a math error | A floating-point math error occurred; possible corruption of cnc.tem, cncm.job, or cncm.wcs files. Action: delete corrupted files and reboot software; contact dealer. | §16.2, p.435 |
| 204 | Exiting CNC. . . Normal Exit | The CNC control software is shutting down normally. | §16.2, p.435 |
| 222 | Autotune run | Autotune has been run. | §16.2, p.435 |

## §16.3 Messages and Prompts in the Operator Status Window Status Messages (§16.3, p.435-437)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 301 | Stopped | A job has ended normally or the Operator has aborted the job. | §16.3, p.435 |
| 302 | Moving. . . | Motors are moving while a CNC program is running. | §16.3, p.435 |
| 303 | Paused. . . | Motion is paused while a CNC program is running (FEED HOLD). | §16.3, p.435 |
| 304 | MDI. . . | The CNC software is running in MDI mode. | §16.3, p.435 |
| 305 | Processing. . . | The CNC software is running in a mode other than MDI. | §16.3, p.436 |
| 306 | Job Finished | A normal end of the CNC program. | §16.3, p.436 |
| 307 | Operator abort: job canceled | ESC or CYCLE CANCEL was pressed; job is cancelled. | §16.3, p.436 |
| 308 | Waiting for input #NN | M100 or M101 is executing; the program continues once the specified input opens or closes. | §16.3, p.436 |
| 309 | Waiting for CYCLE START button | M0, M1, M100/75, or Block Mode was executed. Action: press Cycle Start. | §16.3, p.436 |
| 310 | Waiting for output #NN | M100 or M101 is executing; the program continues once the specified output opens or closes. | §16.3, p.436 |
| 311 | Waiting for memory #NN | M100 or M101 is executing; the program continues once the specified memory bit changes to the correct state. | §16.3, p.436 |
| 312 | Waiting for PLC operation (Mnn) | The PLC program is not clearing the PLC operation in progress. | §16.3, p.436 |
| 313 | Waiting for dwell time | G4 is executing; the program waits for the specified dwell time and then continues. | §16.3, p.436 |
| 314 | Waiting for system #NN | M100 or M101 is executing; the program continues once the specified PLC system variable changes to the correct state. | §16.3, p.436 |
| 315 | Searching. . . | A run/search is currently in progress. | §16.3, p.436 |
| 317 | Waiting for automatic tool change | mfunc6.mac is executing. | §16.3, p.436 |
| 318 | Operator abort probing cancelled | ESC or CYCLE CANCEL was pressed while doing a probing move. | §16.3, p.436 |
| 319 | Probing cycle cancelled | The probing cycle was cancelled. | §16.3, p.436 |
| 320 | Probe stuck | The probe is stuck or hit an object when it was not expecting contact. | §16.3, p.436 |
| 322 | Stall: probing cancelled | The probing was cancelled because of a stall. | §16.3, p.436 |
| 323 | Stall: job cancelled | The job was cancelled because of a stall. | §16.3, p.436 |
| 324 | Limit: probing cancelled | The probing was cancelled because of a limit error. | §16.3, p.436 |
| 325 | Limit: job cancelled | The job was cancelled because of a limit error. | §16.3, p.436 |
| 326 | Fault: probing cancelled | The probing was cancelled because of a fault. | §16.3, p.436 |
| 327 | Fault: job cancelled | The job was cancelled because of a fault. | §16.3, p.436 |
| 328 | Cutter comp error: job cancelled | The job was cancelled because of a cutter comp error. | §16.3, p.436 |
| 329 | Invalid parameter: job cancelled | The job was cancelled because of an invalid parameter. | §16.3, p.436 |
| 330 | Canned cycle error: job cancelled | The job was cancelled because of a canned cycle error. | §16.3, p.437 |
| 332 | Search Failed | A run/search was unable to find the requested G-code line. | §16.3, p.437 |
| 334 | Locating position to resume job. . . | A run/search is currently locating the job continuation point in the program. | §16.3, p.437 |
| 335 | Emergency Stop Released | The Emergency Stop Button has been released. | §16.3, p.437 |
| 336 | Digitize cancelled | ESC or CYCLE CANCEL was pressed during digitizing. | §16.3, p.437 |
| 337 | Digitize complete | A digitizing routine ran to completion. | §16.3, p.437 |
| 338 | Job Cancelled | ESC or CYCLE CANCEL was pressed during the job run. | §16.3, p.437 |
| 339 | Jogging. . . | An axis jog key is currently pressed and the machine is moving the corresponding axis. | §16.3, p.437 |
| 340 | Limit (#__) cleared | A previously-tripped limit switch is now in the "untripped" position. | §16.3, p.437 |
| 341 | Probing Cycle Finished | A probing cycle ran to completion. | §16.3, p.437 |
| 342 | Waiting for motion to stop | The PC is waiting for the MPU11 to complete its motion. | §16.3, p.437 |
| 343 | Waiting for stop reason reset | A PC is waiting for the MPU11 to reset the stop reason (part of the PC/MPU11 communications handshake). | §16.3, p.437 |
| 344 | Feed Rate modified due to spindle | The effective feed rate has been lowered because the spindle is spinning slower than the threshold percentage of the commanded spindle speed (threshold set by Parameter 149). | §16.3, p.437 |
| 345 | Waiting for spindle to get up to speed | Job progress is paused until the actual spindle speed reaches the threshold percentage of the commanded spindle speed (threshold set by Parameter 149). | §16.3, p.437 |
| 346 | Waiting for spindle direction | Job progress is paused until the spindle turns in the commanded direction. | §16.3, p.437 |
| 347 | Reset Cleared | The reset state has been cleared. | §16.3, p.437 |

## §16.4 Abnormal Stops (Faults) (§16.4, p.437-443)

Abnormal stops are detected in this order: PLC, servo drive, spindle drive, lube, then ESTOP
(Router Manual §16.4, p.437).

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 401 | PLC failure detected | MPU11 stopped with PLC failure bit set; job cancelled. Action: check PLC fibers and PLC logic power. | §16.4, p.437 |
| 404 | Spindle drive fault detected | MPU11 stopped with spindle drive fault bit set; job cancelled. Action: check the inverter for a fault or reset the spindle contactor OCR, then cycle the EMERGENCY STOP. | §16.4, p.438 |
| 405 | Lubricant level low | MPU11 stopped with low lube fault bit set; the current job finishes but nothing works after that. Action: add lube or check the low lube switch wiring, then cycle the EMERGENCY STOP. | §16.4, p.438 |
| 406 | Emergency Stop detected | MPU11 stopped with no fault bits set; job cancelled. Action: release the Emergency Stop button. | §16.4, p.438 |
| 407 | limit (#__) tripped | MPU11 stopped with a limit switch tripped; job cancelled. Action: clear the limit switch. | §16.4, p.438 |
| 408 | Programmed action timer expired | M103's time expired before M104 was encountered; job cancelled. Action: find out why the timer expired before the specified action was completed. | §16.4, p.438 |
| 409 | _Axis (_) lag | Can be caused by insufficient torque (not enough current) or insufficient speed (not enough voltage) on a given axis. Action: check power and cabling between axis motors, drives, and controller for low voltage, noise, or shorts. | §16.4, p.438 |
| 410 | _ axis position error | A position error greater than one motor encoder turn was detected on any axis; all axis motion stops, motor power is released, and the CNC program is aborted. Probable causes: a backwards-wired motor, noise on the motor cables, or an encoder error. Action: jog and watch DRO direction to check for backwards wiring, check motor cabling/grounding, or fast-jog to isolate an encoder error by swapping motors between axes (see manual for the full numbered procedure). | §16.4, p.438 |
| 411 | _ axis full power without motion | 90% Power (a PID Output greater than 115) is applied to an axis with no motion greater than 0.0005 in. for longer than Parameter 61 (default 0.5 sec); all axis motion stops and the CNC program is aborted. Probable causes: a physical stop, a servo drive shutdown from a limit switch input, or the Z-home switch doubling as the Z+ limit switch. Action: slow-jog off a physical stop and set travel limits, check for a tripped limit switch, or check the switch signal for noise (see manual for the full numbered procedure); no motion when jogging toward the error direction indicates a servo drive failure. | §16.4, p.439 |
| 412 | _ axis encoder differential error | An error was detected in the differential signal levels for this axis encoder, indicating a loose/severed cable or a bad encoder; stops all motion and cancels the job. Action: reconnect/replace the encoder or encoder cable. | §16.4, p.439 |
| 417 | Abnormal end of job | Job was ended without reason. | §16.4, p.439 |
| 418 | Search Line or Block not found | The requested search input data was not found in the loaded CNC file. Action: type in the correct search input data or load the correct job. | §16.4, p.439 |
| 419 | Search line in embedded subprogram | The requested search line is found but is part of an embedded/extracted subprogram. Action: use another line number. | §16.4, p.439 |
| 420 | _ axis motor overheating | The software estimates one or more motors reached the warning temperature (Parameter 29), or the temperature file is corrupted; job cancelled. Action: contact dealer; determine what is causing the motor(s) to overheat, or delete the cnc.tem file and reboot. | §16.4, p.439 |
| 421 | Motor(s) too hot: job canceled | The software estimates one or more motors reached the limit temperature (Parameter 30); the job cannot run until the motor(s) cools down. Action: contact dealer; determine what is causing the motor(s) to overheat or delete the cnc.tem file and reboot. | §16.4, p.440 |
| 422 | Check Jog Panel cable | Jog panel failure or loose cable. Action: reconnect the jog panel cable. | §16.4, p.440 |
| 428 | Check MPG cable | MPG failure, loose cable, or it is turned off. Action: reconnect the MPG cable and turn the axis selector knob to an axis. | §16.4, p.440 |
| 434 | _ idling too high: Releasing power | The axis is not moving and no job is running, but the axis has stopped against abnormal resistance; power is released to the motors. Action: run Autotune to adjust the motor settings. | §16.4, p.440 |
| 435 | _ axis runaway: Check motor wiring | Motor was in a runaway fault condition; power to the motor is automatically shut off. Action: check the motor wiring. | §16.4, p.440 |
| 436 | Servo drive shutdown | The servo drive hardware detected an overcurrent or overvoltage condition, shown on the drive's LEDs; it stops all motion, removes motor power, and reports the fault to the CNC software via the PLC. Action: on DC systems check the servo drive's LEDs and fibers 4&5; on an AC system check that P178 bit 4 is set. | §16.4, p.440 |
| 437 | Servo power removed | An axis was moving more than 300 RPM while power was supposed to be off, from a backwards-wired motor, a shorted servo drive, or inertia after motion was canceled on an unbalanced axis; power to the motors is released. Action: check the motor wiring, servo drive, or the Kg value in the PID (must not exceed +/-5). | §16.4, p.440 |
| 438 | Spindle slave position error | The slaved axis moved too far in the wrong direction during a spindle-slaved move (such as rigid tapping); job cancelled. Action: check Parameter 34 for an incorrect plus/minus sign in front of the encoder counts. | §16.4, p.440 |
| 439 | _ axis servo drive data output error | Logic power failure or loss of communication from the drive to the MPU11. Action: check that the logic LED is on and the fiber optic cables to the drive; for SD1 drives keep bus cables shielded and short; power down and check drive connections. | §16.4, p.441 |
| 441 | _ axis overvoltage | Input power exceeded 340VDC; the control board shuts down the drive and removes power, and the motor brake engages for five seconds. Action: check that input voltage is below 340VDC; lower the incoming VAC if not. | §16.4, p.441 |
| 442 | _ axis undervoltage | The drive's input power is less than 80VDC. Action: check the supply voltage. | §16.4, p.441 |
| 443 | _ axis commutation encoder bad | The control detected an invalid commutation zone value (0 or 7). Action: perform a motor Move Sync in the Drive Menu; check for a wiring problem in the encoder cable/motor end cap, an encoder cable shield connected at the motor end, a bad encoder, unconnected motor power cable shields, or an improperly grounded drive. | §16.4, p.441 |
| 444 | _ axis overtemperature detected | The drive overtemp sensor was tripped; the motor is not given power. Action: the drive is being run at overcapacity, the cooling fan isn't functioning, or the fan's airflow is blocked. | §16.4, p.441 |
| 445 | _ axis overcurrent detected | Overcurrent is detected on an axis; the motor is not given power. Action: try to jog the axis (the drive resets the current limit and tries to move the motor); if the error returns, check for a short in the motor output. | §16.4, p.441 |
| 446 | _ axis servo drive data input failure | Communication checksum error; the motor is not given power. Action: check the fiber optic cables; verify continuity between the drive chassis, ground strip, and Earth ground. | §16.4, p.441 |
| 447 | _ axis (#) bad index pulse detected | Noise was picked up by an encoder cable or a misaligned encoder; the motor is not given power. Action: remove the noise or align the encoder. | §16.4, p.441 |
| 449 | Manual movement detected in restricted area | Unexpected manual movement of the axis was detected when Z-axis summing is active. Action: physically lock the Z-axis manual quill. | §16.4, p.441 |
| 450 | Voltage brake applied | An overvoltage condition was detected; electronic braking offloaded excess voltage to the dropping resistors. Action: usually innocuous even if occasional; a continuous stream means contact your dealer. | §16.4, p.442 |
| 451 | Current brake applied | An overcurrent spike was detected on the drive. Action: usually innocuous even if occasional; frequent occurrence may mean a higher-current drive is needed, and a continuous stream means hit E-Stop and contact your dealer. | §16.4, p.442 |
| 452 | PC Receive Data Error | A fatal communication error between the MPU and PC, detected on the PC side. Action: restart the software to clear the error; frequent occurrence may indicate a network configuration or Ethernet cable issue. | §16.4, p.442 |
| 453 | CPU Receive Data Error | A fatal communication error between the MPU and PC, detected on the MPU11 side. Action: restart the software to clear the error; frequent occurrence may indicate a network configuration or Ethernet cable issue. | §16.4, p.442 |
| 453 | Jogging while probe detected | The probe was in a tripped state while a jog key was being pressed. | §16.4, p.442 |
| 454 | axis scale encoder differential error | An error was detected in the differential signal levels for this axis scale encoder, indicating a loose/severed cable or a bad encoder; stops all motion and cancels the job. Action: reconnect/replace the scale encoder or scale encoder cable. | §16.4, p.442 |
| 455 | axis encoder quadrature error | The axis encoder skipped a transition state in its count-up/count-down sequence, indicating a loose/severed cable or a bad encoder; stops all motion and cancels the job. Action: reconnect/replace the encoder or encoder cable. | §16.4, p.442 |
| 456 | axis scale encoder quadrature error | The scale encoder skipped a transition state in its count-up/count-down sequence, indicating a loose/severed cable or a bad encoder; stops all motion and cancels the job. Action: reconnect/replace the scale encoder or scale encoder cable. | §16.4, p.442 |
| 457 | Unable to find home | A commanded move sought either an index pulse or a hard stop, but neither was found. Action: reconnect/replace the encoder or encoder cable if seeking an index pulse; check that the hard stop was not broken off or overrun. | §16.4, p.443 |
| 459 | TT1 or Probe is not connected | A Tool Measure operation was aborted because the required TT1 or Probe is not connected. Action: check the TT1 or Probe wiring and plug. | §16.4, p.443 |
| 460 | TT1 and Probe are both connected | A Tool Measure operation was aborted because both a TT1 and Probe were connected. Action: make sure the TT1 and Probe are not plugged in at the same time; also check the wiring. | §16.4, p.443 |
| 461 | Spindle axis is not set | An operation aborted because the spindle axis parameter (35) has an incorrect value. Action: contact dealer. | §16.4, p.443 |
| 462 | Triangular Rotary Axis Out of Range | A triangular rotary axis (tilt table or articulated head machine) is at a position out of range for angular calculation. Action: contact dealer. | §16.4, p.443 |
| 470 | brake wattage exceeded | The brake wattage was exceeded on the indicated ACDC drive. Action: contact dealer. | §16.4, p.443 |
| 487 | Invalid tilt table parameters | One or more values in the tilt table configuration are incorrect. Action: contact dealer. | §16.4, p.443 |
| 490 | Reset Initiated, Press Reset to clear. | The reset state has been set and needs cleared by pressing Reset. Action: press Reset to clear state. | §16.4, p.443 |

> The manual reuses code 444 for a different message in §16.11 (p.450: `__ modified: __ → __`,
> "A servo drive configuration parameter was modified"). It also reuses code 453 for two
> different messages on the same page (p.442, rows above). Neither reuse is resolved here;
> both are kept as printed.

> The `#__`/`_` placeholder for the limit-switch number is printed inconsistently across
> pages: p.437 prints `Limit (#__) cleared` (capital L, code 340, §16.3), p.438 prints
> `limit (#__) tripped` (lowercase l, code 407, §16.4), and p.438 also prints `_Axis (_) lag`
> (code 409, §16.4, capital A directly after the underscore, no space). Each is kept exactly
> as its own page prints it.

## §16.5 CNC Syntax Errors (§16.5, p.443-446)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 501 | Invalid character on line NNNNN | Invalid character on the CNC line; job cancelled. Action: remove the character from the program. | §16.5, p.443 |
| 502 | Invalid G-code on line NNNNN | Invalid G-code encountered on the CNC line; job cancelled. Action: correct the invalid G-code. | §16.5, p.443 |
| 503 | Invalid M-function on line NNNNN | Invalid M-function encountered on the CNC line; job cancelled. Action: correct the invalid M-code. | §16.5, p.443 |
| 504 | Invalid parameter on line NNNNN | Invalid or missing number after a letter; job cancelled. Action: correct the program. | §16.5, p.443 |
| 505 | Invalid value on line NNNNN | Value out of range (T, H, D); job cancelled. Action: correct the program. | §16.5, p.443 |
| 506 | Only 1 M-code per line | More than one M-code appears on the line; job cancelled. Action: move the 2nd M-code to the next line. | §16.5, p.443 |
| 507 | No closing quote | The closing quotation mark (") is missing; job cancelled. Action: add the missing quotation mark. | §16.5, p.443 |
| 508 | Macro nesting too deep | The macro nesting limit was exceeded on an attempt to invoke a subroutine; job cancelled. Action: create a second program. | §16.5, p.443 |
| 509 | Option not available | An attempt was made to access a locked software option; job cancelled. Action: contact Dealer. | §16.5, p.443 |
| 510 | Too many macro arg's | Too many arguments were given in a G65 macro; job cancelled. Action: correct the number of arguments. | §16.5, p.443 |
| 511 | Missing parameter | A parameter is required or expected but not found; job cancelled. Action: correct the program. | §16.5, p.444 |
| 513 | Expected "=" | An error in the expression to the left of "=", a missing "=", or an orphaned parameter; job cancelled. Action: correct the equation. | §16.5, p.444 |
| 514 | Empty expression | The expression contains no operands; job cancelled. Action: correct the expression. | §16.5, p.444 |
| 515 | Syntax error in expression | An illegal character was in the number, variable, or function; job cancelled. Action: correct the program. | §16.5, p.444 |
| 516 | Unmatched bracket (parenthesis) | Brackets or parentheses are paired improperly or misplaced; job cancelled. Action: correct the program. | §16.5, p.444 |
| 517 | Evaluation stack overflow | Brackets or parentheses are nested too deeply; job cancelled. Action: correct the program. | §16.5, p.444 |
| 518 | Undefined variable | The variable name does not exist; job cancelled. Action: correct the program. | §16.5, p.444 |
| 519 | Too many variables | The space allotted for user-defined variables has been exceeded; job cancelled. Action: correct the program. | §16.5, p.444 |
| 520 | Invalid variable name | The variable name contains an illegal character; job cancelled. Action: correct the program. | §16.5, p.444 |
| 521 | Divide by zero | There was an attempt to divide by zero; job cancelled. Action: correct the program. | §16.5, p.444 |
| 522 | Domain error | An imaginary number would result (square root of a negative number); job cancelled. Action: correct the program. | §16.5, p.444 |
| 523 | Invalid value in assignment | There was an attempt to assign an illegal value to a system variable; job cancelled. Action: correct the program. | §16.5, p.444 |
| 524 | Variable is read-only | There was an attempt to assign a value to a read-only system variable; job cancelled. Action: correct the program. | §16.5, p.444 |
| 525 | Missing P value | A P parameter was expected but was missing. | §16.5, p.444 |
| 526 | M22x Missing initial variable | M224 or M225 were not immediately followed by a #variable reference. Action: see M224 and G225. | §16.5, p.444 |
| 527 | M22x initial variable parse error | M224 or M225 were immediately followed by an invalid #variable reference. Action: correct the program. | §16.5, p.444 |
| 528 | M225 String variable not allowed | M225 was immediately followed by a string #variable (invalid); only numeric variables are allowed here. Action: correct the program. | §16.5, p.444 |
| 529 | M225 invalid variable | The #variable specified after M225 was not valid, or not readable due to a machine error. Action: correct the program. | §16.5, p.444 |
| 530 | M224 invalid variable | The #variable specified after M224 was read-only, or not writeable due to a machine error. Action: correct the program. | §16.5, p.444 |
| 531 | M22x missing initial quote | The beginning of the quoted (") format string was not found or was in the wrong place on the G-code line. Action: see M200, M223, M224, or M225. | §16.5, p.444 |
| 532 | M22x missing end quote | The format string did not end with a quote ("). Action: see M200, M223, M224, or M225. | §16.5, p.445 |
| 533 | M22x embedded quote not allowed | The format string contained a quote (") in the middle of it. Action: see M200, M223, M224, or M225. | §16.5, p.445 |
| 534 | M22x character limit exceeded | The format string was too long. Action: correct the program. | §16.5, p.445 |
| 535 | M22x invalid format string | The format string contained invalid format codes. Action: correct the program. | §16.5, p.445 |
| 536 | M22x missing format specifier | The format code was missing its specifier. Action: correct the program. | §16.5, p.445 |
| 537 | M22x Missing Argument | A format code was specified in the format string, but its corresponding #variable argument was missing. Action: correct the program. | §16.5, p.445 |
| 538 | M22x argument parse error | A format code was specified in the format string, but its corresponding #variable argument had a syntax error. Action: correct the program. | §16.5, p.445 |
| 539 | M22x variable type mismatch | A string format code's corresponding #variable argument was numeric, or a numeric format code's corresponding #variable argument was a string. Action: correct the program. | §16.5, p.445 |
| 540 | M22x variable cannot be read | A format code's corresponding #variable argument was invalid, or there was a machine error accessing it. Action: correct the program. | §16.5, p.445 |
| 542 | M22x character limit exceeded | The resulting formatted string after all format codes were processed was too long. Action: correct the program. | §16.5, p.445 |
| 543 | Missing L parameter | An L-code was missing. Action: correct the program. | §16.5, p.445 |
| 544 | Too many axes | More than one axis was specified with M128, or the Simultaneous Contouring feature is not enabled (without it, a maximum of three axes are allowed per G-code line). Action: specify fewer axes on the G-code line, or contact Dealer about the Simultaneous Contouring feature. | §16.5, p.445 |
| 545 | Value out of range | A parse error occurred because the value was out of range. Action: correct the value. | §16.5, p.445 |
| 547 | Move by counts not allowed | Cutter comp (G41/G42) was on when M128 was specified. Action: issue G40 (Cutter compensation off) before issuing M128. | §16.5, p.445 |
| 548 | String too long | A quoted string was too long (usually a file name longer than its allowed limit). Action: shorten the file name. | §16.5, p.445 |
| 549 | Line too long | A line in a G-/M-code program is too long (more than 1023 characters). Action: shorten the program line. | §16.5, p.445 |
| 550 | Invalid L parameter | The value associated with the L-code is invalid. Action: give the correct value. | §16.5, p.445 |
| 551 | Invalid R value | The value associated with the R-code is invalid. Action: give the correct value. | §16.5, p.445 |
| 552 | File encryption error | Error while parsing an encrypted G-code file. | §16.5, p.446 |
| 557 | License Import Error | Imported license doesn't match serial number or software version. Action: check that the correct license is being imported; contact dealer. | §16.5, p.446 |

> Code 526's Action on p.444 prints `See M224 and G225`; the manual is quoted as printed,
> without asserting whether `G225` should instead read `M225`.

## §16.6 Cutter Compensation Errors (§16.6, p.446)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 601 | Error: no compensation in MDI | G41 or G42 was entered while in MDI; MDI is not canceled, but cutter compensation does not go into effect (the remainder of the line is processed). Action: do not use G41 or G42 in MDI. | §16.6, p.446 |
| 603 | Arc as first uncomp. move on line NNNNN | An arc was specified as the first move after the end of compensation (G40); job cancelled. Action: the first move after G40 must be a linear move. | §16.6, p.446 |
| 604 | Plane must be XY on line NNNNN | Cutter compensation was started with the YZ or ZX plane selected; job cancelled. Action: remove cutter compensation for YZ or ZX plane moves; this option is not available. | §16.6, p.446 |
| 605 | Canned cycle not allowed on line NNNNN | A canned cycle was attempted during compensation; job cancelled. Action: do not use cutter compensation with canned cycles. | §16.6, p.446 |
| 606 | G53 not allowed on line NNNNN | A G53 was attempted during compensation; job cancelled. Action: choose a different work coordinate. | §16.6, p.446 |
| 607 | Set home not allowed on line NNNNN | A M26 was attempted during compensation; job cancelled. Action: do not use M26 with cutter compensation. | §16.6, p.446 |
| 608 | Ref. point move not allowed on line NNNNN | A G28, G29, or G30 was attempted during compensation; job cancelled. Action: do not use return points with cutter compensation. | §16.6, p.446 |

## §16.7 Parameter Setting Errors (§16.7, p.446)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 701 | G10 error: no R-value on line NNNNN | G10 used with no R-value; job cancelled. Action: input an R-value. | §16.7, p.446 |
| 702 | G10 error: invalid D on line NNNNN | Job cancelled; D0 cannot be set (it is always zero). Action: change D to a valid value. | §16.7, p.446 |
| 703 | G10 error: invalid H on line NNNNN | G10 H0 Rxx was specified; job canceled (H0 cannot be set; it is always zero). Action: change H to a valid value. | §16.7, p.446 |
| 704 | G10 error: invalid P on line NNNNN | A G10 was used with an unknown P value; job cancelled. Action: change P to a valid value. | §16.7, p.446 |
| 705 | G10 error: No D, H, or P on line NNNNN | A G10 was used without a D, H, or P to assign a value; job cancelled. Action: add a valid D, H, or P value. | §16.7, p.446 |

## §16.8 Canned Cycle Errors (§16.8, p.447)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 801 | Error: No R-point on line NNNNN | No R-value was specified; job cancelled. Action: add an R-point. | §16.8, p.447 |
| 802 | Error: Q = 0 on line NNNNN | A Q-value of 0 was specified (Q is used for G73 and G83 only); job cancelled. Action: insert a non-zero Q-value. | §16.8, p.447 |
| 803 | Error: No Z-point on line NNNNN | No Z-value was specified for the canned cycle; job cancelled. Action: add a Z-value. | §16.8, p.447 |
| 804 | Error: Ggg invalid on line NNNNN (gg = 76, 86, 87, 88) | An unimplemented canned cycle was requested; job cancelled. Action: change to a valid G-code. | §16.8, p.447 |
| 805 | Error: No Q-value on line NNNNN | A Q-value was not specified for G73 or G83; job cancelled. Action: insert a Q-value. | §16.8, p.447 |
| 806 | Error: No P-value on line NNNNN | A P-value (dwell time) was not specified for G82 or G89; job cancelled. Action: add a P-value. | §16.8, p.447 |
| 807 | Error: Cannot execute G__ when axis B is rotated | On an Articulated Head machine with the TWCS feature enabled, a non-compound canned cycle (G73, G74, G76, G80, G81, G82, G83, G84, G85, or G89) was issued on a WCS set to TWCS=No while the spindle head was tilted (rotary B axis not at 0); job cancelled. Action: either move B to 0 or issue the compound canned cycle version of the erroneous G-code, such as G173, G174, G176, G181, G182, G183, G184, G185, or G189. | §16.8, p.447 |

## §16.9 Miscellaneous Errors/Messages (§16.9, p.447-449)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 901 | Ref. point invalid on line NNNNN | A G30 with an invalid P-value (must be 1 or 2) was issued; job cancelled. Action: change the P-value to 1 or 2. | §16.9, p.447 |
| 902 | No prior G28 or G30 on line NNNNN | A G29 with no preceding G28 or G30 was issued. Action: add a G29 or G30. | §16.9, p.447 |
| 903 | Warning: No coordinates for G92 on line NNNNN | G92 with no axis coordinates to set; the remainder of the line is processed and the job continues. Action: add coordinates. | §16.9, p.447 |
| 905 | Warning: 0 radius arc on line NNNNN | An arc move was specified with a zero radius; the move is done as a linear move and the job continues. Action: specify a radius. | §16.9, p.447 |
| 906 | Warning: unknown arc on line NNNNN | Position of an arc move could not be determined from the parameters (e.g. G91 G2 X0 Y0 R1); the move is done as a linear move and the job continues. Action: correct program. | §16.9, p.447 |
| 907 | _ axis travel exceeded on line NNNNN | The software travel limit would be exceeded by the requested move; job cancelled. Action: check program, part zero, or tool offset. | §16.9, p.447 |
| 909 | Program too long: job canceled | Attempt to run a job over 1MB in length without the unlimited program size option; job cancelled. Action: contact Dealer or break up program. | §16.9, p.447 |
| 910 | No subroutines in MDI | Specified O9100-O9999 in MDI, which would begin an embedded subprogram; MDI cancelled. Action: insert subroutines into MDI. | §16.9, p.447 |
| 911 | Illegal recursion | Attempt to execute a subprogram or macro that calls itself, directly or indirectly; job cancelled. Action: call correct subprogram. | §16.9, p.448 |
| 913 | Could not open file filename.ext | Attempt to call a subprogram or macro, but the subprogram file does not exist; job cancelled. Action: make sure the file name is correct and is in the ncfiles directory. | §16.9, p.448 |
| 915 | DSP window retry sN fN rN | DSP window checking failed; the move is repeated unless the maximum retries have been reached (s = number of successes, f = number of failures, r = number of times the maximum retry value has been reached). | §16.9, p.448 |
| 916 | Unexpected probe contact | Probe tripped when a cycle did not expect contact. | §16.9, p.448 |
| 917 | Invalid tilt lookup table | The tilt lookup table file (tilt.tab) has an invalid format or was not found. | §16.9, p.448 |
| 918 | Probe unable to detect surface | Probe travelled the maximum distance without contact, DSP window checking failed, or probe repeatability failed. | §16.9, p.448 |
| 919 | DSP window failed maximum retries | DSP probe reached the maximum retry limit without a successful window. | §16.9, p.448 |
| 920 | Unable to clear obstacle | Probing cycle failed to clear an obstacle. | §16.9, p.448 |
| 921 | Unable to determine corner | Probing cycle failed to find a corner (inside and outside corner). | §16.9, p.448 |
| 922 | Out of memory | Problem allocating memory. | §16.9, p.448 |
| 923 | Error: Z-home not set | Z-home is not set. Action: set Z-home. | §16.9, p.448 |
| 924 | File read error | Problem reading the job file; occurs if the file opened successfully but there was an error while reading it. | §16.9, p.448 |
| 925 | Error reading job file | Same as code 924, but at a different place in the code. | §16.9, p.448 |
| 926 | Failed to locate job continuation position | Job continuation from the Run Menu failed. Action: do a Run/Search. | §16.9, p.448 |
| 927 | Too many subprogram calls | Nesting level of subprograms is too high (a subprogram calls another, which calls another, and so on). Action: reduce the nesting level of subprograms. | §16.9, p.448 |
| 928 | Error Loading Log Configuration file. . . Using defaults | There was an error while loading the log configuration file; default settings will be used. | §16.9, p.448 |
| 929 | Log Level set to __ | The logging level parameter (140) has been changed. | §16.9, p.448 |
| 930 | Log Level Configuration file not found. . . Creating new configuration. | The log level configuration file was not found; a default file will be created. | §16.9, p.448 |
| 931 | Error during transformed move to home | A transformed move to home (M25) command attempted to move below the G28 Z-position. | §16.9, p.448 |
| 932 | Error during Tool Check | A general error condition occurred when the Tool Check key was pressed. | §16.9, p.449 |
| 933 | Log file initialized | There was an error in trimming the log file or it did not exist, so a new log file has been created. | §16.9, p.449 |
| 934 | Warning: Excess precision truncated | A CNC program used axis positioning precision greater than what is displayed, so the actual commanded positions are truncated; happens when the Simultaneous Contouring feature is not enabled. Action: contact Dealer for information about obtaining the Simultaneous Contouring feature. | §16.9, p.449 |
| 935 | _ axis (#) scale disabled | A scale is enabled for this axis but compensation was disabled. Scale compensation is disabled at initial power up, configuration changes, and during homing moves. Action: home the machine. | §16.9, p.449 |
| 935 | Probe failed reset retries | Probe failed to reset after three tries; the probing operation may have been started too close to the surface. Action: move the probe further away from the surface and do the probing operation again; if this continues to fail persistently, call dealer. | §16.9, p.449 |
| 936 | _ axis (#) scale enabled | A scale is enabled for this axis and compensation was enabled; happens after homing the axis. Action: Not Applicable. | §16.9, p.449 |
| 936 | Probe failed to reset | Probe failed to reset; the probing operation may have been started too close to the surface. Action: move probe further away from surface and do the probing operation again; if this continues to fail persistently, call dealer. | §16.9, p.449 |
| 944 | MPU requested resend | The MPU requested a resend. (Status Message.) | §16.9, p.449 |
| 945 | PC requested resend | The PC requested a resend. (Status Message.) | §16.9, p.449 |
| 946 | PC resending | The PC is resending. (Status Message.) | §16.9, p.449 |
| 947 | PC received data out of order | The PC needed to reorder data received from the MPU. (Status Message.) | §16.9, p.449 |
| 948 | PC packet error | The PC received bad data from the MPU and will try to recover by requesting a resend. (Status Message.) | §16.9, p.449 |
| 949 | Drive map does not match hardware | One or more of the drive mapping Parameters 300–307 is misconfigured. Action: contact Dealer. | §16.9, p.449 |

> The manual reuses codes 935 and 936 for two different messages each, both within §16.9
> (p.449, rows above). Neither reuse is resolved here; both are kept as printed.

## §16.10 Scaling/Mirroring Errors (§16.10, p.449-450)

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 1001 | Invalid scaling parameter on line NNNNN | Invalid parameter specified (I, J, K, P); job cancelled. Action: remove or change invalid parameter. | §16.10, p.449 |
| 1002 | Invalid scaling center on line NNNNN | Invalid parameter specified (X, Y, Z); job cancelled. Action: remove or change invalid parameter. | §16.10, p.449 |
| 1003 | G-code not allowed when scaling on line NNNNN | G28/G29/G30/G92 is not allowed when scaling or mirroring is turned on; job cancelled. Action: move G-code to appropriate line. | §16.10, p.450 |
| 1004 | Turn scaling off before rescaling | Tried to rescale while scaling is turned on; job cancelled. Action: turn scaling off, then rescale. | §16.10, p.450 |
| 1005 | Cannot scale arcs with different scale factors | Scaling factors of the arc axes are different; job cancelled. Action: correct scaling factors, or separate scaling operations. | §16.10, p.450 |
| 1100–1199 | (range, no single message text) | Custom messages defined in `cncxmsg.txt`; contact your dealer with questions about a particular message. This style of message should be replaced with the `plcmsg.txt` format on MPU11 systems. | §16.10, p.450 |

## §16.11 Configuration Modification Messages (§16.11, p.450)

This table has no Action column in the manual.

| Code | Message | Meaning | Ref |
|---|---|---|---|
| 111 | __ modified: __ → __ | An axis configuration parameter was modified. | §16.11, p.450 |
| 444 | __ modified: __ → __ | A servo drive configuration parameter was modified. | §16.11, p.450 |
| 555 | __ modified: __ → __ | A PID configuration parameter was modified. | §16.11, p.450 |
| 556 | Axis converted: → __ | A PID configuration parameter was converted. | §16.11, p.450 |
| 777 | __ modified: __ → __ | An axis configuration parameter was modified. | §16.11, p.450 |
| 888 | G30 Z modified: → __ | Z-coordinate of Secondary Reference Point was modified. | §16.11, p.450 |
| 999 | Parm # modified: → __ | A machine parameter was modified. | §16.11, p.450 |
