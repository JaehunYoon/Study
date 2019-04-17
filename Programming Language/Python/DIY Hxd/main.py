import binascii

import mbr
import mbr_part

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
    elif select == 0:
        exit()
