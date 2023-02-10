import sys
from pathlib import Path
import json
import zipfile

def main():
    if(len(sys.argv) < 2):
        print("Playlist required!", file=sys.stderr)
        sys.exit(1)
    playlist_file = sys.argv[1]
    # playlist_file = Path("C:/OneDrive/vg_classic/playlists/Atari - 2600.lpl")
    # print(playlist_file.is_file())
    with open(playlist_file, "rb") as json_file:
        playlist = json.load(json_file)
    if len(playlist["items"]) == 0:
        print("This script doesn't work with empty playlist", file=sys.stderr)
        sys.exit(1)
    rom_ref_0 = playlist["items"][0]["path"]
    rom_path = Path(rom_ref_0.replace("\\", "/")).parent
    rom_extension = Path(rom_ref_0).suffix
    db_name = playlist["items"][0]["db_name"]
    # print(rom_ref_0, rom_path, rom_extension, db_name)
    # json.dump(playlist, sys.stdout, indent="  ")
    existing_rom_refs = set()
    for item in playlist["items"]:
        existing_rom_refs.add(item["path"])
    # print(existing_rom_refs)
    rom_glob = rom_path.glob("*.zip")
    rom_refs = []
    for rom_file_path in rom_glob:
        rom_ref = str(rom_file_path)
        with zipfile.ZipFile(rom_file_path, "r") as zip_ref:
            # print(zip_ref.namelist())
            if len(zip_ref.namelist()) == 1:
                rom_name = next(x for x in zip_ref.namelist())
            else:
                rom_name = next((x for x in zip_ref.namelist() if x.lower().endswith(rom_extension)), None)
            # print(rom_name)
            if rom_name == None:
                print("Skipping " + rom_ref)
                continue
            rom_ref += "#" + rom_name
            rom_ref = rom_ref.replace("/", "\\")
            # print(rom_ref)
            if not rom_ref in existing_rom_refs:
                rom_refs.append(rom_ref)
    # print(rom_refs)
    if len(rom_refs) == 0:
        print("Nothing to update!")
        exit(0)
    for rom_ref in rom_refs:
        rom_label = rom_ref.split("#")[-1]
        rom_label = rom_label[0:rom_label.rfind(".")]
        playlist["items"].append(
            {
                "path": rom_ref,
                "label": rom_label,
                "core_path": "DETECT",
                "core_name": "DETECT",
                "crc32": "DETECT",
                "db_name": db_name
            }
        )
    json.dump(playlist, sys.stdout, indent="  ")
    # with open(playlist_file, "w") as json_file:
        # json.dump(playlist, json_file, indent="  ")
    print("{} title(s) updated.".format(len(rom_refs)))

if __name__ == '__main__':
    main()
    sys.exit(0)
