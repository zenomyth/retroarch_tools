import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

range_mod = 1.5
alpha_mod = 2.0

h = 2248
w = 1080
h_min = 1150
h_max = 1900

overlay_num = 0

# Dpad
dpad_radius = 200
dpad_margin = 10
dpad_center = Point(dpad_radius + dpad_margin, 1575)
touch_center_dpad = 80 # Distance from dpad frame to touch center of each direction
touch_radius_dpad = touch_center_dpad + dpad_margin
touch_radius_diagonal_dpad = 60 + dpad_margin
print('overlay1_desc%d = "nul,%f,%f,rect,%f,%f"' % (overlay_num, dpad_center.x / w, dpad_center.y / h, dpad_radius / w, (dpad_radius + 10) / h))
print('overlay1_desc%d_overlay = dpad.png' % (overlay_num))
overlay_num += 1
left_center = Point(dpad_center.x - dpad_radius + touch_center_dpad, dpad_center.y)
print('overlay1_desc%d = "left,%f,%f,radial,%f,%f"' % (overlay_num, left_center.x / w, left_center.y / h, touch_radius_dpad / w, touch_radius_dpad / h))
overlay_num += 1
right_center = Point(dpad_center.x + dpad_radius - touch_center_dpad, dpad_center.y)
print('overlay1_desc%d = "right,%f,%f,radial,%f,%f"' % (overlay_num, right_center.x / w, right_center.y / h, touch_radius_dpad / w, touch_radius_dpad / h))
overlay_num += 1
up_center = Point(dpad_center.x, dpad_center.y - dpad_radius + touch_center_dpad)
print('overlay1_desc%d = "up,%f,%f,radial,%f,%f"' % (overlay_num, up_center.x / w, up_center.y / h, touch_radius_dpad / w, touch_radius_dpad / h))
overlay_num += 1
down_center = Point(dpad_center.x, dpad_center.y + dpad_radius - touch_center_dpad)
print('overlay1_desc%d = "down,%f,%f,radial,%f,%f"' % (overlay_num, down_center.x / w, down_center.y / h, touch_radius_dpad / w, touch_radius_dpad / h))
overlay_num += 1
print('overlay1_desc%d = "left|down,%f,%f,radial,%f,%f"' % (overlay_num, left_center.x / w, down_center.y / h, touch_radius_diagonal_dpad / w, touch_radius_diagonal_dpad / h))
overlay_num += 1
print('overlay1_desc%d = "right|up,%f,%f,radial,%f,%f"' % (overlay_num, right_center.x / w, up_center.y / h, touch_radius_diagonal_dpad / w, touch_radius_diagonal_dpad / h))
overlay_num += 1
print('overlay1_desc%d = "up|left,%f,%f,radial,%f,%f"' % (overlay_num, left_center.x / w, up_center.y / h, touch_radius_diagonal_dpad / w, touch_radius_diagonal_dpad / h))
overlay_num += 1
print('overlay1_desc%d = "down|right,%f,%f,radial,%f,%f"' % (overlay_num, right_center.x / w, down_center.y / h, touch_radius_diagonal_dpad / w, touch_radius_diagonal_dpad / h))
overlay_num += 1

