#!/usr/bin/env python3
# Generates the spindle_toggle VCP button (XML + AUTO/MAN SVGs): python3 tools/gen_spindle_toggle.py
import math, sys, os
W, H = 100, 216.6          # one column by two rows at the stock cell pitch
CX, CY = 50, H / 2
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "resources", "vcp", "Buttons", "spindle_toggle")

# Arial Bold advance widths (em) for centering, since text-anchor is ignored.
ADV = {'A': .722, 'U': .722, 'T': .611, 'O': .778, 'M': .833, 'N': .722}
def text(s, y, size, fill):
    x = CX - sum(ADV[c] for c in s) * size / 2
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial" font-weight="bold" '
            f'font-size="{size}" fill="{fill}">{s}</text>')

def hexagon(r):
    pts = [(CX + r * math.cos(math.radians(30 + 60 * i)), CY + r * math.sin(math.radians(30 + 60 * i))) for i in range(6)]
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)

def svg(up):
    lit_on, lit_off = '#EC1C24', '#81151C'
    txt_on, txt_off = '#FFFFFF', '#C9A0A3'
    a_lamp, m_lamp = (lit_on, lit_off) if up else (lit_off, lit_on)
    a_txt, m_txt = (txt_on, txt_off) if up else (txt_off, txt_on)
    tip_y = 52 if up else H - 52
    sgn = -1 if up else 1
    # Bat handle: tapers from the bushing to the ball, with a shadow edge on the right.
    base_y = CY + sgn * 6
    lever = f'{CX-6.5:.1f},{base_y:.1f} {CX+6.5:.1f},{base_y:.1f} {CX+4:.1f},{tip_y:.1f} {CX-4:.1f},{tip_y:.1f}'
    shadow = f'{CX+2:.1f},{base_y:.1f} {CX+6.5:.1f},{base_y:.1f} {CX+4:.1f},{tip_y:.1f} {CX+1.2:.1f},{tip_y:.1f}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <title>spindle_toggle {'auto' if up else 'manual'}</title>
  <defs>
    <linearGradient id="plate" x1="0" y1="0" x2="100" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#5a5d61"/>
      <stop offset="0.5" stop-color="#3a3c3f"/>
      <stop offset="1" stop-color="#2a2b2d"/>
    </linearGradient>
    <radialGradient id="nut" cx="{CX-7}" cy="{CY-7}" r="30" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#f4f4f4"/>
      <stop offset="0.6" stop-color="#a7aaae"/>
      <stop offset="1" stop-color="#5d6064"/>
    </radialGradient>
    <linearGradient id="chrome" x1="{CX-7}" y1="0" x2="{CX+7}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#8d9094"/>
      <stop offset="0.35" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#6b6e72"/>
    </linearGradient>
    <radialGradient id="ball" cx="{CX-3}" cy="{tip_y-3}" r="10" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="0.5" stop-color="#c3c6ca"/>
      <stop offset="1" stop-color="#5d6064"/>
    </radialGradient>
  </defs>
  <rect x="3" y="3" width="94" height="{H-6:.1f}" rx="8" fill="url(#plate)" stroke="#111111" stroke-width="2"/>
  <circle cx="9" cy="9" r="2.2" fill="#8d9094"/><circle cx="91" cy="9" r="2.2" fill="#8d9094"/>
  <circle cx="9" cy="{H-9:.1f}" r="2.2" fill="#8d9094"/><circle cx="91" cy="{H-9:.1f}" r="2.2" fill="#8d9094"/>
  <rect x="17" y="14" width="66" height="26" rx="4" fill="{a_lamp}" stroke="#111111" stroke-width="1.5"/>
  {text('AUTO', 33.5, 17, a_txt)}
  <rect x="17" y="{H-40:.1f}" width="66" height="26" rx="4" fill="{m_lamp}" stroke="#111111" stroke-width="1.5"/>
  {text('MAN', H-20.5, 17, m_txt)}
  <polygon points="{hexagon(22)}" fill="url(#nut)" stroke="#333333" stroke-width="1.5"/>
  <circle cx="{CX}" cy="{CY}" r="13" fill="#4a4d51" stroke="#222222" stroke-width="1"/>
  <circle cx="{CX}" cy="{CY}" r="9" fill="url(#chrome)"/>
  <polygon points="{lever}" fill="url(#chrome)" stroke="#444444" stroke-width="0.8"/>
  <polygon points="{shadow}" fill="#000000" fill-opacity="0.18"/>
  <circle cx="{CX}" cy="{tip_y}" r="9" fill="url(#ball)" stroke="#444444" stroke-width="0.8"/>
</svg>
'''
os.makedirs(out, exist_ok=True)
for name, up in (('spindle_toggle_auto.svg', True), ('spindle_toggle_man.svg', False)):
    s = svg(up)
    assert s.isascii()
    open(os.path.join(out, name), 'w', newline='').write(s.replace('\n', '\r\n'))
xml = '''<vcp_button>
	<skin_event_num>2</skin_event_num>
	<plc_output>
		<number>1058</number>
		<image_on>spindle_toggle_auto.svg</image_on>
		<image_off>spindle_toggle_man.svg</image_off>
	</plc_output>
</vcp_button>
'''
open(os.path.join(out, 'spindle_toggle.xml'), 'w', newline='').write(xml.replace('\n', '\r\n'))
