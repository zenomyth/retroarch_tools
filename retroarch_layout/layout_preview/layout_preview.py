import sys
import os
import re
import tomllib
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

FUNC_COLORS = {
    'nul':        (100, 100, 100, 80),
    'up':         ( 65, 105, 225, 100),
    'down':       ( 65, 105, 225, 100),
    'left':       ( 65, 105, 225, 100),
    'right':      ( 65, 105, 225, 100),
    'a':          (220,  20,  60, 100),
    'b':          (255, 165,   0, 100),
    'x':          (100, 149, 237, 100),
    'y':          (218, 165,  32, 100),
    'start':      ( 60, 179, 113, 120),
    'select':     ( 60, 179, 113, 120),
    'l':          (147, 112, 219, 100),
    'r':          (147, 112, 219, 100),
    'l1':         (147, 112, 219, 100),
    'r1':         (147, 112, 219, 100),
    'l2':         (147, 112, 219,  80),
    'r2':         (147, 112, 219,  80),
    'menu_toggle':(255, 215,   0, 120),
    'overlay_next':(255, 140,   0, 120),
    'load_state': (  0, 206, 209, 100),
    'save_state': (  0, 206, 209, 100),
    'toggle_fast_forward': (255, 105, 180, 100),
    'analog_left':(255,  20, 147,  80),
    'analog_right':(255, 20, 147, 80),
}

def resolve(path, base):
    if os.path.isabs(path):
        return path
    return os.path.normpath(os.path.join(base, path))

def load_config(toml_path):
    with open(toml_path, 'rb') as f:
        cfg = tomllib.load(f)
    base = os.path.dirname(os.path.abspath(toml_path))
    result = {
        'cfg_path': resolve(cfg['input']['cfg'], base),
        'output_path': resolve(cfg['output']['path'], base),
        'design_w': cfg['screen']['width'],
        'design_h': cfg['screen']['height'],
        'phone_w': None,
        'phone_h': None,
    }
    if 'phone' in cfg:
        result['phone_w'] = cfg['phone']['width']
        result['phone_h'] = cfg['phone']['height']
    return result

def parse_cfg(filepath):
    overlays = {}

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                continue

            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()

            if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
                value = value[1:-1]

            m = re.match(r'overlay(\d+)_(.+)', key)
            if not m:
                continue

            idx = int(m.group(1))
            rest = m.group(2)

            if idx not in overlays:
                overlays[idx] = {}
            overlays[idx][rest] = value

            dm = re.match(r'desc(\d+)(?:_(.+))?', rest)
            if dm:
                desc_idx = int(dm.group(1))
                desc_prop = dm.group(2)

                descs = overlays[idx].setdefault('_descs', {})
                if desc_idx not in descs:
                    descs[desc_idx] = {}

                if desc_prop:
                    descs[desc_idx][desc_prop] = value
                else:
                    parts = [p.strip() for p in value.split(',')]
                    if len(parts) == 6:
                        descs[desc_idx]['func'] = parts[0]
                        descs[desc_idx]['x'] = float(parts[1])
                        descs[desc_idx]['y'] = float(parts[2])
                        descs[desc_idx]['shape'] = parts[3]
                        descs[desc_idx]['rx'] = float(parts[4])
                        descs[desc_idx]['ry'] = float(parts[5])

    return overlays

def get_color(func):
    if func in FUNC_COLORS:
        return FUNC_COLORS[func]
    if '|' in func:
        return (200, 200, 200, 60)
    return (180, 180, 180, 80)

