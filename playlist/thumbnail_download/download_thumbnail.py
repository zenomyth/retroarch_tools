import sys
from urllib.parse import unquote, quote
from difflib import get_close_matches
import urllib.request

def get_titles():
    with open("ps1_titles.txt", "r") as f:
        titles = f.readlines()
    for t in titles:
        t = t.strip()
        if t.endswith(".png"):
            t = t[:-4]
        t = unquote(t)
        print(t)

def main():
    with open("ps1_titles.txt", "r") as f:
        titles = [line.rstrip() for line in f]
    ps_game = "Final Fantasy Anthology - Final Fantasy V (USA) (v1.1).m3u"
    matches = get_close_matches(ps_game, titles, n=1)
    standard_name = matches[0]
    print(standard_name)
    target_dir = "C:\\bin\\RetroArch-Win64\\thumbnails\\Sony - Playstation\\"
    base_url = "http://thumbnails.libretro.com/Sony%20-%20PlayStation/"
    named_boxarts_url = base_url + "Named_Boxarts/" + quote(standard_name) + ".png"
    urllib.request.urlretrieve(named_boxarts_url, target_dir + "Named_Boxarts\\" + standard_name + ".png")
    named_snaps_url = base_url + "Named_Snaps/" + quote(standard_name) + ".png"
    urllib.request.urlretrieve(named_snaps_url, target_dir + "Named_Snaps\\" + standard_name + ".png")
    named_titles_url = base_url + "Named_Titles/" + quote(standard_name) + ".png"
    urllib.request.urlretrieve(named_titles_url, target_dir + "Named_Titles\\" + standard_name + ".png")

if __name__ == '__main__':
    main()
    sys.exit(0)
