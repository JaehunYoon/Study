import binascii

# with open("bin/ex01.vhd", "rb") as f:
#     f.seek(446)
#     text = f.read(16)
#     string = list(binascii.b2a_hex(text).upper().decode())

# for i in range(1, len(string), 2):
#     string[i-1] += string[i]
#     string[i] = ''

# while '' in string:
#     string.remove('')

# print(" ".join(string))


def nav_bar():
    print("offset(h)", end=" ")
    for i in range(16):
        print(f"{hex(i)[2:].zfill(2).upper()}", end=" ")
    print()
    print("=" * 75, end='')
    print()

with open("bin/ex01.vhd", "rb") as f:
    f.seek(0)
    text = f.read(512)
    string = list(binascii.b2a_hex(text).upper().decode())

for i in range(1, len(string), 2):
    string[i-1] += string[i]
    string[i] = ''

while '' in string:
    string.remove('')

# print(" ".join(string))
print(string[0:16])

nav_bar()
