# Advanced VCP displays: PLC words, text and switching

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`).

The heavier, less common features: live PLC data on the panel, plain text without an image, and
groups of objects switched in and out of the same space. Buttons that span several grid cells are
a skin-file edit, in [skin-and-grid.md](skin-and-grid.md) — which also holds the skin tags, the
children of `<vcp_skin>`. Button tags are children of `<vcp_button>`
([button-anatomy.md](button-anatomy.md)).

> Prose paths below use CNC12 Router's `c:\cncr` (Router Manual §1.8, p.13). The manual prints
> mill paths under `c:\cncm`; code blocks, error messages and `[sic]` quotes keep them
> unchanged, so substitute `c:\cncr` when copying one.

---

## Buttons larger than one cell

Button spans are a skin-file edit: `row_span` and `column_span` on the skin's `<button>` line, with
the manual's worked `m55` example, are in [skin-and-grid.md](skin-and-grid.md).

The manual describes the spans as scaling the button graphic larger than just one button space
(VCP Manual p.43). Sizing the button's own SVG to match the span is a separate job — the
field-verified note in [button-anatomy.md](button-anatomy.md) records that the spans enlarge the
*cell* while the SVG must declare the spanned size itself.

## Live PLC data: `<plc_word>`

New for CNC12 VCP v5.0+, PLC Words allow the VCP to display CNC data on the panel in real time,
gathered from the CNC's PLC program. The first use of the feature was the Feedrate Override
percentage value, which was previously hard coded in Acorn VCP 4.82 and earlier and Oak/Allin1DC
VCP 4.22 and earlier. PLC words can be displayed on top of any VCP button or on the VCP borders: add
the `plc_word` node within a `border` node or a `vcp_button` node (VCP Manual p.45).

The stock Acorn Mill skin displays the current feedrate override percentage like this
(VCP Manual p.45):

```xml
<border>
       <column_span>3</column_span>
       <column_start>4</column_start>
       <fill>Transparent</fill>
       <row_span>1</row_span>
       <row_start>11</row_start>
       <outline_color>Transparent</outline_color>
       <outline_thickness>1</outline_thickness>
       <plc_word>
              <number>31</number>
              <color>#000000</color>
              <fontsize>22</fontsize>
              <font>Sergio UI</font>
              <fontstyle>bold</fontstyle>
              <verticalalignment>bottom</verticalalignment>
              <horizontalalignment>center</horizontalalignment>
              <marginbottom>-5</marginbottom>
              <percentage>true</percentage>
       </plc_word>
