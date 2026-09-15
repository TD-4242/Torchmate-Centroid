# Acorn Axis Pairing and Squaring Reference

Pairing two axis motors (typically a moving-gantry router's dual Y motors) to move as one,
either in software (Wizard §6.7) or hardware, and homing/squaring the paired axis. See
[wizard.md](wizard.md#axis-homing-and-travel-66) for the Wizard homing page and
[wiring.md](wiring.md#home-and-limit-switches-57) for home/limit switch wiring and the Wizard
input names (`HomeAll`, `SlavedHomeInput`, etc).
Source: Acorn Install §6.7; Pairing Guide rev19.

## Software vs hardware pairing

**Software Pairing**: CNC12 sends one axis's step/direction signals to two Acorn axis outputs
(e.g. `Y` and `4th Axis`), so both motors move in unison; the Acorn effectively becomes a
3-axis controller, since the 4th axis output is consumed by the slaved motor (Pairing Guide
p.3). Both motors must share the same `Steps per revolution` and `Overall Turns Ratio`. If the
paired motors face each other and would spin opposite ways when paired, set
`Reverse direction of 4th axis motor` in the Wizard (Pairing Guide p.3).

**Hardware Pairing**: two drives are wired in parallel to one Acorn axis output, freeing the
4th axis drive port for other use (e.g. a rotary table) — effectively turning Acorn into a
5-axis drive output board (Pairing Guide p.4). Same `steps per rev`/`turns ratio` requirement,
plus matching motor/drive size and type; any direction reversal is done at the drive (a
software or DIP-switch setting) or by swapping motor leads, not in the Wizard (Pairing Guide
p.4).

## License requirement

Software axis pairing requires a Pro license; it is not included in the Free version of Acorn
CNC12 (Acorn Install §6.7, p.81).

> The install manual's Pro-license statement (Acorn Install §6.7, p.81) differs from the
> Pairing Guide's Auto Square Homing rules, which require "CNC12 Mill version 5.xx+ with Pro
> or Ultimate license" (Pairing Guide p.14, p.22); the guide's Ultimate-license allowance is
> not stated in the manual.

## Wizard fields (§6.7)

- `Axis to pair with 4th Axis`: select the axis for Software Pairing (Acorn Install §6.7,
  p.81).
- `Reverse direction of 4th axis motor`: `Yes` reverses the 4th axis motor's direction
  relative to the master axis, for paired motors mounted to spin opposite ways (Acorn Install
  §6.7, p.81).
- `Paired axes squaring/alignment`: `Manual` or `Automatic` Squaring/Alignment (Acorn Install
  §6.7, p.81).
- `Master Axis squaring/alignment distance`: maximum independent movement of the master axis
  during the home program, always away from the master home switch, typically close to the
  slave switch's offset from square (Acorn Install §6.7, p.81).
- `Feedrate of Homing Movements`: speed the home program uses to seek the home switches (Acorn
  Install §6.7, p.81).
- `Home Switch Deadband Distance`: travel into the home switch after it trips, to eliminate
  switch flicker; cheaper switches typically need more deadband (Acorn Install §6.7, p.82).
- `Master Axis Home Switch PLC Input`: shows the input set for the master home switch in Input
  Definitions (Acorn Install §6.7, p.82).
- `Slave Axis Home Switch PLC Input`: shows the input set for `SlavedHomeInput` in Input
  Definitions (Acorn Install §6.7, p.82).

## Homing and squaring methods

Software Pairing supports three homing/squaring methods (Pairing Guide p.3):
1. **Auto Homing and Auto Squaring** — fully automatic homing and squaring.
2. **Auto Homing with Manual Squaring** — operator squares the gantry manually, then
   `Auto Home to Switch` finds home.
3. **Manual homing with Manual Squaring** — operator squares the gantry manually, jogs to
   home, and presses cycle start to set home there.

Hardware Pairing supports the same three methods plus a fourth, Clearpath hard-stop homing
(Pairing Guide p.4).

### Hardware pairing procedure (Pairing Guide p.5-21)

**a. Manual homing, manual squaring** — no home/limit switches; choose `Simple Home` in the
Wizard homing menu, and in the Wizard Axis Pairing menu choose `No Software Pairing` and the
hardware-paired axis number (Pairing Guide p.5).

> Adjust the machine mechanically so the gantry naturally rests near square, with no spring
> or windup, before starting (Pairing Guide p.5).

1. Power off; manually square the gantry; mark the square position or install hard stops
   (Pairing Guide p.5).
2. Power up the Acorn; the hardware-paired gantry motors move in unison from power-up
   (Pairing Guide p.5).
3. Jog all axes to the desired home position and press cycle start to set home there (Pairing
   Guide p.5).
4. Set `Software Travel Limits` per axis in the Wizard axis configuration menu, in machine
   coordinates measured from home (Pairing Guide p.5).
5. `Park` the machine at the home position before shutdown, so the gantry stays square and
   near home for the next power-up (Pairing Guide p.6).

Daily use: if not parked at home, manually re-square the gantry against the marks, jog to home
and press cycle start (Pairing Guide p.6-7).

**b. Auto homing, manual squaring** — three home switches (axes 1-3) wired into `HomeAll`
(Pairing Guide p.9).
1. Wire the axis 1-3 home switches into `HomeAll`; in the Wizard homing menu choose
   `Automatic Homing` and set homing directions, sequence and rates (Pairing Guide p.9-10).
2. In the Wizard Axis Pairing menu, select the hardware-paired axis number and leave
   autosquaring off, since squaring is manual (Pairing Guide p.10).
3. First time, or after a fault: power off and manually square/mark the gantry; power up
   (motors pair automatically); jog near the switches and press cycle start to auto-home all
   axes; set `Software Travel Limits` (Pairing Guide p.11).
4. Subsequently: verify the machine is parked and square, then press cycle start to home
   (Pairing Guide p.12).

**c. Auto homing, auto squaring (Relay Auto Squaring)** — the hardware-paired gantry motors'
step signals run through a relay output, `AutoSquareRelayForHardPair`, that the home program
opens to move the master and slave independently for squaring, keeping the 4th axis free for
other use (Pairing Guide p.13).

> Auto Square Homing does not correct a mechanically out-of-square machine: the gantry must
> already be close to square in its relaxed (unpowered) state, close to square at power-up,
> and close to square before starting the home program (Pairing Guide p.14).

1. Wire a dedicated master and slave home switch on opposite sides of the gantry: the slave
   switch into its own input (`SlavedHomeInput`), the master switch in series with the other
   axes' switches into `HomeAll` (Pairing Guide p.13).
2. Assign `AutoSquareRelayForHardPair` to an output (Pairing Guide p.16).
3. Mechanically square the gantry and install both switches in line with it; then unbolt and
   offset the master switch away from the gantry (commonly 0.025") so the slave switch trips
   first — the slave must trip before the master (Pairing Guide p.14, p.19).
4. Home program sequence: home Z first, then X, then drive the paired gantry (in unison) until
   the slave switch trips and clears; unpair the gantry motors, seek the master switch
   independently, back off by the squaring distance, re-pair the motors, and set machine home
   for all axes (Pairing Guide p.18).
5. If the drive uses an enable signal, jumper the paired axes' enable lines so the non-moving
   side holds position during the independent squaring move (Pairing Guide p.33).

**d. Clearpath hard-stop homing with auto squaring** — an alternative for Teknic Clearpath
motors: each axis homes to a mechanical hard stop instead of a switch, still frees the 4th
axis output, and needs no home switches; requires the Teknic Power Hub and setup per Centroid
Tech Bulletin #319 (Pairing Guide p.20).
1. Power up and jog clear of obstructions (Pairing Guide p.20).
2. Press cycle start; each axis drives to its hard stop, backs off, and sets home there
   (Pairing Guide p.20).

### Software pairing procedure (Pairing Guide p.22-41)

**Auto homing, auto squaring** — requires normally-closed home switches for axes 1-3 wired
into `HomeAll` and the axis-4 (slave) switch wired into `SlavedHomeInput`; normally-open
switches, NPN proximity switches (series or parallel), and individual `FirstAxisHomeOk` …
`ThirdAxisHomeOk` inputs are also supported, each with its own wiring diagram (Pairing Guide
p.25, p.28-32).

> Normally-open home/limit switches are not recommended: they are more susceptible to noise
> and false trips, and give no protection on a wire break (Pairing Guide p.41).

1. Measure gantry side-to-side play, then mechanically square the gantry (Pairing Guide p.23).
2. Home temporarily with MDI `M26/X/Y/Z` and jog the paired gantry to the switch-install
   location; mount the master and slave switches in line with the now-square gantry (Pairing
   Guide p.23).
3. Unbolt the master switch and offset it away from the gantry (commonly 0.025"-0.15", up to
   about two-thirds of the play measured in step 1) so the slave switch trips first; set
   `Master Axis squaring/alignment distance` in the Wizard to that offset (Pairing Guide p.23).
4. Run the Wizard-generated home program, check squareness, and trim
   `Master Axis squaring/alignment distance` up or down until the gantry homes square (Pairing
   Guide p.23).
5. First-time procedure: power off and roughly square the gantry, power up, jog near the
   switches and press cycle start; the machine homes Z, then X, then seeks the slave switch,
   then squares the master independently against the squaring distance; set
   `Software Travel Limits` (Pairing Guide p.34).
6. `Park` near home before shutdown, e.g. `G53 X1Y1Z-1 L100` in `park.mac` (Pairing Guide
   p.34).
7. Subsequently: power on and press cycle start to home, square and set home automatically
   (Pairing Guide p.34).

> If Estop, Cycle Cancel, ESC or Reset interrupts the independent master/slave squaring move,
> the axes are left unpaired and the software travel limit values are lost. Press the VCP
> `Re-pair Axes` button (its LED turns green when paired) before jogging, and re-enter the
> travel limits or use `Restore Report` (Pairing Guide p.38).

**Auto homing, manual squaring** — three home switches (axes 1-3) wired into `HomeAll`; the
Wizard `Paired Axis Alignment type` field set to `No Auto Squaring` prompts the operator to
square manually before each homing cycle (Pairing Guide p.35-36).
1. In the Wizard, choose `Automatic Homing` and configure directions, sequence and travel
   limits; set `Paired Axis Alignment type` to `No Auto Squaring` (`Slave Axis Home Switch PLC
   Input` is unused with manual squaring) (Pairing Guide p.35-36).
2. First time, or after a fault: power off and manually square/mark the gantry; power up
   (motors pair automatically); jog near the switches and press cycle start to auto-home all
   axes; set `Software Travel Limits` (Pairing Guide p.37).
3. `Park` near home before shutdown so the gantry stays square (Pairing Guide p.37).
4. Subsequently: verify the machine is parked and square, then press cycle start to home
   (Pairing Guide p.37).

The Wizard auto-generates the `cncm.hom` home program and its matching PLC program from these
settings; to hand-edit `cncm.hom`, set the Wizard to not overwrite it when
`Write Settings to CNC Control Configuration` is pressed (Pairing Guide p.39).

## CNC12 v5.4+ changes

CNC12 v5.4+ keeps all Acorn axis-pairing wiring, Wizard configuration and setup identical to
earlier versions, but rewrites the underlying motion-engine technique for software-paired
axes: Auto Squaring homing runs significantly faster, and two new M-codes, `M294` and `M295`,
pair and unpair any paired axes instantly and independently — for example to let a custom home
or other program unpair and re-pair a slave axis as needed (Pairing Guide p.2). Details are in
the CNC12 v5.4 release notes starting at page 16:
https://www.centroidcnc.com/centroid_diy/downloads/centroid_cnc12_download/cnc12_v5.40.00_release_notes.pdf
(Pairing Guide p.2).
