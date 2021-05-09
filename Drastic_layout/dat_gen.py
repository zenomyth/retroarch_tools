import sys

def format_block(x, y, w, h):
    data = [0] * 8
    data[0] = (x >> 8) & 0xFF
    data[1] = x & 0xFF
    data[2] = (y >> 8) & 0xFF
    data[3] = y & 0xFF
    data[4] = (w >> 8) & 0xFF
    data[5] = w & 0xFF
    data[6] = (h >> 8) & 0xFF
    data[7] = h & 0xFF
    return data

def generate_action_layout():
    data = [0] * 111
    device_width = 1080
    screen_width = 800
    screen_height = screen_width // 4 * 3
    dpad_y = 1291
    dpad_width = 320
    abxy_width = 400
    index = 0
    # Unknown field
    data[index + 3] = 7
    index += 4
    # Upper screen
    data[index:index + 8] = format_block((device_width - screen_width) // 2, 0, screen_width, screen_height)
    index += 8
    # Lower screen
    data[index:index + 8] = format_block((device_width - screen_width) // 2, screen_height, screen_width, screen_height)
    index += 8
    # Unknown field
    data[index + 1] = 1
    index += 2
    # Dpad
    data[index:index + 8] = format_block(0, dpad_y, dpad_width, dpad_width)
    index += 8
    # ABXY
    data[index:index + 8] = format_block(device_width - abxy_width // 2, dpad_y + dpad_width // 2, abxy_width, abxy_width)
    index += 8
    # L
    data[index:index + 8] = format_block(0, 1150, 135, 45)
    index += 8
    # R
    data[index:index + 8] = format_block(device_width - 135, 1150, 135, 45)
    index += 8
    # Start
    data[index:index + 8] = format_block(device_width // 2 + 20, dpad_y + dpad_width, 160, 80)
    index += 8
    # Select
    data[index:index + 8] = format_block(device_width // 2 - 20 - 160, dpad_y + dpad_width, 160, 80)
    index += 8
    # Unknown field
    data[index] = 1
    index += 1
    # Enable field for Dpad, L, R, Start, Select
    for i in range(5):
        data[index + i] = 1
    index += 5
    # Extra button I
    data[index:index + 8] = format_block(0, dpad_y + dpad_width + 80 + 100, 100, 100)
    index += 8
    # Extra button II
    data[index:index + 8] = format_block(200, dpad_y + dpad_width + 80 + 100, 100, 100)
    index += 8
    # Extra button III
    data[index:index + 8] = format_block(400, dpad_y + dpad_width + 80 + 100, 100, 100)
    index += 8
    # Enable field for extra button and ABXY
    for i in range(7):
        data[index + i] = 1
    index += 7
    print(data)
    f = open('LC_2_Pokemon Diamond (v05) (U)(Legacy).dat', 'wb')
    f.write(bytes(data))
    f.close()

def main():
    generate_action_layout()

if __name__ == '__main__':
    main()
    sys.exit(0)
