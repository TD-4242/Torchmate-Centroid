---
name: centroid-vcp
description: "Use when customizing a Centroid CNC12 Virtual Control Panel (VCP) on Acorn or other CNC12 controls - moving, creating, or deleting buttons; button XML/SVG and graphics; LED colors and image swaps; logos, borders, backgrounds, hover/touch effects; wiring a button to a skin event, macro, app, or PLC bit; big buttons and live PLC-word displays; and diagnosing a VCP that will not load. Generic to the Centroid VCP. Source: VCP 2.0 Users Manual rev28 plus labeled field-verified notes."
---

# Centroid VCP Customization

## When to use / when not

Use this skill to **customize the Virtual Control Panel**: moving, creating and deleting buttons,
editing button `.XML` and `.SVG` files, LED colors and image swaps, logos, borders, backgrounds,
hover and touch effects, binding a button to a skin event, macro or external app, big buttons and
live PLC-word displays, and diagnosing a VCP that will not load. It is a generic capture of the
official **VCP 2.0 Users Manual** (`rev 28 5-14-26`), which covers Acorn CNC, Acorn Plasma,
AcornSix, Hickory, Oak, Allin1DC and MPU11 (VCP Manual p.1) -- not specific to any one machine.

**Do not use this skill** for the PLC logic behind a skin event number, `SV_*` system variables,
PLC word definitions, or macro-to-PLC interaction -- use `centroid-plc-programming`
([SKILL.md](../centroid-plc-programming/SKILL.md)).

**Do not use this skill** for *operating* the control -- the VCP button legend, menus, jogging,
part zeros, running jobs, G/M-code and parameter lookups -- use `centroid-cnc12-router-ops`
([SKILL.md](../centroid-cnc12-router-ops/SKILL.md)).

**Do not use this skill** for Acorn hardware installation, wiring, or Wizard configuration pages
(including the Wizard `VCP Preferences` skin drop-down and `VCP Aux Keys` assignment) -- use
`centroid-acorn-install` ([SKILL.md](../centroid-acorn-install/SKILL.md)).

## Essentials

The VCP lets the CNC user employ a mouse and/or a finger (touch screen monitor) as a Human
Interface to the CNC controller (VCP Manual p.2). On Acorn the VCP is the primary operator control
interface; on Oak, Allin1DC, AcornSix, Hickory and MPU11 it can replace the hard operator's panel,
work alongside it, or not be used at all, and `P219 =1` activates it for Oak, Allin1DC, Hickory
(when not using the Wizard) and MPU11 (VCP Manual p.3).

### Two layers

The VCP is defined by a 'skin' -- a text file that defines what buttons, graphics, borders and
colors make up the VCP (VCP Manual p.2). Customization is done mainly through a set of `.XML`
files, macros and `.SVG` image files for the graphics; the Acorn Mill default skin is primarily
defined by two XML files, the skin XML file and the individual button XML files
(VCP Manual p.7).

> Change *where* a button is -> edit the skin file ([skin-and-grid.md](reference/skin-and-grid.md)).
> Change *what* a button is -> edit the button folder ([button-anatomy.md](reference/button-anatomy.md)).

Buttons sit on an even repeating grid pattern which is used to identify the button location -- the
Cycle Start button is on Row 10 and Column 6, the X positive jog key on Row 8 Column 5, the Park
button on Row 2 Column 6 (VCP Manual p.6). One `<button>` line places one button folder
(VCP Manual p.8):

```xml
<button row="10" column="6">cycle_start</button>
```

Each button has its own folder holding two files, for example `x_positive.SVG` and
`x_positive.XML`, the `.SVG` being the graphics file drawn on screen (VCP Manual p.12).

After any skin or button edit: File, Save, close CNC12 if it was open, wait a few seconds and
restart CNC12 to see the changes (VCP Manual p.8).

### Navigating the VCP files

CNC12 Router installs to `c:\cncr` (Router Manual §1.8, p.13), so the VCP tree is:

