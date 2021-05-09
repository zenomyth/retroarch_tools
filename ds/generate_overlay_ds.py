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

class overlay:
    def __init__(self):
        self.name = None
        self.fullscreen = 'true'
        self.normalized = 'true'
        self.range_mod = None
        self.alpha_mod = None
        self.width = None
        self.height = None
        self.descs = []
    def add_single_button(self, func, x, y, shape, rx, ry, img, target):
        desc = overlay_desc()
        desc.func = func
        desc.x = x
        desc.y = y
        desc.shape = shape
        desc.rx = rx
        desc.ry = ry
        desc.img = img
        desc.target = target
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

# portrait
ol_portrait = overlay()
ol_portrait.name = 'portrait'
ol_portrait.range_mod = '1.5'
ol_portrait.alpha_mod = '2.0'
ol_portrait.width = 1080
ol_portrait.height = 2248

# dpad
ol_portrait.add_single_button('nul', 160, 2050, 'rect', 160, 160, 'dpad.png', None)
ol_portrait.add_cross_touch('up', 'right', 'down', 'left', 160, 2050, 96, 96, 64)
ol_portrait.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', 160, 2050, 96, 96, 48)

# abxy
ol_portrait.add_cross_image('abxy_x.png', 'abxy_a.png', 'abxy_b.png', 'abxy_y.png', ol_portrait.width - 200, 2050, 136, 136, 64)
ol_portrait.add_cross_touch('x', 'a', 'b', 'y', ol_portrait.width - 200, 2050, 136, 136, 64)
ol_portrait.add_diagonal_touch('a|x', 'b|a', 'y|b', 'x|y', ol_portrait.width - 200, 2050, 68, 68, 24)

# ss
ol_portrait.add_lr('select', 'start', ol_portrait.width / 2, 2200, 100, 80, 20, 'ss_select.png', 'ss_start.png', None, None)

# lr
ol_portrait.add_lr('l', 'r', ol_portrait.width / 2, 1810, ol_portrait.width / 2 - 90, 90, 30, 'trigger_l.png', 'trigger_r.png', None, None)

# sl
ol_portrait.add_lr('load_state', 'save_state', ol_portrait.width / 2, 1810, ol_portrait.width / 2 - 390, 30, 30, 'func_load.png', 'func_save.png', None, None)

# ff
ol_portrait.add_single_button('toggle_fast_forward', 460, 1810, 'rect', 30, 30, 'func_ff.png', None)

# main menu
ol_portrait.add_single_button('menu_toggle', ol_portrait.width / 2, 1810, 'rect', 30, 30, 'rgui.png', None)

overlays.append(ol_portrait)

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
        print('overlay%d_desc%d = "%s,%f,%f,%s,%f,%f"' % (i, j, desc.func, desc.x / overlays[i].width, desc.y / overlays[i].height, desc.shape, desc.rx / overlays[i].width, desc.ry / overlays[i].height))
        if desc.img is not None:
            print('overlay%d_desc%d_overlay = %s' % (i, j, desc.img))
        if desc.target is not None:
            print('overlay%d_desc%d_next_target = "%s"' % (i, j, desc.target))
    print()

sys.exit(0)