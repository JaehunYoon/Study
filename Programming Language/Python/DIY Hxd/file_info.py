from mbr_part import open_file

import binascii


root_dir_start = 0


def file_info():

    string = open_file(0)

    part_num = 1
    index = 0
    lba_addr = 0
    lba = 0
    loop = True

    for index in range(0, 32, 16):
        if string[index+4] == '0C':
            temp = string[index+8:index+12]
            temp.reverse()
            lba = int("".join(temp), 16)
            get_root_dir_start(lba)
            print(f"파일 정보(Root Dir 섹터번호: {root_dir_start}\n")
            print(f"Partition [{part_num}]-------------------------\n")
            print()
            index += 16
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
            elif string[ext_index+4] == '05' or string[ext_index+20] == '00':
                loop = False
            else:
                if string[ext_index+4] == '0C' or string[ext_index+20] == '0C':
                    temp = string[ext_index+8:ext_index+12]
                    temp.reverse()
                    lba = lba_addr + int(''.join(temp), 16)
                    get_root_dir_start(lba)
                    print(f"파일 정보(Root Dir 섹터번호: {root_dir_start}\n")
                    print(f"Partition [{part_num}]-------------------------\n")
                    print()
                part_num += 1
            ext_index += 16


def get_root_dir_start(lba_addr):
    global root_dir_start
    with open("bin/ex01.vhd", "rb") as f:
        f.seek(lba_addr * 512)
        text = f.read(90)
        string = list(binascii.b2a_hex(text).upper().decode())

    for i in range(1, len(string), 2):
        string[i-1] += string[i]
        string[i] = ''

    while '' in string:
        string.remove('')

    reserved_sector_count = int("".join(string[15:13:-1]), 16)
    fat_size_32 = int("".join(string[39:35:-1]), 16)
    root_dir_start = lba_addr + reserved_sector_count + fat_size_32 * 2