# ABXY
abxy_radius = 250
abxy_margin = 10
abxy_center = Point(w - abxy_radius - abxy_margin, 1575)
touch_center_abxy = 80
touch_radius_abxy = touch_center_abxy + abxy_margin
a_center = Point(abxy_center.x + abxy_radius - touch_center_abxy, abxy_center.y)
print('overlay1_desc%d = "nul,%f,%f,radial,%f,%f"' % (overlay_num, a_center.x / w, a_center.y / h, touch_center_abxy / w, touch_center_abxy / h))
print('overlay1_desc%d_overlay = a.png' % (overlay_num))
overlay_num += 1
print('overlay1_desc%d = "a,%f,%f,radial,%f,%f"' % (overlay_num, a_center.x / w, a_center.y / h, touch_radius_abxy / w, touch_radius_abxy / h))
overlay_num += 1
b_center = Point(abxy_center.x, abxy_center.y + abxy_radius - touch_center_abxy + 5)
print('overlay1_desc%d = "nul,%f,%f,radial,%f,%f"' % (overlay_num, b_center.x / w, b_center.y / h, touch_center_abxy / w, touch_center_abxy / h))
print('overlay1_desc%d_overlay = b.png' % (overlay_num))
overlay_num += 1
print('overlay1_desc%d = "b,%f,%f,radial,%f,%f"' % (overlay_num, b_center.x / w, b_center.y / h, touch_radius_abxy / w, touch_radius_abxy / h))
overlay_num += 1
x_center = Point(abxy_center.x, abxy_center.y - abxy_radius + touch_center_abxy - 5)
print('overlay1_desc%d = "nul,%f,%f,radial,%f,%f"' % (overlay_num, x_center.x / w, x_center.y / h, touch_center_abxy / w, touch_center_abxy / h))
print('overlay1_desc%d_overlay = x.png' % (overlay_num))
overlay_num += 1
print('overlay1_desc%d = "x,%f,%f,radial,%f,%f"' % (overlay_num, x_center.x / w, x_center.y / h, touch_radius_abxy / w, touch_radius_abxy / h))
overlay_num += 1
y_center = Point(abxy_center.x - abxy_radius + touch_center_abxy, abxy_center.y)
print('overlay1_desc%d = "nul,%f,%f,radial,%f,%f"' % (overlay_num, y_center.x / w, y_center.y / h, touch_center_abxy / w, touch_center_abxy / h))
print('overlay1_desc%d_overlay = y.png' % (overlay_num))
overlay_num += 1
print('overlay1_desc%d = "y,%f,%f,radial,%f,%f"' % (overlay_num, y_center.x / w, y_center.y / h, touch_radius_abxy / w, touch_radius_abxy / h))
overlay_num += 1

# Start / Select
ss_radius_w = 60
ss_radius_h = 60
ss_y = 1250
start_x = w / 2 + 80
print('overlay1_desc%d = "start,%f,%f,rect,%f,%f"' % (overlay_num, start_x / w, ss_y / h, ss_radius_w / w, ss_radius_h / h))
print('overlay1_desc%d_overlay = start.png' % (overlay_num))
overlay_num += 1
select_x = w - start_x
print('overlay1_desc%d = "select,%f,%f,rect,%f,%f"' % (overlay_num, select_x / w, ss_y / h, ss_radius_w / w, ss_radius_h / h))
print('overlay1_desc%d_overlay = select.png' % (overlay_num))
overlay_num += 1

# L / R
lr_radius_w = 100
lr_radius_h = 50
lr_y = 1200
l_x = 100
print('overlay1_desc%d = "l,%f,%f,rect,%f,%f"' % (overlay_num, l_x / w, lr_y / h, lr_radius_w / w, lr_radius_h / h))
print('overlay1_desc%d_overlay = l1.png' % (overlay_num))
overlay_num += 1
r_x = w - l_x
print('overlay1_desc%d = "r,%f,%f,rect,%f,%f"' % (overlay_num, r_x / w, lr_y / h, lr_radius_w / w, lr_radius_h / h))
print('overlay1_desc%d_overlay = r1.png' % (overlay_num))
overlay_num += 1

# next / rgui / rotate
nrr_radius_w = 40
nrr_radius_h = 40
nrr_y = 1050
next_x = w / 2 - 120
print('overlay1_desc%d = "overlay_next,%f,%f,rect,%f,%f"' % (overlay_num, next_x / w, nrr_y / h, nrr_radius_w / w, nrr_radius_h / h))
print('overlay1_desc%d_overlay = next.png' % (overlay_num))
print('overlay1_desc%d_next_target = "menu"' % (overlay_num))
overlay_num += 1
rgui_x = w / 2
print('overlay1_desc%d = "menu_toggle,%f,%f,rect,%f,%f"' % (overlay_num, rgui_x / w, nrr_y / h, nrr_radius_w / w, nrr_radius_h / h))
print('overlay1_desc%d_overlay = rgui.png' % (overlay_num))
overlay_num += 1
rotate_x = w - next_x
print('overlay1_desc%d = "overlay_next,%f,%f,rect,%f,%f"' % (overlay_num, rotate_x / w, nrr_y / h, nrr_radius_w / w, nrr_radius_h / h))
print('overlay1_desc%d_overlay = rotate.png' % (overlay_num))
print('overlay1_desc%d_next_target = "landscape"' % (overlay_num))
overlay_num += 1

sys.exit(0)