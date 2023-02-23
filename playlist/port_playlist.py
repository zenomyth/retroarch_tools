import sys
import json
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "an", ["help"])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr)
        return 2
    android_flag = False
    for o, a in opts:
        if o == "-a":
            android_flag = True
        elif o in ("-h", "--help"):
            print("Usage: python {} [-a] <firmware-folder>".format(Path(__file__).name))
            print("       -a  convert for Android")
            return 0
        else:
            assert False, "unhandled option"

    if len(args) < 1:
        print("Playlist required!", file=sys.stderr)
        sys.exit(1)
    playlist_file = args[0]
    with open(playlist_file, "rb") as json_file:
        playlist = json.load(json_file)
    if len(playlist["items"]) == 0:
        print("This script doesn't work with empty playlist", file=sys.stderr)
        sys.exit(1)
    rom_path_1 = "C:\\OneDrive\\vg_classic\\"
    core_path_1 = "cores\\"
    core_ext_1 = ".dll"
    path_delim_1 = "\\"
    if android_flag:
        rom_path_2 = "/storage/emulated/0/0/vg/"
        core_path_2 = "cores/"
        core_ext_2 = "_android.so"
        path_delim_2 = "/"
    else:
        rom_path_2 = "/storage/roms/0/vg_classic/"
        core_path_2 = "/tmp/cores/"
        core_ext_2 = ".so"
        path_delim_2 = "/"
    playlist.update({"default_core_path": playlist["default_core_path"].replace(core_path_1, core_path_2).replace(core_ext_1, core_ext_2)})
    for item in playlist["items"]:
        item.update({"path": item["path"].replace(rom_path_1, rom_path_2).replace(path_delim_1, path_delim_2)})
    json.dump(playlist, sys.stdout, indent="  ")
    print("")

if __name__ == '__main__':
    main()
    sys.exit(0)
