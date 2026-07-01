import os


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
        for func, px, py in [(func_n, x, y - dy), (func_e, x + dx, y), (func_s, x, y + dy), (func_w, x - dx, y)]:
            desc = overlay_desc()
            desc.func = func
            desc.x = px
            desc.y = py
            desc.shape = 'radial'
            desc.rx = desc.ry = r
            self.descs.append(desc)

    def add_diagonal_touch(self, func_ne, func_se, func_sw, func_nw, x, y, dx, dy, r):
        for func, px, py in [(func_ne, x + dx, y - dy), (func_se, x + dx, y + dy), (func_sw, x - dx, y + dy), (func_nw, x - dx, y - dy)]:
            desc = overlay_desc()
            desc.func = func
            desc.x = px
            desc.y = py
            desc.shape = 'radial'
            desc.rx = desc.ry = r
            self.descs.append(desc)

    def add_cross_image(self, img_n, img_e, img_s, img_w, x, y, dx, dy, r):
        for img, px, py in [(img_n, x, y - dy), (img_e, x + dx, y), (img_s, x, y + dy), (img_w, x - dx, y)]:
            desc = overlay_desc()
            desc.img = img
            desc.x = px
            desc.y = py
            desc.shape = 'radial'
            desc.rx = desc.ry = r
            self.descs.append(desc)

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


def get_console_name(script_path):
    name = os.path.splitext(os.path.basename(script_path))[0]
    name = name.replace('generate_overlay_', '')
    return name


def load_config(config_path=None):
    import tomllib
    if config_path is None:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.toml')
    with open(config_path, 'rb') as f:
        cfg = tomllib.load(f)
    margin = cfg.get('layout', {}).get('margin', 0)
    return cfg['screen']['width'], cfg['screen']['height'], cfg['output']['directory'], margin


def write_output(overlays, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='\n') as f:
        f.write('overlays = %d\n' % len(overlays))
        f.write('\n')
        for i in range(len(overlays)):
            ol = overlays[i]
            f.write('overlay%d_full_screen = %s\n' % (i, ol.fullscreen))
            f.write('overlay%d_normalized = %s\n' % (i, ol.normalized))
            f.write('overlay%d_name = "%s"\n' % (i, ol.name))
            f.write('overlay%d_range_mod = %s\n' % (i, ol.range_mod))
            f.write('overlay%d_alpha_mod = %s\n' % (i, ol.alpha_mod))
            f.write('\n')
        for i in range(len(overlays)):
            f.write('overlay%d_descs = %d\n' % (i, len(overlays[i].descs)))
            for j in range(len(overlays[i].descs)):
                desc = overlays[i].descs[j]
                f.write('overlay%d_desc%d = "%s,%f,%f,%s,%f,%f"\n' % (
                    i, j, desc.func,
                    desc.x / overlays[i].width,
                    desc.y / overlays[i].height,
                    desc.shape,
                    desc.rx / overlays[i].width,
                    desc.ry / overlays[i].height
                ))
                if desc.img is not None:
                    f.write('overlay%d_desc%d_overlay = %s\n' % (i, j, desc.img))
                if desc.target is not None:
                    f.write('overlay%d_desc%d_next_target = "%s"\n' % (i, j, desc.target))
                if hasattr(desc, 'range_mod') and desc.range_mod is not None:
                    f.write('overlay%d_desc%d_range_mod = %s\n' % (i, j, desc.range_mod))
                if hasattr(desc, 'pct') and desc.pct is not None:
                    f.write('overlay%d_desc%d_pct = %s\n' % (i, j, desc.pct))
                if hasattr(desc, 'movable') and desc.movable is not None:
                    f.write('overlay%d_desc%d_movable = %s\n' % (i, j, desc.movable))
            f.write('\n')
