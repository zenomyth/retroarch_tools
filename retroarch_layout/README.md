# RetroArch Layout Generator

Generates RetroArch overlay config (`.cfg`) files for touchscreen gamepad layouts.

## Usage

Run any generator to produce its corresponding `<console>.cfg`:

```bash
python generate_overlay_nes.py
python generate_overlay_snes.py
python generate_overlay_ps.py
...
```

Output goes to the directory specified in `config.toml` (e.g. `C:\hiroshi\data\temp\vg\nes.cfg`).

## Configuration

Edit `config.toml` to change display size, output path, or edge margin:

```toml
[screen]
width = 1080
height = 1920

[output]
directory = "C:\\hiroshi\\data\\temp\\vg"

[layout]
margin = 20
```

The `margin` value (in pixels) ensures no touch zone is placed within that distance from the left/right screen edges, preventing conflicts with system gesture navigation.

## Files

| File | Console |
|------|---------|
| `generate_overlay_nes.py` | NES |
| `generate_overlay_snes.py` | SNES |
| `generate_overlay_ps.py` | PlayStation |
| `generate_overlay_gba.py` | Game Boy Advance |
| `generate_overlay_gameboy.py` | Game Boy / Game Boy Color |
| `generate_overlay_ds.py` | Nintendo DS |
| `generate_overlay_n64.py` | Nintendo 64 |
| `common.py` | Shared overlay classes and output logic |
| `config.toml` | Screen size, output dir, and layout margin |
