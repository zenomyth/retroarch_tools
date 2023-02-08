import zipfile
import binascii

# Calculate CRC from zip
filename = "Teenage Mutant Ninja Turtles II - The Arcade Game (U) [!].zip"
z = zipfile.ZipFile(filename)
f = z.open(z.namelist()[0])
# Skip the header
f.seek(16)
buf = f.read()
f.close()
buf = (binascii.crc32(buf) & 0xFFFFFFFF)
crc = "{:08X}".format(buf)