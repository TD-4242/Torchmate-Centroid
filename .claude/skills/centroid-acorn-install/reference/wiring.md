# Acorn Wiring Reference

Electrical cabinet layout, input/output, E-stop, axis drive, home/limit switch, spindle and spindle
encoder wiring for the Centroid Acorn controller. See
[hardware.md](hardware.md#board-specifications) for board I/O counts and connector specs.
Source: Acorn Install Ch 5; printed pages cited inline.

## Cabinet layout and drive-type connections (§5.1)

Stepper drives connect through the Acorn's DB25 port, typically via a DB25 breakout board; AC servo
drives connect to the Acorn's screw-terminal headers (Acorn Install §5.1, p.34). Centroid publishes
example drive-hookup schematics, searchable by drive brand, on its online schematics library
(Acorn Install §5.1, p.35).

Suggested panel layout (Acorn Install §5.1, p.37):

| Component | Position |
| --- | --- |
| Main power supply | Upper right |
| Over-current protection (fuses) | Top center |
| Master ON/OFF switch | Upper right corner |
| Variable frequency drive | Upper left |
| E-stop contactor | Center right |
| Axis drives | Lower right |
| Acorn | Bottom center |
| Acorn 24VDC logic power supply | Left center |
| Acorn relay module | Lower left |
| Cabinet cooling fan | Left of relay module |
| `TB1` terminal block | Center |

Wiring practice (Acorn Install §5.1, p.37, p.39):
- Keep high-voltage/noisy equipment (transformers, contactors) and power lines away from
  low-voltage boards and signal lines; ground all cabinet chassis points to a single ground bus bar.
- Leave at least 2 in of clearance between wire ducts and circuit boards; keep cabinet wiring runs
  under 6 ft.
- Fit a snubber (Centroid's Quencharc network, `Centroid PART# 1819`) across every contactor,
  solenoid and relay coil.
- Wire gauge: `22 AWG` stranded for signal wiring (limit/home switches, VFD I/O); `18 AWG` stranded
  for 5/12/24VDC low-current power, including powering the Acorn; `16/14/12 AWG` for axis drive,
  contactor, spindle and pump power, sized to the drive's current draw.

## Inputs (§5.2)

Acorn inputs are sourcing 24VDC: the Acorn supplies +24VDC at the input pin, and an external switch
or sensor must sink it to `COM` to activate the input (the "contact closure to ground (COM)" method).
+24VDC for inputs is supplied via `24IN` on `H4` or `H5`, which are tied together internally; inputs
1-8 sink to `0VDC COM` through home switches, drives, inverters, probes and other sensors
(Acorn Install §5.2, p.44). Proximity and Hall-effect sensors used as inputs must be NPN type,
compatible with +24VDC (Acorn Install §5.2, p.44). See [hardware.md](hardware.md#io-map) for
per-terminal input assignments.

## Outputs (§5.3)

The Acorn has 8 relay outputs; each output toggles one SPDT relay (Acorn Install §5.3, p.45). See
[hardware.md](hardware.md#io-map) for per-terminal output assignments.

> App D describes the same outputs differently: the Acorn's `H10` outputs are 8 open-collector
> drivers (max `50 mA`) normally wired by ribbon cable to an external 8-relay board, and it is
> that board's relays that are SPDT (Acorn Install App D, p.126, p.129). See
> [hardware.md](hardware.md#io-map) for the output terminal table.

## +24VDC jumper to inputs (§5.4)

Jumper the spare `+24VDC` terminal on `H9` to either `H1` or `H4 24V IN` (`H1` and `H4` are tied
together internally on the Acorn) (Acorn Install §5.4, p.45).

> The manual names this +24VDC junction `H4`/`H5` in §5.2 (p.44) but `H1`/`H4` in §5.4 (p.45) and
> App D (p.129); see [hardware.md](hardware.md#io-map).

## E-Stop circuit (§5.5)

E-stop basics (Acorn Install §5.5, p.46):
- The E-stop circuit must be normally closed: the switch is closed while the machine is in its
  operational state, so a wire break or switch failure trips the fault instead of masking it.
- Multiple E-stop switches wire in series with each other.

> **NOTE:** Wiring E-stop in a normally-open (NO) configuration is dangerous — it will not stop the
> machine on a wire break or switch failure. Do not use an NO switch for E-stop
> (Acorn Install §5.5, p.46).

E-stop switch and signals (Acorn Install §5.5, p.47):
- Use a DPST, normally-closed, twist-to-release E-stop switch (e.g. `Centroid PART# 1009` with
  `#5934`).
- `Input 8` on `H1` is typically the E-stop input, wired in series with all E-stop switches.
- Any Acorn output can energize the E-stop contactor; Centroid typically uses `Output 1`, whose PLC
  designation is `NoFaultOut`. `Output 1`'s relay is rated up to 10A at 125VAC or 5A at 30VDC.
- Wire a normally-closed E-stop button: one NC terminal to Acorn power-supply `COM` (or the spare
  `COM` on `H9`), the other NC terminal to `H1 IN8`.

> The manual gives a different Output 1 relay rating elsewhere: `0.01-10A` at 125VAC or `0.01-10A`
> at 28VDC in the App D electrical specifications (Acorn Install App D, p.129), versus up to `10A`
> at 125VAC or `5A` at 30VDC here (Acorn Install §5.5, p.47).
>
> **Advisory (not in the manual):** because the manual gives two DC ratings for this relay, design
> the E-stop contactor circuit to the lower one (`5A` at `30VDC`), or confirm against the rating of
> the relay board actually installed.

E-stop contactor (Acorn Install §5.5, p.47):
- Power the E-stop contactor from a separate supply (never the Acorn logic supply) and energize it
  from Acorn Output Relay 1's NO contacts (`NoFaultOut`); fit a snubber across the contactor coil.
- For larger AC-servo machines, Centroid recommends a Schneider Electric/Telemecanique
  `LC1DT40B7A` or similar (`Centroid PART# 14374`), which includes its own snubber and is
  controlled with 24VAC.

Test the E-stop wiring from the Wizard's Input Definitions menu: set the `IN8 EstopOk` input to
normally-closed (green) and write settings; cycling the switch should toggle CNC12's message
`406 Estop detected` / `335 released`, and the PLC Diagnostic app (`Alt+I`) shows the input live
(Acorn Install §5.5, p.49-51).

## Axis drive wiring (§5.6)

Each Acorn drive schematic has a corresponding Drive Type in the Wizard; selecting that Drive Type
configures CNC12 to match the schematic (Acorn Install §5.6, p.52).

> **IMPORTANT:** Wire, configure and test one axis drive and motor on the bench first; only
> replicate the setup to the remaining drives once that axis jogs correctly from the Virtual Control
> Panel (Acorn Install §5.6, p.52).

Two ways to connect an axis drive (Acorn Install §5.6, p.52):
- Drive headers `H2`/`H3`: open-collector step/direction/enable outputs, generally reserved for AC
  servo drives.
- DB25 connector: for drives using +5VDC logic inputs; the recommended method for most stepper
  drives (e.g. Leadshine).

The DB25 can also connect directly to legacy PC-parallel-port-based controls via a straight-through
cable (compatible with, e.g., the Gecko G540); for non-standard DB25 pin configurations, the Wizard
can reassign the Acorn's DB25 pin functions instead of requiring a custom cable
(Acorn Install §5.6, p.55). See [hardware.md](hardware.md#db25-h6-connector-pinout) for the DB25
pinout.

## Home and limit switches (§5.7)

All home and limit switch inputs should be normally closed, so the switch is closed while the machine
is in its operational state (Acorn Install §5.7, p.56).

> **NOTE:** Using normally-open switches for limit or home is dangerous — the machine will not stop
> on a wire break or switch failure, and NO wiring is also more susceptible to noise-induced false
> trips (Acorn Install §5.7, p.56).

If using proximity sensors for home/limit, they must be 3-wire NPN type; 2-wire sensors are
unreliable and should be avoided (Acorn Install §5.7, p.56). Centroid's preferred wiring puts every
axis's home switch, normally closed, in series into one `HomeAll` input, conserving inputs
(schematic `S14954`) (Acorn Install §5.7, p.56).

Centroid's two recommended home/limit configurations (Acorn Install §5.7, p.58):
1. One home switch per axis, all wired into `HomeAll`; rely on CNC12 Software Travel Limits for
   over-travel protection on both ends of each axis (schematic `S14954`, omitting the `LimitAll`
   connection).
2. As above, plus a limit switch on each end of each axis, all wired into one `LimitAll` input
   (schematic `S14954`).

Home switches (Acorn Install §5.7, p.58):
- Define the machine home position; active only during the home program (`cncm.hom` for
  mill/router/plasma, `cnct.hom` for lathe) and ignored during normal operation.
- Should be normally closed, mounted so over-travel cannot crush the switch, and of CNC-duty
  (not long-throw industrial) type.

Limit switches (Acorn Install §5.7, p.60):
- Indicate an over-travel event and trigger a CNC12 E-stop; last-resort crash protection.
- Should be normally closed; can share one `LimitAll` input or use individual inputs; active at all
  times but can be commanded to be ignored (e.g. to jog off a tripped limit).
- On Acorn/AcornSix (open-loop/hybrid), re-homing is recommended after any limit-triggered E-stop.

Wizard home input assignments (Acorn Install §5.7, p.63):

| Wizard input name | Description |
| --- | --- |
| `HomeAll` | One input for all home switches. |
| `FirstAxishomeOk` … `FourthAxishomeOk` | One input per individual axis home switch (axes 1-4). |
| `SlavedHomeInput` | Used with the canned autosquaring paired-axis routine. |
| `ZriHomingAll` | Input for the axis motor encoder index (marker) pulse. |

Wizard limit input assignments (Acorn Install §5.7, p.63):

| Wizard input name | Description |
| --- | --- |
| `LimitAll` | One input for all limit switches. |
| `FirstAxisMinusLimitOk` / `FirstAxisPlusLimitOk` … `FourthAxisMinusLimitOk` / `FourthAxisPlusLimitOk` | One input per axis, per direction (axes 1-4). |

Wizard combined home/limit input assignments (Acorn Install §5.7, p.63):

| Wizard input name | Description |
| --- | --- |
| `FirstAxisHomeLimitOk` … `FourthAxisHomeLimitOk` | One switch used as both home and limit for that axis, one input per switch (axes 1-4). |

Zri homing uses a closed-loop drive that closes an Acorn input on the axis motor encoder's marker
pulse (once per revolution); the home switch gets the axis "in the ballpark" and the Zri input then
sets home precisely at the marker pulse (Acorn Install §5.7, p.64). Test home/limit wiring with the
PLC Diagnostic menu (`Alt+I`): tripping a switch by hand should flip its input LED from green to red
(Acorn Install §5.7, p.57, p.64-65).

## Spindle motor (§5.8)

> **STOP:** Bench-test the spindle analog output (board-level test) before wiring the spindle
> (Acorn Install §5.8, p.66).

Two wiring methods (Acorn Install §5.8, p.66):
1. Three-phase direct to the spindle motor via contactor(s): lower cost, but CNC12 cannot control
   spindle speed (mechanical pulleys only). A reversing contactor with snubber
   (`Centroid PART# 14375`) can reverse direction.
2. Preferred: a spindle controller (VFD/inverter/AC drive — the terms are used interchangeably).
   Centroid does not sell spindle controllers but recommends Delta Products VFDs, Automation Direct
   GS2/GS3 AC drives, or Yaskawa VS (Varispeed) inverters (Acorn Install §5.8, p.67).

Example Wizard spindle I/O assignment (Acorn Install §5.8, p.67):

| I/O | Assignment |
| --- | --- |
| `Input 5` | `SpinOk` (spindle fault feedback) |
| `Input 6` | Spindle fault input |
| `Output 4` | `SpinFwd` |
| `Output 5` | `SpinRev` |
| `Output 6` | Inverter fault reset |

> **WARNING:** If a DC spindle drive's analog inputs are not verified isolated, connecting them to
> the Acorn's 0-10V analog output may severely damage the Acorn and the drive; use a signal isolator
> (e.g. KB Electronics `KBSI-240D`) or an isolated drive (Acorn Install §5.8, p.67).

Fit a snubber (`Centroid PART# 1819`) across every spindle contactor coil (Acorn Install §5.8, p.68).

## Spindle encoder (§5.9)

Spindle-slaved moves (rigid tapping, lathe threading) require a spindle encoder wired to the Acorn,
meeting these prerequisites (Acorn Install §5.9, p.69):
- Encoder cable must be twisted-pair, shielded; the shield must be grounded to the DB-9 connector's
  metal shell (solder it if the connector provides no other attachment method).
- Encoder output must be RS422 differential quadrature with A, B and Z channels; a 1000-line encoder
  is suitable for a spindle (check the encoder's rating against the spindle's maximum RPM).

> **NOTE:** Failure to ground the cable shield may cause encoder errors in the software
> (Acorn Install §5.9, p.69).

Output voltage levels (Acorn Install §5.9, p.70):

| Characteristic | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- |
| Encoder channel low level | 0.0 | 0.3 | 0.5 | V |
| Encoder channel high level | 3.0 | 3.5 | 5.0 | V |

Encoder connector pinout (Acorn Install §5.9, p.70):

| Pin | Signal |
| --- | --- |
| 1 | Not used |
| 2 | Common (ground) |
| 3 | Z- |
| 4 | A- |
| 5 | B- |
| 6 | Z+ |
| 7 | A+ |
| 8 | B+ |
| 9 | +5V |

> "The +5V is an output provided by the ALLIN1DC." [sic] (Acorn Install §5.9, p.70)

After wiring, set the Wizard's Spindle Encoder Counts (encoder counts per revolution × 4, e.g. `4000`
for a 1000-line encoder) under `F7-Utility → F10 Acorn Wizard → SPINDLE → SETUP`, then verify the
count under `F1-Setup → F3-Config` (password `137`) → `F4-PID` by manually rotating the encoder one
revolution and comparing the recorded count to the Wizard value (Acorn Install §5.9, p.70).
