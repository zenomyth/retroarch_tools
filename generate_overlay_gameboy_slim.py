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

# portrait
ol_portrait = overlay()
ol_portrait.name = 'portrait'
ol_portrait.range_mod = '1.5'
ol_portrait.alpha_mod = '2.0'
ol_portrait.width = 1080
ol_portrait.height = 2248

# dpad
ol_portrait.add_single_button('nul', 210, 1575, 'rect', 200, 210, 'dpad.png', None)
ol_portrait.add_cross_touch('up', 'right', 'down', 'left', 210, 1575, 120, 120, 90)
ol_portrait.add_diagonal_touch('right|up', 'down|right', 'left|down', 'up|left', 210, 1575, 120, 120, 70)

# ab
ol_portrait.add_ab('nul', 'nul', ol_portrait.width - 190, 1575, 100, 40, 80, 80, 'b.png', 'a.png', None, None)
ol_portrait.add_ab('b', 'a', ol_portrait.width - 190, 1575, 100, 40, 90, 90, None, None, None, None)
ol_portrait.add_single_button('a|b', ol_portrait.width - 190, 1575, 'rect', 15, 15, None, None)

# ss
ol_portrait.add_lr('select', 'start', ol_portrait.width / 2, 1250, 79, 59, 57, 'select.png', 'start.png', None, None)

# sl
ol_portrait.add_lr('load_state', 'save_state', ol_portrait.width / 2, 1050, ol_portrait.width / 2 - 60, 50, 50, 'load.png', 'save.png', None, None)

# ff
ol_portrait.add_single_button('toggle_fast_forward', 260, 1050, 'rect', 50, 50, 'ff2.png', None)

# abss
ol_portrait.add_single_button('a|b|select|start', ol_portrait.width - 260, 1050, 'rect', 50, 50, 'abss.png', None)

# main menu
ol_portrait.add_single_button('menu_toggle', ol_portrait.width / 2, 1050, 'rect', 40, 40, 'rgui.png', None)

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