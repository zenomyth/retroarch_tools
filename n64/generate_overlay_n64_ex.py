import sys
import copy

class overlay_desc:
    def __init__(self):
        self.func = 'nul'
        self.x = None
        self.y = None
        self.shape = None
        self.rx = None
        self.ry = None
        self.img = None
        self.target = None
        self.range_mod = None
        self.pct = None
        self.movable = None

class overlay:
    def __init__(self):
        self.name = None
        self.fullscreen = 'true'
        self.normalized = 'true'
        self.range_mod = None
        self.alpha_mod = None
        self.width = None
        self.height = None
        self.upper_margin = None
        self.lower_margin = None
        self.descs = []
    def add_single_button(self, func, x, y, shape, rx, ry, img, target=None, range_mod=None, pct=None, movable=None):
        desc = overlay_desc()
        desc.func = func
        desc.x = x
        desc.y = y
        desc.shape = shape
        desc.rx = rx
        desc.ry = ry
        desc.img = img
        desc.target = target
        desc.range_mod = range_mod
        desc.pct = pct
        desc.movable = movable
        self.descs.append(desc)
    def add_cross_touch(self, func_n, func_e, func_s, func_w, x, y, dx, dy, r):
        desc_n = overlay_desc()
        desc_n.func = func_n
        desc_n.x = x
        desc_n.y = y - dy
        desc_n.shape = 'radial'
        desc_n.rx = desc_n.ry = r
        self.descs.append(desc_n)
        desc_e = overlay_desc()
        desc_e.func = func_e
        desc_e.x = x + dx
        desc_e.y = y
        desc_e.shape = 'radial'
        desc_e.rx = desc_e.ry = r
        self.descs.append(desc_e)
        desc_s = overlay_desc()
        desc_s.func = func_s
        desc_s.x = x
        desc_s.y = y + dy
        desc_s.shape = 'radial'
        desc_s.rx = desc_s.ry = r
        self.descs.append(desc_s)
        desc_w = overlay_desc()
        desc_w.func = func_w
        desc_w.x = x - dx
        desc_w.y = y
        desc_w.shape = 'radial'
        desc_w.rx = desc_w.ry = r
        self.descs.append(desc_w)
    def add_diagonal_touch(self, func_ne, func_se, func_sw, func_nw, x, y, dx, dy, r):
        desc_n = overlay_desc()
        desc_n.func = func_ne
        desc_n.x = x + dx
        desc_n.y = y - dy
        desc_n.shape = 'radial'
        desc_n.rx = desc_n.ry = r
        self.descs.append(desc_n)
        desc_e = overlay_desc()
        desc_e.func = func_se
        desc_e.x = x + dx
        desc_e.y = y + dy
        desc_e.shape = 'radial'
        desc_e.rx = desc_e.ry = r
        self.descs.append(desc_e)
        desc_s = overlay_desc()
        desc_s.func = func_sw
        desc_s.x = x - dx
        desc_s.y = y + dy
        desc_s.shape = 'radial'
        desc_s.rx = desc_s.ry = r
        self.descs.append(desc_s)
        desc_w = overlay_desc()
        desc_w.func = func_nw
        desc_w.x = x - dx
        desc_w.y = y - dy
        desc_w.shape = 'radial'
        desc_w.rx = desc_w.ry = r
        self.descs.append(desc_w)
    def add_cross_image(self, img_n, img_e, img_s, img_w, x, y, dx, dy, r):
        desc_n = overlay_desc()
        desc_n.img = img_n
        desc_n.x = x
        desc_n.y = y - dy
        desc_n.shape = 'radial'
        desc_n.rx = desc_n.ry = r
        self.descs.append(desc_n)
        desc_e = overlay_desc()
        desc_e.img = img_e
        desc_e.x = x + dx
        desc_e.y = y
        desc_e.shape = 'radial'
        desc_e.rx = desc_e.ry = r
        self.descs.append(desc_e)
        desc_s = overlay_desc()
        desc_s.img = img_s
        desc_s.x = x
        desc_s.y = y + dy
        desc_s.shape = 'radial'
        desc_s.rx = desc_s.ry = r
        self.descs.append(desc_s)
        desc_w = overlay_desc()
        desc_w.img = img_w
        desc_w.x = x - dx
        desc_w.y = y
        desc_w.shape = 'radial'
        desc_w.rx = desc_w.ry = r
        self.descs.append(desc_w)
    def add_ab(self, func_b, func_a, x, y, dx, dy, rx, ry, img_l, img_r, target_b, target_a):
        desc_b = overlay_desc()
        desc_b.func = func_b
        desc_b.x = x - dx
        desc_b.y = y + dy
        desc_b.shape = 'rect'
        desc_b.rx = rx
        desc_b.ry = ry
        desc_b.img = img_l
        desc_b.target = target_b
        self.descs.append(desc_b)
        desc_a = overlay_desc()
        desc_a.func = func_a
        desc_a.x = x + dx
        desc_a.y = y - dy
        desc_a.shape = 'rect'
        desc_a.rx = rx
        desc_a.ry = ry
        desc_a.img = img_r
        desc_a.target = target_a
        self.descs.append(desc_a)
    def add_lr(self, func_l, func_r, x, y, d, rx, ry, img_l, img_r, target_l, target_r):
        desc_l = overlay_desc()
        desc_l.func = func_l
        desc_l.x = x - d
        desc_l.y = y
        desc_l.shape = 'rect'
        desc_l.rx = rx
        desc_l.ry = ry
        desc_l.img = img_l
        desc_l.target = target_l
        self.descs.append(desc_l)
        desc_r = overlay_desc()
        desc_r.func = func_r
        desc_r.x = x + d
        desc_r.y = y
        desc_r.shape = 'rect'
        desc_r.rx = rx
        desc_r.ry = ry
        desc_r.img = img_r
        desc_r.target = target_r
        self.descs.append(desc_r)

