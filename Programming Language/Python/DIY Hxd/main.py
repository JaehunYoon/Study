import binascii

import mbr
import mbr_part
import fat32
import file_info


FILE_OPEN = False


def open_file():
    global FILE_OPEN
    location = input("파일 경로 입력 > ")
    mbr.set_file(location)
    FILE_OPEN = True

while True:
    print("1. 파일 열기")
    print("2. 섹터 정보")
    print("3. 파티션 정보")
    print("4. FAT32 정보")
    print("5. 파일 정보")
    print("0. 종료")
    print()
    select = int(input("메뉴 선택 : "))

    if select == 1:
        open_file()
    elif select == 2:
        if not FILE_OPEN:
            open_file()
        mbr.show_mbr()
    elif select == 3:
        mbr_part.show_partition()
    elif select == 4:
        fat32.print_fat()
    elif select == 5:
        file_info.file_info()
    elif select == 0:
        exit()