</border>
```

> The example blocks print `<font>Sergio UI</font>` (VCP Manual p.45, p.49, p.53), while the prose
> and the `<text>` example give the default font as `Segoe UI` (VCP Manual p.49, p.50).

### Which word to display

`<number>` identifies which PLC word to display — `<number>31</number>` above. These PLC word
numbers are found in the PLC program itself (VCP Manual p.45), under the Word Definitions section
of the PLC program source file, `c:\cncr\XXXX.src`, which is a text file (VCP Manual p.46). For
example `W31` is Word #31, which equals the current Feedrate Override Percentage value
(VCP Manual p.46). Commonly used stock PLC word values (VCP Manual p.46):

| Value | Word definition |
| --- | --- |
| Spindle Speed Override % | `SpinOverride_W is W19` |
| Feedrate Override % | `FinalFeedOverride_W is W31` |
| Target Voltage Override % | `TargetVoltage_W is W7` |
| Current Carousel Position | `CurrentCarouselPosition_W is W54` |
| Current Turret Position | `CurrentTurretPosition_W is W52` |

Those five are not the whole list: the manual reprints the stock `Word Definitions` block of a
typical Acorn Mill PLC program (`cncm/acorn_mill_plc.src`), roughly `W1` to `W89`
(VCP Manual p.46-47). Take the authoritative list from the machine's own `.src`.

Users can also create their own word values. The manual's example tracks a 4-tool lathe turret:
define the word in the Word Definitions section (`CurrentTurretPosition_W IS W52`), add the logic
that assigns it (`IF TurretInput1 THEN CurrentTurretPosition_W = 1` and so on for inputs 2-4),
compile the PLC program, then add `<plc_word>` with `<number> 52</number>` to the XML file of the
button the value should appear on (VCP Manual p.48).

Save all files, shut down and restart CNC12; when the turret changes tools the current position is
displayed on that button. Any value in the PLC, once assigned a word value, can be displayed this
way — the manual names an analog input from a pressure gauge, calculated math done by the PLC, and
system variables as further examples (VCP Manual p.48). The PLC side is `centroid-plc-programming`
([syntax.md](../../centroid-plc-programming/reference/syntax.md) for word definitions and stage
logic).

### `<plc_word>` styling nodes

All defaults and value lists below are from VCP Manual p.49.

| Node | Sets | Values and default |
| --- | --- | --- |
| `<type>` | what type of PLC word is displayed | `Int` (such as 10), `Float` (such as 10.1234, valid values -2147483648 to 2147483647), and also available but typically not used `Double` (64 bit) and `DoubleFloat` (64 bit), range -9223372036854775808 to 9223372036854775807. Defaults to Integer type if no type is set. |
| `<significant>` | digits after the decimal point | For all types except `Int`; defaults to `2` if the node is not used. |
| `<color>` | color of the text | Hex code; default `#000000`. |
| `<font>` | font of the text | Default `Segoe UI`; allowed fonts are the Microsoft font list at <https://learn.microsoft.com/en-us/typography/font-list/>, and the name must be entered exactly as it is displayed in the list, spaces and all. |
| `<fontsize>` | font size | Integer; default `16`. |
| `<fontstyle>` | style the text is displayed in | `bold`, `italics`, `normal` or `oblique`; defaults to normal. |
| `<verticalalignment>` | vertical alignment | `top`, `center` or `bottom`; default bottom. |
| `<horizontalalignment>` | horizontal alignment | `left`, `right` or `center`; default left. |
| `<marginbottom>`, `<margintop>`, `<marginleft>`, `<marginright>` | margins on the text, for fine tuning where it is displayed | Integer; default `0`. |
| `<percentage>` | adds a percentage sign to the end of the word value | `true` = display the `%` sign. |

> The `<type>` bounds are as p.49 prints them, but they are the signed 32-bit and 64-bit
> *integer* limits. The PLC Manual defines `FW` and `DFW` as 32-bit and 64-bit floating-point
> words (PLC Manual, PDF p.13; see
> [resources.md](../../centroid-plc-programming/reference/resources.md)), so do not treat these as
> float ranges.

> The `<type>` example on p.49 is introduced as "PLC word set to Integer value and 5 decimal
> places" but the block itself prints `<type>float</type>` with `<significant>5</significant>`
> (VCP Manual p.49).

### Field notes on PLC word display

No manual page states the following; they are board-agnostic behaviors of CNC12 and the VCP.

- **Field-verified (CNC12, 2026-07):** `<type>Float</type>` reads the `FW` register of the same
  `<number>`, not the integer word — `<number>11</number>` with type float displayed `FW11`, while
  the default `Int` type reads `W11`. A float the PLC computes in `FWn` is therefore directly
  displayable with no integer scaling.
- **Field-verified (CNC12, 2026-07):** a font named in `<font>` must be installed on the Windows
  control PC *for all users* (right-click the font, "Install for all users"), or the VCP process
  does not see it and silently substitutes another font, shifting the text.
- **Field-verified (CNC12, 2026-07):** `<percentage>true</percentage>` can overlap the digits at
  some font and size combinations. Leaving it off and placing the `%` as a separate `<text>` in the
  same `<border>`, nudged with a margin node, avoids the overlap.

## Static text without an image