def draw_preview(cfg_path, output_path, design_w, design_h, phone_w=None, phone_h=None):
    overlays = parse_cfg(cfg_path)

    if not overlays:
        print("No overlays found.")
        return

    idx = min(overlays.keys())
    ol = overlays[idx]

    if phone_w and phone_h:
        canvas_w, canvas_h = phone_w, phone_h

        overlay_h_by_w = int(design_h * phone_w / design_w)
        if overlay_h_by_w <= phone_h:
            overlay_w = phone_w
            overlay_h = overlay_h_by_w
            offset_x = 0
            offset_y = (phone_h - overlay_h) // 2
        else:
            overlay_w = int(design_w * phone_h / design_h)
            overlay_h = phone_h
            offset_x = (phone_w - overlay_w) // 2
            offset_y = 0

        img = Image.new('RGB', (canvas_w, canvas_h), (10, 10, 15))
        overlay_bg = Image.new('RGB', (overlay_w, overlay_h), (18, 18, 28))
        img.paste(overlay_bg, (offset_x, offset_y))
        mode = 'phone'
    else:
        canvas_w, canvas_h = design_w, design_h
        overlay_w, overlay_h = design_w, design_h
        offset_x = offset_y = 0
        img = Image.new('RGB', (canvas_w, canvas_h), (18, 18, 28))
        mode = 'design'

    draw = ImageDraw.Draw(img, 'RGBA')

    try:
        font = ImageFont.truetype("arial.ttf", 16)
        small_font = ImageFont.truetype("arial.ttf", 12)
        title_font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        title_font = font = small_font = ImageFont.load_default()

    name = ol.get('name', f'overlay{idx}')
    info = f"Overlay: {name}  |  layout {design_w}x{design_h}"
    if mode == 'phone':
        info += f"  |  phone {phone_w}x{phone_h}"
    if 'range_mod' in ol:
        info += f"  |  range_mod={ol['range_mod']}"
    if 'alpha_mod' in ol:
        info += f"  |  alpha_mod={ol['alpha_mod']}"
    draw.text((10, 6), info, fill=(220, 220, 220), font=title_font)

    cfg_basename = os.path.basename(cfg_path)
    draw.text((10, canvas_h - 22), f"Config: {cfg_basename}", fill=(100, 100, 110), font=small_font)

    if mode == 'phone':
        border_color = (40, 40, 50, 255)
        draw.rectangle(
            [offset_x, offset_y, offset_x + overlay_w - 1, offset_y + overlay_h - 1],
            outline=border_color, width=1
        )

    descs = ol.get('_descs', {})

    for desc_idx in sorted(descs.keys()):
        desc = descs[desc_idx]

        func = desc.get('func', '?')
        x = desc.get('x', 0)
        y = desc.get('y', 0)
        shape = desc.get('shape', 'rect')
        rx = desc.get('rx', 0)
        ry = desc.get('ry', 0)

        px = int(x * overlay_w) + offset_x
        py = int(y * overlay_h) + offset_y
        prx = int(rx * overlay_w)
        pry = int(ry * overlay_h)

        if prx < 1 or pry < 1:
            continue

        color = get_color(func)

        x0 = px - prx
        y0 = py - pry
        x1 = px + prx
        y1 = py + pry

        if shape == 'rect':
            draw.rectangle([x0, y0, x1, y1], fill=color, outline=(255, 255, 255, 100), width=1)
        elif shape == 'radial':
            draw.ellipse([x0, y0, x1, y1], fill=color, outline=(255, 255, 255, 100), width=1)

        overlay_img = desc.get('overlay', None)

        if func != 'nul':
            label = func
            if 'next_target' in desc:
                label = f"{func} \u2192 {desc['next_target']}"
            fnt = font
        elif overlay_img:
            label = os.path.splitext(overlay_img)[0]
            if 'next_target' in desc:
                label = f"{label} \u2192 {desc['next_target']}"
            fnt = small_font
        else:
            label = f"#{desc_idx}"
            fnt = small_font

        bbox = draw.textbbox((0, 0), label, font=fnt)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = max(0, min(px - tw // 2, canvas_w - tw))
        ty = max(0, min(py - th // 2, canvas_h - th))
        draw.text((tx, ty), label, fill=(255, 255, 255, 220), font=fnt)

    img.save(output_path)
    print(f"Saved: {output_path}")
    print(f"  Overlay: {ol.get('name', '?')}  |  {len(descs)} descriptors")
    if mode == 'phone':
        print(f"  Phone: {phone_w}x{phone_h}  |  overlay area: {overlay_w}x{overlay_h}  |  offset: ({offset_x}, {offset_y})")
    else:
        print(f"  Layout: {design_w}x{design_h}")

if __name__ == '__main__':
    toml_path = os.path.join(SCRIPT_DIR, 'layout_preview.toml')

    if len(sys.argv) > 1:
        if sys.argv[1] == '--config' and len(sys.argv) > 2:
            toml_path = os.path.abspath(sys.argv[2])

    if not os.path.exists(toml_path):
        print(f"Config not found: {toml_path}")
        sys.exit(1)

    config = load_config(toml_path)

    if len(sys.argv) > 1 and sys.argv[1] != '--config':
        config['cfg_path'] = os.path.abspath(sys.argv[1])
        config['output_path'] = os.path.join(
            os.path.dirname(config['output_path']),
            os.path.splitext(os.path.basename(config['cfg_path']))[0] + '.png'
        )

    if not os.path.exists(config['cfg_path']):
        print(f"Input cfg not found: {config['cfg_path']}")
        sys.exit(1)

    draw_preview(
        config['cfg_path'],
        config['output_path'],
        config['design_w'],
        config['design_h'],
        config['phone_w'],
        config['phone_h'],
    )
