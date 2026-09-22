# VCP skins and the button grid (the layout layer)

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`).

The VCP is editable in two layers. This file is the layout layer — the skin file that places
named buttons on a grid. The button layer, each button's own folder, is
[button-anatomy.md](button-anatomy.md); LEDs, image swaps and styling are
[visual-states.md](visual-states.md).

> Change *where* a button is -> edit the skin file (this file).
> Change *what* a button is -> edit the button folder ([button-anatomy.md](button-anatomy.md)).

> Every path the manual prints is a mill path under `c:\cncm`. On CNC12 Router the same tree
> lives under `c:\cncr` (Router Manual §1.8, p.13); the manual's own strings are quoted unchanged
> below.

---

## What a skin is, and the stock skins

The VCP is defined by a 'skin' — a text file that defines what buttons, graphics, borders and
colors make up the VCP. Centroid provides 'stock' VCP skins which can be used as-is or modified,
and CNC12 automatically installs a stock skin as a default so every CNC12 installation has a
working VCP immediately (VCP Manual p.2).

CNC12 Mill, Lathe, Router and Plasma each have their own unique stock VCP skins, pre-tailored to
the common uses and functions of those machine tools (VCP Manual p.2). Any one CNC installation
ships several stock skins that are very similar but with a few differences — for instance, stock
skins with Diagonal Jog Key functionality (VCP Manual p.4).

On Acorn and AcornSix, which stock skin to use (or start with) is selected from the drop-down menu
in the Wizard `VCP Preferences` menu (VCP Manual p.5) — see
`centroid-acorn-install`, [wizard.md](../../centroid-acorn-install/reference/wizard.md).

On Acorn the VCP is the primary operator control interface. On Oak, Allin1DC, AcornSix, Hickory
and MPU11 it can replace the hard operator's panel, work alongside it, or not be used at all; set
`P219 =1` to activate the VCP for Oak, Allin1DC, Hickory (when not using the Wizard) and MPU11
(VCP Manual p.3).

## Where skins live and which one is active

Two XML files primarily define a skin's appearance: the skin XML file, located in the
`c:\cncm\resources\vcp\skins` folder (the manual's example is `acorn_mill_vcp_skin.VCP`), and the
individual button XML files in `c:\cncm\resources\vcp\Buttons\name of button folder`
(VCP Manual p.7).

You can have any number of VCP skins. On startup the VCP is commanded to use a particular skin
with the `options.xml` file located in the `c:\cncm\resources\vcp\` folder; to change to a skin
with a different name, edit `options.xml` with the name of the skin to be used (VCP Manual p.7).
`options.xml` holds an `<ArrayOfVcpOption>` of `<VcpOption>` entries; the active skin is the
`Skin` option's `<Value>`, given without the file extension (VCP Manual p.7):

```xml
<VcpOption>
    <Name>Skin</Name>
    <Value>acorn_mill_vcp_skin</Value>
