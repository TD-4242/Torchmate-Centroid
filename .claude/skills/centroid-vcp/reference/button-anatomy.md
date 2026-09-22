# VCP button anatomy: the folder, the XML and the SVG

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`).

This is the button layer: each button is a self-contained folder. The skin that places it on
the grid is the layout layer, [skin-and-grid.md](skin-and-grid.md); what the button *shows* is
[visual-states.md](visual-states.md).

> Paths the manual prints are mill paths under `c:\cncm`. On CNC12 Router the same tree lives
> under `c:\cncr` (Router Manual §1.8, p.13); the manual's own strings are quoted unchanged below.

---

## The button folder

Button graphics are located in the `c:\cncm\resources\vcp\Buttons\` directory and each button has
its own folder. The X axis positive jog button's files are in
`c:\cncm\resources\vcp\Buttons\x_positive`; opening that folder you find two files,
`x_positive.SVG` and `x_positive.XML`, the `.SVG` being the graphics file drawn on screen
(VCP Manual p.12).

The button XML files are typically named the same as the button itself: the Cycle Start button is
in the folder `c:\cncm\resources\vcp\Buttons\cycle_start` and is called `cycle_start.XML`
(VCP Manual p.7). That folder name is what the skin's `<button>` line names
([skin-and-grid.md](skin-and-grid.md)).

Any browser can be used to view a `.SVG` file — right click it and use "Open" or "Open with" and
pick a browser (VCP Manual p.12).

## Why SVG

"SVG" stands for "Scalable Vector Graphics", an open standard XML-based VECTOR graphic format.
Centroid chose it because it scales with no resolution loss, is lightweight, which keeps the VCP
running smooth and reliable, is easy to create and modify, and has a large online support
community. SVG documents are plain text files that describe lines, curves, shapes, colors and
text, and can be manipulated with Adobe Illustrator, Corel Draw or InkScape. Centroid recommends
InkScape (free, open source, SVG is its native format) to create trouble-free SVG files for the
VCP (VCP Manual p.12).

## Button XML tag reference

Every tag below is a child of the root `<vcp_button>` element (VCP Manual p.18, p.19). A button can
be as small as a bare `<skin_event_num>` (VCP Manual p.19); an indicator button may omit even that
(VCP Manual p.21).

| Tag | Purpose | Manual | Detailed in |
|-----|---------|--------|-------------|
| `<skin_event_num>` | Assigns PLC logic to the button — CNC12 knows what function you want for the button from this number. | p.36 | [actions.md](actions.md) |
| `<plc_output>` with `<number>`, `<color_on>`, `<color_off>` | LED indicator light color for the output's ON and OFF state. | p.18 | [visual-states.md](visual-states.md) |
| `<plc_output>` with `<number>`, `<image_on>`, `<image_off>` | Swap the whole graphic on the output function's ON/OFF state. | p.20 | [visual-states.md](visual-states.md) |
| `<plc_input>` with `<number>`, `<image_on>`, `<image_off>` | Indicator: swap the graphic on a PLC input's state. | p.21 | [visual-states.md](visual-states.md) |
| `<plc_memory>` with `<number>`, `<image_on>`, `<image_off>` | Indicator: swap the graphic on a PLC memory location's state. | p.44 | [visual-states.md](visual-states.md) |
| `<on_click_swap>` | Swap the button image while the button is being clicked/pressed. | p.19 | [visual-states.md](visual-states.md) |
| `<run>` with `<line>` or `<macro>` | Run a single line of G-code, or a macro, immediately. | p.33 | [actions.md](actions.md) |
| `<app>` | Launch an external program. | p.34 | [actions.md](actions.md) |
| `<plc_word>` | Display a live PLC word value on top of the button. | p.45 | [advanced.md](advanced.md) |
| `<switch>` with `<switch_on>`/`<switch_off>`, `<remove>`, `<add>`, `<image_on>`/`<image_off>` | Switch groups of buttons, borders and images in and out on press. | p.53 | [advanced.md](advanced.md) |

The stock Work Light button is a `<skin_event_num>` plus an LED (VCP Manual p.18):

```xml
<vcp_button>
       <skin_event_num>20</skin_event_num>
       <plc_output>
              <number>1076</number>
              <color_on>#EC1C24</color_on>
              <color_off>#81151C</color_off>
       </plc_output>