overlays = []

# analog-portrait
ol_analog = overlay()
ol_analog.name = 'analog-portrait'
ol_analog.range_mod = '1.5'
ol_analog.alpha_mod = '2.0'
ol_analog.width = 1080
ol_analog.height = 2248
ol_analog.upper_margin = 209
ol_analog.lower_margin = 129
dpad_height = 1550
ab_height = dpad_height
c_height = 1325
ss_height = 1775
lr_height = 1225
menu_height = 1025

# thumbstick
ol_analog.add_single_button('nul', 210, dpad_height, 'radial', 200, 200, 'thumbstick-background.png')
ol_analog.add_single_button('analog_left', 210, dpad_height, 'radial', 130, 130, 'thumbstick-pad.png', None, '3.5', '0.75', 'true')

# ab
ol_analog.add_ab('nul', 'nul', ol_analog.width - 190, ab_height, 100, 40, 80, 80, 'b.png', 'a.png', None, None)
ol_analog.add_ab('y', 'b', ol_analog.width - 190, ab_height, 100, 40, 90, 90, None, None, None, None)

# c
ol_analog.add_cross_image('upc.png', 'rightc.png', 'downc.png', 'leftc.png', ol_analog.width / 2, c_height, 130, 130, 60)
ol_analog.add_cross_touch('r2|x', 'r2|a', 'r2|b', 'r2|y', ol_analog.width / 2, c_height, 130, 130, 70)

# s
ol_analog.add_single_button('start', ol_analog.width / 2, ss_height, 'radial', 60, 60, 'start.png')

# zr
ol_analog.add_lr('l2', 'r', ol_analog.width / 2, lr_height, ol_analog.width / 2 - 110, 100, 50, 'z.png', 'r.png', None, None)

# sl
ol_analog.add_lr('load_state', 'save_state', ol_analog.width / 2, menu_height, ol_analog.width / 2 - 60, 50, 50, 'load.png', 'save.png', None, None)

# ff
ol_analog.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff2.png', None)

# digital
ol_analog.add_single_button('overlay_next', ol_analog.width - 260, menu_height, 'rect', 50, 50, 'digital-icon.png', 'digital-portrait')

# main menu
ol_analog.add_single_button('menu_toggle', ol_analog.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_analog)

