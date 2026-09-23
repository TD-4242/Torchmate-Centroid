# VCP visual states and styling

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`).

How a button shows state (LEDs, image swaps) and how the panel is styled (background, borders,
logos, hover and click feedback). Button tags here are children of `<vcp_button>`
([button-anatomy.md](button-anatomy.md)); skin tags are children of `<vcp_skin>`
([skin-and-grid.md](skin-and-grid.md)).

> Prose paths below use CNC12 Router's `c:\cncr` (Router Manual §1.8, p.13). The manual prints
> mill paths under `c:\cncm`; code blocks, error messages and `[sic]` quotes keep them
> unchanged, so substitute `c:\cncr` when copying one.

---

## LED indicator light color

Some VCP buttons have LED indicator lights, used primarily to indicate that the button's function
is on or activated (Rapid Over, Feed Hold) and also to indicate which choice is currently selected
(the jog speed Fast/Slow Tortoise and Hare, the Jog Incremental / Continuous selection buttons).
The LEDs are not part of the button `.SVG` graphics — the VCP overlays them onto the button
graphics automatically, and the VCP hard code automatically puts the radial gradient effect on the
LED (VCP Manual p.18).

`<color_on>` and `<color_off>` in the button's `<plc_output>` node set the ON and OFF colors, in
HEX (VCP Manual p.18):

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

`<number>` is the LED number associated with the output (VCP Manual p.25). To remove the LED
indicator light from a button entirely, delete the whole `<plc_output>` block, leaving just the
`<skin_event_num>` (VCP Manual p.18).

## Swap the image while the button is pressed

`<on_click_swap>` swaps the button image with another while the button is being clicked on, which
can be used to create a variety of UI effects. Create the swap `.SVG` in the same button folder —
the manual saves `x_positive.svg` as `x_positive_swap.svg` and recolors the background — then name
it in the tag (VCP Manual p.19):

```xml
<vcp_button>
       <skin_event_num>39</skin_event_num>
       <on_click_swap>x_positive_swap.svg</on_click_swap>
</vcp_button>
```

## Swap the image on the output function's state

Instead of an LED, the VCP can swap between two distinct `.SVG` graphics depending on the state of
the button's function — it works exactly like the LED indicator light, but with two whole
graphics. Put `<image_on>` and `<image_off>` inside `<plc_output>` in place of the color lines
(VCP Manual p.20):

```xml
<vcp_button>
       <skin_event_num>20</skin_event_num>
       <plc_output>
              <number>1076</number>
              <image_on>work_light.svg</image_on>
              <image_off>work_light_off.svg</image_off>
       </plc_output>
</vcp_button>
```

**Field-verified (CNC12, 2026-07):** `image_on` means the PLC bit is on, nothing more — it does not
mean "the active choice". For mode toggles the sense of the bit is only knowable from the PLC
program or by flipping it on the real machine, and several stock bits read the reverse of what the
label suggests (jog-mode bit ON = incremental; the slow/fast override bit ON = slow, so the "on"
image is the tortoise). Design both SVGs for the two bit states, verify on the machine, and record
the verified polarity, otherwise the next editor "fixes" it backwards.

A two-image toggle is the same mechanism as the output swap above: two SVGs on one bit
(VCP Manual p.20). The manual's indicator example carries no `<skin_event_num>` at all and acts
purely as an indicator light (VCP Manual p.21); `<skin_event_num>` is how PLC logic is assigned to
a VCP button (VCP Manual p.36).

## Indicator from a PLC input or memory bit

A VCP button can act purely as an indicator light that comes on when an input is active, by
swapping the button image based on the state of that input. The manual's example is a virtual
probe indicator with `probe_trip.svg` and `probe_clear.svg` in a `probe_indicator` folder
(VCP Manual p.21):

```xml
<vcp_button>
       <plc_input>
              <number>7</number>
              <image_on>probe_trip.svg</image_on>
              <image_off>probe_clear.svg</image_off>
       </plc_input>
</vcp_button>
```

`<number>` is the input to watch — in that example the "Probe Tripped" input definition was
assigned to input #7 with the Acorn Wizard, so the trip image shows when input 7 is
closed/activated. Place the new button on the grid with a skin line such as
`<button row="7" column="1">probe_indicator</button>` (VCP Manual p.21).

`<plc_memory>` is the same mechanism watching a memory location instead of an input
(VCP Manual p.44):

```xml
<vcp_button>
       <plc_memory>
              <number>7</number>
              <image_on>mem_on.svg</image_on>
              <image_off>mem_off.svg</image_off>
       </plc_memory>