</vcp_button>
```

> The manual gives the Work Light button two different pairs of numbers: `skin_event_num` `20`
> with `plc_output` `1076` in the LED and image-swap examples (VCP Manual p.18, p.20), and
> `skin_event_num` `73` with `plc_output` `1112` in the explanation of what a skin event number is
> (VCP Manual p.36). Take the numbers for your machine from its own PLC source file, not from the
> examples.

## Change an existing button's graphic

Navigate to the button's folder and make a backup copy of its `.svg`. Open the original with a
vector graphics editing software such as Inkscape, change it (the manual's example swaps the jog
key's safety-yellow background and black text for a black background and white text), and be sure
to save the edited file in the proper folder — for `x_positive`, that is
`c:\cncm\resources\vcp\Buttons\x_positive`. Restart CNC12 to see the changes, then repeat the
process for the other buttons (VCP Manual p.13, p.14).

## SVG practices the VCP expects (VCP Manual p.60)

The SVG library the VCP employs supports a wide variety of SVG features but there are limits. The
VCP wants a clean SVG that contains ONLY Vectors (lines and arcs), Colors and Gradients; avoid
embedded bitmap images and fonts. Opening a bitmap (`.JPG`, `.PNG`, `.BMP`) and saving it as
`.SVG` does not convert it to vectors — it embeds the bitmap, which does not scale or display well
and is often fuzzy (VCP Manual p.60).

The manual's general SVG advice (VCP Manual p.60):

- Convert all fonts (words) to lines and arcs before saving — "Object to Path" in Inkscape,
  "create/convert to outlines" in Adobe Illustrator.
- Open the existing button `.svg` file, rename it and then modify it (this way the size/artboard
  is correct).
- Delete all unnecessary art, and all unused/unnecessary/hidden layers.
- Keep all art within the art board.
- If a graphic misbehaves, keep ungrouping until the `.svg` displays on the VCP — convoluted
  grouping can cause issues.
- Look for elements with no color or no line thickness and delete them; make sure all elements
  have a color assigned, since an uncolored element may default to white on screen and then not
  display properly in the VCP.

The full symptom list for a VCP that will not start is in
[troubleshooting.md](troubleshooting.md).

### Field notes on sizing and text

No manual page states the following; they are board-agnostic behaviors of the VCP renderer.

- **Field-verified (CNC12, 2026-07):** rendered size tracks the SVG's declared
  `width`/`height`/artboard — the graphic is drawn at its declared size rather than stretched to
  fill the cell, and the skin's `row_span`/`column_span` enlarge the *cell* only, so a multi-cell
  button needs a full-span artboard or it renders small inside a big cell. Keep `width`, `height`
  and `viewBox` on the `<svg>` element; for a span, copy a stock SVG of the same span to get the
  numbers right, and to show normal-size art centered in a larger span pad the full-span artboard
  rather than stretching the art. This is why the manual's "rename an existing button `.svg` so
  the size/artboard is correct" advice works.
- **Field-verified (CNC12, 2026-07):** `text-anchor` is effectively ignored. Position button text
  with an explicit `x` — either convert the text to paths, or compute the left-edge `x` from the
  character advance widths of a font actually installed on the control PC.
- **Field-verified (CNC12, 2026-07):** only a subset of SVG renders. `<filter>` is not supported,
  gradients must use absolute `userSpaceOnUse` coordinates, and transforms are limited to a single
  `matrix()`. A violation can take down the whole VCP silently — see
  [troubleshooting.md](troubleshooting.md).

## Create a new button

The manual's worked example creates a `laser_set_xy` button (VCP Manual p.22-23):

1. Navigate to `c:\cncm\resources\vcp\Buttons` and right click "New", "Folder"; call it
   `laser_set_xy`.
2. Copy an existing button's XML into the new folder and rename it `laser_set_xy.XML` — the
   manual copies the `M56` button XML.
3. Create the graphic with InkScape, place the `.SVG` in the `laser_set_xy` folder and name it
   `laser_set_xy`.
4. Edit the skin XML file and insert (or modify an existing) `<button>` line to assign the
   location where the new button should appear. The manual replaces the `m56` line:
   `<button row="3" column="5">laser_set_xy</button>`.
5. Save and restart CNC12; the new graphic appears on the VCP.

Because the XML was copied from the `M56` button, pressing it still runs the stock M56 macro. The
manual's fix is to edit that macro — `mfunc56.mac`, located in the `c:\cncm` folder — with the
commands the new button should run (VCP Manual p.23).

> The prose says to "keep the location (Row 4 , Column 4) the same", but the skin excerpt on the
> same page shows the `m56` line at `row="3" column="5"` both before and after the edit
> (VCP Manual p.22).

### Point a copied button at a different function

To make a copied button drive an output instead of running the copied macro, change its
`<skin_event_num>` to the skin event number associated with that output. The manual's example
copies the `M57` button (`<skin_event_num>67</skin_event_num>`, which the Acorn PLC program
assigns to the m-code M57) into a `laser_on_off` folder and re-points it (VCP Manual p.24-25):

| Wizard Acorn Output Name | Skin Event Number | Associated LED output number |
| --- | --- | --- |
| `LaserAlignActivate` | `207` | `1127` |

```xml
<vcp_button>
       <skin_event_num>207</skin_event_num>
       <plc_output>
              <number>1127</number>
              <color_on>#EC1C24</color_on>
              <color_off>#81151C</color_off>
       </plc_output>
</vcp_button>
```

All skin event numbers can be found in the Acorn PLC source file (`acorn_mill_plc.src`)
(VCP Manual p.25) — see `centroid-plc-programming`,
[acorn-plc.md](../../centroid-plc-programming/reference/acorn-plc.md). Choosing the number is
covered in [actions.md](actions.md).
