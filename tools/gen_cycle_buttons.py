#!/usr/bin/env python3
# Generates the stacked Cycle Cancel / Cycle Start pushbutton (housing image + two buttons): python3 tools/gen_cycle_buttons.py
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'vcp')
H = 216.6              # housing spans two rows at the stock cell pitch
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
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="{H}" viewBox="0 0 100 {H}">
  <defs>
    <linearGradient id="body" x1="0" y1="0" x2="100" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#3a3a3a"/><stop offset="0.5" stop-color="#1c1c1c"/><stop offset="1" stop-color="#0a0a0a"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="98" height="{H-2:.1f}" rx="7" fill="url(#body)" stroke="#000000" stroke-width="1.5"/>
  <rect x="4" y="4" width="92" height="{H-8:.1f}" rx="5" fill="none" stroke="#4a4a4a" stroke-width="1"/>
</svg>
'''

def stop_button():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <defs>{cap('red', 7, 99, '#ff6b6b', '#e8262c', '#a3161b')}</defs>
  <rect x="8" y="7" width="84" height="92" rx="4" fill="url(#red)" stroke="#5c0d10" stroke-width="1.2"/>
  <rect x="11" y="9.5" width="78" height="6" rx="3" fill="#ffffff" fill-opacity="0.25"/>
  {icon([RING, FRAME], 70, 50, 54)}
</svg>
'''

def start_button(lit):
    lens = ('#fff2b0', '#ffb300', '#d97a00') if lit else ('#8a6a2a', '#5e4210', '#3a2806')
    ribs = '#ffe28a' if lit else '#4a340c'
    rib_lines = ''.join(f'<line x1="{x}" y1="3" x2="{x}" y2="29" stroke="{ribs}" stroke-width="0.8" stroke-opacity="0.6"/>'
                        for x in range(13, 89, 3))
    rib_lines += ''.join(f'<line x1="10" y1="{y}" x2="90" y2="{y}" stroke="{ribs}" stroke-width="0.8" stroke-opacity="0.6"/>'
                         for y in range(5, 29, 3))
    glow = ('<rect x="12" y="4" width="76" height="8" rx="3" fill="#ffffff" fill-opacity="0.35"/>' if lit else '')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <defs>{cap('lens', 1, 31, *lens)}{cap('green', 34, 97, '#4fd17f', '#0f8a45', '#045228')}</defs>
  <rect x="8" y="1" width="84" height="30" rx="3" fill="url(#lens)" stroke="#2a1a00" stroke-width="1.2"/>
  {rib_lines}{glow}
  <rect x="8" y="34" width="84" height="63" rx="4" fill="url(#green)" stroke="#02331a" stroke-width="1.2"/>
  <rect x="11" y="36.5" width="78" height="5" rx="2.5" fill="#ffffff" fill-opacity="0.25"/>
  {icon([BAR, FRAME], 56, 50, 66.5)}
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
