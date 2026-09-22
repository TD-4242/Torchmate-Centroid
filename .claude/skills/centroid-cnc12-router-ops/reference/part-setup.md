# CNC12 Part Setup: Part Zeros, Work Coordinate Systems, and CSR

Set the part position, configure Work Coordinate Systems (WCS), rotate the coordinate system (CSR), and enable
Transformed WCS (TWCS) for Articulated Head machines. Source: Router Manual Ch 4 (Set Part Zeros).

Access via `F1 – Set Part Zeros` from the main screen; see [interface.md](interface.md) §F1 – Set Part Zeros for
that menu's 10 sub-keys (Router Manual §3.1, p.42).

---

## 4.1 Operation Description

Setting the part zero position establishes a coordinate system with an origin at part zero (Router Manual §4.1,
p.50).

The Set Part Zeros screen has its own softkey bar, distinct from the top-level `F1 – Set Part Zeros` menu in
[interface.md](interface.md):

| Softkey | Label | Description |
|---|---|---|
| `F1` | Next Axis | Toggles to the next axis. Discards any changes made to the current axis but not yet accepted. |
| `F2` | Auto | Uses the probe to automatically measure and set part position. Requires the probe's assigned tool number to have its height and diameter offsets set, and `Parameter 12` set to that tool number. See Ch 9. |
| `F3` | Probe | Opens the probing operations menu. See Ch 9 for details. |
| `F4` | Prev WCS | Selects the previous work coordinate; only affects the currently-selected work coordinate. |
| `F5` | Next WCS | Selects the next work coordinate; only affects the currently-selected work coordinate. |
| `F6` | CSR | Opens the CSR menu for automatic coordinate-system-rotation detection. Appears only when the Coordinate System Rotation software option is unlocked. |
| `F7` | WCS Table | Opens the Work Coordinate System (WCS) Configuration screen. See §4.8. |
| `F8` | Set | Accepts the position for the current axis, correcting for edge finder diameter based on the approach direction. Does not automatically advance to the next axis. |

(Router Manual Ch 4 intro, p.50 — printed before the §4.1 heading.)

> Note: this table's `F8 – Set` conflicts with the per-axis Set Part Position procedure below, whose on-screen
> diagram reads `F10 – Set` / `SHIFT+F10` (Router Manual Ch 4 intro, p.50 vs §4.1.1, p.51). Quoted as printed; no
> reconciliation attempted.

### 4.1.1 Setting Up X- or Y-axis (p.51)

Set Part Position procedure:
1. Select Axis using mouse or arrow keys
2. Jog to Touch-off on Part
3. Edit the value if necessary
4. Press `F10 – Set` to set the current Part Position, or `SHIFT+F10` to set all Part Positions

Fields:

| Field | Description |
|---|---|
| `Part Position` | Enter the value of your part zero position or the offset. |
| `Edge Finder Diameter` | Enter the diameter of the tool or edge finder used to determine the part zero. The value entered is stored. |
| `Approach From` | Toggle the direction the edge finder or probe approaches the part from. |

### 4.1.2 Setting up Z-Axis or 4th/5th Linear Axis (p.52)

Same four-step Set Part Position procedure as §4.1.1.

Fields:

| Field | Description |
|---|---|
| `Part Position` | Enter the value of your part zero position or the offset. |
| `Tool Number` | Enter the Tool Library tool number in use. When non-zero, the controller uses that tool's Height Offset to calculate the actual position. |

Z-axis Tool Number examples (p.52):
- Example 1 (reference tool): set `Tool Number` to `0` — this tells the controller the reference tool is in use.
- Example 2 (non-reference tool, not a ball nose cutter): set `Tool Number` to the tool's assigned number in the Tool Library (confirm its height offset is set).
- Example 3 (ball nose cutter, other than the reference tool): set `Part Position` to the surface position plus the ball nose cutter's nose radius; set `Tool Number` to the tool's assigned Tool Library number.

> The Tool and Offset libraries must be up-to-date before setting the Z-axis Part Zero (p.52).

### 4.1.3 Setting up Rotary Axis (p.53)

Same four-step Set Part Position procedure as §4.1.1.

### 4.1.4 Using Multiple Work Coordinate Systems (p.53)

If using multiple work coordinates, set the part position separately for each one:
1. Set the position for each axis in the first coordinate system.
2. Move to the next fixture.
3. Press `F9 – WCS CSR Table` to open the WCS CSR Table; use the arrow keys to choose between the six visible WCS options, and `F1 – Next Table` to see the next six.

