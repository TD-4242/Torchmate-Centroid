# G-code index

Source: Router Manual Ch 12 (§12.1-§12.48, p.243-279). One row per code per section: the
canned cycles appear once for the §12.28 summary table and again for their own sections, and
G81 also for §12.33. The Ref column gives the section with full syntax.

| Code | Name | Summary | Ref |
|---|---|---|---|
| G00 | Rapid Positioning | Moves at the machine's maximum rate to the specified position, absolute or incremental per G90/G91; the default positioning mode. | §12.1, p.244 |
| G01 | Linear Interpolation | Moves in a straight line to the specified position at the programmed feed rate. | §12.2, p.245 |
| G02 | Circular/Helical Interpolation CW | Arcs clockwise (viewer's perspective) to the end position, given by a radius or by I/J/K center offsets. | §12.3, p.245 |
| G03 | Circular/Helical Interpolation CCW | Arcs counter-clockwise to the end position, given by a radius or by I/J/K center offsets. | §12.3, p.245 |
| G04 | Dwell | Stops motion for a P (or X) time in seconds, 0.01-327.67. | §12.4, p.248 |
| G09 | Decelerate and Stop | Decelerates to a stop and dwells 0.01 seconds, for the current block only; equivalent to G4 P0.01. | §12.5, p.248 |
| G10 | Parameter Setting | Sets a machine parameter or tool offset from within a program. | §12.6, p.248 |
| G17 | Circular Interpolation Plane XY | Selects the XY plane for G02/G03; the default plane. | §12.7, p.249 |
| G18 | Circular Interpolation Plane ZX | Selects the ZX plane for G02/G03. | §12.7, p.249 |
| G19 | Circular Interpolation Plane YZ | Selects the YZ plane for G02/G03. | §12.7, p.249 |
| G20 | Select Inch Units | Interprets subsequent dimensions and feed rates as inches, without changing the native machine units. | §12.8, p.249 |
| G21 | Select Metric Units | Interprets subsequent dimensions and feed rates as metric, without changing the native machine units. | §12.9, p.249 |
| G22 | Work Envelope On | Turns on a programmable work envelope in machine coordinates, limits set by X/Y/Z (+) and I/J/K (-). | §12.10, p.249 |
| G23 | Work Envelope Off | Turns off the work envelope set by G22. | §12.10, p.249 |
| G28 | Return to Reference Point | Moves to the first reference point, optionally by way of an intermediate point. | §12.11, p.250 |
| G29 | Return from Reference Point | Moves from the intermediate point stored by a preceding G28 or G30 back toward the work piece. | §12.12, p.250 |
| G30 | Return to Secondary Reference Point | Works like G28 but targets the second reference point by default; a P parameter selects either point. | §12.13, p.251 |
| G37 | PWM Velocity Modulation On/Off | Turns PWM velocity modulation on or off, to reduce over-burn as the tool changes speed through corners. | §12.14, p.251 |
| G40 | Cutter Compensation Cancel | Cancels G41/G42 cutter compensation. | §12.15, p.251 |
| G41 | Cutter Compensation Left | Offsets the cutter half the D-code tool diameter to the left of the work piece, relative to travel direction. | §12.15, p.251 |
| G42 | Cutter Compensation Right | Offsets the cutter half the D-code tool diameter to the right of the work piece, relative to travel direction. | §12.15, p.251 |
| G43 | Tool Length Compensation (+) | Applies positive tool length compensation for the selected H-offset tool, from the part surface up. | §12.16, p.254 |
| G44 | Tool Length Compensation (-) | Applies negative tool length compensation, used only when there is an absolute machine home. | §12.16, p.254 |
| G49 | Tool Length Compensation Cancel | Cancels tool length compensation (also canceled by G43 H00). | §12.16, p.254 |
| G43.3 | Tool Length Compensation (+) with Axis Tilt Compensation | Like G43, plus X/Z compensation for 5th-axis tilt, on machines with a triangular rotary 5th axis. | §12.17, p.254 |
| G43.4 | Rotary Tool Center Point | With G43.3 active, keeps the tool tip moving in a straight line during a G1 feed move. | §12.18, p.255 |
| G50 | Scaling/Mirroring Off | Cancels scaling or mirroring turned on by G51. | §12.19, p.255 |
| G51 | Scaling/Mirroring On | Scales or mirrors subsequent positions, lines, and arcs about a center point, using I/J/K scale factors (negative to mirror). | §12.19, p.255 |
| G52 | Offset Local Coordinate System | Shifts the local coordinate system origin by a specified, non-cumulative distance. | §12.20, p.256 |
| G53 | Rapid Positioning in Machine Coordinates | One-shot rapid move in machine coordinates; usable only with absolute positioning (G90). | §12.21, p.256 |
| G54 | Select Work Coordinate System #1 | Selects WCS #1 for interpreting subsequent absolute positions (E1, or with P1 the extended WCS #7). | §12.22, p.256 |
| G55 | Select Work Coordinate System #2 | Selects WCS #2 for interpreting subsequent absolute positions. | §12.22, p.256 |
| G56 | Select Work Coordinate System #3 | Selects WCS #3 for interpreting subsequent absolute positions. | §12.22, p.256 |
| G57 | Select Work Coordinate System #4 | Selects WCS #4 for interpreting subsequent absolute positions. | §12.22, p.256 |
| G58 | Select Work Coordinate System #5 | Selects WCS #5 for interpreting subsequent absolute positions. | §12.22, p.256 |
| G59 | Select Work Coordinate System #6 | Selects WCS #6 for interpreting subsequent absolute positions. | §12.22, p.256 |
| G61 | Modal Decelerate and Stop | Decelerates to a stop and dwells 0.01 seconds at the end of every block, until canceled by G64. | §12.23, p.257 |
| G64 | G-code Geometry Smoothing Mode | Cancels Modal Decelerate and Stop and, with an ON/OFF/preset argument, turns Smoothing mode on or off. | §12.24, p.257 |
| G65 | Call Macro | Calls a numbered or named macro file, passing argument letters A-Z (excluding G, L, N, O, P) as variables. | §12.25, p.258 |
| G68 | Coordinate Rotation On | Rotates subsequent positions, lines, and arcs by an angle R about a center point, until G69. | §12.26, p.260 |
| G69 | Coordinate Rotation Off | Cancels coordinate rotation from G68, or the Transformed Work Coordinate System from G68.1. | §12.26, p.260 |
| G68.1 | Transformed Work Coordinate System | Turns on the Transformed Work Coordinate System for the job; G69 turns it off. | §12.27, p.261 |
| G73 | High-speed Peck Drilling | Canned-cycle table entry: intermittent feed into the hole, rapid retract out. | §12.28, p.262 |
| G74 | Counter-tapping | Canned-cycle table entry: feeds in, spindle CW then dwells at bottom, feeds out; left-hand thread. | §12.28, p.262 |
| G76 | Fine Bore Cycle | Canned-cycle table entry: feeds in, dwells and orients the spindle at bottom, rapids out. | §12.28, p.262 |
| G80 | Cancel Canned Cycles | Cancels an active canned drilling, boring, or tapping cycle. | §12.28, p.262 |
| G81 | Drilling and Spot Drilling | Canned-cycle table entry: feeds in, rapid retract out. | §12.28, p.262 |
| G82 | Drill with Dwell | Canned-cycle table entry: feeds in, dwells at bottom, rapid retract out. | §12.28, p.262 |
| G83 | Deep Hole Drilling | Canned-cycle table entry: intermittent feed into the hole, rapid retract out. | §12.28, p.262 |
| G84 | Tapping | Canned-cycle table entry: feeds in, spindle CCW then dwells at bottom, feeds out; right-hand thread. | §12.28, p.262 |
| G85 | Boring | Canned-cycle table entry: feeds in, feeds out. | §12.28, p.262 |
| G89 | Boring Cycle with Dwell | Canned-cycle table entry: feeds in, dwells at bottom, feeds out. | §12.28, p.262 |
| G73 | High-speed Peck Drilling | Drills in a series of Q-depth pecks at feed rate with rapid retracts between pecks; the retract amount is set by G10 P73. | §12.29, p.265 |
| G74 | Counter-tapping | Left-hand tapping cycle; start the spindle CCW before G74, which reverses it at the bottom of the hole. | §12.30, p.266 |
| G76 | Fine Bore Cycle | Bores to depth, then retracts a Q distance off the wall in Y+ after orienting the spindle via M19; requires a custom M19 macro. | §12.31, p.267 |
| G81 | Drilling and Spot Drilling | Drills a hole with a single feed-rate move, then retracts at the rapid rate. | §12.32, p.267 |
| G81 | Air Drill Cycle Transformation | Setting Parameter 81 (via G10 P81) makes G81 execute an M-function instead of moving Z, e.g. for air-actuated drills. | §12.33, p.268 |
| G82 | Drill with Dwell | Like G81, but adds an optional dwell at the bottom of the hole before retracting. | §12.34, p.269 |
| G83 | Deep Hole Drilling | Periodically retracts to clear chips, then resumes drilling from where it left off, per the Parameter 83 clearance. | §12.35, p.270 |
| G84 | Tapping | Right-hand tapping cycle; start the spindle CW before G84, which reverses it at the bottom of the hole. | §12.36, p.272 |
| G85 | Boring | Like G81, but retracts at a feed rate instead of rapid; usable for tapping with reversing tap heads. | §12.37, p.275 |
| G89 | Boring Cycle with Dwell | Like G85, but adds an optional dwell at the bottom of the hole before retracting. | §12.38, p.276 |
| G90 | Absolute Positioning Mode | Interprets subsequent coordinates as absolute positions relative to the origin. | §12.39, p.276 |
| G91 | Incremental Positioning Mode | Interprets subsequent coordinates as distances relative to the last point. | §12.39, p.276 |
| G92 | Set Absolute Position | Sets the current position to the specified coordinates in the active Work Coordinate System. | §12.40, p.276 |
| G93 | Inverse Time | Interprets F as the inverse of the minutes a move is allowed to take, instead of a feed rate; modal until G94. | §12.41, p.277 |
| G93.1 | Velocity Scrubber for Smoothed Inverse Time Data | Substitutes inverse-time feed rates with an optimized feed rate so the tool tip moves at a set physical speed; requires Smoothing on. | §12.42, p.277 |
| G94 | Cancel Inverse Time | Cancels G93/G93.1 inverse-time mode and returns to regular feed-per-minute rates. | §12.43, p.278 |
| G98 | Initial Point Return | Sets the +Z return level to the initial point after a canned cycle; the default. | §12.44, p.278 |
| G99 | R Point Return | Sets the +Z return level to point R after a canned cycle. | §12.45, p.278 |
| G117 | Rotation of Pre-set Arc Plane XY | Like G17, but adds optional P/Q angles rotating the XY arc plane away from orthogonal. | §12.46, p.278 |
| G118 | Rotation of Pre-set Arc Plane ZX | Like G18, but adds optional P/Q angles rotating the ZX arc plane away from orthogonal. | §12.46, p.278 |
| G119 | Rotation of Pre-set Arc Plane YZ | Like G19, but adds optional P/Q angles rotating the YZ arc plane away from orthogonal. | §12.46, p.278 |
| G173 | Compound High-speed Peck Drilling | Tilted-head equivalent of G73, for an Articulated Head machine when the WCS is not transformed. | §12.47, p.279 |
| G174 | Compound Counter-tapping | Tilted-head equivalent of G74. | §12.47, p.279 |
| G176 | Compound Fine Bore Cycle | Tilted-head equivalent of G76. | §12.47, p.279 |
| G181 | Compound Drilling and Spot Drilling | Tilted-head equivalent of G81. | §12.47, p.279 |
| G182 | Compound Drill with Dwell | Tilted-head equivalent of G82. | §12.47, p.279 |
| G183 | Compound Deep Hole Drilling | Tilted-head equivalent of G83. | §12.47, p.279 |
| G184 | Compound Tapping | Tilted-head equivalent of G84. | §12.47, p.279 |
| G185 | Compound Boring | Tilted-head equivalent of G85. | §12.47, p.279 |
| G189 | Compound Boring Cycle with Dwell | Tilted-head equivalent of G89. | §12.47, p.279 |
| G180 | Cancel Canned Cycles | Functionally identical to G80. | §12.48, p.279 |

## Modal notes

- G-codes are organized into groups A-P (Router Manual Ch 12 group table, p.243-244). If a line
  specifies two codes from the same group, only the last one specified stays active (Router
  Manual Ch 12, Note 3, p.244).
- Group B (`G04`, `G09`, `G10`, `G28`, `G29`, `G30`, `G52`, `G53`, `G92`) codes are one-shot,
  active only for the line they appear on; every other G-code is modal until superseded by
  another code from its own group (Router Manual Ch 12 group table, p.243-244; Note 4, p.244).
- A Group A code (`G00`-`G03`) used while a canned cycle is active cancels the canned cycle;
  canned-cycle codes have no effect on Group A codes (Router Manual Ch 12 group table, p.243;
  Note 5, p.244).
- `G61` is canceled by any form of `G64` (Router Manual §12.24, p.257).
- Canned cycles are modal and are canceled by `G80`; `G00`, `G01`, `G02`, or `G03` also cancel them
  (Router Manual §12.28, p.264).
