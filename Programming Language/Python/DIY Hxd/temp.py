import binascii

with open("bin/ex01.vhd", "rb") as f:
    f.seek(1468672 * 512 + 446)
    text = f.read(32)
    string = list(binascii.b2a_hex(text).upper().decode())

for i in range(1, len(string), 2):
    string[i-1] += string[i]
    string[i] = ''

while '' in string:
    string.remove('')

part_num = 1
index = 0
lba_addr = 0

for index in range(0, 32, 16):
    print(f"Partition [{part_num}]", end=" ")
    part_num += 1
    print(" ".join(string[index:index+16]), end=" ")
    print()

while True:
    ext_index = 0
    with open("bin/ex01.vhd", "rb") as f:
        if index == 16:
            f.seek(0 * 512 + 446 + 32)
        else:
            f.seek(lba_addr * 512 + 446)
        text = f.read(32)
        string = list(binascii.b2a_hex(text).upper().decode())

    for i in range(1, len(string), 2):
        string[i-1] += string[i]
        string[i] = ''

    while '' in string:
        string.remove('')
    
    while string[ext_index+4] != '00':
        if string[ext_index+4] == '05':
            temp = string[ext_index+8:ext_index+12]
            temp.reverse()
            lba_addr = int("".join(temp), 16)
            print(lba_addr)
            exit
        print(f"Partition [{part_num}]", end=" ")
        print(" ".join(string[ext_index:ext_index+16]), end=" ")
        print()

        part_num += 1
        ext_index += 16
        if ext_index == 32:
            exit()

    print(string[ext_index: ext_index+16])
    exit()