The currently-selected coordinate system is always displayed above the DRO. See §4.8 for a complete description
of setting up each work coordinate.

> **NOTICE** This procedure does NOT apply to tilt table setup (p.53).

---

## 4.2 Part Setup Examples (Router Manual §4.2, p.53-55)

### Example 1: Setting the X-axis Part Zero with No Offset (p.53-54)

Scenario: set the left edge of the part as the X-axis origin, using a `0.25` diameter edge finder approaching from
the left (`-X`) side.

Steps:
1. Move the Edge Finder to the left edge of the part (p.53).
2. Select the `Edge Finder Diameter` field for the X-axis (p.54).
3. Type `.25` and press `ENTER`.
4. Press `SPACE` until `Left (-)` is displayed.
5. Press `F10 – Set` to accept the values.

| Axis | Part Position | Edge Finder Diameter | Approach From |
|---|---|---|---|
| X | 0 | 0.25 | Left (-) |

Since no offset is applied, Part Position is zero. Once `F10 – Set` is pressed, the X-axis DRO reads `-0.125` — the
center of the Edge Finder sits to the left (minus) of the part by 0.125 inches (half the Edge Finder Diameter).

Formula: `Position (Approach from) Edge Finder Diameter / 2`, where `(Approach from)` is the sign of the approach
direction: `0.0 - .25/2 = -0.125` (p.54).

### Example 2: X-axis Origin Offset Into the Part by One Inch (p.54-55)

Scenario: offset the X-axis origin one inch into the part from the left edge, using the same edge finder and
approach.

Steps (p.54):
1. Move the Edge Finder to the left edge of the part.
2. Select the `Part Position` field for the X-axis.
3. Type `-1` and press `ENTER`.
4. Press `SPACE` until `Left (-)` is displayed.
5. Press `F10 – Set` to accept the value.

| Axis | Part Position | Edge Finder Diameter | Approach From |
|---|---|---|---|
| X | -1 | 0.25 | Left (-) |

Part Position equals `-1.0` because the Edge Finder is one inch to the left (minus direction) of the desired
X-axis origin. Once `F10 – Set` is pressed, the X-axis DRO reads `-1.125`.

Formula: `Position - Edge Finder Diameter/2 = -1.0 - .25/2 = -1.125` (p.55).

---

## 4.3 Set Part Zeros Manually (Router Manual §4.3, p.55)

Manually set the Part Position per axis, with all enabled axes displayed in rows. Enter numeric values under
`Part Position` and `Edge Finder Diameter`; toggle `Approach` by clicking the approach label or pressing `SPACE`
with it highlighted.

## 4.4 Set Part Zeros by Laser (Router Manual §4.4, p.55)

Enable and disable the laser crosshairs (must be set up via the CNC12 Wizard). Jog the machine until the
crosshairs are at the desired position, enter the current X position into the X part-position field (and the same
for Y), then press `SHIFT+F10` to set both positions, or `F10` with X or Y selected to set that axis only.

## 4.5 Set Part Zeros by Probe (Router Manual §4.5, p.56-57)

Specify the probe diameter or select a probing cycle to determine part zero, assuming a probe is connected and
configured via the CNC12 Wizard. A Pro or Ultimate license is required to unlock all probing cycles; Bore is
available in the Free version of CNC12. Select a probing cycle to continue; the probing cycle page gives
instructions for running it (p.56).

> For probing cycles themselves, see Router Manual Ch 9 (p.104); this section covers only the operator procedure
> for reaching them.

### 4.5.1 Configuring Touch Probe (p.56-57)

Configuring a Touch Probe in CNC12 is simplified by the CNC12 Wizard. From the Main Screen, press
`F7 – Utility Menu`, then `F10 – Acorn Wizard`. Alternatively, from the Set Part Zeros menu, press `F3 – Probe`,
then `F9 – Probe Setup` (p.56).

1. Assign an input for `ProbeTripped` under `Primary System > Input Definitions` (e.g. `Probe` input type on
   `IN7`), matching how the probe is wired to the CNC Control Board (p.56).
2. Navigate in the Wizard to `Touch Devices > Touch Probe` to configure the probe (p.57).
3. Depending on the probe and setup, configure `Probe Type`, input state when tripped, probe tool number, fast
   and slow probe rate, recovery distance, maximum probing distance, probe protection and warnings, and probe
   jogging rates (p.57).

## 4.6 Set Part Zeros by Plate (Router Manual §4.6, p.58-59)

Specify the current bit diameter, Z clearance amount, magnet reminder, flute reminder, and whether Z is set by
touch-plate probing, assuming a touch plate is connected and configured via the CNC12 Wizard (p.58).

