import sys
import copy

class overlay:
    name = None
    fullscreen = 'true'
    normalized = 'true'
    range_mod = None
    alpha_mod = None
    width = None
    height = None
    descs = []
    def __init__(self):
        pass

class overlay_desc:
    name = None
    x = None
    y = None
    shape = None
    rx = None
    ry = None
    img = None
    target = None
    def __init__(self):
        pass

overlays = []

ol_portrait = overlay()
ol_portrait.name = 'portrait'
ol_portrait.range_mod = '1.5'
ol_portrait.alpha_mod = '2.0'
ol_portrait.width = 1080
ol_portrait.height = 2248

# dpad
dpad = overlay_desc()
dpad.name = 'nul'
dpad.x = 210
dpad.y = 1575
dpad.shape = 'rect'
dpad.rx = 200
dpad.ry = 210 # The image looks better when stretched a bit on Y axis
dpad.img = 'dpad.png'
ol_portrait.descs.append(dpad)
dpad_btn_to_center_dist = 120
dpad_btn_r = 90
dpad_btn_diagonal_r = 70
dpad_left = overlay_desc()
dpad_left.name = 'left'
dpad_left.x = dpad.x - dpad_btn_to_center_dist
dpad_left.y = dpad.y
dpad_left.shape = 'radial'
dpad_left.rx = dpad_btn_r
dpad_left.ry = dpad_btn_r
ol_portrait.descs.append(dpad_left)
dpad_right = overlay_desc()
dpad_right.name = 'right'
dpad_right.x = dpad.x + dpad_btn_to_center_dist
dpad_right.y = dpad.y
dpad_right.shape = 'radial'
dpad_right.rx = dpad_btn_r
dpad_right.ry = dpad_btn_r
ol_portrait.descs.append(dpad_right)
dpad_up = overlay_desc()
dpad_up.name = 'up'
dpad_up.x = dpad.x
dpad_up.y = dpad.y - dpad_btn_to_center_dist
dpad_up.shape = 'radial'
dpad_up.rx = dpad_btn_r
dpad_up.ry = dpad_btn_r
ol_portrait.descs.append(dpad_up)
dpad_down = overlay_desc()
dpad_down.name = 'down'
dpad_down.x = dpad.x
dpad_down.y = dpad.y + dpad_btn_to_center_dist
dpad_down.shape = 'radial'
dpad_down.rx = dpad_btn_r
dpad_down.ry = dpad_btn_r
ol_portrait.descs.append(dpad_down)
dpad_left_down = overlay_desc()
dpad_left_down.name = 'left|down'
dpad_left_down.x = dpad.x - dpad_btn_to_center_dist
dpad_left_down.y = dpad.y + dpad_btn_to_center_dist
dpad_left_down.shape = 'radial'
dpad_left_down.rx = dpad_btn_diagonal_r
dpad_left_down.ry = dpad_btn_diagonal_r
ol_portrait.descs.append(dpad_left_down)
dpad_right_up = overlay_desc()
dpad_right_up.name = 'right|up'
dpad_right_up.x = dpad.x + dpad_btn_to_center_dist
dpad_right_up.y = dpad.y - dpad_btn_to_center_dist
dpad_right_up.shape = 'radial'
dpad_right_up.rx = dpad_btn_diagonal_r
dpad_right_up.ry = dpad_btn_diagonal_r
ol_portrait.descs.append(dpad_right_up)
dpad_up_left = overlay_desc()
dpad_up_left.name = 'up|left'
dpad_up_left.x = dpad.x - dpad_btn_to_center_dist
dpad_up_left.y = dpad.y - dpad_btn_to_center_dist
dpad_up_left.shape = 'radial'
dpad_up_left.rx = dpad_btn_diagonal_r
dpad_up_left.ry = dpad_btn_diagonal_r
ol_portrait.descs.append(dpad_up_left)
dpad_down_right = overlay_desc()
dpad_down_right.name = 'down|right'
dpad_down_right.x = dpad.x + dpad_btn_to_center_dist
dpad_down_right.y = dpad.y + dpad_btn_to_center_dist
dpad_down_right.shape = 'radial'
dpad_down_right.rx = dpad_btn_diagonal_r
dpad_down_right.ry = dpad_btn_diagonal_r
ol_portrait.descs.append(dpad_down_right)

