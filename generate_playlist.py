import sys
import subprocess
from os import listdir
from os.path import isfile, join, basename, splitext

print('{')
print('  "version": "1.4",')
# print('  "default_core_path": "C:\\\\bin\\\\RetroArch\\\\cores\\\\bsnes_libretro.dll",')
# print('  "default_core_name": "Nintendo - SNES / SFC (bsnes)",')
print('  "default_core_path": "C:\\\\bin\\\\RetroArch\\\\cores\\\\mesen_libretro.dll",')
print('  "default_core_name": "Nintendo - NES / Famicom (Mesen)",')
print('  "label_display_mode": 0,')
print('  "right_thumbnail_mode": 0,')
print('  "left_thumbnail_mode": 0,')
print('  "sort_mode": 0,')
print('  "items": [')

# mypath = "/c/Users/Xeno/OneDrive/VG/02_snes_rom"
mypath = "/c/Users/Xeno/OneDrive/VG/01_nes_rom"
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
# print("\n".join(onlyfiles))
for f in onlyfiles:
    # print(f)
    out = subprocess.Popen(['7z', 'l', '-slt', f],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    out_str = stdout.decode('utf-8')
    path_trait = '----------\nPath = '
    idx = out_str.find(path_trait)
    idx2 = out_str.find('\n', idx + len(path_trait))
    content_path = out_str[idx + len(path_trait):idx2]
    path = f.replace('/c/', 'C:/').replace('/', '\\\\') + '#' + content_path
    root, ext = splitext(f)
    label = basename(root)
    crc_trait = 'CRC = '
    idx = out_str.find(crc_trait)
    idx2 = out_str.find('\n', idx + len(crc_trait))
    crc = out_str[idx + len(crc_trait):idx2]
    print('    {')
    print('      "path": "' + path + '",')
    print('      "label": "' + label + '",')
    print('      "core_path": "DETECT",')
    print('      "core_name": "DETECT",')
    print('      "crc32": "' + crc + '|crc",')
    # print('      "db_name": "Nintendo - Super Nintendo Entertainment System.lpl"')
    print('      "db_name": "Nintendo - Nintendo Entertainment System.lpl"')
    print('    },')
    # break

print('  ]')
print('}')

sys.exit(0)