### 4.6.1 Configuring Touch Plate (p.58-59)

Configuring a Touch Plate in CNC12 is simplified by the CNC12 Wizard. From the Main Screen, press
`F7 – Utility Menu`, then `F10 – Acorn Wizard`. Alternatively, from the Set Part Zeros menu, press `F4 – Plate`,
then `F8 – Plate Setup` (p.58).

1. Assign an input for `TouchPlateTripped` under `Primary System > Input Definitions` (e.g. `Probe` input type on
   `IN6`) (p.58).
2. Navigate in the Wizard to `Touch Devices > Touch Plate` to configure the plate; select a preset (e.g.
   `AvidCNC Touch Plate`) or `Define Your Own` and enter the touch plate's dimensions (p.59).
3. Configure input state when tripped, the functioning-verification warning, fast and slow probing rate, max
   probing distance, and retract distance (p.59).

## 4.7 Set Part Zeros by Auto Zero (p.60)

To Auto Zero an axis with a probe: confirm the probe is connected and functional, select the axis to zero, then
press `F7 – Auto Zero`. The displayed image changes to represent the probe and axis being zeroed, and the
selected tool changes to the tool number assigned to the probe. Press `CYCLE START` to begin. If
`Display warning to verify that Probe is functioning properly` is set to `Yes` in the CNC12 Wizard, a confirmation
message appears; lightly touch the stylus until `WARNING: PROBE TRIPPED` appears, then press `CYCLE START` to
begin the Auto Zero process (p.60).

## 4.8 Work Coordinate System (WCS) Configuration (p.60-62)

Press `F9 – WCS CSR Table` from the Set Part Zeros menu to open the Work Coordinate System (WCS) Table, which
gives access to reference return points, coordinate system origins, and work envelope. Confirm Home has been set
properly, or coordinate system positions will be incorrect. All values on this screen are in machine coordinates
(p.60).

All coordinate systems are relative to the Home position set during control power-up; while on this screen the DRO
shows actual machine position relative to Home, not the position relative to the WCS origin. If the Coordinate
System Rotation option is unlocked, the CSR angle for each coordinate system can also be set. On Articulated Head
machines with TWCS enabled (`Parameter 166`), the `TWCS=Yes/No` setting differentiates which WCSs are transformed
— see §4.10 (p.60).

Regular and Extended Work Coordinate Systems (p.61): Regular WCS #1-6 are standard; extended WCS #7-18 are an
extra-cost option.

| WCS | G-code | WCS | G-code | WCS | G-code |
|---|---|---|---|---|---|
| WCS #1 | `G54` | WCS #7 | `G54 P1` | WCS #13 | `G54 P7` |
| WCS #2 | `G55` | WCS #8 | `G54 P2` | WCS #14 | `G54 PS` [sic] |
| WCS #3 | `G56` | WCS #9 | `G54 PS` [sic] | WCS #15 | `G54 P9` |
| WCS #4 | `G57` | WCS #10 | `G54 P4` | WCS #16 | `G54 P10` |
| WCS #5 | `G58` | WCS #11 | `G54 PS` [sic] | WCS #17 | `G54 P11` |
| WCS #6 | `G59` | WCS #12 | `G54 P6` | WCS #18 | `G54 P12` |

> Note: the manual's WCS table prints `G54 PS` for WCS #9, #11, and #14 (Router Manual §4.8, p.61) rather than
> following the `P1`-`P12` sequence the other rows use; confirmed against the printed page image, and quoted
> exactly as printed with no correction inferred.

The WCS currently in use is shown in the upper-left corner of the screen, above the DRO; the DRO always displays
the tool position from the WCS in use (p.61).

To change the WCS in use (p.61):
- From the Main Screen, press `F1 – Set Part Zeros`, then `F9 – WCS CSR Table`.
- Select a WCS coordinate and press `F9 – Set as Active WCS`.
- Or use `ALT+=` for the next WCS coordinate and `ALT+-` for the previous.

After selecting a new WCS, "you can set up the WCS using the part setup menus for X and Z to define a new Part
Zero position with this WCS" (Router Manual §4.8, p.61) — see §4.1-§4.7. Once set, the control remembers the
WCS's Part Zero until changed, even after shutdown (p.61).

> Note: the manual's own wording names only X and Z here (Router Manual §4.8, p.61), though the surrounding
> Part Setup sections (§4.1-§4.7) cover X, Y, and Z. Quoted as printed; no reconciliation attempted.

