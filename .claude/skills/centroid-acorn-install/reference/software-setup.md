# Acorn Software Setup Reference

Windows configuration, CNC12 install, licensing, the communications stress test,
configuration reports, and the bench-test software procedures for the Acorn controller.
Source: Acorn Install Ch 3, Ch 4, App A.

## Windows 10/11 configuration

(Acorn Install §3.1, p.12-13)

Only Windows 10 and 11 are supported; Windows 8.1, 7 and older, macOS, and Linux are not.
A Centroid-supplied CNCPC ships with Windows already configured and CNC12 preinstalled —
skip this section. A self-built or self-bought PC must meet the prerequisites on the
Acorn quick start guide page, and can be configured for CNC use with the free **Centroid
CNC PC Tuner** app; Tech Bulletin TB309 covers the same configuration.

Before installing CNC12, uninstall (not just disable) all anti-virus, anti-malware, and
3rd-party firewall software, then reboot — about 99% of CNC12-to-Acorn communication
problems are caused by such software. The built-in Windows Firewall works fine with CNC12
if access is allowed as specified in Appendix B.

## CNC12 installation

(Acorn Install §3.2, p.14-21). With the Acorn in bench configuration and powered up with a
heartbeat (§2.2), install as follows:

1. Download the latest CNC12 installer (`centroid_acorn_cnc12_vX.xx_installer`), extract
   it, and copy the extracted installer to the desktop.
2. The CNC PC and Acorn must be powered up and connected via the shielded Ethernet cable
   for the entire install. Double-click the installer to start.
3. Past Windows Defender SmartScreen ("More info" -> "Run anyway") and User Account
   Control ("Yes"), accept the software license agreement ("I Agree").
4. Choose whether to install a desktop shortcut icon.
5. Select **Acorn** as the control board, then select the machine type: `CNC12 Mill`,
   `Lathe`, `Router`, or `Plasma` (the manual documents the rest of the install assuming a
   mill).
6. Select default units, `Imperial` or `Metric`, and click Install.
7. **Network Adapter Setup** (Acorn still powered and connected): select the network
   adapter connected to the Acorn from the list, click Next, then Yes to change that
   adapter's IP address. Centroid recommends a PC with two Ethernet ports — one for the
   Acorn, one for internet access — and installing with the port that shows no network
   access, so CNC12 binds the correct one. Never connect the Acorn through a USB-to-Ethernet
   adapter.
8. If CNC12 detects a CNC PC Ethernet port already set up for CNC use, it asks whether to
   reuse it — Yes to reuse, No to pick a different port.
9. Click Finish to complete the install.
10. Start CNC12 from the desktop icon. On first start it may show a firmware-update
    message while it updates the Acorn's BBG firmware to match the installed CNC12
    version — do not power off the Acorn while this runs. The CNC12 main screen then
    appears.

## License file

(Acorn Install §3.3, p.22)

1. Save the emailed `license.dat` file to the CNC PC desktop from a Windows PC (an Apple
   computer corrupts the file).
2. With the Acorn powered up and CNC12 running: `F7` Utility -> `F8` Option -> `F2` Import
   License, select `license.dat`, and click Open. CNC12 confirms the license was
   successfully imported.

## Communications stress test

(Acorn Install §3.4, p.23-26)

1. Press the Reset button to clear the reset trip state.
2. Home CNC12 with Cycle Start. By default CNC12 installs in `Simple Homing` mode, which
   sets home at the current position with no motion.
3. Load `stressTest.cnc` (`F2` Load).
4. Press Cycle Start to run it and wait for the results. If the test fails, do not
   proceed — resolve the communication issue first.

Causes of communication errors (p.26): an RJ45 bulkhead connector; a non-shielded Ethernet
cable, or a shielded cable that is itself bad; a USB-to-Ethernet adapter; outdated Ethernet
adapter drivers (use the manufacturer's drivers); any anti-virus software installed (must
be uninstalled, not just disabled); the Windows Firewall blocking `cncm.exe`, `cncr.exe`,
or `cnct.exe`; power-saving or auto-IP behavior resetting the adapter's address (uncheck
"Obtain an IP address automatically" and select "Use the following IP address" instead);
and on some Intel adapters, the advanced "speed and duplex" setting needing to be changed
from auto-negotiate to `100Mbps half duplex`.

## Configuration reports

(Acorn Install §3.5, p.27)

CNC12 can capture all CNC and machine-specific configuration settings plus operation logs
into a `report.zip` file, usable to restore settings after a failed HD/PC or to roll an
installation back to a previously known-good state. CNC12 auto-generates a report weekly;
a fresh one can be created any time:

1. `F7` Utility
2. `F7` Create Report
3. Choose the save location in the dialog that appears.

> Once the machine is configured and running, back up `report.zip` to a USB memory stick
> or network drive, in a safe location off the CNCPC.

## CNC12 software configuration

(Acorn Install §4.1, p.28-29)

With the Acorn powered on with a heartbeat and the Ethernet cable connected, start CNC12
from the desktop icon. If CNC12 times out on start, press any key to exit and try again —
some CNCPCs do this once on the very first start. If the timeout happens consistently,
there is a communications issue or the Acorn has no logic power; see the communications
stress test (§3.4) to resolve it.

## Spindle bench test

(Acorn Install §4.2, p.30-33)

1. Start CNC12 with the Acorn powered up.
2. Press Reset on the Virtual Control Panel.
3. Set home with Cycle Start; the XYZ DRO reads `0.0000` for each axis.
4. Load `spindlebenchtest.cnc` (`F2` Load) from `C:/cncm/ncfiles`.
5. Set a digital voltage meter (DVM) to VDC and insert its leads into the H8 screw
   terminals, tightened to firmly grip the probes.
6. With `spindlebenchtest.cnc` loaded, press Cycle Start to begin (a second press may be
   needed).
7. Enter each requested voltage reading in the Voltage Reading box and press Cycle Start
   to continue; the program flags an error if the spindle output is off. It exits with
   "Job finished" on success.

The Acorn's analog output for VFD spindle-speed control is 0 to +10VDC. With the default
3000 rpm max spindle speed, that range maps 0-3000rpm to 0-10V, so `S1500` outputs
+5VDC and `S1000` outputs approximately +3.33VDC.

## App A: Windows 10/11 configuration

(Acorn Install App A, p.114)

Appendix A points to the same two references as §3.1 for the full Windows 10/11
configuration procedure: the Acorn quick start guide page and Tech Bulletin TB309
(`https://www.centroidcnc.com/dealersupport/tech_bulletins/uploads/309.pdf`).
