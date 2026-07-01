import os
import sys
import copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from common import overlay, load_config, write_output, get_console_name

screen_w, screen_h, output_dir, margin = load_config()

overlays = []

dpad_center = margin + 210
ab_center = screen_w - margin - 260
lr_d = screen_w // 2 - margin - 70
sl_d = screen_w // 2 - margin - 50

ol_portrait = overlay()
ol_portrait.name = 'portrait'
ol_portrait.range_mod = '1.5'
ol_portrait.alpha_mod = '2.0'
ol_portrait.width = screen_w
ol_portrait.height = screen_h
dpad_height = 1350
abxy_height = dpad_height
lr_height = 1025
ss_height = lr_height
menu_height = 825

ol_portrait.add_single_button('nul', dpad_center, dpad_height, 'rect', 200, 200, 'ps_dpad.png', None)
ol_portrait.add_cross_touch('up', 'right', 'down', 'left', dpad_center, dpad_height, 120, 120, 90)
ol_portrait.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', dpad_center, dpad_height, 120, 120, 70)

ol_portrait.add_cross_image('ps_x.png', 'ps_a.png', 'ps_b.png', 'ps_y.png', ab_center, abxy_height, 170, 175, 80)
ol_portrait.add_cross_touch('x', 'a', 'b', 'y', ab_center, abxy_height, 170, 175, 90)
ol_portrait.add_diagonal_touch('a|x', 'b|a', 'y|b', 'x|y', ab_center, abxy_height, 85, 87.5, 30)

ol_portrait.add_lr('select', 'start', ol_portrait.width / 2, ss_height, 80, 50, 40, 'ps_select.png', 'ps_start.png', None, None)

ol_portrait.add_lr('l', 'r', ol_portrait.width / 2, lr_height, lr_d, 70, 42, 'ps_l1.png', 'ps_r1.png', None, None)
ol_portrait.add_lr('l2', 'r2', ol_portrait.width / 2, lr_height, ol_portrait.width / 2 - 230, 70, 42, 'ps_l2.png', 'ps_r2.png', None, None)

ol_portrait.add_lr('load_state', 'save_state', ol_portrait.width / 2, menu_height, sl_d, 50, 50, 'load.png', 'save.png', None, None)

ol_portrait.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff.png', None)

ol_portrait.add_single_button('menu_toggle', ol_portrait.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_portrait)

output_path = os.path.join(output_dir, get_console_name(__file__) + '.cfg')
write_output(overlays, output_path)
print(f'Written: {output_path}')

sys.exit(0)
