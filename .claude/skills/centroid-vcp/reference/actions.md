# VCP button actions: skin events, macros and apps

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`).

How a button *does* something: bind it to PLC logic with a skin event number, run a macro or a
single line of G-code, or launch an external program. The tags here are children of `<vcp_button>`
([button-anatomy.md](button-anatomy.md)); where the button sits on the grid is
[skin-and-grid.md](skin-and-grid.md) and what it shows is [visual-states.md](visual-states.md).

> Paths the manual prints are mill paths under `c:\cncm`. On CNC12 Router the same tree lives
> under `c:\cncr` (Router Manual §1.8, p.13); the manual's own strings are quoted unchanged below.

---

## `<skin_event_num>`: assigning PLC logic to a button

The `skin_event_num` is the way PLC logic can be assigned to a VCP button. The skin event number
is associated with a piece of logic that creates the desired action of a machine tool function;
that logic is described in the PLC program and the skin event number is in the PLC program too.
Said another way, CNC12 knows what function you want for a particular VCP button from this number
(VCP Manual p.36).

Outputs defined in the Wizard have an associated skin event number, and the stock VCP button XML
files use these skin event numbers to link the button to the functionality defined in the PLC
program (VCP Manual p.35). The manual's Work Light example (VCP Manual p.36):

```xml
<vcp_button>
       <skin_event_num>73</skin_event_num>
       <plc_output>
              <number>1112</number>
              <color_on>#EC1C24</color_on>
              <color_off>#81151C</color_off>
       </plc_output>
</vcp_button>
```

| Wizard Acorn Output Name | Skin Event Number | Associated LED output number |
| --- | --- | --- |
| `Worklight` | `73` | `1112` |

`skin_event_num` `73` tells CNC12 to use the logic associated with skin event 73 in the PLC
program — the Work Light ON/OFF output logic, corresponding to the WorkLight output selected in
the Acorn Wizard. The physical output the work light is wired to is the user's choice in the
Wizard; the skin event number for a particular function stays the same no matter which physical
output number is used (VCP Manual p.36).

> The manual gives the Work Light button two different pairs of numbers: `73`/`1112` here
> (VCP Manual p.36) and `20`/`1076` in the LED and image-swap examples (VCP Manual p.18, p.20).
> See [button-anatomy.md](button-anatomy.md).

## Finding the skin event number for a function

Two lookups, both in the manual (VCP Manual p.35, p.36):

1. From the button — open the button's XML file to see which `skin_event_num` it uses. The
   manual's example opens `c:cncm\resources\vcp\buttons\flood_coolant\flood_coolant.xml` [sic] and
   finds `22`, the number assigned to the Flood Pump button logic in the PLC program; the
   associated Flood Pump LED output number is `1078` (VCP Manual p.35).

   ```xml
   <vcp_button>
          <skin_event_num>22</skin_event_num>
          <plc_output>
                 <number>1078</number>
                 <color_on>#EC1C24</color_on>
                 <color_off>#81151C</color_off>
          </plc_output>
   </vcp_button>
   ```

2. From the PLC source — all `skin_events` numbers can be viewed in the PLC source file that the
   Acorn Wizard creates from the Wizard choices — for the manual's examples that file is
   `acorn_mill_plc.src`, located in the `cncm` directory. It is a text file; open it with
   Notepad ++, select "Search" then "Find" and search for `skin_event`, which brings you to the
   `System variables: Virtual Control Panel Events` section (VCP Manual p.35). With the number in
   hand, search the PLC source for it and read the related PLC logic (VCP Manual p.36).

The manual prints the first 23 skin events of the complete list contained in the PLC program source
file (VCP Manual p.35):

```
;------------------------------------------------------------------------------
; System variables: Virtual Control Panel Events
;------------------------------------------------------------------------------
;Maximum Number of Skin Events is 255

