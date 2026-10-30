#!/usr/bin/env python3
# Generates the toggle-switch VCP buttons (XML + two state SVGs each): python3 tools/gen_toggle_switches.py
import math, os
W, H = 100, 216.6          # one column by two rows at the stock cell pitch
CX, CY = 50, H / 2
BUTTONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp', 'Buttons')

# folder, skin event, PLC output, legend shown with the lever up (bit on), legend for lever down.
TOGGLES = [
    ('spindle_toggle', 2, 1058, 'AUTO', 'MAN'),   # SpinAutoModeLED: on = auto
    ('jog_toggle', 26, 1082, 'INCR', 'CONT'),     # IncrContLED: on = incremental
]

# Arial Bold advance widths (em) for centering, since text-anchor is ignored.
ADV = {'A': .722, 'U': .722, 'T': .611, 'O': .778, 'M': .833, 'N': .722, 'I': .278, 'C': .722, 'R': .722}
def text(s, y, size, fill):
    x = CX - sum(ADV[c] for c in s) * size / 2
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial" font-weight="bold" '
            f'font-size="{size}" fill="{fill}">{s}</text>')

def hexagon(r):
    # Flat top and bottom, points left and right.
    pts = [(CX + r * math.cos(math.radians(60 * i)), CY + r * math.sin(math.radians(60 * i))) for i in range(6)]
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)

def svg(name, up, top, bottom):
    a_txt, m_txt = ('#FFFFFF', '#5c5c5c') if up else ('#5c5c5c', '#FFFFFF')
    sgn = -1 if up else 1
    ball_y = CY + sgn * 31
    shaft_y = min(CY, ball_y)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <title>{name} {(top if up else bottom).lower()}</title>
  <defs>
    <linearGradient id="rim" x1="0" y1="0" x2="100" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f2f2f2"/>
      <stop offset="0.5" stop-color="#b9b9b9"/>
      <stop offset="1" stop-color="#7d7d7d"/>
    </linearGradient>
    <linearGradient id="plate" x1="0" y1="0" x2="0" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#2e2e2e"/>
      <stop offset="1" stop-color="#050505"/>
    </linearGradient>
    <linearGradient id="nut" x1="0" y1="{CY-34}" x2="0" y2="{CY+34}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#a8a8a8"/>
      <stop offset="1" stop-color="#4a4a4a"/>
    </linearGradient>
    <linearGradient id="nutface" x1="0" y1="{CY-28}" x2="0" y2="{CY+28}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#7c7c7c"/>
      <stop offset="1" stop-color="#5a5a5a"/>
    </linearGradient>
    <radialGradient id="bush" cx="{CX}" cy="{CY-6}" r="22" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#6e6e6e"/>
      <stop offset="1" stop-color="#262626"/>
    </radialGradient>
    <linearGradient id="shaft" x1="{CX-9}" y1="0" x2="{CX+9}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#2a2a2a"/>
      <stop offset="0.4" stop-color="#8a8a8a"/>
      <stop offset="1" stop-color="#1e1e1e"/>
    </linearGradient>
    <radialGradient id="ball" cx="{CX-4}" cy="{ball_y-8}" r="20" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e6e6e6"/>
      <stop offset="0.45" stop-color="#8c8c8c"/>
      <stop offset="1" stop-color="#262626"/>
    </radialGradient>
  </defs>
  <rect x="1.5" y="1.5" width="97" height="{H-3:.1f}" rx="7" fill="url(#rim)" stroke="#3a3a3a" stroke-width="1"/>
  <rect x="5" y="5" width="90" height="{H-10:.1f}" rx="5" fill="url(#plate)" stroke="#000000" stroke-width="1"/>
  {text(top, 52, 20, a_txt)}
  {text(bottom, H-34, 20, m_txt)}
  <polygon points="{hexagon(39)}" fill="url(#nut)" stroke="#1a1a1a" stroke-width="1.5"/>
  <polygon points="{hexagon(33)}" fill="url(#nutface)" stroke="#9c9c9c" stroke-width="1"/>
  <circle cx="{CX}" cy="{CY}" r="23" fill="#4c4c4c" stroke="#8a8a8a" stroke-width="1.2"/>
  <circle cx="{CX}" cy="{CY}" r="18" fill="url(#bush)" stroke="#1a1a1a" stroke-width="1"/>
  <rect x="{CX-9}" y="{shaft_y:.1f}" width="18" height="31" fill="url(#shaft)"/>
  <circle cx="{CX}" cy="{ball_y:.1f}" r="17" fill="url(#ball)" stroke="#1a1a1a" stroke-width="1"/>
</svg>
'''
XML = """<vcp_button>
	<skin_event_num>{event}</skin_event_num>
	<plc_output>
		<number>{output}</number>
		<image_on>{on}</image_on>
		<image_off>{off}</image_off>
	</plc_output>
</vcp_button>
"""

def write(path, text):
    assert text.isascii()
    open(path, 'w', newline='').write(text.replace('\n', '\r\n'))

for name, event, output, top, bottom in TOGGLES:
    out = os.path.join(BUTTONS, name)
    os.makedirs(out, exist_ok=True)
    on, off = f'{name}_{top.lower()}.svg', f'{name}_{bottom.lower()}.svg'
    write(os.path.join(out, on), svg(name, True, top, bottom))
    write(os.path.join(out, off), svg(name, False, top, bottom))
    write(os.path.join(out, f'{name}.xml'), XML.format(event=event, output=output, on=on, off=off))
