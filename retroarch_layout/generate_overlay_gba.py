import os
import sys
import copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from common import overlay, load_config, write_output, get_console_name

screen_w, screen_h, output_dir = load_config()

overlays = []

ol_portrait = overlay()
ol_portrait.name = 'portrait'
ol_portrait.range_mod = '1.5'
ol_portrait.alpha_mod = '2.0'
ol_portrait.width = screen_w
ol_portrait.height = screen_h
dpad_height = 1350
ab_height = dpad_height
ss_height = 1575
lr_height = 1025
menu_height = 825

ol_portrait.add_single_button('nul', 210, dpad_height, 'rect', 200, 200, 'gba_dpad.png', None)
ol_portrait.add_cross_touch('up', 'right', 'down', 'left', 210, dpad_height, 120, 120, 90)
ol_portrait.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', 210, dpad_height, 120, 120, 70)

ol_portrait.add_ab('nul', 'nul', ol_portrait.width - 190, ab_height, 100, 40, 80, 80, 'gba_b.png', 'gba_a.png', None, None)
ol_portrait.add_ab('b', 'a', ol_portrait.width - 190, ab_height, 100, 40, 90, 90, None, None, None, None)
ol_portrait.add_single_button('a|b', ol_portrait.width - 190, ab_height, 'rect', 15, 15, None, None)

ol_portrait.add_lr('select', 'start', ol_portrait.width / 2, ss_height, 110, 100, 31, 'gba_select.png', 'gba_start.png', None, None)

ol_portrait.add_lr('l', 'r', ol_portrait.width / 2, lr_height, ol_portrait.width / 2 - 110, 100, 55, 'gba_l.png', 'gba_r.png', None, None)

ol_portrait.add_lr('load_state', 'save_state', ol_portrait.width / 2, menu_height, ol_portrait.width / 2 - 60, 50, 50, 'load.png', 'save.png', None, None)

ol_portrait.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff.png', None)

ol_portrait.add_single_button('menu_toggle', ol_portrait.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_portrait)

output_path = os.path.join(output_dir, get_console_name(__file__) + '.cfg')
write_output(overlays, output_path)
print(f'Written: {output_path}')

sys.exit(0)
