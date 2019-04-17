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