</vcp_button>
```

## Mouse hover and click effects

Both are skin-level nodes. The default Button Hover Effect is a simple white outline around the
button, referred to in the skin as `on_hover`; the default Button Click/Finger Press effect is a
black outline, referred to as `on_click`. For both, the color and opacity can easily be changed
and the effect can be eliminated by using the word `Transparent` for the color. The opacity
control also affects the button graphic and can be used to create a darkening effect on the button
itself when clicked (VCP Manual p.32).

```xml
<on_hover>
              <opacity>100</opacity>
              <outline_color>#ffffff</outline_color>
</on_hover>
<on_click>
        <opacity>100</opacity>
        <outline_color>#000000</outline_color>
</on_click>
```

## Borders: outlines and solid fills

In the skin XML file, both outline and solid fill backgrounds can be created with the `<border>`
control, to signify related groups of buttons or for other effects. A `<border>` spans a rectangle
of the grid. A solid blue fill with a black outline around the spindle control buttons
(VCP Manual p.31):

```xml
<border>
        <column_span>2</column_span>
        <column_start>1</column_start>
        <fill>#00007F</fill>
        <row_span>4</row_span>
        <row_start>1</row_start>
        <outline_color>#000000</outline_color>
        <outline_thickness>2</outline_thickness>
</border>
```

Setting `<fill>Transparent</fill>` gives an outline-only box — the manual's second example is a
black outline around the coolant controls (VCP Manual p.31). A `<border>` can also carry a
`<plc_word>` and a `<group>` (VCP Manual p.45, p.51); see [advanced.md](advanced.md).

## VCP background color

The VCP background color defaults to the medium grey color, and can be changed to any color by
adding a `<background>` line to the skin XML file just after the first line (VCP Manual p.15):

```xml
<vcp_skin>
       <background># E9E0B7 </background>
       <border>
```

The manual prints the value with spaces inside the tag, as `# E9E0B7` (VCP Manual p.15) and
`# A6A5A0` (VCP Manual p.16). Colors in both the skin and the button XML files are expressed in
HEX color code. If the `<background>#HEXCODE</background>` line is missing from the skin, the VCP
defaults to the gray background color `#A6A5A0` (VCP Manual p.15).

For those who don't want to edit any XML files, the Centroid CNC12 color picker can also be used
to change the VCP background color (VCP Manual p.16); it opens from the CNC12 Utility menu as
`F5 Color Picker` (VCP Manual p.64).

**Field-verified (CNC12, 2026-07):** saving from CNC12's own VCP options screen rewrites the skin
file, and has been observed resetting a custom `<background>` back to the stock grey. Keep a
backup of the skin before touching that screen.

## An image as the background

The VCP supports using an image as the background in addition to solid colors; the manual's
example is a brushed stainless steel `.jpg`. Put the path inside `<background>` at the top of the
skin `.xml` file (VCP Manual p.17):

```xml
<vcp_skin>
       <background>
              c:\cncm\resources\vcp\images\stainless-steel.jpg
       </background>
```

The manual's notes (VCP Manual p.17):

- VCP image nodes can accept `.jpg` and `.png` (and possibly other, untested) image formats.
- The image should be larger in size (pixels) than the VCP for best results.
- The image upper right corner will be placed in the upper right corner of the VCP background.
- Any parts of the image that are larger than the VCP are simply cropped.
- The sample `.jpg` is included in the `c:\cncr\resources\vcp\images` folder, and an example skin
  using it is included in the `skins\custom\` folder.

## Logos and icons: static images

Static graphics can be used as icons or logos, and the VCP overlays them on top of the VCP itself.
They are in the same `.SVG` format as the button images and live in
`c:\cncr\resources\vcp\images\` — the stock examples are `coolant.SVG` and `acornlogo.SVG`. They
are controlled in the skin with `<image>` nodes (VCP Manual p.27).

```xml
<image>
       <column_span>3</column_span>
       <column_start>4</column_start>
       <row_span>1</row_span>
       <row_start>1</row_start>
       <path>C:\cncm\resources\vcp\images\acornlogo.svg</path>
</image>
```

The manual annotates the nodes: column span is the distance in columns that the image will
overlay, column start is the column number to start the span, row span is the distance in rows
that the image will overlay, row start is the position that the image will start the row span, and
`<path>` is the image filename and path (VCP Manual p.28). The coolant image takes up one button
space, so its row and column spans are both 1 (VCP Manual p.28); the Acorn logo above spans three
button lengths and is one row high (VCP Manual p.29).

To replace an image, edit the filename in `<path>` to point the VCP to a different image — for a
new logo, create the image, save it into `c:\cncr\resources\vcp\images` and edit `<path>`
(VCP Manual p.28, p.29). To delete an image, delete those lines from the skin; the space is now
available for a button if desired (VCP Manual p.28, p.30).

An `<image>` can also carry a `<group>` for switching (VCP Manual p.51); see
[advanced.md](advanced.md).
