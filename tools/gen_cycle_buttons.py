#!/usr/bin/env python3
# Generates the stacked Cycle Cancel / Cycle Start pushbutton (housing image + two buttons): python3 tools/gen_cycle_buttons.py
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp')
# Stock cell pitch is 126 x 116.6 with 100 x 100 cells; each button is 2x2 cells, the housing 2x4.
W, BH = 226, 216.6
H = 449.8
CAP = 170                    # both caps are square
LAMP = CAP * 0.25            # lamp height as a share of a cap
SEP = 6                      # housing showing between each cap and the lamp
CX = (W - CAP) / 2
LAMP_Y0, LAMP_Y1 = H / 2 - LAMP / 2, H / 2 + LAMP / 2   # centered on the housing, straddling the row gap
RED_Y = LAMP_Y0 - SEP - CAP
GREEN_Y = LAMP_Y1 + SEP
START_Y = H - BH                               # top of the Cycle Start cell in housing coordinates
EXT = 14                     # housing art extends this far past its four rows, top and bottom
LAMP_MEM = 1020        # free MEM bit; lit while a job runs once the PLC drives it

# Stock icon artwork (cycle_start.svg / cycle_cancel.svg, 100x100), reused on the caps.
FRAME = ('M89.15,45.05v-34.2H54.21L45.05,4.9v5.95h-34.2v34.84l-6.02,9.26h6.02v34.2h34.76l9.34,6.07v-6.07h34.2V54.33'
         'l6.03-9.28H89.15z M88.34,45.05h-6.03l6.03,9.28v34.01H54.95v-5.99l-9.22,5.99H11.66V54.95h6.04l-6.04-9.29v-34h33.39v6.11l9.4-6.11'
         'h33.89V45.05z')
BAR = 'M48.06,30.22h5.8v41.15h-5.8z'
RING = ('M50.57,74.25c-13.05,0-23.68-10.62-23.68-23.68S37.52,26.9,50.57,26.9s23.68,10.62,23.68,23.68S63.63,74.25,50.57,74.25z '
        'M50.57,32.64c-9.89,0-17.94,8.05-17.94,17.94s8.05,17.94,17.94,17.94s17.94-8.05,17.94-17.94S60.46,32.64,50.57,32.64z')

def icon(paths, size, cx, cy):
    s = size / 100
    body = ''.join(f'<path d="{d}" fill="#FFFFFF"/>' for d in paths)
    return f'<g transform="matrix({s:.3f},0,0,{s:.3f},{cx - 50 * s:.2f},{cy - 50 * s:.2f})">{body}</g>'

def cap(id_, y0, y1, light, mid, dark):
    return (f'<linearGradient id="{id_}" x1="0" y1="{y0}" x2="0" y2="{y1}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{light}"/><stop offset="0.5" stop-color="{mid}"/><stop offset="1" stop-color="{dark}"/>'
            '</linearGradient>')

def lamp(lit, dy):
    lens = ('#fff2b0', '#ffb300', '#d97a00') if lit else ('#8a6a2a', '#5e4210', '#3a2806')
    ribs = '#ffe28a' if lit else '#4a340c'
    y0, y1 = LAMP_Y0 + dy, LAMP_Y1 + dy
    out = (f'<defs>{cap("lens", y0, y1, *lens)}</defs>'
           f'<rect x="{CX}" y="{y0:.1f}" width="{CAP}" height="{y1-y0:.1f}" rx="5" fill="url(#lens)" stroke="#2a1a00" stroke-width="1.5"/>')
    out += ''.join(f'<line x1="{x}" y1="{y0+2:.1f}" x2="{x}" y2="{y1-2:.1f}" stroke="{ribs}" stroke-width="1" stroke-opacity="0.6"/>'
                   for x in range(int(CX) + 4, int(CX + CAP) - 2, 4))
    out += ''.join(f'<line x1="{CX+2}" y1="{y0+k:.1f}" x2="{CX+CAP-2}" y2="{y0+k:.1f}" stroke="{ribs}" stroke-width="1" stroke-opacity="0.6"/>'
                   for k in range(4, int(y1 - y0) - 1, 4))
    if lit:
        out += f'<rect x="{CX+5}" y="{y0+4:.1f}" width="{CAP-10}" height="12" rx="5" fill="#ffffff" fill-opacity="0.35"/>'
    return out