SkinSpinOverPlus_M               IS SV_SKIN_EVENT_1 ; Row 1 Column 1
SkinSpinAutoMan_M                IS SV_SKIN_EVENT_2 ; Row 1 Column 2
SkinAux1_M                       IS SV_SKIN_EVENT_3 ; Row 1 Column 3
SkinAux2_M                       IS SV_SKIN_EVENT_4 ; Row 1 Column 4
SkinAux3_M                       IS SV_SKIN_EVENT_5 ; Row 1 Column 5
SkinSpin100_M                    IS SV_SKIN_EVENT_6 ; Row 2 Column 1
SkinSpinCW_M                     IS SV_SKIN_EVENT_7 ; Row 2 Column 2
SkinAux4_M                       IS SV_SKIN_EVENT_8 ; Row 1 Column 6
SkinAux5_M                       IS SV_SKIN_EVENT_9 ; Row 2 Column 3
SkinAux6_M                       IS SV_SKIN_EVENT_10 ; Row 2 Column 4
SkinSpinOverMinus_M              IS SV_SKIN_EVENT_11 ; Row 3 Column 1
SkinSpinCCW_M                    IS SV_SKIN_EVENT_12 ; Row 3 Column 2
SkinAux7_M                       IS SV_SKIN_EVENT_13 ; Row 2 Column 5
SkinAux8_M                       IS SV_SKIN_EVENT_14 ; Row 2 Column 6
SkinAux9_M                       IS SV_SKIN_EVENT_15 ; Row 3 Column 3
SkinSpinStop_M                   IS SV_SKIN_EVENT_16 ; Row 4 Column 1
SkinSpinStart_M                  IS SV_SKIN_EVENT_17 ; Row 4 Column 2
SkinAux10_M                      IS SV_SKIN_EVENT_18 ; Row 3 Column 4
SkinAux11_M                      IS SV_SKIN_EVENT_19 ; Row 3 Column 5
SkinAux12_M                      IS SV_SKIN_EVENT_20 ; Row 3 Column 6
SkinCoolAutoMan_M                IS SV_SKIN_EVENT_21 ; Row 5 Column 1
SkinCoolFlood_M                  IS SV_SKIN_EVENT_22 ; Row 5 Column 2
SkinCoolMist_M                   IS SV_SKIN_EVENT_23 ; Row 5 Column 3........................
```

That excerpt stops at event 23, so the numbers for Aux keys 13-16 and for everything above 23 come
from the machine's own PLC source, not from this page. The `SV_SKIN_EVENT_n` side of the PLC
language is covered by `centroid-plc-programming`
([system-variables.md](../../centroid-plc-programming/reference/system-variables.md) for the
variables, [acorn-plc.md](../../centroid-plc-programming/reference/acorn-plc.md) for the
Wizard-generated source).

## Auxiliary keys: buttons that run a macro

16 skin events are used to create what are called Auxiliary Keys (the manual uses "keys" and
"buttons" interchangeably). These auxiliary keys are mapped to a macro using the Wizard VCP Aux key
configuration menu or CNC12 parameters; use one of the 16 Aux key skin event numbers to turn any
button into an auxiliary key that runs the assigned macro when pressed (VCP Manual p.37).

On the Acorn Mill VCP the buttons already defined as auxiliary keys are `M55,56,57,58`,
`Rest Home` [sic], `Park`, `Set Axis 0` and `Set All 0`. Any button that runs a macro is an
auxiliary key and is defined as such by one of those skin event numbers (VCP Manual p.37). The M56
button is Auxiliary key 11 and its XML file contains only these three lines (VCP Manual p.37):

```xml
<vcp_button>
       <skin_event_num>19</skin_event_num>
</vcp_button>
```

Assignment is done from the Acorn Wizard Preferences `VCP Aux Keys` menu: when a macro
(`mfuncXX.mac`) is assigned to an Aux key, that button runs the macro when pressed. `None` means no
macro is assigned to that Aux button — most likely it is being used with a different PLC skin event
(a non-macro PLC function such as turning an output ON or OFF) or is not in use at all
(VCP Manual p.38).

To make an auxiliary button run a particular macro, it is often easiest to edit the macro already
assigned to it: `M55`, `M56`, `M57` and `M58` are auxiliary buttons assigned to run the macros
M55, M56, M57 and M58, so opening `mfunc55.mac` with Notepad ++ and editing it is the whole job
(VCP Manual p.38). Macros are typically used for more complex actions than turning an output on or
off — for a simple on/off switch, use one of the preprogrammed outputs (worklight on/off, vacuum
on/off, laser on/off) and its button folder in the VCP resources folder (VCP Manual p.38).

Aux keys 1 through 16 are located on the VCP grid beginning with Row 1, Column 3 through Row 4
Column 6, but that is only a default position — an auxiliary button can be moved to any other
button location on the VCP, and the function goes along with it (VCP Manual p.39). The skin event
number in the button XML file determines whether a button is an Aux key, not the position of the
button (VCP Manual p.38, p.39). Moving one is an ordinary skin edit
([skin-and-grid.md](skin-and-grid.md)).

### Software axis pairing takes over Aux key 10

The `Axes Paired` button is automatically injected into the VCP button layout by the Acorn Wizard
when any two axes are software paired. Its default location is Row 3 / Column 4 and it uses the
same skin event number as Auxiliary key 10 — the Wizard "takes over" the Auxiliary 10 button
(typically pre-assigned to M55) and uses the M75 macro for the re-pairing code, so with software
paired axes the Auxiliary 10 button is dedicated to the axes-paired functionality and cannot be
used for anything else. When software pairing is selected in the Wizard pairing menu, the Wizard
removes whichever button is at Row 3, Column 4 and replaces it with the axes pairing button — or
with the M55 button if axes pairing is off — unless a custom VCP is in use. The button can be moved
like any other by editing the skin (VCP Manual p.62). Pairing itself is `centroid-acorn-install`,
[axis-pairing.md](../../centroid-acorn-install/reference/axis-pairing.md).

## Run a macro or a line of G-code directly

A way to run a macro directly from any VCP button was introduced in CNC12 v5.08. `<run>` allows a
VCP button to run either a single line of G-code or a macro immediately, with or without the need
for a cycle start button press. Insert the commands directly into the button `.xml` file
(VCP Manual p.33):

```xml
<vcp_button>
      <run>
         <line>G0 X0 Y0</line>
      </run>
