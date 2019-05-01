import mbr_part
import binascii
from mbr_part import *


def print_fat():
    print("\nFAT32 정보")
    print()

    string = mbr_part.open_file(0)

    part_num = 1
    index = 0
    lba_addr = 0
    lba = 0
    loop = True

    for index in range(0, 32, 16):
        if string[index+4] == '0C':
            print(f"Partition [{part_num}]-------------------------")
            temp = string[index+8:index+12]
            temp.reverse()
            lba = int("".join(temp), 16)
            print(string[index+4], lba)
            fat_partition(lba)
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
            elif string[ext_index+4] != '05' and string[ext_index+20] != '00':
                # print_part(string, ext_index, part_num)
                part_num += 1
                # part_info(string, part_num, lba_addr)
                if string[ext_index+4] == '0C' or string[ext_index+20] == '0C':
                    print(f"Partition [{part_num}]-------------------------")
                    print()
                    print_part(string, ext_index, part_num)
                    temp = string[ext_index+8:ext_index+12]
                    # lba = lba_addr + int(''.join(string[0:16]), 16)
                    print(string[ext_index+4], lba)
                    fat_partition(lba)
            elif string[ext_index+4] == '05' or string[ext_index+20] == '00':
                # print_part(string, ext_index, part_num)
                # part_info(string, part_num, lba_addr)
                print()
                loop = False
            ext_index += 16


def temp():
    print()


def fat_partition(lba_addr):
    with open("bin/ex01.vhd", "rb") as f:
        f.seek(lba_addr * 512)
        text = f.read(90)
        string = list(binascii.b2a_hex(text).upper().decode())
    
    print(string)
    # if partition type == "0C":
    #     f.seek(lba_addr * 512)
    #     f.read(90)
