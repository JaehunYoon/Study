import binascii

file_directory = ""


def set_file(open_directory):
    global file_directory
    file_directory = open_directory


def nav_bar():
    print("offset(h)", end=" ")
    for i in range(16):
        print(f"{hex(i)[2:].zfill(2).upper()}", end=" ")
    print()
    print("=" * 75, end='')
    print()


def show_mbr():
    global file_directory

    while True:
        inp = int(input("입력 : "))

        if inp == -1:
            return

        with open(f"bin/{file_directory}", "rb") as f:
            inp *= 512
            f.seek(inp)
            text = f.read(512)
            string = list(binascii.b2a_hex(text).upper().decode())

        for i in range(1, len(string), 2):
            string[i-1] += string[i]
            string[i] = ''
        
        while '' in string:
            string.remove('')

        nav_bar()

        for index in range(0, 512, 16):
            print(hex(index)[2:].zfill(8).upper(), end="  ")
            print(" ".join(string[index:index+16]), end=" ")
            for c in range(16):
                t = int(string[index + c], 16)
                print(chr(t) if 32 <= t <= 127 else '.', end="")
            print()


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
    lba_address = t
    while True:
        with open("bin/ex01.vhd", "rb") as f:
            f.seek(lba_address)
            print(f"lba는 {lba_address}")
            text = f.read(16)
            string = binascii.b2a_hex(text)

        temp = []
        lba_address = 0
        num = 0
        if lba is True:
            for i in string:
                if space:
                    space = False
                    temp[num] += chr(i).upper()
                    num += 1
                elif not space:
                    space = True
                    temp.append(chr(i).upper())
            temp.reverse()
            lba_address = int(("0x" + "".join(temp[4:8])), 0)
            lba = False
        elif not lba:
            print(string)
            print("lba 아님")
            exit()
        # 확장 파티션을 나타내는 코드를 작성해야함
