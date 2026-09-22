# VCP troubleshooting: when the panel will not start

Source: `docs/official/centroid_vcp_users_manual.pdf` (VCP Manual, `rev 28 5-14-26`). Printed page
= PDF page; every citation below was checked against a single-page extract
(`pdftotext -layout -f N -l N docs/official/centroid_vcp_users_manual.pdf -`), and the three error
dialogs were read from the page images rendered with `pdftoppm`.

Symptoms after a skin or button edit, the messages CNC12 puts up, and how to check an edit without
the machine. The files being edited are the skin ([skin-and-grid.md](skin-and-grid.md)) and the
button folders ([button-anatomy.md](button-anatomy.md)).

> Paths the manual prints are mill paths under `c:\cncm`. On CNC12 Router the same tree lives
> under `c:\cncr` (Router Manual §1.8, p.13); the manual's own strings are quoted unchanged below.

---

## The VCP will not start after editing an XML or SVG file

The VCP will fail to start for a number of reasons. The manual's advice for beginners is to make
one change at a time and keep backup copies of files, so it is easy to revert to a working setup.
Common reasons the VCP will fail to start (VCP Manual p.56):

- typo in SVG filename (a filename is being called that doesn't exist)
- missing SVG file, the SVG file being called isn't in the correct location
- Incompatible SVG file see below for more info.
- missing XML file for a button
- typos in the button XML file

The VCP has error and warning messages for common items to give some indication of why it didn't
start. Renaming a button's SVG — or moving it, or not having it in the correct button folder —
produces a `CNC Virtual Control Panel: Error!` dialog naming the button and the two file reasons
(VCP Manual p.56):

```
Button: park
- typo in SVG filename (a filename is being called that doesn't exist)
- missing SVG file, the SVG file being called isn't in the correct location
```

Often the VCP will still start and run for simple errors such as this; in the manual's example the
Park button is simply missing when the VCP starts (VCP Manual p.56).

A missing XML file for a button produces its own message. Incorrect file names, a missing file, an
incorrect path and typos within the XML file all generate this warning (VCP Manual p.57):

```
- missing XML file for flood_coolant button
- typos in flood_coolant button XML file (bad path or filename)
```

In that case the button graphic still displays but the functionality of the button doesn't work,
since the XML file which described the button functionality is missing (VCP Manual p.57).

## The VCP does not show up at all

With a message (VCP Manual p.58):

- The skin has a bad filename — the issue could be either in the `options.xml` file or a typo in
  the skin file name itself.
- The skin is not in the location the VCP is expecting: `options.xml` may be pointing at the wrong
  place (bad path), or the skin is not where `options.xml` says.

Both produce a `Could not find file` message naming the path the VCP tried
(VCP Manual p.58):

```
Could not find file
'C:\cncm\resources\vcp\skins\acorn_mill_vcp_skin.vcp'.
```

With no warning message at all, the manual lists four causes and their fixes (VCP Manual p.58):

| Cause | Solution |
| --- | --- |
| Typos in the skin XML file | Review the XML and fix the typos. |
| The required Windows .NET framework is not installed on the PC | Run Windows update, pick the .NET framework updates and install them. |
| The PC is running in Windows Tablet mode | Set Windows to desktop mode. |
| Windows `Region` is not set to United States | Set Windows `Region` to USA. |

**Field-verified (CNC12, 2026-07):** an unsupported SVG feature belongs on that no-message list. The
renderer accepts only a subset of SVG (the subset is listed in
[button-anatomy.md](button-anatomy.md)), and a violation produces no dialog at all — CNC12 runs
normally while the VCP simply never appears. Because nothing names the offender, the way to find it
is to bisect: make throwaway copies of the skin, each carrying one suspect feature, point
`options.xml` at each in turn, restart CNC12 and see which one kills the panel. Delete the test
skins afterwards.

## The VCP looks skewed or chopped off

Set the Windows display resolution to `1920x1080` (VCP Manual p.59).

## The lower third of the VCP is missing after installing a new CNC12 version

This is caused by using the CNC12 utility feature `restore report` with a `report.zip` file from an
older version of CNC12. Restore Report works within a given version number of CNC12: building a new
CNC PC for an existing machine, the `report.zip` copies all the settings from the old computer to
the new one when the SAME version of CNC12 is installed (VCP Manual p.55).

## Upgrading CNC12 with a custom VCP in use

If the VCP has never been customized, upgrading is simple — a new stock VCP with more features is
installed and configured automatically. With a custom VCP in use, `restore report` cannot be used to
update to a newer version of CNC12, so the migration is done by hand (VCP Manual p.61):

1. Install the new version of CNC12; the installer makes a backup of the existing/working CNC12
   version.
2. For Acorn and AcornSix, use the Wizard to configure the installation as normal.
3. Edit one of the stock, Centroid-provided VCP skins of the new version with the old
   customizations — copy over any custom buttons and macros from the old install — so the result has
   the new VCP's features plus the old customizations.

A hand-edited PLC program migrates the same way: edit the new Wizard-generated (Acorn and AcornSix)
or new Centroid-provided (Oak, Allin1DC and MPU11) PLC program with the old customizations,
recompile, and customize the VCP 2.0 skin to match the application if necessary (VCP Manual p.61).

## An SVG that displays in a browser but not on the VCP

The SVG library the VCP employs supports a wide variety of SVG graphic features, but there are
limits, and one of the more common mistakes is embedding a font or opening a bitmap image (`.JPG`,
`.PNG`, `.BMP`) and saving it as a `.SVG` — which embeds the bitmap or font rather than converting
it, and does not scale or display well. The VCP wants a clean SVG that contains ONLY Vectors (lines
and arcs), Colors and Gradients (VCP Manual p.60). Convert a bitmap to vector format first;
InkScape has free tools for both manual and automatic conversion (VCP Manual p.60). The full
practice list — convert fonts to lines and arcs, rename an existing button `.svg` so the
size/artboard is correct, delete unnecessary art and hidden layers, keep art within the art board,
ungroup, and give every element a color — is in
[button-anatomy.md](button-anatomy.md) (VCP Manual p.60).

## Edit discipline

- Make one change at a time and keep backup copies of the files, so reverting to a working setup is
  easy (VCP Manual p.56).
- Restart CNC12 after a skin or button edit; the changes appear on the restart
  (VCP Manual p.8, p.13).
- Keep a backup of the skin before touching CNC12's VCP options screen: saving from it rewrites the
  skin file, a field-verified behavior recorded in [visual-states.md](visual-states.md).

## What to check before restarting

The failure lists above read as a checklist in reverse (VCP Manual p.56, p.57, p.58):

- Every name in a skin `<button>` line has a matching button folder, and each of those folders holds
  the button's `.XML`.
- Every `.SVG` a button XML names exists in that button's folder, spelled exactly as the XML
  spells it.
- The skin XML and each button XML are free of typos.
- The skin name and path in `options.xml` match the skin file that is actually installed.

## Verifying an edit without the machine

Starting with CNC12 v5.04 the VCP can be run without being connected to a CNC control board, which
makes checking graphics customizations easier. Download and unzip the "Offline Mill and Lathe
installer", run it, choose Mill or Lathe or install both, and follow the on-screen instructions. The
installed directories are `c:\Centroid_Mill_Intercon_Offline` and
`c:\Centroid_Lathe_Intercon_Offline`, and the VCP folder is in the same location as on the online
CNC controller system, `....\resources\VCP`. The Mill offline version can be used to test any Mill,
Router or Plasma VCP graphics set (VCP Manual p.63).

The manual notes it is always ideal to work on the actual control system when building a new VCP
button or feature, since that is where a macro can actually run and interact with the PLC program —
but that is not always practical, certainly for the graphics design part of a new skin
(VCP Manual p.63).