WCS CSR Table softkeys (p.61-62):

| Softkey | Label | Description |
|---|---|---|
| `F1` | Next Table | Cycles through viewing the other WCS entries (six per page). |
| `F2` | Lock/Unlock Table | Locks or unlocks WCS tables from editing (see `Parameter 45`). |
| `F3` | +.001 | Increases existing cell values by `0.001` inches (`0.01` mm metric). |
| `F4` | -.001 | Decreases existing cell values by `0.001` inches (`0.01` mm metric). |
| `F5` | Abs/Inc | Cycles between Absolute and Incremental modes for altering existing cell values. |
| `F6` | Return Points | Accesses the menu that sets the machine's reference return points; used with G28 and G30 (Ch 12). Specified in machine coordinates. The Z-coordinate of the first reference point is also the Z-home position used by M2, M6, and M25 (Ch 13). `F2 – Teach` copies current axis machine coordinate values to the table. |
| `F7` | Work Envelope | Defines the axis `-` and `+` envelope limits (machine coordinates) used with the G22 G-code; the X, Y, Z and I, J, K parameters from a G22 code are stored here so later G22 codes need not repeat them unless they change. |
| `F8` | Clear Cell or Column | Clears the selected cell or column's contents. |
| `F9` | Set As Active WCS | Sets the currently-selected column as the active WCS. |
| `F10` | Save | Saves the current WCS table configuration. |

> Note: the work envelope (`F7`) only applies to programmed moves; jogging outside the work envelope is still
> possible (p.62).

---

## 4.9 Coordinate System Rotation (CSR) (Router Manual §4.9, p.62-63)

CSR saves setup time: rather than clamping the part and indicating its edge to square it with the machine axes,
CSR automatically rotates the coordinate system to the angle of the probed part or fixture, compensating for
different orientations. Clamp the part, then probe two points along the X- or Y-axis of the material (p.62).

CSR menu softkeys (p.63):

| Softkey | Label | Description |
|---|---|---|
| `F1` | Orient | Selects the CSR measurement orientation: front, back, left, or right. |
| `F2` | Manual Teach CSR | Default screen without a Pro or Ultimate license. Jog to the first position, press `F10` to accept, jog to the second position, press `F10` to accept; CSR is calculated from the two points and applied to the current WCS. |
| `F3` | Laser Teach CSR | Same two-point procedure as Manual Teach CSR, using the laser crosshairs to align to the part instead of jogging blind. |
| `F4` | Probe CSR | Default screen with a Pro or Ultimate license. Jog the probe near the first position, press `CYCLE START` to probe it; repeat for the second position. CSR is calculated and applied to the current WCS. |
| `F5` | Touch Plate CSR | Choose orientation with `F1`, position the tool per the touch plate type, press `CYCLE START` to probe each of two points against the touch plate. |
| `F6` | Probe Cycles | Choose a probing cycle to determine CSR. Without a Pro or Ultimate license, only Bore is available; with one, Bore, Boss, Slot, Web, Inside Corner, Outside Corner, Single Axis, and Find Angle are available. |
| `F7` | Zero CSR | Zeros the current CSR. |
| `F8` | MDI | Runs a single-line command, e.g. `G1`, `X2`, `Y3`, `F20`. |
| `F9` | WCS CSR Table | Opens the WCS CSR Table (§4.8). |
| `F10` | Accept | Accepts the currently-entered CSR from the Manual Teach CSR or Laser Teach CSR menu. |

## 4.10 Transformed WCS (TWCS=Yes) (Router Manual §4.10, p.64)

Applies only to Articulated Head machines with the TWCS feature enabled via `Parameter 166` (see Ch 15). On such a
machine, a WCS with `TWCS=Yes` is a transformed WCS (TWCS).

When a TWCS is selected:
- The DRO shows axis positions transformed based on the B-axis (5th-axis) position, per the TWCS's frame of
  reference.
- The WCS label shows `TWCS` to indicate the selected WCS is transformed.
- Probing Cycle results are shown based on the TWCS frame of reference.

Move types transformed automatically when running a CNC program with a TWCS selected:
- `G0`, `G1`, `G2`, `G3`
- Protected move probing functions `M115`, `M116`, `M125`, `M126`
- Canned Cycles `G73`, `G74`, `G76`, `G81`, `G82`, `G83`, `G84`, `G85`, `G89`
- `M25`
- Moves involving CSR and Cutter Compensation

Move types NOT transformed:
- Homing moves `M91`/`M92`
- Move to switch `M105`/`M106`
- Move axis by counts `M128`
