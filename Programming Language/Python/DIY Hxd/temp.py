import binascii


lba_address = 0

with open("bin/ex01.vhd", "rb") as f:
    f.seek(446)
    text = f.read(16)
    string = list(binascii.b2a_hex(text).upper().decode())

for i in range(1, len(string), 2):
    string[i-1] += string[i]
    string[i] = ''

while '' in string:
    string.remove('')

print(" ".join(string))
