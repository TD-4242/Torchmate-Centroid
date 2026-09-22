# Machine parameter index

Source: Router Manual §15.7 (p.320-396). Parameters can also be set with G10 or #variable
assignment, and many are set by the Acorn Wizard (§15.7, p.320).

## Bit-mapped parameters

A bit-mapped parameter is stored as a single number representing a 16-bit value, where each
bit's Value = 2^bit (bit 0 = 1, bit 1 = 2, bit 2 = 4, ... bit 15 = 32768). To enable a set of
bits, add their values together and enter the sum into the parameter; to disable a bit,
subtract its value. For example, enabling Parameter 10's bits 0, 3, and 5 (values 1, 8, and
32) gives a total of 41 (§15.7.1, p.321-322).

| Parameter | Name | Summary | Ref |
|---|---|---|---|
| 0 | E-Stop PLC Bit | Sets the PLC bit the physical E-Stop switch is wired to. | §15.7.2, p.331 |
| 1 | Machine and Jog key orientation | Bit-mapped; see manual | §15.7.3, p.332 |
| 2 | G-code Interpretation Control and Slaving Rotary axis feed rate | Bit-mapped; see manual | §15.7.4, p.332 |
| 3 | Modal Tool and Height Offset Control | Bit-mapped; see manual | §15.7.5, p.333 |
| 4 | Remote File Loading Flag & Advanced File Ops | Bit-mapped; see manual | §15.7.6, p.333 |
| 5 | Machine Home/Startup Setup | Bit-mapped; see manual | §15.7.7, p.333 |
| 6 | Auto Tool Changer Installed | Tells the control whether an ATC is installed, affecting M6 and Tool Offset Setup behavior. | §15.7.8, p.333 |
| 7 | Display Colors | Selects the color scheme used for displays. | §15.7.9, p.334 |
| 8 | Available Coolant Systems | Tells Intercon which coolant systems are available on the machine. | §15.7.10, p.334 |
| 9 | Display Language | Selects the language used for menus, prompts, and error messages. | §15.7.11, p.334 |
| 10 | Macro M-function Control/Probe Stop Handling | Bit-mapped; see manual | §15.7.12, p.334 |
| 11 | DP4 PLC Input Number and Contact State | Sets the PLC input number and contact state used by the DP4 touch probe. | §15.7.13, p.335 |
| 12 | Touch Probe Tool Number | Sets the tool number used to look up the touch probe's offset in the Tool Offset Library. | §15.7.14, p.335 |
| 13 | Recovery Distance | Sets how far the probe backs off a surface before returning to take a reading during probing cycles. | §15.7.15, p.335 |
| 14 | Fast Probing Rate | Sets the feed rate used for probe positioning moves and initial surface detection. | §15.7.16, p.335 |
| 15 | Slow Probing Rate | Sets the feed rate used for the final probe measurement move. | §15.7.17, p.336 |
| 16 | Maximum Probing Distance | Sets the maximum distance the Boss and Web probing cycles search for a surface. | §15.7.18, p.336 |
| 17 | Detector Location Return Point | Sets the reference return point above a permanently mounted TT-1 tool detector for the Auto tool offset function. | §15.7.19, p.336 |
| 18 | PLC Input Spindle Inhibit Parameter | Sets the PLC input wired to the Spindle Inhibit probe or touch-off block. | §15.7.20, p.336 |
| 19 | MPG modes | Bit-mapped; see manual | §15.7.21, p.337 |
| 20–30 (also 132–135, 236–239) | Motor Temperature Estimation | Sets the ambient, overheating, and cancellation temperatures plus per-axis heating/cooling coefficients for motor temperature estimation. | §15.7.22, p.337 |
| 31 | Legacy SPIN232 Com Port | Sets the COM port CNC12 uses to send spindle commands to a legacy SPIN232. | §15.7.23, p.338 |
| 32 | Autonomous Digitizing Offset Files | Bit-mapped; see manual | §15.7.24, p.338 |
| 33 | Spindle Motor Gear Ratio | Sets the gear or belt ratio between the spindle motor and chuck in high gear range. | §15.7.25, p.339 |
| 34 | Spindle Encoder Counts/Rev | Sets the counts-per-revolution and count direction for the spindle encoder. | §15.7.26, p.339 |
| 35 | Spindle Encoder Axis Number | Sets the axis number the spindle encoder is assigned to for spindle-slaved movements. | §15.7.27, p.339 |
| 36 | Rigid Tapping Enable/Disable | Bit-mapped; see manual | §15.7.28, p.339 |
| 37 | Spindle Deceleration Time (Rigid Tapping Parameter) | Sets the spindle deceleration time used with Rigid Tapping before the spindle switches direction. | §15.7.29, p.340 |
| 38 | Multi-axis Max Feed Rate | Limits the feed rate along all commanded move vectors for multi-axis moves. | §15.7.30, p.340 |
| 39 | Feed Rate Override Percentage Limit | Limits the upper end of the Feed Rate Override Knob percentage. | §15.7.31, p.340 |
| 40 | Basic Jog Increment | Sets the basic jog increment for linear axes used with the x1/x10/x100 jog keys. | §15.7.32, p.340 |
| 41 | Rotary Axis Jog Increment | Sets the jog increment for rotary axes used with the x1/x10/x100 jog keys. | §15.7.33, p.340 |
| 42 | Password for Configuration Menus | Sets the password required for full access to the configuration menus. | §15.7.34, p.340 |
| 43 | Automatic tool measurement options | Bit-mapped; see manual | §15.7.35, p.341 |
| 44 | TT1 PLC input number | Sets the PLC input number the TT1 tool detector is wired into. | §15.7.36, p.341 |
| 45 | WCS Lockout | Bit-mapped; see manual | §15.7.37, p.341 |
| 46 | Active G-codes Display | Controls where and whether the currently active G-codes are displayed. | §15.7.38, p.342 |
| 48 | Grid Digitize Patch Playback Z rapid clearance amount | Sets the extra Z-clearance above the original surface level used when a Grid Digitize patch is played back. | §15.7.39, p.342 |
| 49–51 | Small Arc Feed Rate Limiting | Sets the feed rate limits for small-radius arc moves. | §15.7.40, p.342 |
| 56 | Feedrate Override Display Properties / Inverse Time Interpolation | Bit-mapped; see manual | §15.7.41, p.343 |
| 57 | Use Generic Load Meter Data from PLC | Sets which axes read load meter data from PLC system variables instead of PID output. | §15.7.42, p.344 |
| 61–62 | Stall Detection Parameters | Sets the current and time thresholds used to detect low- and high-power axis stall conditions. | §15.7.43, p.344 |
| 63 | High Power Idle PID Multiplier | Sets a constant used to detect abnormal motor resistance when an axis is idle and holding position. | §15.7.44, p.344 |
| 64 | Fourth/Fifth-axis Pairing | Removed in CNC12 v5.40.0 and replaced by Parameters 551-558 (see §15.7.253). | §15.7.45, p.344 |
| 65–67 | Spindle Gear Ratios | Sets the gear ratio of each lower spindle speed range relative to high range on a multi-range spindle drive. | §15.7.46, p.345 |
| 68 | Minimum Rigid Tapping Spindle Speed (Rigid Tapping Parameter) | Sets the spindle speed the control slows to near the end of a Rigid Tapping cycle. | §15.7.47, p.345 |
| 69 | Duration For Minimum Spindle Speed (Rigid Tapping Parameter) | Sets how long the control holds the minimum spindle speed during a Rigid Tapping cycle. | §15.7.48, p.345 |
| 70 | Offset Library Inc/Decrement Amount | Sets the increment and decrement amounts used in the Offset Library. | §15.7.49, p.346 |
| 71 | Part Setup Detector Height | Sets the tool detector height so Part Setup's Auto feature can use the TT1 detector instead of the probe. | §15.7.50, p.346 |
| 72 | Data M-function Options | Bit-mapped; see manual | §15.7.51, p.346 |
| 73 | Peck Drill Retract Amount (Canned Cycle Parameter) | Sets the retract amount used during a G73 peck drilling cycle. | §15.7.52, p.346 |
| 74 | M-function executed at bottom of tapping cycle (Canned Cycle Parameter) | Sets the M-function executed at the bottom of a G84 tapping cycle or after a G74 counter-tapping cycle. | §15.7.53, p.346 |
| 75 | Summing Control | Controls which axes are summed together, which position type is summed, and which axis bears the summed effect. | §15.7.54, p.346 |
| 76 | Manual Input Unrestricted Distance | Sets the maximum distance from the summed axis start of travel where manual movement is allowed without a fault, for use with Z-axis summing. | §15.7.55, p.347 |
| 77 | Manual Input Movement Tolerance | Sets the manual movement tolerance allowed on a quill-locking mechanism while a job is running. | §15.7.56, p.348 |
| 78 | Spindle Speed Display and Operations | Bit-mapped; see manual | §15.7.57, p.348 |
| 79 | Paired Axes Re-sync Delay Time (milliseconds) | Sets the delay before the control re-syncs paired axes, or prompts Cycle Start if negative. | §15.7.58, p.348 |
| 80 | Voltage Brake Message Frequency | Sets how many times the voltage-brake message must occur before it is shown in the message window and log. | §15.7.59, p.348 |
| 81 | Air Drill M-function (Canned Cycle Parameter) | Sets the M-function called in place of Z-axis movement during a G81 drilling cycle. | §15.7.60, p.349 |
| 82 | Spindle Drift Adjustment (Rigid Tapping Parameter) | Sets the coast-to-stop angle used when the spindle turns off at the Rigid Tapping minimum speed. | §15.7.61, p.349 |
| 83 | Deep Hole Clearance Amount (Canned Cycle Parameter) | Sets the clearance amount used during a G83 deep hole drilling cycle. | §15.7.62, p.349 |
| 84 | M-function executed at return to initial point of tapping cycle (Canned Cycle Parameter) | Sets the M-function executed after a G84 tapping cycle returns to its initial point, or at the bottom of a G74 counter-tapping cycle. | §15.7.63, p.349 |
| 85 | “Door Open” Interlock PLC bit | Sets the PLC bit and polarity a system integrator uses to limit movement to slow jog rate when a safety door is open. | §15.7.64, p.349 |
| 86 | Rapid/Linear vector rate limit | Limits the number of rapid and/or linear moves per second, for testing purposes. | §15.7.65, p.349 |
| 87–90 (and also 252–255) | Autotune Ka Performance parameters for axes 1, 2, 3, 4 | Sets the Autotune kA acceleration performance values for axes 1-4 (and 5-8 via a second parameter range). | §15.7.66, p.350 |
| 91–94 (and also 166–169) | Axis Properties for axes 1, 2, 3, 4 | Bit-mapped; see manual | §15.7.67, p.350 |
| 95–98 (and also 156–159) | Autotune Move Distance / Auto Delay Calculation Move Distance for axes 1, 2, 3, 4 | Sets the maximum per-axis move distance used by Autotune or Auto Delay Calculation for axes 1-4 (and 5-8 via a second parameter range). | §15.7.68, p.351 |
| 99 | Cutter Compensation Look-ahead | Sets how many line or arc events the G-code interpreter looks ahead when Cutter Compensation is active. | §15.7.69, p.352 |
| 100 | Intercon comment generation | Turns Intercon comment generation on or off. | §15.7.70, p.352 |
| 101 | Intercon clearance amount | Sets the Intercon clearance amount. | §15.7.71, p.352 |
| 102 | Intercon spindle coolant delay | Sets the Intercon spindle coolant delay. | §15.7.72, p.352 |
| 103 | Intercon corner feed rate override | Sets the Intercon corner feed rate override. | §15.7.73, p.352 |
| 104 | Intercon modal line parameters | Turns Intercon's modal linear parameter display on or off. | §15.7.74, p.352 |
| 105 | Intercon modal arc parameters | Turns Intercon's modal arc parameter display on or off. | §15.7.75, p.352 |
| 106 | Intercon modal drilling cycle parameters | Turns Intercon's modal drilling cycle parameter display on or off. | §15.7.76, p.352 |
| 107 | Intercon chamfer blend | Configures Intercon's chamfer blend option. | §15.7.77, p.352 |
| 108 | Intercon polar display | Turns Intercon's polar display on or off. | §15.7.78, p.352 |
| 109 | Intercon modal display | Turns Intercon's modal display on or off. | §15.7.79, p.352 |
| 110 | Wizard Password | Enables a password prompt when opening the Wizard, using the password from Parameter 42. | §15.7.80, p.353 |
| 111 | Intercon no spindle stop during tool change | Tells Intercon whether to stop the spindle during a tool change. | §15.7.81, p.353 |
| 112 | Intercon no coolant stop during tool change | Tells Intercon whether to stop the coolant during a tool change. | §15.7.82, p.353 |
| 113 | Hide Features Parameters | Bit-mapped; see manual | §15.7.83, p.353 |
| 114 | Intercon use G28 during tool change | Tells Intercon whether to suppress G28 calls during a tool change. | §15.7.84, p.353 |
| 115 | Intercon Help | Toggles automatic display of Intercon help windows. | §15.7.85, p.353 |
| 116 | A-axis Y-coordinate | Sets the Y-coordinate of the A-axis center of rotation for Dig to CAD export. | §15.7.86, p.353 |
| 117 | A-axis Z-coordinate | Sets the Z-coordinate of the A-axis center of rotation for Dig to CAD export. | §15.7.87, p.353 |
| 118 | B-axis X-coordinate | Sets the X-coordinate of the B-axis center of rotation for Dig to CAD export. | §15.7.88, p.354 |
| 119 | B-axis Z-coordinate | Sets the Z-coordinate of the B-axis center of rotation for Dig to CAD export. | §15.7.89, p.354 |
| 120 | Probe Stuck Clearance Amount | Sets the clearance distance used to try to recover from a stuck probe condition. | §15.7.90, p.354 |
| 121 | Grid digitize prediction minimum Z-pullback | Sets the minimum Z-pullback distance used when Grid Digitize predicts a part surface slope. | §15.7.91, p.354 |
| 122 | Grid digitizing deadband move distance | Sets the deadband distance used for Grid Digitize clearance move calculations. | §15.7.92, p.354 |
| 123 | Radial Clearance Move | Sets the positioning move made when a Radial Digitizing probe gets unexpected contact while traversing toward the center point. | §15.7.93, p.354 |
| 128 | Dry Run PLC Bit | Sets the PLC bit checked at job start to determine whether Dry Run mode is in effect. | §15.7.94, p.355 |
| 129 | Dry Run Feed Rate | Sets the feed rate used in Dry Run mode. | §15.7.95, p.355 |
| 130–131 | 3rd /4th axis on/off selection | Sets the axis label and disabled-state display for the 3rd and 4th axes. | §15.7.96, p.355 |
| 132–135 | Motor Heating Coefficients for axes 5–8 | Sets the motor heating coefficients for axes 5-8; see Parameters 20-30. | §15.7.97, p.356 |
| 136 | G76 Fine Bore Retract Angle | Sets the retract angle for a G76 fine bore cycle. | §15.7.98, p.356 |
| 137 | Load Meter Filter Size | Sets the number of samples averaged for the load meter display. | §15.7.99, p.356 |
| 138 | DRO Encoder Deadband | Sets the deadband amount used by the anti-flicker DRO filter. | §15.7.100, p.356 |
| 139 | Special Dwell between Moves | Sets a dwell time inserted between moves, similar to G61, with exceptions for certain move types. | §15.7.101, p.356 |
| 140 | Message log priority level | Sets the minimum priority level of messages written to the message log. | §15.7.102, p.356 |
| 141 | Maximum message log lines | Sets the maximum number of lines retained in the message log. | §15.7.103, p.357 |
| 142 | Message log trim amount | Sets how many extra lines above the minimum accumulate before the message log is trimmed. | §15.7.104, p.357 |
| 143 | DRO properties (load meter, DTG) | Bit-mapped; see manual | §15.7.105, p.357 |
| 144 | Comparison rounding | Sets the decimal-place precision used for comparison operators in expressions. | §15.7.106, p.357 |
| 145 | Advanced macro properties (fast branching) | Turns fast branching on or off for macro program-block searches. | §15.7.107, p.358 |
| 146 | Feed hold threshold for feed rate override | Sets the feed rate override percentage below which feed hold engages. | §15.7.108, p.358 |
| 147 | Number of Messages in Operator Message Window | Sets how many status messages are remembered in the Operator Message Window. | §15.7.109, p.358 |
| 148 | Miscellaneous Jogging Options | Bit-mapped; see manual | §15.7.110, p.358 |
| 149 | Spindle Speed Threshold | Sets the spindle speed threshold percentage used by the spindle-slaved feed rate and up-to-speed functions enabled by Parameter 78. | §15.7.111, p.359 |
| 150 | Backplot Graphics display options | Bit-mapped; see manual | §15.7.112, p.359 |
| 151 | Repeatability tolerance for probing and radial digitizing | Sets the repeatability tolerance for probing and radial digitizing, enabling a second measurement-per-point check. | §15.7.113, p.359 |
| 153 | Probe Protection | Enables Probe Protection, which stops motion if the probe trips during specified G-codes and M-codes. | §15.7.114, p.359 |
| 154 | Touch Screen Options | Displays a half-width ESC key in menus to support touchscreen input. | §15.7.115, p.360 |
| 155 | Probe Type | Sets the type of probe being used. | §15.7.116, p.360 |
| 156–159 | Autotune Move Distance / Auto Delay Calculation Move Distance for axes 5, 6, 7, 8 | Sets the Autotune/Auto Delay Calculation move distance for axes 5-8; see Parameters 95-98. | §15.7.117, p.360 |
| 160 | Enhanced ATC | Enables and sets the type (carousel or random) of enhanced Automatic Tool Changer options. | §15.7.118, p.360 |
| 161 | ATC Maximum Tool Bins | Sets the number of tool changer bins used with the enhanced ATC option. | §15.7.119, p.361 |
| 162 | Intercon M6 Initial M-Code | Sets the M-code Intercon posts at the start of an M6 tool change. | §15.7.120, p.361 |
| 163 | Gang Tooling | Enables the tool library to select front-mount or back-mount tool approach for gang tooling. | §15.7.121, p.361 |
| 164 | ATC Feature | Enables the ATC Reset feature for ATC3 PLC programs. | §15.7.122, p.361 |
| 165 | Acceleration/Deceleration Options | Bit-mapped; see manual | §15.7.123, p.361 |
| 166–169 | Axis Properties for axes 5, 6, 7, 8 | Sets the axis properties for axes 5-8; see Parameters 91-94. | §15.7.124, p.362 |
| 170–179 | PLC Parameter | Reserves a block of parameters for data sent to the PLC, with Parameters 177-179 standardized for specific applications. | §15.7.125, p.362 |
| 170 | Enable Keyboard Jogging and Set Feed Rate Override Control | Bit-mapped; see manual | §15.7.126, p.362 |
| 178 | PLC I/O configuration (PLC program specific) | Bit-mapped; see manual | §15.7.127, p.362 |
| 179 | Lube Pump Operation | Sets lube pump minutes/seconds timing. | §15.7.128, p.363 |
| 180 | Clear Home Switch Distance | Sets the distance moved before an error is raised while clearing the home switch during homing. | §15.7.129, p.363 |
| 181 | Clear Index Pulse Distance | Sets the allowed travel beyond one motor revolution while searching for an index pulse during reference mark homing. | §15.7.130, p.363 |
| 186 | Probe Stuck retry disable | Disables the control's automatic retry when a probe is detected in a stuck condition. | §15.7.131, p.363 |
| 187 | Hard Stop Homing | Sets the motor current used while homing off of hard stops. | §15.7.132, p.363 |
| 188–199 | Aux Key Functions | Assigns a function to each of Aux Keys 1-12. | §15.7.133, p.364 |
| 200–207 | OPTIC 4 Tach Volts Per 1000 RPM | Sets the tachymeter output volts per 1000 RPM on Optic4 boards for axes 1-8. | §15.7.134, p.364 |
| 208–215 | MPU-based Lash/Screw Compensation Acceleration Coefficient | Sets the acceleration coefficient for MPU-based Lash/Screw Compensation for axes 1-8. | §15.7.135, p.364 |
| 216 | PC-based Lash Compensation on/off | Selects which Lash Compensation algorithm is used (PC-based vs. default). | §15.7.136, p.365 |
| 217 | PC-based Screw Compensation on/off | Selects which Screw Compensation algorithm is used (PC-based vs. default). | §15.7.137, p.365 |
| 218 | USB MPG Options | Sets whether a Wireless USB MPG is connected and which driver/type CNC12 and the PLC use for it. | §15.7.138, p.365 |
| 220–231 | Smoothing Parameters | Configures the Smoothing feature used during feed-per-minute moves, including the on/off switch. | §15.7.139, p.365 |
| 236–239 | Motor Cooling Coefficients for axes 5–8 | Sets the motor cooling coefficients for axes 5-8; see Parameters 20-30. | §15.7.140, p.366 |
| 240 | Rigid Tapping Accel Rate Distance | Sets the acceleration rate distance used for Rigid Tapping; -1 disables it for servo motors only. | §15.7.141, p.366 |
| 241 | Rigid Tapping Rotational Step Size (Degrees) | Sets the rotational step size used to sync pitch with the spindle in Rigid Tapping. | §15.7.142, p.366 |
| 242 | Minimum Angle Threshold for application of Accel/decel in Threading moves | Sets the minimum angle threshold for applying accel/decel during G32 threading moves. | §15.7.143, p.366 |
| 243 | Threading Control | Bit-mapped; see manual | §15.7.144, p.366 |
| 244 | Tool Touch-off device PLC input number | Sets the PLC input number the Tool Touch-off device is wired into. | §15.7.145, p.367 |
| 245 | G71, G72, G74, G75, G76 D/P/Q “implied float” re-interpretation threshold for Inch units | Sets the implied-float re-interpretation threshold for G71/G72/G74/G75/G76 D/P/Q values in inch units. | §15.7.146, p.367 |
| 246 | G71, G72, G74, G75, G76 D/P/Q “implied float” re-interpretation threshold for MM units | Sets the implied-float re-interpretation threshold for G71/G72/G74/G75/G76 D/P/Q values in millimeter units. | §15.7.147, p.367 |
| 247 | G70 Multiple Pass Behavior Suppression | Selects single-pass or multi-pass compatibility behavior for the G70 finishing cycle. | §15.7.148, p.368 |
| 248 | Tool Wear Adjustment magnitude limit | Sets the magnitude limit allowed in the Tool Wear Adjustment menu. | §15.7.149, p.368 |
| 252–255 | Autotune Ka Performance parameters for axes 5, 6, 7, 8 | Sets the Autotune kA acceleration performance values for axes 5-8; see Parameters 87-90. | §15.7.150, p.368 |
| 256 | Drive Mode | Sets the drive mode, which also controls availability and behavior of the PID Menu's Tune key. | §15.7.151, p.368 |
| 257 | TT1 connection detection PLC input | Sets the PLC input for TT1 connection detection, used with the Spindle Inhibit parameter. | §15.7.152, p.369 |
| 258 | Velocity/Torque Mode override in Precision mode | Bit-mapped; see manual | §15.7.153, p.369 |
| 259 | Manual Axis Designation | Bit-mapped; see manual | §15.7.154, p.369 |
| 260 | Accelerated Graphics Backplot | Controls the interface presented by the Accelerated Graphics Backplot feature. | §15.7.155, p.369 |
| 261 | Precision Mode Standoff Tolerance Percentage | Sets the encoder-count percentage threshold that must be exceeded before Precision Mode standoff correction is made. | §15.7.156, p.369 |
| 262 | Precision Mode Standoff Delay Time | Sets how long an axis must stay at rest before a Precision Mode standoff correction is made. | §15.7.157, p.369 |
| 263 | DRO Display Precision | Sets the number of decimal places shown on the DRO display. | §15.7.158, p.369 |
| 264 | Rapid Override | Bit-mapped; see manual | §15.7.159, p.370 |
| 267 | Comm Error Threshold | Sets how often communication error messages must occur before a dialog box notifies the user. | §15.7.160, p.370 |
| 268 | Fixed Rotary Table Position | Determines whether graphing a rotary job accounts for the center line coordinate parameters (116-119). | §15.7.161, p.371 |
| 269 | Rotary Center Line Threshold | Sets the maximum allowed difference between the rotary WCS and the center line coordinates. | §15.7.162, p.371 |
| 270–271 | XY Skew Correction | Sets XY skew correction values to correct for a non-perpendicular X and Y axis; 0 disables it. | §15.7.163, p.371 |
| 278 | Spindle Speed Display Precision | Sets the number of decimal digits shown on the Spindle Speed display. | §15.7.164, p.372 |
| 281 | Tool Touch-off Device X stylus size | Sets the Tool Touch-off Device's X stylus size. | §15.7.165, p.372 |
| 282 | Tool Touch-off Device Z stylus size | Sets the Tool Touch-off Device's Z stylus size. | §15.7.166, p.372 |
| 283 | Auto Tool Touch-off safety clearance | Sets the safety clearance used by the Auto Tool Touch-off cycles in the Tool Geometry Offset Library. | §15.7.167, p.372 |
| 284–291 | Brake Resistor Wattage for ACDC Drives 1–8 | Sets the brake resistor wattage for ACDC Drives 1-8, used to trigger a brake-wattage-exceeded warning. | §15.7.168, p.372 |
| 292–295 | Aux Key Functions 13–16 | Assigns a function to Aux Keys 13-16; see §15.7.133. | §15.7.169, p.372 |
| 299 | Report Option Bits | Sets whether the directory listing is hidden in the Report.zip text file. | §15.7.170, p.372 |
| 300–307 | Drive assignment to Axes 1–8 | Assigns a physical drive to each of axes 1-8; requires a power cycle to take effect. | §15.7.171, p.373 |
| 308–315 | Encoder assignment to Axes 1–8 | Assigns an encoder to each of axes 1-8 for motion feedback; requires a power cycle to take effect. | §15.7.172, p.373 |
| 316 | Absolute Encoder Bits | Bit-mapped; see manual | §15.7.173, p.374 |
| 317 | Single-turn Absolute Encoder Bits | Bit-mapped; see manual | §15.7.174, p.374 |
| 318 | Five-axis Configuration | Sets five-axis system configuration, including scale encoder drive assignment for an articulated fifth axis. | §15.7.175, p.374 |
| 319 | Five-axis Options | Bit-mapped; see manual | §15.7.176, p.374 |
| 321 | MPU13 DSP Probe Input | Sets the PLC input number for the DSP probe on an MPU13 (Hickory) system; has no effect on MPU11/MPU12. | §15.7.177, p.375 |
| 322 | Disable Absolute Encoder Warnings | Bit-mapped; see manual | §15.7.178, p.375 |
| 323 | MPU11 Encoder Speed Filter | Bit-mapped; see manual | §15.7.179, p.375 |
| 324–331 | Axis Boxcar size | Sets the maximum boxcar filter sample size per axis, used to smooth PID output on jumpy drives. | §15.7.180, p.375 |
| 332–335 | Encoder error suppression | Bit-mapped; see manual | §15.7.181, p.375 |
| 336–339 | Motor torque estimation for velocity mode drives | Enables and configures a more accurate axis load meter display for velocity mode drives. | §15.7.182, p.376 |
| 340–347 | Precision Mode delay (in milliseconds) for axes 1–8 | Sets per-axis delay values used to synchronize precision mode drives. | §15.7.183, p.376 |
| 348, 351, and 354 | MPG/Handwheel Encoder Input 1, 2, and 3 | Sets the encoder input for MPG/Handwheel 1, 2, and 3. | §15.7.184, p.376 |
| 349, 352, and 355 | MPG/Handwheel Detents per Revolution 1, 2, and 3 | Sets the detents-per-revolution for MPG/Handwheel 1, 2, and 3. | §15.7.185, p.377 |
| 350, 353, and 356 | MPG/Handwheel Encoder Counts per Revolution 1, 2, and 3 | Sets the encoder counts-per-revolution for MPG/Handwheel 1, 2, and 3. | §15.7.186, p.377 |
| 357–364 | Axis Drive Max RPM for Axes 1–8 | Sets the drive/motor max RPM per axis used by the PID algorithm's KV1 calculation. | §15.7.187, p.377 |
| 365 | Drive power-on delay | Sets the delay between drive power-on and the start of commanded motion. | §15.7.188, p.377 |
| 366–367 | Probe / TT1 deceleration multiplier | Sets the deceleration rate multiplier for probe and TT1 stopping moves. | §15.7.189, p.378 |
| 368 | Autonomous Digitizing Angle Adjustment | Sets the angle adjustment made to avoid shanking during Autonomous Digitizing. | §15.7.190, p.378 |
| 369 | Tool Check Max Absolute Angle | Limits the absolute B-axis angle for tool check and five-axis autonomous digitizing on articulated-head systems. | §15.7.191, p.378 |
| 374–379 | ACDC Drive Debug Log Settings | Configures ACDC drive debug logging, including which axes are logged, log size, and collection type. | §15.7.192, p.378 |
| 387–389 | Debugging Parameters | Reserved debugging parameters that should be left at 0. | §15.7.193, p.379 |
| 392–394 | DP-7 parameters | Sets parameters specific to the DP-7 probe, used only when Parameter 155 = 2. | §15.7.194, p.379 |
| 395 | Probing Setup Traverse Speed | Sets the probing traverse feed rate for macro-based probing cycles on engine block systems. | §15.7.195, p.379 |
| 396 | Probing Setup Plunge Speed | Sets the probing plunge feed rate for macro-based probing cycles on engine block systems. | §15.7.196, p.379 |
| 397 | Combustion Chamber Clearance Height | Sets the clearance height used during combustion chamber digitizing. | §15.7.197, p.379 |
| 398 | Port/block mode | Shows the current Port/Block system mode, set by the Port/Block menu and not meant to be edited manually. | §15.7.198, p.379 |
| 399 | AD1 arc chord tolerance adjustment | Sets the arc chord tolerance used to approximate arc moves when Smoothing is off. | §15.7.199, p.379 |
| 400 | Run Menu Cycle Start Enabled | Enables or disables the CYCLE START button on the Run Menu. | §15.7.200, p.380 |
| 401 | Forget Last Job Loaded | Causes the last loaded job to be forgotten and replaced with a placeholder name on startup. | §15.7.201, p.380 |
| 403 | Disable Keyboard Jogging Legend | Prevents the Keyboard Jogging Legend from launching with ALT+J. | §15.7.202, p.380 |
| 405 | Tool Touch-off Type | Selects the type of tool touch-off device being used. | §15.7.203, p.380 |
| 406 | Probe State When Tripped | Selects whether the probe reads open or closed when tripped. | §15.7.204, p.380 |
| 407 | Tool Touchoff State When Tripped | Selects whether the Tool Touch-off device reads open or closed when tripped. | §15.7.205, p.380 |
| 409 | Probe Type | Selects the type of probe connected. | §15.7.206, p.380 |
| 410 | Probe/Tool Touch-off Warning | Configures the Probe/Tool Touch-off Warning. | §15.7.207, p.380 |
| 411 | MPG Type | Selects the type of MPG connected. | §15.7.208, p.380 |
| 413 | Park macro | Runs the park.mac macro when the Park function is used from the shutdown menu. | §15.7.209, p.381 |
| 414 | WMPG sleep rate | Sets how often, in milliseconds, the Wireless MPG checks for user input while idle. | §15.7.210, p.381 |
| 415 | Ether1616 Configuration Bits | Bit-mapped; see manual | §15.7.211, p.381 |
| 416 | Spindle Inhibit | Inhibits the spindle when the spindle-inhibit detect is on. | §15.7.212, p.381 |
| 417 | Preview G-code Before Job | Turns on a G-code preview of the active job before it runs. | §15.7.213, p.381 |
| 418 | Assign Enter Key to Cycle Start | Assigns the keyboard Enter key to act as the Cycle Start button. | §15.7.214, p.381 |
| 419 | PLC Worklight and Popup Pin Output | Configures the Worklight-at-startup and Popup Pin PLC output. | §15.7.215, p.381 |
| 420 | Analog/PWM 1 Settings | Sets the Analog/PWM 1 settings; on Acorn this sets Analog Voltage only, via the Wizard and PLC. | §15.7.216, p.382 |
| 421 | Clean Fan Filter Reminder | Sets how many days pass before the Clean Fan Filter reminder message is shown; 0 disables it. | §15.7.217, p.382 |
| 422 | PLC Diagnostics Display | Selects Basic or Advanced PLC Diagnostics Display shown with ALT+I. | §15.7.218, p.382 |
| 423 | Display Scale Position on DRO | Bit-mapped; see manual | §15.7.219, p.382 |
| 424 | PWM Laser Output Delay | Sets a millisecond delay for Laser output to compensate for motor-induced timing offsets. | §15.7.220, p.383 |
| 425 | Force Rehoming After EStop Condition | Bit-mapped; see manual | §15.7.221, p.383 |
| 430 | RTG Spindle Speed RPM Display | Enables a real-time display of the current spindle speed in RPM. | §15.7.222, p.383 |
| 440 | Stopped for Jogging Continue Bit | Sets the behavior when the control is at an M0/M200/M201 stop while Parameter 10 allows M0 jogging. | §15.7.223, p.383 |
| 441–449 | MPG (1-9) Axis Selection | Sets the axis selection for MPG 1 through 9. | §15.7.224, p.384 |
| 450 | USB-BOB Feed Knob Multiplier | Sets the PLC multiplier applied to the USB-BOB Feed Knob's rate of change. | §15.7.225, p.384 |
| 451 | USB-BOB Spindle Knob Multiplier | Sets the PLC multiplier applied to the USB-BOB Spindle Knob's rate of change. | §15.7.226, p.384 |
| 452 | USB-BOB Rapid Knob Multiplier | Sets the PLC multiplier applied to the USB-BOB Rapid Knob's rate of change. | §15.7.227, p.384 |
| 454 | USB-BOB Feed Knob Custom Rate | Sets the feed rate percentage applied when the USB-BOB Feedrate Custom % input is activated. | §15.7.228, p.385 |
| 455 | USB-BOB Spindle Knob Custom Rate | Sets the spindle percentage applied when the USB-BOB Spindle Custom % input is activated. | §15.7.229, p.385 |
| 456 | USB-BOB Rapid Knob Custom Rate | Sets the rapid percentage applied when the USB-BOB Rapid Custom % input is activated. | §15.7.230, p.385 |
| 459 | Second Spindle Encoder Axis Number | Sets the axis number the second spindle's encoder is assigned to for spindle-slaved movements. | §15.7.231, p.385 |
| 460 | Second Spindle Maximum Speed | Sets the maximum speed for the second spindle. | §15.7.232, p.385 |
| 461 | Second Spindle Minimum Speed | Sets the minimum speed for the second spindle. | §15.7.233, p.385 |
| 462 | Second Spindle Encoder Counts/Revolution | Sets the counts-per-revolution for the second spindle encoder, and its count direction sign. | §15.7.234, p.386 |
| 470, 473, 476, 479, 482, and 485 | MPG/Handwheel Encoder Inputs 4, 5, 6, 7, 8, and 9 | Sets the encoder input for MPG/Handwheel 4 through 9. | §15.7.235, p.386 |
| 471, 474, 477, 480, 483, and 486 | MPG/Handwheel Detents per Revolution 4, 5, 6, 7, 8, and 9 | Sets the detents-per-revolution for MPG/Handwheel 4 through 9. | §15.7.236, p.386 |
| 472, 475, 478, 481, 484, and 487 | MPG/Handwheel Counts per Revolution 4, 5, 6, 7, 8, and 9 | Sets the encoder counts-per-revolution for MPG/Handwheel 4 through 9. | §15.7.237, p.387 |
| 495 | USB-BOB Auto Detect on Power Cycle | Automatically detects connected USB-BOB panels and sets their port number parameters on restart. | §15.7.238, p.387 |
| 496–499 | USB-BOB Panel Port Numbers | Sets the port numbers the USB-BOB panels are plugged into; can be set automatically via Parameter 495. | §15.7.239, p.387 |
| 507 | 5th -axis Pairing – Slave Axis | Sets the Acorn Axis Squaring slave axis for fifth-axis pairing, used by Wizard macros. | §15.7.240, p.387 |
| 508 | 5th -axis Pairing – Master Axis | Sets the Acorn Axis Squaring master axis for fifth-axis pairing, used by Wizard macros. | §15.7.241, p.387 |
| 540 | Touch Plate Input | Sets the PLC input number the Touch Plate device is wired into. | §15.7.242, p.388 |
| 541 | Touch Plate Detect | Sets the PLC input number the Touch Plate Detect input is wired into. | §15.7.243, p.388 |
| 542 | Touch Plate State When Tripped | Selects whether the Touch Plate reads open or closed when tripped. | §15.7.244, p.388 |
| 543 | Touch Plate Wall Height | Sets the Touch Plate wall height used in Touch Plate calculations. | §15.7.245, p.388 |
| 544 | Touch Plate Wall Thickness | Sets the Touch Plate wall thickness used in Touch Plate calculations. | §15.7.246, p.388 |
| 545 | Touch Plate Internal Diameter | Sets the Touch Plate internal diameter used in Touch Plate calculations. | §15.7.247, p.388 |
| 546 | Touch Plate Max Distance | Sets the maximum distance the tool travels searching for the Touch Plate. | §15.7.248, p.388 |
| 547 | Touch Plate Retract Distance | Sets the distance the tool retracts after first contacting the Touch Plate before making a second, more accurate approach. | §15.7.249, p.388 |
| 548 | Touch Plate Fast Rate | Sets the feed rate used for the first, fast approach to the Touch Plate. | §15.7.250, p.388 |
| 549 | Touch Plate Slow Rate | Sets the feed rate used for the second, more accurate approach to the Touch Plate. | §15.7.251, p.389 |
| 550 | Touch Plate Attributes | Bit-mapped; see manual | §15.7.252, p.389 |
| 551–558 | Axis pairing parameters | Defines which axes are paired together and to which master axis, including chained master-slave pairings (Pro/Ultimate License features). | §15.7.253, p.389 |
| 559 | Forced slaved axis display | Bit-mapped; see manual | §15.7.254, p.390 |
| 560 | Laser X-offset | Sets the Laser X-offset length. | §15.7.255, p.390 |
| 561 | Laser Y-offset | Sets the Laser Y-offset length. | §15.7.256, p.390 |
| 571–578 | Maximum scale difference | Sets the maximum allowable scale difference before a scale error is reported, for scale inputs 1-8. | §15.7.257, p.390 |
| 579 | Paired axis resync tolerance | Sets the maximum distance a slaved axis can be from its sync position before prompting the user after power is restored. | §15.7.258, p.390 |
| 580 | Tangential Knife Axis Enable Bits | Bit-mapped; see manual | §15.7.259, p.390 |
| 581 | Tangential Knife Axis Direction Bits | Bit-mapped; see manual | §15.7.260, p.391 |
| 600 | A-axis Expected Velocity Switch Point | Sets the A-axis expected velocity switch point used for scale correction on five-axis systems with a scaled rotary A-axis. | §15.7.261, p.391 |
| 601 | A-axis Scale Switch To Velocity | Sets the velocity used for A-axis scale correction once the expected velocity exceeds the switch point. | §15.7.262, p.391 |
| 602 | A-scale Correction Meter Max Deflection Count | Sets the A-scale correction meter max deflection count, used by technicians to tune scale corrections. | §15.7.263, p.391 |
| 603 | B-axis Expected Velocity Switch Point | Sets the B-axis expected velocity switch point used for scale correction on five-axis systems with a scaled rotary B-axis. | §15.7.264, p.391 |
| 604 | B-axis Scale Switch To Velocity | Sets the velocity used for B-axis scale correction once the expected velocity exceeds the switch point. | §15.7.265, p.392 |
| 605 | B-scale Correction Meter Max Deflection Count | Sets the B-scale correction meter max deflection count, used by technicians to tune scale corrections. | §15.7.266, p.392 |
| 620–635 | Scale proportional constant and Scale max correction velocity | Overrides the Scales menu velocity settings with per-axis scale proportional constants and maximum correction velocities. | §15.7.267, p.392 |
| 700–799 | Dedicated Block of Parameters usable in Custom PLC Programs | Reserves Parameters 700-799 for Custom PLC Programs and defines their properties via parm_attribs.xml. | §15.7.268, p.392 |
| 800–813 | DB25 Pin Selection | Sets the function assigned to each DB25 pin on Acorn Control Boards; configured by the Wizard. | §15.7.269, p.394 |
| 814 | Analog/PWM 2 Settings | Sets the Analog/PWM 2 settings; on Acorn this sets PWM only, via the Wizard and PLC. | §15.7.270, p.394 |
| 815 | PWM Options | Bit-mapped; see manual | §15.7.271, p.394 |
| 817 | PWM Power Level Floor | Sets the minimum PWM power level floor percentage applied to nonzero S commands. | §15.7.272, p.395 |
| 830 | ATC Type | Sets the ATC type. | §15.7.273, p.395 |
| 852 | Carousel Skip Count on Reverse | Sets the skip-count logic used so a carousel that double-counts on reverse reports its bin location correctly. | §15.7.274, p.395 |
| 855 | MPG Performance | Sets the MPG performance mode (Smooth, Balanced, or Quick). | §15.7.275, p.395 |
| 856 | VCP Jogging State on Acorn Power Up | Sets the VCP jogging state on Acorn power up. | §15.7.276, p.395 |
| 900–999 | Reserved for Centroid PLC Program Use | Reserves Parameters 900-999 for Centroid PLC Program use, not for Custom PLC Programs. | §15.7.277, p.395 |
| 911–915 | Input Inversion | Bit-mapped; see manual | §15.7.278, p.395 |
| 916–920 | Input Force | Bit-mapped; see manual | §15.7.279, p.395 |
| 921–925 | Output Force On | Bit-mapped; see manual | §15.7.280, p.396 |
| 926–930 | Output Force Off | Bit-mapped; see manual | §15.7.281, p.396 |
| 931–935 | Memory Bit Force On | Bit-mapped; see manual | §15.7.282, p.396 |
| 936–940 | Memory Bit Force Off | Bit-mapped; see manual | §15.7.283, p.396 |
| 982 | Spindle Speed Variation Cycle Time (in seconds) | Sets the cycle time for the PLC-driven Spindle Speed Variation feature to ramp normal-max-min-normal speed. | §15.7.284, p.396 |
| 983 | Spindle Speed Variation Amount (+/- rpm) | Sets the RPM variation amount applied above and below the commanded spindle speed by the PLC-driven Spindle Speed Variation feature. | §15.7.285, p.396 |
| 984 | Feed Rate Variation Cycle Time (in milliseconds) | Sets the cycle time for the PLC-driven Feed Rate Variation feature to ramp from 100% to 0% and back. | §15.7.286, p.396 |
| 997 | Spindle Cooling Fan Delay Timer | Sets the spindle cooling fan delay timer. | §15.7.287, p.396 |

> Note: Parameters 387-389 are printed here as reserved debugging parameters that should be
> left at 0 (Router Manual §15.7.193, p.379), while `Alt E`'s screenshot action fires only when
> Parameter 389 is greater than 0 (Router Manual §2.28.2, p.34; see
> [operator-panel.md](operator-panel.md) §2.28). Both are quoted as printed; not reconciled here.