</vcp_button>

<vcp_button>
      <run>
         <macro>C:\cncm\ncfiles\myMacro.cnc</macro>
      </run>
</vcp_button>
```

The manual's notes (VCP Manual p.33):

- These types of VCP buttons will only work when being pressed from the main menu of CNC12.
- Both a macro and a G-code line cannot be run at the same time.

Two `<line>` nodes in one `<run>` do not both run: the first line is run and the second is ignored
(VCP Manual p.33). Mixing `<line>` and `<macro>` in one `<run>` is also not supported — the line is
ignored completely and the macro is run instead (VCP Manual p.34). For more than one line, put the
lines in a macro file and use the `<macro>` option (VCP Manual p.33, p.34).

## Launch an external application

"Use the `<app>` command directly in the `VC{` [sic] button .xml file to launch an external
program." The manual's example is the Centroid Plasma VCP launching the Plasma Profile Manager app
(VCP Manual p.34):

```xml
<vcp_button>
   <app>C:\cncm\PlasmaProfileManager.exe</app>
</vcp_button>
```

## Worked example: re-purpose an Aux key and move it

The manual walks through turning Aux 11 (the `M56` button on the Acorn Mill VCP) into a spindle
warm-up button and putting it where the Spindle CCW button was (VCP Manual p.40, p.41):

1. Open the `M56` button folder, make a backup copy of the `M56.SVG` file, copy the new spindle
   warm-up graphic in and rename it `m56.SVG`. Restart CNC12 and the Aux 11 key shows the new
   graphic (VCP Manual p.40).
2. Edit the macro file for M56, `mfunc56.mac`, and insert the spindle warm-up commands — the manual
   prints a typical warm-up macro that steps the spindle through `S6000` to `S14000` with `G4`
   dwells between the steps (VCP Manual p.40).
3. Edit the VCP skin: delete the `<button row="3" column="2">spindle_ccw</button>` line, then change
   the `m56` button's position from column 5 to column 2. Save and restart CNC12
   (VCP Manual p.41).

> Step 1 says to open the `M56` button folder and back up `M56.SVG`, then to copy the new graphic
> "into the M55 button folder" and rename it `m56.SVG` (VCP Manual p.40).

Instead of hijacking the button, you can copy the whole `M56` folder, rename the copy and the files
inside it to `spin_warm`, `spin_warm.xml` and `spin_warm.svg`, put `spin_warm` in the skin in place
of `spindle_ccw`, delete the `m56` line, and then edit `mfunc56.mac` and the new `.svg`
(VCP Manual p.42).

## Reading and driving PLC bits

Reading a bit is a button display concern: `<plc_output>`, `<plc_input>` and `<plc_memory>` with a
`<number>` show a PLC bit's state as an LED or an image swap
([visual-states.md](visual-states.md)); a live PLC word value is [advanced.md](advanced.md).

Driving a bit is a PLC and macro concern. A button carries a skin event number or runs a macro; the
logic behind the number, the `SV_` system variables and the M-codes a macro uses to set and reset
bits are `centroid-plc-programming`
([SKILL.md](../../centroid-plc-programming/SKILL.md)).
