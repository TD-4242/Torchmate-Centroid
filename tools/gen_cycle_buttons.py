#!/usr/bin/env python3
# Generates the stacked Cycle Cancel / Cycle Start pushbutton (housing image + two buttons): python3 tools/gen_cycle_buttons.py
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp')
# Stock cell pitch is 126 x 116.6 with 100 x 100 cells; each button is 2x2 cells, the housing 2x4.
W, BH = 226, 216.6
H = 449.8
LAMP_OUT = 1100        # UnusedR9C4LED; lit while a job runs once the PLC drives it

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

def housing():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="body" x1="0" y1="0" x2="{W}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3a3a3a"/><stop offset="0.5" stop-color="#1c1c1c"/><stop offset="1" stop-color="#0a0a0a"/>
    </linearGradient>
  </defs>
  <rect x="1.5" y="1.5" width="{W-3}" height="{H-3:.1f}" rx="12" fill="url(#body)" stroke="#000000" stroke-width="2"/>
  <rect x="6" y="6" width="{W-12}" height="{H-12:.1f}" rx="9" fill="none" stroke="#4a4a4a" stroke-width="1.2"/>
</svg>
'''

def stop_button():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{BH}" viewBox="0 0 {W} {BH}">
  <defs>{cap('red', 14, BH, '#ff6b6b', '#e8262c', '#a3161b')}</defs>
  <rect x="15" y="14" width="{W-30}" height="{BH-14:.1f}" rx="7" fill="url(#red)" stroke="#5c0d10" stroke-width="1.5"/>
  <rect x="21" y="19" width="{W-42}" height="10" rx="5" fill="#ffffff" fill-opacity="0.25"/>
  {icon([RING, FRAME], 150, W / 2, 118)}
</svg>
'''

def start_button(lit):
    lens = ('#fff2b0', '#ffb300', '#d97a00') if lit else ('#8a6a2a', '#5e4210', '#3a2806')
    ribs = '#ffe28a' if lit else '#4a340c'
    ly0, ly1 = 0, 52
    rib_lines = ''.join(f'<line x1="{x}" y1="{ly0+2}" x2="{x}" y2="{ly1-2}" stroke="{ribs}" stroke-width="1" stroke-opacity="0.6"/>'
                        for x in range(20, W - 16, 4))
    rib_lines += ''.join(f'<line x1="17" y1="{y}" x2="{W-17}" y2="{y}" stroke="{ribs}" stroke-width="1" stroke-opacity="0.6"/>'
                         for y in range(ly0 + 4, ly1 - 1, 4))
    glow = (f'<rect x="20" y="4" width="{W-40}" height="13" rx="5" fill="#ffffff" fill-opacity="0.35"/>' if lit else '')
    gy = ly1 + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{BH}" viewBox="0 0 {W} {BH}">
  <defs>{cap('lens', ly0, ly1, *lens)}{cap('green', gy, BH - 14, '#4fd17f', '#0f8a45', '#045228')}</defs>
  <rect x="15" y="{ly0}" width="{W-30}" height="{ly1-ly0}" rx="5" fill="url(#lens)" stroke="#2a1a00" stroke-width="1.5"/>
  {rib_lines}{glow}
  <rect x="15" y="{gy}" width="{W-30}" height="{BH-14-gy:.1f}" rx="7" fill="url(#green)" stroke="#02331a" stroke-width="1.5"/>
  <rect x="21" y="{gy+5}" width="{W-42}" height="9" rx="4.5" fill="#ffffff" fill-opacity="0.25"/>
  {icon([BAR, FRAME], 120, W / 2, (gy + BH - 14) / 2)}
</svg>
'''

def write(path, text):
    assert text.isascii()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', newline='').write(text.replace('\n', '\r\n'))

write(os.path.join(ROOT, 'images', 'cycle_pushbutton_housing.svg'), housing())
write(os.path.join(ROOT, 'Buttons', 'cycle_cancel_pb', 'cycle_cancel_pb.svg'), stop_button())
write(os.path.join(ROOT, 'Buttons', 'cycle_cancel_pb', 'cycle_cancel_pb.xml'),
      '<vcp_button>\n\t<skin_event_num>46</skin_event_num>\n</vcp_button>\n')
write(os.path.join(ROOT, 'Buttons', 'cycle_start_pb', 'cycle_start_pb_lit.svg'), start_button(True))
write(os.path.join(ROOT, 'Buttons', 'cycle_start_pb', 'cycle_start_pb.svg'), start_button(False))
write(os.path.join(ROOT, 'Buttons', 'cycle_start_pb', 'cycle_start_pb.xml'),
      f'<vcp_button>\n\t<skin_event_num>50</skin_event_num>\n\t<plc_output>\n\t\t<number>{LAMP_OUT}</number>\n'
      '\t\t<image_on>cycle_start_pb_lit.svg</image_on>\n\t\t<image_off>cycle_start_pb.svg</image_off>\n\t</plc_output>\n</vcp_button>\n')
