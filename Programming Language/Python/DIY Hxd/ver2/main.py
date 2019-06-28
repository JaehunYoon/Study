from func import *


FILE_OPEN = False
location = ""


def open_file():
    global FILE_OPEN, location
    location = input("파일 경로 입력 > ")
    # 파일 경로 지정하는 함수에 location 파라미터 값으로 넣기
    FILE_OPEN = True
    return location

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
        location = open_file()
    elif select == 2:
        if not FILE_OPEN:  # 파일 경로가 지정되지 않은 상태일 경우 파일 열기를 선행으로 수행
            ShowMbrSector(open_file()).show()
        # 섹터 정보를 조회하는 함수
        else:
            ShowMbrSector(location).show()
    elif select == 3:
        if not FILE_OPEN:
            ShowPartition(open_file()).show()
        # 파티션 정보를 조회하는 함수
        else:
            ShowPartition(location).show()
    elif select == 4:
        # FAT32 정보를 조회하는 함수
        if not FILE_OPEN:
            ShowFat32Info(open_file()).show()
        else:
            ShowFat32Info(location).show()
    elif select == 5:
        # 루트 디렉토리의 파일 정보를 조회하는 함수
        print("5")
    elif select == 0:
        exit()