`<text>` is a way to directly display text onto the VCP without the need of an image — used in the
skin `.vcp` XML file for cases where text is wanted when not using an image or button SVG. It goes
inside a `<border>`, which supplies the position and span (VCP Manual p.50):

```xml
<border>
      <column_span>2</column_span>
      <column_start>1</column_start>
      <fill>Transparent</fill>
      <row_span>1</row_span>
      <row_start>8</row_start>
      <text>
         <content>This is sample text&#13;With a new line</content>
         <fontsize>20</fontsize>
         <color>#ffffff</color>
         <font>Segoe UI</font>
         <horizontalalignment>center</horizontalalignment>
         <verticalalignment>center</verticalalignment>
      </text>
</border>
```

The manual's notes: `&#13;` is a carriage return (adds a new line), and the feature functions in a
similar fashion to the VCP feature called `plc_word` (VCP Manual p.50).

## Groups and switching

The switching feature gives the VCP the ability to have different buttons, borders and images
defined to occupy the same space but only appear when wanted. To use it, each button, border and
image (referred to collectively as an "object") requires a group to be defined in the `.vcp` XML
file; that group can then be called on when it should be displayed (VCP Manual p.51).

Groups for borders and images are defined with a child node; groups for buttons are defined with an
attribute (VCP Manual p.51):

```xml
<border>
 <group>group_name</group>
</border>
<image>
 <group>group_name</group>
</image>
<button row="Y" column="X" group="group_name"></button>
```

A common use is the rapid-to-feedrate control swap: with Rapid Override ON the override controls get
a blue background and the display swaps to rapid override %, with it OFF a grey background and the
feedrate override % display (VCP Manual p.51). The stock skins with the word "rapid" in them swap
the background image, override text and PLC word on the Rapid/Feed selection made with the Rapid
Feed toggle button (VCP Manual p.52). Multiple borders, images and buttons can be added to any given
group — `acorn_router_vcp_skin.vcp` puts both the rapid override border and the border carrying its
`<plc_word>` into `rapid_group` (VCP Manual p.52, p.53).

What to do with those groups is defined in the button `.XML` itself. The manual's `rapid_feed.xml`
(VCP Manual p.53):

```xml
<vcp_button>
       <switch>
          <switch_on>
             <remove>feed_group</remove>
             <remove>feed_button_group</remove>
             <add>rapid_group</add>
             <image_on>rapid_feed_lit.svg</image_on>
          </switch_on>
          <switch_off>
             <remove>rapid_group</remove>
             <add>feed_group</add>
             <add>feed_button_group</add>
             <image_off>rapid_feed.svg</image_off>
          </switch_off>
          <remove>linked_group</remove>
          <add>unlinked_group</add>
       </switch>
    </vcp_button>
```

## Hiding groups at startup

For VCP start up the `<hide_group>` is often used: this node is inserted into the skin (`.vcp` file)
to hide all of the groups that are unwanted at start up. If this is not done, all objects will be
visible at VCP startup, resulting in a mess. The manual's example file
`acorn_router_vcp_rapid_skin.vcp` hides the rapid group beginning on line 121, because the VCP
defaults to the feedrate override control being displayed at startup (VCP Manual p.54):

```xml
<hide_group>
        <group>rapid_group</group>
</hide_group>
```

The same page then gives the convention as (VCP Manual p.54):

```xml
<hideGroup>
       <group>group_name_1</group>
       <group>group_name_2</group>
</hideGroup>
```

> The manual spells this node both ways on the same page: `<hide_group>` in the prose and in the
> line-121 excerpt, and `<hideGroup>` in the "Convention to hide on start up" block and the Note
> under it (VCP Manual p.54).

There is no limit on how many groups can be hidden, and no limit on how many objects can be added
to the VCP, but performance may suffer as more objects are added — the manual estimates decreased
performance would start to become visible at approximately 1000 objects (VCP Manual p.54).
