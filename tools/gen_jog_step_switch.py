#!/usr/bin/env python3
# Generates the 3-position jog-step switch (plate image + x1/x10/x100 buttons): python3 tools/gen_jog_step_switch.py
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp')
W, CELL, PITCH = 100, 100, 116.6
H = 2 * PITCH + CELL          # one column by three rows
SX = 70                        # slot centerline; legends sit left of it
LX = 10                        # legend left edge (text-anchor is ignored)

# folder, skin event, PLC output (on = this step selected), legend
STEPS = [
    ('jog_step_x1', 27, 1083, 'x1'),
    ('jog_step_x10', 28, 1084, 'x10'),
    ('jog_step_x100', 29, 1085, 'x100'),
]

def plate():
    ys = [i * PITCH + CELL / 2 for i in range(3)]
    ticks = ''.join(f'<rect x="{SX + 18}" y="{y - 1.5:.1f}" width="6" height="3" fill="#8a8a8a"/>' for y in ys)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.1f}" viewBox="0 0 {W} {H:.1f}">
  <title>jog step switch plate</title>
  <defs>
    <linearGradient id="rim" x1="0" y1="0" x2="100" y2="{H:.1f}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f2f2f2"/>
      <stop offset="0.5" stop-color="#b9b9b9"/>
      <stop offset="1" stop-color="#7d7d7d"/>
    </linearGradient>
    <linearGradient id="plate" x1="0" y1="0" x2="0" y2="{H:.1f}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#2e2e2e"/>
      <stop offset="1" stop-color="#050505"/>
    </linearGradient>
    <linearGradient id="slot" x1="{SX - 10}" y1="0" x2="{SX + 10}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#000000"/>
      <stop offset="0.6" stop-color="#1c1c1c"/>
      <stop offset="1" stop-color="#3a3a3a"/>
    </linearGradient>
  </defs>
  <rect x="1.5" y="1.5" width="97" height="{H - 3:.1f}" rx="7" fill="url(#rim)" stroke="#3a3a3a" stroke-width="1"/>
  <rect x="5" y="5" width="90" height="{H - 10:.1f}" rx="5" fill="url(#plate)" stroke="#000000" stroke-width="1"/>
  <rect x="{SX - 14}" y="{ys[0] - 26:.1f}" width="28" height="{ys[2] - ys[0] + 52:.1f}" rx="14" fill="#7a7a7a" stroke="#1a1a1a" stroke-width="1"/>
  <rect x="{SX - 10}" y="{ys[0] - 22:.1f}" width="20" height="{ys[2] - ys[0] + 44:.1f}" rx="10" fill="url(#slot)"/>
  {ticks}
</svg>
'''

# Arial Bold advance widths (em) for the legends.
ADV = {'x': .556, '1': .556, '0': .556}
def button(name, legend, on):
    cy = CELL / 2
    size = 18
    w = sum(ADV[c] for c in legend) * size
    x = LX + (SX - 22 - LX - w) / 2
    lever = f'''
  <circle cx="{SX}" cy="{cy}" r="9" fill="#3a3a3a"/>
  <circle cx="{SX}" cy="{cy}" r="16" fill="url(#ball)" stroke="#1a1a1a" stroke-width="1"/>''' if on else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{CELL}" viewBox="0 0 {W} {CELL}">
  <title>{name} {'on' if on else 'off'}</title>
  <defs>
    <radialGradient id="ball" cx="{SX - 4}" cy="{cy - 7}" r="19" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e6e6e6"/>
      <stop offset="0.45" stop-color="#8c8c8c"/>
      <stop offset="1" stop-color="#262626"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{CELL}" fill="#000000" fill-opacity="0.01"/>
  <text x="{x:.1f}" y="{cy + size * 0.36:.1f}" font-family="Arial" font-weight="bold" font-size="{size}" fill="{'#FFFFFF' if on else '#9a9a9a'}">{legend}</text>{lever}
</svg>
'''

XML = """<vcp_button>
	<skin_event_num>{event}</skin_event_num>
	<plc_output>
		<number>{output}</number>
		<image_on>{name}_on.svg</image_on>
		<image_off>{name}_off.svg</image_off>
	</plc_output>
</vcp_button>
"""

def write(path, text):
    assert text.isascii()
    open(path, 'w', newline='').write(text.replace('\n', '\r\n'))

write(os.path.join(ROOT, 'images', 'jog_step_plate.svg'), plate())
for name, event, output, legend in STEPS:
    out = os.path.join(ROOT, 'Buttons', name)
    os.makedirs(out, exist_ok=True)
    write(os.path.join(out, f'{name}_on.svg'), button(name, legend, True))
    write(os.path.join(out, f'{name}_off.svg'), button(name, legend, False))
    write(os.path.join(out, f'{name}.xml'), XML.format(event=event, output=output, name=name))
