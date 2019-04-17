import binascii


def open_file(lba_addr):
    with open("bin/ex01.vhd", "rb") as f:
        f.seek(lba_addr * 512 + 446)
        text = f.read(32)
        string = list(binascii.b2a_hex(text).upper().decode())

    for i in range(1, len(string), 2):
        string[i-1] += string[i]
        string[i] = ''

    while '' in string:
        string.remove('')

    return string


def print_part(string, index, part_num):
    print(f"Partition [{part_num}]", end=" ")
    print(" ".join(string[index:index+16]), end=" ")
    print()


def show_partition():
    print("\nPartition 정보\n")

    string = open_file(0)

    part_num = 1
    index = 0
    lba_addr = 0
    loop = True

    for index in range(0, 32, 16):
        print_part(string, index, part_num)
        part_info(string, part_num)
        part_num += 1

    while loop is True:
        ext_index = 0
        if index == 16:
            with open("bin/ex01.vhd", "rb") as f:
                f.seek(lba_addr * 512 + 446 + 32)
                text = f.read(32)
                string = list(binascii.b2a_hex(text).upper().decode())

            for i in range(1, len(string), 2):
                string[i-1] += string[i]
                string[i] = ''

            while '' in string:
                string.remove('')
            index = 9999
        else:
            string = open_file(lba_addr)

        while string[ext_index+4] != '00':
            if string[ext_index+4] == '05':
                temp = string[ext_index+8:ext_index+12]
                temp.reverse()
                lba_addr = int("".join(temp), 16)
                if lba_addr != 1259648:
                    lba_addr += 1259648
                break
            elif string[ext_index+4] != '05' and string[ext_index+20] != '00':
                print_part(string, ext_index, part_num)
                part_num += 1
                part_info(string, part_num, lba_addr)
            else:
                print_part(string, ext_index, part_num)
                part_info(string, part_num, lba_addr)
                print()
                loop = False
            ext_index += 16


def part_info(part_arr, chk, lba_addr=None):
    temp = []
    if chk == 1:
        temp = part_arr[0:16]
        print_part_info(temp)
    elif chk == 2:
        temp = part_arr[16:32]
        print_part_info(temp)
    else:
        temp = part_arr[0:16]
        if chk == 4:
            print_part_info(temp)
        else:
            print_part_info(temp, lba_addr)


def print_part_info(part_arr, lba_addr=None):
    if part_arr[0] == '80':
        print("\nBoot Flag    0x80 (System Partition)")
    else:
        print("\nBoot Flag    0")
    temp = part_arr[1:4]
    temp.reverse()
    print(f"CHS Start    {''.join(temp)}")
    print(f"type         {part_arr[4]}")
    temp = part_arr[5:8]
    temp.reverse()
    print(f"CHS end      {''.join(temp)}")
    temp = part_arr[8:12]
    temp.reverse()
    if lba_addr is not None:
        print(f"LBA Start    {str(lba_addr + int(''.join(temp), 16))}")
    else:
        print(f"LBA Start    {str(int(''.join(temp), 16))}")
    print()