# abxy
abxy_x = ol_portrait.width - 260
abxy_y = dpad.y
abxy_btn_to_center_dist_x = 170
abxy_btn_to_center_dist_y = 175
abxy_btn_r = 80
abxy_btn_touch_r = 90
abxy_btn_a = overlay_desc()
abxy_btn_a.name = 'nul'
abxy_btn_a.x = abxy_x + abxy_btn_to_center_dist_x
abxy_btn_a.y = abxy_y
abxy_btn_a.shape = 'radial'
abxy_btn_a.rx = abxy_btn_r
abxy_btn_a.ry = abxy_btn_r
abxy_btn_a.img = 'a.png'
ol_portrait.descs.append(abxy_btn_a)
abxy_touch_a = copy.deepcopy(abxy_btn_a)
abxy_touch_a.name = 'a'
abxy_touch_a.rx = abxy_btn_touch_r
abxy_touch_a.ry = abxy_btn_touch_r
abxy_touch_a.img = None
ol_portrait.descs.append(abxy_touch_a)
abxy_btn_b = overlay_desc()
abxy_btn_b.name = 'nul'
abxy_btn_b.x = abxy_x
abxy_btn_b.y = abxy_y + abxy_btn_to_center_dist_y
abxy_btn_b.shape = 'radial'
abxy_btn_b.rx = abxy_btn_r
abxy_btn_b.ry = abxy_btn_r
abxy_btn_b.img = 'b.png'
ol_portrait.descs.append(abxy_btn_b)
abxy_touch_b = copy.deepcopy(abxy_btn_b)
abxy_touch_b.name = 'b'
abxy_touch_b.rx = abxy_btn_touch_r
abxy_touch_b.ry = abxy_btn_touch_r
abxy_touch_b.img = None
ol_portrait.descs.append(abxy_touch_b)
abxy_btn_y = overlay_desc()
abxy_btn_y.name = 'nul'
abxy_btn_y.x = abxy_x - abxy_btn_to_center_dist_x
abxy_btn_y.y = abxy_y
abxy_btn_y.shape = 'radial'
abxy_btn_y.rx = abxy_btn_r
abxy_btn_y.ry = abxy_btn_r
abxy_btn_y.img = 'y.png'
ol_portrait.descs.append(abxy_btn_y)
abxy_touch_y = copy.deepcopy(abxy_btn_y)
abxy_touch_y.name = 'y'
abxy_touch_y.rx = abxy_btn_touch_r
abxy_touch_y.ry = abxy_btn_touch_r
abxy_touch_y.img = None
ol_portrait.descs.append(abxy_touch_y)
abxy_btn_x = overlay_desc()
abxy_btn_x.name = 'nul'
abxy_btn_x.x = abxy_x
abxy_btn_x.y = abxy_y - abxy_btn_to_center_dist_y
abxy_btn_x.shape = 'radial'
abxy_btn_x.rx = abxy_btn_r
abxy_btn_x.ry = abxy_btn_r
abxy_btn_x.img = 'x.png'
ol_portrait.descs.append(abxy_btn_x)
abxy_touch_x = copy.deepcopy(abxy_btn_x)
abxy_touch_x.name = 'x'
abxy_touch_x.rx = abxy_btn_touch_r
abxy_touch_x.ry = abxy_btn_touch_r
abxy_touch_x.img = None
ol_portrait.descs.append(abxy_touch_x)

# ss
ss_x = ol_portrait.width / 2
ss_y = 1250
ss_btn_to_center_dist = 80
ss_rx = 60
ss_ry = 60
ss_start = overlay_desc()
ss_start.name = 'start'
ss_start.x = ss_x + ss_btn_to_center_dist
ss_start.y = ss_y
ss_start.shape = 'rect'
ss_start.rx = ss_rx
ss_start.ry = ss_ry
ss_start.img = 'start.png'
ol_portrait.descs.append(ss_start)
ss_select = overlay_desc()
ss_select.name = 'select'
ss_select.x = ss_x - ss_btn_to_center_dist
ss_select.y = ss_y
ss_select.shape = 'rect'
ss_select.rx = ss_rx
ss_select.ry = ss_ry
ss_select.img = 'select.png'
ol_portrait.descs.append(ss_select)

# lr
lr_x = ol_portrait.width / 2
lr_y = 1200
lr_btn_to_center_dist = ol_portrait.width / 2 - 110
lr_rx = 100
lr_ry = 50
lr_l = overlay_desc()
lr_l.name = 'l'
lr_l.x = lr_x - lr_btn_to_center_dist
lr_l.y = lr_y
lr_l.shape = 'rect'
lr_l.rx = lr_rx
lr_l.ry = lr_ry
lr_l.img = 'l1.png'
ol_portrait.descs.append(lr_l)
lr_r = overlay_desc()
lr_r.name = 'r'
lr_r.x = lr_x + lr_btn_to_center_dist
lr_r.y = lr_y
lr_r.shape = 'rect'
lr_r.rx = lr_rx
lr_r.ry = lr_ry
lr_r.img = 'r1.png'
ol_portrait.descs.append(lr_r)

# nrr
nrr_x = ol_portrait.width / 2
nrr_y = 1050
nrr_rx = 40
nrr_ry = 40
nrr_rgui = overlay_desc()
nrr_rgui.name = 'menu_toggle'
nrr_rgui.x = nrr_x
nrr_rgui.y = nrr_y
nrr_rgui.shape = 'rect'
nrr_rgui.rx = nrr_rx
nrr_rgui.ry = nrr_ry
nrr_rgui.img = 'rgui.png'
ol_portrait.descs.append(nrr_rgui)

overlays.append(ol_portrait)

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
        print('overlay%d_desc%d = "%s,%f,%f,%s,%f,%f"' % (i, j, desc.name, desc.x / overlays[i].width, desc.y / overlays[i].height, desc.shape, desc.rx / overlays[i].width, desc.ry / overlays[i].height))
        if desc.img is not None:
            print('overlay%d_desc%d_overlay = %s' % (i, j, desc.img))
        if desc.target is not None:
            print('overlay%d_desc%d_next_target = "%s"' % (i, j, desc.target))

sys.exit(0)