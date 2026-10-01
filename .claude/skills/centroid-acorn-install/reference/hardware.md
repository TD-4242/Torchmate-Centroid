# Acorn Hardware Reference

Kit contents, board specifications, relay board/power, LEDs, and bench-test setup for the
Centroid Acorn controller.
Source: Acorn Install Ch 1, Ch 2, App D; printed pages cited inline.

## Kit contents

The Acorn CNC Controller Kit (Part# 14455) includes (Acorn Install Ch 1, p.7):

| Item | Part # |
| --- | --- |
| Acorn with BeagleBone Green installed, all terminal blocks installed | 14756 |
| 8-output relay board with flat cable | 14734 |
| Meanwell RD-35B power supply | 8903 |
| 110VAC input cord (for the power supply) | 14459 |
| 24V output cable, power supply to Acorn H9 header | 14460 |
| 15ft shielded Cat5E Ethernet cable | 7269 |

## Board specifications

(Acorn Install App D, p.123)

| Characteristic | Value |
| --- | --- |
| Function | Motion Control Processor, PLC, and Drive Interface |
| Maximum number of axes | 4 |
| Maximum pulse rate | 400kHz |
| Control interface | 100 Mb/s Ethernet to PC |
| Drive application | Drives with step and direction inputs |
| Digital PLC inputs | 8 |
| Digital PLC outputs | 8 |
| Analog output resolution | 12 bits |
| Dimensions (W*D*H) | 5.4 * 4.2 * 0.7 inches |

### DB25 (H6) connector pinout

(Acorn Install App D, p.125)

| Pin | Signal | Pin | Signal |
| --- | --- | --- | --- |
| 1 | Output 1 | 14 | Output 2 |
| 2 | Step 1 | 15 | Input 5 |
| 3 | Direction 1 | 16 | Output 3 |
| 4 | Step 2 | 17 | Output 4 |
| 5 | Direction 2 | 18-22 | (unused) |
| 6 | Step 3 | 23 | (unused) |
| 7 | Direction 3 | 24 | (unused) |
| 8 | Step 4 | 25 | (unused) |
| 9 | Direction 4 | | 24V COM (shell) |
| 10 | Input 1 | | Chassis GND (shell) |
| 11 | Input 2 | | |
| 12 | Input 3 | | |
| 13 | Input 4 | | |

Inputs and outputs on the DB25 are 5V compatible (Acorn Install App D, p.124). DB25 inputs are
not isolated. Screw-terminal inputs are optically isolated and take 24 VDC sensors or switches;
powering them from a separate 24 VDC supply improves isolation and noise immunity (Acorn Install
App D, p.126). Each input may be connected on the DB25 or the screw terminal, not both: screw
terminal input 1 and DB25 input 1 cannot both be used, but screw terminal input 1 can be used with
DB25 input 2 (Acorn Install App D, p.124).

### I/O map

Inputs are sourcing type at screw terminals H1/H4, with inputs 1-5 duplicated as 5V-pullup
logic inputs on DB25 (H6); inputs 6-8 are screw-terminal only. Outputs are open-collector
at H10, with outputs 1-4 duplicated as 5V logic outputs on DB25 (H6); outputs 5-8 are
screw-terminal only. Analog output is a 12-bit DAC on H8 pin 1. (Acorn Install App D,
p.129)

Inputs (Acorn Install App D, p.129):

| Input | Function | Type | Screw terminal connector | Pin | 5V-logic type | DB25 connector | Pin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | General Purpose | Sourcing | H4 | 5 | Logic w/ 5V Pullup | H6 | 10 |
| 2 | General Purpose | Sourcing | H4 | 4 | Logic w/ 5V Pullup | H6 | 11 |
| 3 | General Purpose | Sourcing | H4 | 3 | Logic w/ 5V Pullup | H6 | 12 |
| 4 | General Purpose | Sourcing | H4 | 2 | Logic w/ 5V Pullup | H6 | 13 |
| 5 | General Purpose | Sourcing | H1 | 5 | Logic w/ 5V Pullup | H6 | 15 |
| 6 | General Purpose | Sourcing | H1 | 4 | - | - | - |
| 7 | General Purpose | Sourcing | H1 | 3 | - | - | - |
| 8 | General Purpose | Sourcing | H1 | 2 | - | - | - |

Outputs (Acorn Install App D, p.129):

| Output | Function | Type | Screw terminal connector | Pin | 5V-logic type | DB25 connector | Pin |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | General Purpose | Open Collector | H10 | 2 | 5V Logic | H6 | 1 |
| 2 | General Purpose | Open Collector | H10 | 3 | 5V Logic | H6 | 14 |
| 3 | General Purpose | Open Collector | H10 | 4 | 5V Logic | H6 | 16 |
| 4 | General Purpose | Open Collector | H10 | 5 | 5V Logic | H6 | 17 |
| 5 | General Purpose | Open Collector | H10 | 6 | - | - | - |
| 6 | General Purpose | Open Collector | H10 | 7 | - | - | - |
| 7 | General Purpose | Open Collector | H10 | 8 | - | - | - |
| 8 | General Purpose | Open Collector | H10 | 9 | - | - | - |

### Electrical specifications

(Acorn Install App D, p.129)

| Characteristic | Min | Typ | Max | Unit |
| --- | --- | --- | --- | --- |
| 24V input pullup voltage | 22 | - | 26 | VDC |
| 24V input on voltage | 0 | - | 5.9 | VDC |
| 24V input off voltage | 19.1 | - | 26 | VDC |
| 24V input operating current | 9 | 11 | 15 | mA |
| Open collector output current | 0 | 10 | 50 | mA |
| Open collector output voltage | 0 | 24 | Vsupply | VDC |
| Analog output voltage | 0 | - | 10 | V |
| Analog output resolution | - | 12 | - | bits |

## Relay board and power

The 8-relay board (Part# 14734) connects to the Acorn with the included flat white
10-conductor cable (Acorn Install Ch 2, p.9). The Meanwell RD-35B power supply's 5-pin
terminal block plugs into Acorn header H9; the supply is pre-wired for 110VAC but also
runs on up to 240VAC (Acorn Install Ch 2, p.9-10). Relay output current rating is 0.01-10A
@ 125VAC or 0.01-10A @ 28VDC; the relay board draws 0.3A on its 5V supply (Acorn Install
App D, p.129).

## LEDs

(Acorn Install §2.2, p.10-11)

The green Power LED (upper right corner of the Acorn) lights with 24VDC applied and also
serves as the BeagleBone Green (BBG) heartbeat: it flashes when the BBG firmware has
booted and is running. On the BBG itself, a blue Heartbeat LED blinks rapidly while
booting, then settles to one pulse per second once booted and running.

> If the Power LED is off or the Heartbeat LED does not reach its steady pattern, see the
> Centroid Community CNC Support Forum's LED explainer:
> https://centroidcncforum.com/viewtopic.php?f=61&t=1460

> **NOTICE:** Do not plug anything into the USB port on the BeagleBone Green board.

## Bench test hardware setup

Needed (Acorn Install §2.1, p.8): a large, well-lit bench near outlets (a wooden surface is
ideal; do not use metal or plastic surfaces, surfaces that may contain metal scraps or
shavings, or fabric-covered surfaces, which risks ESD damage to powered boards); a Windows
10/11 PC meeting the Centroid CNCPC minimum specs, or a Centroid-supplied CNCPC; a small
screwdriver set; a digital multimeter.

(Acorn Install §2.2, p.9-10)

1. Connect the relay board to the Acorn with the included flat white 10-conductor cable.
2. Connect the power supply to Acorn header H9 (5-pin terminal block), leaving the
   Meanwell supply unplugged from 110VAC/240VAC for now.
3. Connect the supplied 15ft shielded Ethernet cable between the PC's built-in Ethernet
   port and the Acorn. Do not use a USB-to-Ethernet adapter. The cable must be shielded
   (metal clip around the RJ-45; see Tech Bulletin TB270:
   https://www.centroidcnc.com/dealersupport/tech_bulletins/uploads/270.pdf) — an
   unshielded cable causes intermittent PC data-receive errors from electrical noise.
4. Plug in the Meanwell power supply.
5. Apply power. The green Power LED should light and the BBG Heartbeat LED should settle
   to one pulse per second, confirming the Acorn is booted and ready.
