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
abxy_height = dpad_height
lr_height = 1025
ss_height = 1575
menu_height = 1675

ol_portrait.add_single_button('nul', 210, dpad_height, 'rect', 200, 200, 'ds_dpad.png', None)
ol_portrait.add_cross_touch('up', 'right', 'down', 'left', 210, dpad_height, 120, 120, 90)
ol_portrait.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', 210, dpad_height, 120, 120, 70)

ol_portrait.add_cross_image('ds_x.png', 'ds_a.png', 'ds_b.png', 'ds_y.png', ol_portrait.width - 260, abxy_height, 170, 175, 80)
ol_portrait.add_cross_touch('x', 'a', 'b', 'y', ol_portrait.width - 260, abxy_height, 170, 175, 90)
ol_portrait.add_diagonal_touch('a|x', 'b|a', 'y|b', 'x|y', ol_portrait.width - 260, abxy_height, 85, 87.5, 30)

ol_portrait.add_lr('select', 'start', ol_portrait.width / 2, ss_height, 100, 80, 20, 'ds_select.png', 'ds_start.png', None, None)

ol_portrait.add_lr('l', 'r', ol_portrait.width / 2, lr_height, ol_portrait.width / 2 - 65, 60, 20, 'ds_l.png', 'ds_r.png', None, None)

ol_portrait.add_lr('load_state', 'save_state', ol_portrait.width / 2, menu_height, ol_portrait.width / 2 - 60, 50, 50, 'load.png', 'save.png', None, None)

ol_portrait.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff.png', None)

ol_portrait.add_single_button('menu_toggle', ol_portrait.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_portrait)

output_path = os.path.join(output_dir, get_console_name(__file__) + '.cfg')
write_output(overlays, output_path)
print(f'Written: {output_path}')

sys.exit(0)