def housing(lit):
    hh = H + 2 * EXT
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{hh:.1f}" viewBox="0 0 {W} {hh:.1f}">
  <defs>
    <linearGradient id="body" x1="0" y1="0" x2="{W}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3a3a3a"/><stop offset="0.5" stop-color="#1c1c1c"/><stop offset="1" stop-color="#0a0a0a"/>
    </linearGradient>
  </defs>
  <rect x="1.5" y="1.5" width="{W-3}" height="{hh-3:.1f}" rx="12" fill="url(#body)" stroke="#000000" stroke-width="2"/>
  <rect x="6" y="6" width="{W-12}" height="{hh-12:.1f}" rx="9" fill="none" stroke="#4a4a4a" stroke-width="1.2"/>
  {lamp(lit, EXT)}
</svg>
'''

def cap_svg(id_, y, colors, stroke, paths, icon_size):
    # One square cap on a transparent cell, so the housing and lamp show around it. The near-invisible
    # full-cell rect keeps the VCP from scaling the drawing to the cap's bounds.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{BH}" viewBox="0 0 {W} {BH}">
  <defs>{cap(id_, y, y + CAP, *colors)}</defs>
  <rect width="{W}" height="{BH}" fill="#000000" fill-opacity="0.01"/>
  <rect x="{CX}" y="{y:.1f}" width="{CAP}" height="{CAP}" rx="7" fill="url(#{id_})" stroke="{stroke}" stroke-width="1.5"/>
  <rect x="{CX+6}" y="{y+5:.1f}" width="{CAP-12}" height="10" rx="5" fill="#ffffff" fill-opacity="0.25"/>
  {icon(paths, icon_size, W / 2, y + CAP / 2 + 4)}
</svg>
'''

def write(path, text):
    assert text.isascii()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', newline='').write(text.replace('\n', '\r\n'))

write(os.path.join(ROOT, 'images', 'cycle_pushbutton_housing.svg'), housing(False))
write(os.path.join(ROOT, 'images', 'cycle_pushbutton_housing_lit.svg'), housing(True))
write(os.path.join(ROOT, 'Buttons', 'cycle_cancel_pb', 'cycle_cancel_pb.svg'),
      cap_svg('red', RED_Y, ('#ff6b6b', '#e8262c', '#a3161b'), '#5c0d10', [RING, FRAME], 131))
write(os.path.join(ROOT, 'Buttons', 'cycle_cancel_pb', 'cycle_cancel_pb.xml'),
      '<vcp_button>\n\t<skin_event_num>46</skin_event_num>\n</vcp_button>\n')
write(os.path.join(ROOT, 'Buttons', 'cycle_start_pb', 'cycle_start_pb.svg'),
      cap_svg('green', GREEN_Y - START_Y, ('#4fd17f', '#0f8a45', '#045228'), '#02331a', [BAR, FRAME], 131))
# The lamp lives in the housing image; the PLC bit swaps the lit and unlit housing groups.
write(os.path.join(ROOT, 'Buttons', 'cycle_start_pb', 'cycle_start_pb.xml'), f'''<vcp_button>
\t<skin_event_num>50</skin_event_num>
  <switch>
    <trigger>
      <plc_memory>
        <number>{LAMP_MEM}</number>
      </plc_memory>
    </trigger>
    <switch_on>
      <add>run_lamp_on_group</add>
      <remove>run_lamp_off_group</remove>
    </switch_on>
    <switch_off>
      <add>run_lamp_off_group</add>
      <remove>run_lamp_on_group</remove>
    </switch_off>
  </switch>
</vcp_button>
''')
