import binascii

file_directory = ""


def set_file(open_directory):
    global file_directory
    file_directory = open_directory


def show_mbr():
    global file_directory

    while True:
        inp = int(input("입력 : ")) * 512

        with open(f"bin/{file_directory}", "rb") as f:
            f.seek(inp)
            text = f.read(512)
            string = binascii.b2a_hex(text)

        # 상단 바
        print("offset(h)", end=" ")
        for i in range(16):
            print(f"{hex(i)[2:].zfill(2).upper()}", end=" ")
        print()
        print("=" * 75, end="")
        print()

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


def show_partition():
    print(end="\n\n")
    print("Partition 정보", end="\n\n")

    with open("bin/ex01.vhd", "rb") as f:
        t = 446
        size = 48

        f.seek(t)
        t += size
        text = f.read(size)
        string = binascii.b2a_hex(text)

        cnt = 0
        offset = 1
        temp = []
        arr = []
        space = False
        enter = True

        for i in string:
            if enter is True:
                print(f"Partition [{offset}]", end=" ")
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
                offset += 1
                enter = True
    lba = True

    while True:
        with open("bin/ex01.vhd", "rb") as f:
            f.seek(t)
            text = f.read(16)
            string = binascii.b2a_hex(text)

        temp = []
        lba_address = 0
        num = 0
        if lba is True:
            for i in string:
                if space:
                    print(chr(i).upper(), end=" ")
                    space = False
                    temp[num] += chr(i).upper()
                    num += 1
                elif not space:
                    print(chr(i).upper(), end="")
                    space = True
                    temp.append(chr(i).upper())
            temp.reverse()
            lba_address = int(("0x" + "".join(temp[4:8])), 0)
        exit()