```
c:\cncr\resources\vcp\options.xml            which skin is active
c:\cncr\resources\vcp\skins\                 the skin files
c:\cncr\resources\vcp\Buttons\<folder>\      one folder per button: its .XML and its .SVG
c:\cncr\resources\vcp\images\                static logo, icon and background images
```

From a shell on the control PC:

```cmd
type c:\cncr\resources\vcp\options.xml
dir c:\cncr\resources\vcp\skins
dir c:\cncr\resources\vcp\Buttons
findstr /n "<button" c:\cncr\resources\vcp\skins\<skin>.vcp
```

> The manual prints mill paths under `c:\cncm` -- the skin folder as
> `c:\cncm\resources\vcp\skins`, the button folders as
> `c:\cncm\resources\vcp\Buttons\name of button folder` and `options.xml` in
> `c:\cncm\resources\vcp\` (VCP Manual p.7), and the images folder as
> `c:\cncm\resources\vcp\images\` (VCP Manual p.27). On CNC12 Router the same tree lives under
> `c:\cncr`.

Which stock skin to use (or start with) is selected on Acorn and AcornSix from the drop-down menu
in the Wizard `VCP Preferences` menu (VCP Manual p.5); the file the VCP actually loads at startup
is the `Skin` value in `options.xml` (VCP Manual p.7).

### Button XML tags at a glance

Every tag below is a child of the root `<vcp_button>` element.

| Tag | Purpose | Manual | Detailed in |
|-----|---------|--------|-------------|
| `<skin_event_num>` | Assigns PLC logic to the button -- CNC12 knows what function you want for the button from this number. | p.36 | [actions.md](reference/actions.md) |
| `<plc_output>` with `<number>`, `<color_on>`, `<color_off>` | LED indicator light color for the output's ON and OFF state. | p.18 | [visual-states.md](reference/visual-states.md) |
| `<plc_output>` with `<number>`, `<image_on>`, `<image_off>` | Swap the whole graphic on the output function's ON/OFF state. | p.20 | [visual-states.md](reference/visual-states.md) |
| `<plc_input>` with `<number>`, `<image_on>`, `<image_off>` | Indicator: swap the graphic on a PLC input's state. | p.21 | [visual-states.md](reference/visual-states.md) |
| `<plc_memory>` with `<number>`, `<image_on>`, `<image_off>` | Indicator: swap the graphic on a PLC memory location's state. | p.44 | [visual-states.md](reference/visual-states.md) |
| `<on_click_swap>` | Swap the button image while the button is being clicked/pressed. | p.19 | [visual-states.md](reference/visual-states.md) |
| `<run>` with `<line>` or `<macro>` | Run a single line of G-code, or a macro, immediately. | p.33 | [actions.md](reference/actions.md) |
| `<app>` | Launch an external program. | p.34 | [actions.md](reference/actions.md) |
| `<plc_word>` | Display a live PLC word value on top of the button. | p.45 | [advanced.md](reference/advanced.md) |
| `<switch>` with `<switch_on>`/`<switch_off>`, `<remove>`, `<add>`, `<image_on>`/`<image_off>` | Switch groups of buttons, borders and images in and out on press. | p.53 | [advanced.md](reference/advanced.md) |

Skin-level nodes -- `<background>`, `<border>`, `<image>`, `<on_hover>`, `<on_click>`, `<text>`,
`<plc_word>`, `<group>` and `<hide_group>` -- are listed with their pages in
[skin-and-grid.md](reference/skin-and-grid.md).

The manual's own advice for beginners: make one change at a time and keep backup copies of files,
so it is easy to revert to a working setup (VCP Manual p.56).

## Reference router

| Reference file | Look here when... |
| --- | --- |
| `reference/skin-and-grid.md` | You're moving, deleting or re-sizing a button, picking or switching the active skin in `options.xml`, changing the grid's row and column count, or want the list of what else lives at skin level |
| `reference/button-anatomy.md` | You're creating a copied button, changing a button's graphic, or need the button folder layout, the `<vcp_button>` tag table, or the SVG practices the VCP expects |
| `reference/visual-states.md` | You're setting LED colors, swapping images on a PLC output/input/memory bit or on click, or styling the panel with backgrounds, borders, logos, icons and hover/click effects |
| `reference/actions.md` | You're wiring a button to PLC logic with a skin event number, turning a button into an Aux key that runs a macro, running a line of G-code with `<run>`, or launching an external app with `<app>` |
| `reference/advanced.md` | You need big multi-cell buttons, live PLC-word displays and their styling nodes, static `<text>`, or `<group>`/`<hide_group>` switching |
| `reference/troubleshooting.md` | The VCP will not start, shows no panel at all, looks skewed, or lost its lower third after an upgrade -- plus running the VCP offline to check an edit |

## Field-verified facts

Board-agnostic behaviors of the VCP renderer that no manual page states. Each is labeled
`Field-verified (CNC12, 2026-07)` in the reference file that holds it; the full note is there.

| Field-verified claim | Where |
| --- | --- |
| Rendered size tracks the SVG's declared `width`/`height`/artboard -- the graphic is drawn at its declared size rather than stretched to fill the cell. | [button-anatomy.md](reference/button-anatomy.md) |
| A multi-cell button needs a full-span artboard. The skin's `row_span`/`column_span` enlarge the *cell*; the SVG must declare the spanned size itself or it renders small inside a big cell. | [button-anatomy.md](reference/button-anatomy.md) |
| `text-anchor` is effectively ignored. Position button text with an explicit `x`. | [button-anatomy.md](reference/button-anatomy.md) |
| Only a subset of SVG renders. `<filter>` is not supported, gradients must use absolute `userSpaceOnUse` coordinates, and transforms are limited to a single `matrix()`. | [button-anatomy.md](reference/button-anatomy.md) |
| `image_on` means the PLC bit is on, nothing more -- it does not mean "the active choice". | [visual-states.md](reference/visual-states.md) |
| Saving from CNC12's own VCP options screen rewrites the skin file, and has been observed resetting a custom `<background>` back to the stock grey. | [visual-states.md](reference/visual-states.md) |
| `<type>Float</type>` reads the `FW` register of the same `<number>`, not the integer word. | [advanced.md](reference/advanced.md) |
| A font named in `<font>` must be installed on the Windows control PC *for all users*, or the VCP process does not see it and silently substitutes another font, shifting the text. | [advanced.md](reference/advanced.md) |
| `<percentage>true</percentage>` can overlap the digits at some font and size combinations. | [advanced.md](reference/advanced.md) |
| An unsupported SVG feature produces no dialog at all -- CNC12 runs normally while the VCP simply never appears. | [troubleshooting.md](reference/troubleshooting.md) |

## Useful resources

The manual's own Resources page (VCP Manual p.64):

- Notepad ++: https://notepad-plus-plus.org/ -- "A free powerful text editor used for editing VCP
  XML files. Also useful for editing G and M code programs and macros."
- InkScape: https://inkscape.org/ -- "A free Vector Drawing program. Great for editing and
  creating VCP buttons and graphics. Also useful for CNC Art work."
- YouTube: YouTube.com -- search on "Inkscape for Beginners", "InkScape bitmap to vector" or
  "Inkscape convert image to vector".
- Hex code Color Picker: w3schools.com -- hex color picker website.
- Centroid Technical Support Forum, which has a Custom VCP thread specifically discussing custom
  VCP's with examples: https://centroidcncforum.com/index.php
- Centroid CNC12 software download page:
  https://www.centroidcnc.com/centroid_diy/centroid_cnc_software_downloads.html
- CNC12's Color Picker App, which changes CNC12 colors to match a custom VCP -- open it from the
  CNC12 Utility menu `F5 Color Picker`; video link https://youtu.be/pdNaSI-AtGo