# digital-portrait
ol_digital = overlay()
ol_digital.name = 'digital-portrait'
ol_digital.range_mod = '1.5'
ol_digital.alpha_mod = '2.0'
ol_digital.width = 1080
ol_digital.height = 2248
ol_digital.upper_margin = 209
ol_digital.lower_margin = 129
dpad_height = 1550
ab_height = dpad_height
c_height = 1325
ss_height = 1775
lr_height = 1225
menu_height = 1025

# dpad
ol_digital.add_single_button('nul', 210, dpad_height, 'rect', 200, 200, 'dpad.png', None)
ol_digital.add_cross_touch('up', 'right', 'down', 'left', 210, dpad_height, 120, 120, 90)
ol_digital.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', 210, dpad_height, 120, 120, 70)

# ab
ol_digital.add_ab('nul', 'nul', ol_digital.width - 190, ab_height, 100, 40, 80, 80, 'b.png', 'a.png', None, None)
ol_digital.add_ab('y', 'b', ol_digital.width - 190, ab_height, 100, 40, 90, 90, None, None, None, None)

# c
ol_digital.add_cross_image('upc.png', 'rightc.png', 'downc.png', 'leftc.png', ol_digital.width / 2, c_height, 130, 130, 60)
ol_digital.add_cross_touch('r2|x', 'r2|a', 'r2|b', 'r2|y', ol_digital.width / 2, c_height, 130, 130, 70)

# s
ol_digital.add_single_button('start', ol_digital.width / 2, ss_height, 'radial', 60, 60, 'start.png')

# lr
ol_digital.add_lr('l', 'r', ol_digital.width / 2, lr_height, ol_digital.width / 2 - 110, 100, 50, 'l.png', 'r.png', None, None)

# sl
ol_digital.add_lr('load_state', 'save_state', ol_digital.width / 2, menu_height, ol_digital.width / 2 - 60, 50, 50, 'load.png', 'save.png', None, None)

#ff
ol_digital.add_single_button('toggle_fast_forward', 260, menu_height, 'rect', 50, 50, 'ff2.png', None)

# analog
ol_digital.add_single_button('overlay_next', ol_digital.width - 260, menu_height, 'rect', 50, 50, 'analog-icon.png', 'analog-portrait')

# main menu
ol_digital.add_single_button('menu_toggle', ol_digital.width / 2, menu_height, 'rect', 40, 40, 'rgui.png', None)

overlays.append(ol_digital)

# print the result
print('overlays = %d' % (len(overlays)))
print()

for i in range(len(overlays)):
    ol = overlays[i]
    print('overlay%d_full_screen = %s' % (i, ol.fullscreen))
    print('overlay%d_normalized = %s' % (i, ol.normalized))
    print('overlay%d_name = "%s"' % (i, ol.name))
    print('overlay%d_range_mod = %s' % (i, ol.range_mod))
    print('overlay%d_alpha_mod = %s' % (i, ol.alpha_mod))
    print()

for i in range(len(overlays)):
    print('overlay%d_descs = %d' % (i, len(overlays[i].descs)))
    for j in range(len(overlays[i].descs)):
        desc = overlays[i].descs[j]
        print('overlay%d_desc%d = "%s,%f,%f,%s,%f,%f"' % (i, j, desc.func, desc.x / overlays[i].width, (desc.y - overlays[i].upper_margin) / (overlays[i].height - overlays[i].upper_margin - overlays[i].lower_margin), desc.shape, desc.rx / overlays[i].width, desc.ry / (overlays[i].height - overlays[i].upper_margin - overlays[i].lower_margin)))
        if desc.img is not None:
            print('overlay%d_desc%d_overlay = %s' % (i, j, desc.img))
        if desc.target is not None:
            print('overlay%d_desc%d_next_target = "%s"' % (i, j, desc.target))
        if desc.range_mod is not None:
            print('overlay%d_desc%d_range_mod = %s' % (i, j, desc.range_mod))
        if desc.pct is not None:
            print('overlay%d_desc%d_pct = %s' % (i, j, desc.pct))
        if desc.movable is not None:
            print('overlay%d_desc%d_movable = %s' % (i, j, desc.movable))
    print()

sys.exit(0)