#!/usr/bin/env python3
# Generates the jog_speed VCP button (turtle when slow, rabbit when fast): python3 tools/gen_jog_speed_button.py
import os, re
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp', 'Buttons', 'jog_speed')

# Animal artwork is read from the stock tortoise_hare.svg (hare path first, turtle second).
STOCK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp', 'Buttons', 'tortoise_hare', 'tortoise_hare.svg')
HARE, TURTLE = re.findall(r'<path d="([^"]+)"', open(STOCK).read())
HARE_EYE, HARE_C = (79.41, 71.04), (53.5, 78.0)          # eye and bounding-box center, stock coordinates
TURTLE_EYE, TURTLE_C = (86.4, 23.98), (55.3, 25.0)

def button(bg, path, eye, center, scale):
    tx, ty = 50 - center[0] * scale, 50 - center[1] * scale
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="6" fill="{bg}"/>
  <g transform="matrix({scale},0,0,{scale},{tx:.2f},{ty:.2f})">
    <path d="{path}" fill="#231f20"/>
    <circle cx="{eye[0]}" cy="{eye[1]}" r="1.2" fill="#ffffff"/>
  </g>
</svg>
'''

XML = '''<vcp_button>
	<skin_event_num>38</skin_event_num>
	<plc_output>
		<number>1094</number>
		<image_on>jog_speed_slow.svg</image_on>
		<image_off>jog_speed_fast.svg</image_off>
	</plc_output>
</vcp_button>
'''

def write(name, text):
    assert text.isascii()
    open(os.path.join(OUT, name), 'w', newline='').write(text.replace('\n', '\r\n'))

os.makedirs(OUT, exist_ok=True)
# FastSlowLED_O (OUT1094) is on for slow jog.
write('jog_speed_slow.svg', button('#ffc70e', TURTLE, TURTLE_EYE, TURTLE_C, 1.1))
write('jog_speed_fast.svg', button('#f05a22', HARE, HARE_EYE, HARE_C, 1.05))
write('jog_speed.xml', XML)
