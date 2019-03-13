import binascii

inp = int(input("입력 : ")) * 512


# 상단 바
print("offset(h)", end=" ")
for i in range(16):
    print(f"{hex(i)[2:].zfill(2).upper()}", end=" ")
print()
print("=" * 75, end="")
print()

with open("ex01.vhd", "rb") as f:
    f.seek(inp)
    text = f.read(512)
    string = binascii.b2a_hex(text)

cnt = 0
offset = 0
temp = []
arr = []
space = False
enter = True


for i in string:
    if enter is True:
        print(hex(offset)[2:].zfill(8).upper(), end="  ")
        enter = False

    if len(temp) == 2:
        temp = []

    if space:
        print(chr(i).upper(), end=" ")
        temp.append(chr(i))
        space = False
        cnt += 0.5
    elif not space:
        print(chr(i).upper(), end="")
        temp.append(chr(i))
        space = True
        cnt += 0.5

    if cnt % 16 == 0:
        print("", end=" ")
        for c in arr:
            print(c, end="")
        print()
        arr = []
        offset += 16
        enter = True

    if cnt % 1 == 0:
        t = int("0x" + "".join(temp), 0)
        if 15 <= t <= 127:
            arr.append(chr(t))
        else:
            arr.append('.')
