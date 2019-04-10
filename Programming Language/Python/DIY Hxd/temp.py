import binascii

with open("bin/ex01.vhd", "rb") as f:
    f.seek(0 * 512 + 446)
    text = f.read(32)
    string = list(binascii.b2a_hex(text).upper().decode())

for i in range(1, len(string), 2):
    string[i-1] += string[i]
    string[i] = ''

while '' in string:
    string.remove('')

part_num = 1

for index in range(0, 32, 16):
    print(f"Partition [{part_num}]", end=" ")
    part_num += 1
    print(" ".join(string[index:index+16]), end=" ")
    print()
