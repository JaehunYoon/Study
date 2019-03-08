import binascii

with open("MBR", "rb") as f:
    text = f.read()
    string = binascii.b2a_hex(text)

cnt = 0
space = False

for i in string:
    if space:
        print(chr(i).upper(), end=" ")
        space = False
        cnt += 0.5
    elif not space:
        print(chr(i).upper(), end="")
        space = True
        cnt += 0.5

    if cnt % 16 == 0:
        print()