</VcpOption>
```

> The manual names the same mill skin file differently across its examples:
> `acorn_mill_vcp_skin.VCP` (p.7, p.8), `acorn_mill_skin.vcp` (p.10), `acorn_mill_skin.VCP`
> (p.22), `mill_vcp_skin.VCP` (p.27) and `acorn_skin.vcp` (p.43). Read the folder for the name
> your install actually ships.

## The button grid

The VCP buttons are laid out in an even repeating grid pattern which is used to identify the
button location: for instance the Cycle Start button is on Row 10 and Column 6, the X positive jog
key on Row 8 Column 5, the Park button on Row 2 Column 6. All the locations on the grid are
completely open for use with any button and function (VCP Manual p.6). The grid figure on that
page runs `Column 1` to `Column 6` and `Row 1` to `Row 14`.

Each placement is one `<button>` line inside `<vcp_skin>`, naming the button folder
(VCP Manual p.8):

```xml
<button row="10" column="6">cycle_start</button>
```

## Move a button

Make a copy of the skin file first — the manual's example is `acorn_mill_vcp_skin_backup.VCP` —
then open the skin with Notepad++ and edit the `row`/`column` values of the button's line
(VCP Manual p.8). Moving `cycle_start` from Row 10, Column 6 to Row 10, Column 1 is one attribute
change (VCP Manual p.8):

```xml
<!-- before -->
<button row="10" column="6">cycle_start</button>
<!-- after -->
<button row="10" column="1">cycle_start</button>
```

Then: File, Save, close CNC12 if it was open, wait a few seconds and restart CNC12 to see the
changes (VCP Manual p.8). The result is the Cycle Start button at Row 10, Column 1
(VCP Manual p.9).

## Delete a button

Deleting a button is just as simple as moving one: open the skin file, locate the button line(s)
to be deleted and delete them, then File, Save and restart CNC12 to see the changes
(VCP Manual p.10). The manual's example deletes both 4th-axis jog buttons:

```xml
<button row="7" column="2">4th_positive</button>
<button row="9" column="2">4th_negative</button>
```

**CAUTION** — the Flood, Mist, Vacuum on/off, Router Dust Collection and Router Vac Hold down
buttons work in conjunction with the `Auto / Man` button as an interlock: in Auto mode the G code
program controls those functions unless the user selects MAN. The Auto/Man button is required for
those functions to work as designed, so don't delete it unless you really don't need them — same
with the Spindle Auto/Man button (VCP Manual p.26).

If a deleted button sat inside a `<border>` group box or under a static `<image>`, adjust or
remove that element too ([visual-states.md](visual-states.md)).

## Grid size: number of rows and columns

Starting with CNC12 v5.40.0 the VCP layout number of rows and columns is definable. Two tags,
added with CNC12 v5.4+, are placed right under the `<vcp_skin>` tag (VCP Manual p.11):

```xml
<vcp_skin>
       <column_count>7</column_count>
       <row_count>15</row_count>
```

That example increases the number of columns from 6 to 7 and the number of rows from 14 to 15.
Buttons, images, backgrounds and borders can be used in the additional area just like any other
row or column. When adding rows and columns, be aware that the buttons scale proportionally within
the defined size of the VCP, so the more rows and columns, the smaller the buttons will be
(VCP Manual p.11).

## Buttons larger than one cell

Button size is controlled on the grid the same way logo and icon size is: `row span` and
`column span` tell the VCP to scale the button graphic larger than just one button space
(VCP Manual p.43). They are attributes on the skin's `<button>` line (VCP Manual p.44):

```xml
<button row="3" column="4" row_span="2" column_span="2">m55</button>
```

Make room first by deleting the buttons the enlarged one will cover (VCP Manual p.43). Sizing the
button's SVG to match the span is covered in [button-anatomy.md](button-anatomy.md); the full
worked example is in [advanced.md](advanced.md).

## What else lives at skin level

Besides `<button>` lines, the skin file holds page-wide elements, each detailed elsewhere:

- `<background>` — a solid HEX background color (VCP Manual p.15) or a `.jpg`/`.png` image
  (VCP Manual p.17). See [visual-states.md](visual-states.md).
- `<border>` — outline boxes and solid fill backgrounds that signify related groups of buttons
  (VCP Manual p.31). See [visual-states.md](visual-states.md).
- `<image>` — static logos and icons overlaid on top of the VCP (VCP Manual p.27). See
  [visual-states.md](visual-states.md).
- `<on_hover>` and `<on_click>` — mouse hover and click/finger-press effects (VCP Manual p.32).
  See [visual-states.md](visual-states.md).
- `<text>` — text displayed directly on the VCP without an image or button SVG
  (VCP Manual p.50). See [advanced.md](advanced.md).
- `<plc_word>` — live CNC data gathered from the PLC program, placed inside a `<border>` node or a
  `<vcp_button>` node (VCP Manual p.45). See [advanced.md](advanced.md).
- `<group>` child nodes and the `group="name"` attribute on a `<button>` line — switching sets of
  buttons, borders and images in and out of the same space (VCP Manual p.51); `<hide_group>` hides
  the unwanted groups at VCP startup (VCP Manual p.54). See [advanced.md](advanced.md).

After any skin edit, save and restart CNC12 to load it (VCP Manual p.8, p.10). If the VCP does not
come up afterwards, see [troubleshooting.md](troubleshooting.md).
