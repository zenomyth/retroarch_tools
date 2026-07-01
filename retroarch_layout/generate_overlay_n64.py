import os
import sys
import copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from common import overlay_desc, overlay, load_config, write_output, get_console_name

screen_w, screen_h, output_dir, margin = load_config()

overlays = []

dpad_center = margin + 210
ab_center = screen_w - margin - 190
lr_d = screen_w // 2 - margin - 100
sl_d = screen_w // 2 - margin - 50

ol_analog = overlay()
ol_analog.name = 'analog-portrait'
ol_analog.range_mod = '1.5'
ol_analog.alpha_mod = '2.0'
ol_analog.width = screen_w
ol_analog.height = screen_h
dpad_height = 1350
ab_height = dpad_height
c_height = 1125
ss_height = 1575
lr_height = 1025
menu_height = 825

ol_analog.add_single_button('nul', dpad_center, dpad_height, 'radial', 200, 200, 'n64_thumbstick-background.png')
ol_analog.add_single_button('analog_left', dpad_center, dpad_height, 'radial', 130, 130, 'n64_thumbstick-pad.png', None, '3.5', '0.75', 'true')

ol_analog.add_ab('nul', 'nul', ab_center, ab_height, 100, 40, 80, 80, 'n64_b.png', 'n64_a.png', None, None)
ol_analog.add_ab('y', 'b', ab_center, ab_height, 100, 40, 90, 90, None, None, None, None)

ol_analog.add_cross_image('n64_upc.png', 'n64_rightc.png', 'n64_downc.png', 'n64_leftc.png', ol_analog.width / 2, c_height, 110, 110, 60)
ol_analog.add_cross_touch('r2|x', 'r2|a', 'r2|b', 'r2|y', ol_analog.width / 2, c_height, 110, 110, 70)

ol_analog.add_single_button('start', ol_analog.width / 2, ss_height, 'radial', 60, 60, 'n64_start.png')

ol_analog.add_lr('l2', 'r', ol_analog.width / 2, lr_height, lr_d, 100, 50, 'n64_z.png', 'n64_r.png', None, None)

ol_analog.add_lr('load_state', 'save_state', ol_analog.width / 2, menu_height, sl_d, 50, 50, 'load.png', 'save.png', None, None)

ol_analog.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff.png', None)

ol_analog.add_single_button('overlay_next', ol_analog.width - margin - 40, menu_height, 'rect', 50, 50, 'digital-icon.png', 'digital-portrait')

ol_analog.add_single_button('menu_toggle', ol_analog.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_analog)

ol_digital = overlay()
ol_digital.name = 'digital-portrait'
ol_digital.range_mod = '1.5'
ol_digital.alpha_mod = '2.0'
ol_digital.width = screen_w
ol_digital.height = screen_h
dpad_height = 1350
ab_height = dpad_height
c_height = 1125
ss_height = 1575
lr_height = 1025
menu_height = 825

ol_digital.add_single_button('nul', dpad_center, dpad_height, 'rect', 200, 200, 'n64_dpad.png', None)
ol_digital.add_cross_touch('up', 'right', 'down', 'left', dpad_center, dpad_height, 120, 120, 90)
ol_digital.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', dpad_center, dpad_height, 120, 120, 70)

ol_digital.add_ab('nul', 'nul', ab_center, ab_height, 100, 40, 80, 80, 'n64_b.png', 'n64_a.png', None, None)
ol_digital.add_ab('y', 'b', ab_center, ab_height, 100, 40, 90, 90, None, None, None, None)

ol_digital.add_cross_image('n64_upc.png', 'n64_rightc.png', 'n64_downc.png', 'n64_leftc.png', ol_digital.width / 2, c_height, 110, 110, 60)
ol_digital.add_cross_touch('r2|x', 'r2|a', 'r2|b', 'r2|y', ol_digital.width / 2, c_height, 110, 110, 70)

ol_digital.add_single_button('start', ol_digital.width / 2, ss_height, 'radial', 60, 60, 'n64_start.png')

ol_digital.add_lr('l', 'r', ol_digital.width / 2, lr_height, lr_d, 100, 50, 'n64_l.png', 'n64_r.png', None, None)

ol_digital.add_lr('load_state', 'save_state', ol_digital.width / 2, menu_height, sl_d, 50, 50, 'load.png', 'save.png', None, None)

ol_digital.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff.png', None)

ol_digital.add_single_button('overlay_next', ol_digital.width - margin - 40, menu_height, 'rect', 50, 50, 'analog-icon.png', 'analog-portrait')

ol_digital.add_single_button('menu_toggle', ol_digital.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_digital)

output_path = os.path.join(output_dir, get_console_name(__file__) + '.cfg')
write_output(overlays, output_path)
print(f'Written: {output_path}')

sys.exit(0)
