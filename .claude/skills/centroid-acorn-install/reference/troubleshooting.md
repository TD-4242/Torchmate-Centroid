# Troubleshooting Reference

Source: Acorn Install App B, App C, and the "Useful Technical Resources" list (Ch 1, p.5).

## Symptom -> fix (App B)

| Symptom | Fix |
|---|---|
| `CNC12 Acorn Communication Time Out` at startup (Acorn Install App B, p.115) | Set the Ethernet adapter used for Acorn to a manual IPv4 address `10.168.41.1` / subnet `255.255.255.0` (Acorn Install App B, p.115). Allow `CNCM.EXE`/`CNCT.EXE`/`CNCR.EXE` through Windows Defender Firewall for both Public and Private networks, or turn the firewall off entirely via Windows Search -> `Windows Defender Firewall` -> `Turn Windows Defender Firewall On or Off` (Acorn Install App B, p.115-116; `CNCR.EXE` per Acorn Install §3.4, p.26). Uninstall (not just disable) any antivirus/antispyware software — it can slow Acorn communication even while allowed to run (Acorn Install App B, p.116). Reboot the CNCPC, power-cycle the Acorn, and restart CNC12, letting any firmware update finish (Acorn Install App B, p.116). If it still won't start, update the CNCPC's Ethernet port drivers or try another shielded cable (Acorn Install App B, p.116). |

> App B (p.115) names only `CNCM.EXE`/`CNCT.EXE` for the firewall allow-list; §3.4 (p.26) also
> lists `cncr.exe`. See [software-setup.md](software-setup.md#windows-1011-configuration) for the
> manual's corporate-policy caveat on anti-virus/firewall software.

## PLC diagnostic screen (App B)

Press `alt+i` from the main program window to open the real-time I/O display. The four arrow
keys move the cursor between the `Inputs`, `Outputs`, `Memory`, and `Stages` rows and within a
row; the highlighted item's definition appears below the last row of LED indicators; active
items are green, inactive are red; `alt+i` exits (Acorn Install App B, p.117). Details:
https://www.centroidcnc.com/centroid_diy/downloads/acorn_documentation/cnc12_PLC_diagnostic_screen.pdf
(Acorn Install App B, p.117).

## Support and knowledge base

From Appendix C (Acorn Install App C, p.118):

- Acorn knowledge base: https://centroidcncforum.com/viewforum.php?f=63
- Acorn knowledge base video library: https://centroidcncforum.com/viewforum.php?f=61
- Forum posting guidance — a fresh report (`F7 Utility` -> `F7 Create Report`) is always
  required before posting: https://centroidcncforum.com/viewtopic.php?f=60&t=1043
- All Acorn documentation: https://centroidcncforum.com/viewtopic.php?f=60&t=3397
- Factory Direct Technical Support (purchase):
  https://shopcentroidcnc.com/centroid-factory-direct-11-technical-support/
- Setting up TeamViewer for remote technical support:
  https://centroidcncforum.com/viewtopic.php?f=61&t=1448
- Creating and restoring from a report file:
  https://centroidcncforum.com/viewtopic.php?f=61&t=3216
- Recommended resistive touchscreen example. A touchscreen isn't required (a mouse works
  fine), but resistive touchscreens are preferred for a CNC console over capacitive ones,
  which false-trigger from dust and dirt in a machine shop:
  https://centroidcncforum.com/viewtopic.php?p=70990#p70990

From the "Useful Technical Resources" list (Acorn Install p.5):

- All Acorn documentation links: https://centroidcncforum.com/viewtopic.php?f=60&t=3397
- Acorn CNC knowledge base videos: http://centroidcncforum.com/viewforum.php?f=61
- Acorn CNC tech tips knowledge: http://centroidcncforum.com/viewforum.php?f=63
- Centroid's YouTube channel (Centroid CNC Technical Support):
  https://www.youtube.com/user/CentroidSupport/videos
- Martyscncgarage YouTube playlist (Centroid CNC Acorn Playlist):
  https://tinyurl.com/ascxfev4
- Free Centroid Community CNC Support Forum: https://centroidcncforum.com/viewforum.php?f=20
- Centroid Acorn and its CNC accessories:
  https://www.centroidcnc.com/centroid_diy/acorn_cnc_controller.html
- Centroid CNC components: http://www.centroidcnc.com/centroid_diy/cnc_components.html
- DIY CNC gear: https://www.centroidcnc.com/centroid_diy/diy_cnc_gear.html
