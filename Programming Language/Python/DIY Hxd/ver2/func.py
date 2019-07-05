from binascii import b2a_hex


class Func:
    file_directory = ""
    read_range = 0

    def __init__(self, new_dir):
        self.file_directory = new_dir

    def comb(self, string):
        for i in range(1, len(string), 2):
            string[i-1] += string[i]
            string[i] = ''

        while '' in string:
            string.remove('')

        return string

    def get(self, seek_point):
        with open(self.file_directory, "rb") as f:
            f.seek(seek_point)
            text = f.read(self.read_range)
            return self.comb(list(b2a_hex(text).upper().decode()))


class ShowMbrSector(Func):
    def __init__(self, new_dir):
        super(ShowMbrSector, self).__init__(new_dir)
        self.read_range = 512

    def show(self):
        while True:
            start_point = int(input("입력 : "))

            if start_point == -1:
                return
            start_point *= 512
            string = self.get(start_point)

            # nav bar
            print("offset(h)", end=" ")
            for i in range(16):
                print(hex(i)[2:].zfill(2).upper(), end=" ")
            print()
            print("=" * 75, end='')
            print()

            for index in range(0, 512, 16):
                print(hex(index)[2:].zfill(8).upper(), end="  ")
                print(" ".join(string[index:index+16]), end=" ")
                for c in range(16):
                    t = int(string[index + c], 16)
                    print(chr(t) if 32 <= t <= 127 else '.', end="")
                print()


class ShowPartition(Func):
    part_num = 0
    index = 0
    lba_addr = 0
    extend = False

    def __init__(self, new_dir):
        super(ShowPartition, self).__init__(new_dir)
        self.read_range = 16

    def show(self):
        print("\nPartition 정보\n")

        while True:
            if not self.extend:
                string = self.get(446 + self.index)
                if string[4] == "05":
                    self.extend = True
                    temp = string[8:12]
                    temp.reverse()
                    self.lba_addr = int("".join(temp), 16)
                    self.read_range = 32
                    continue
                elif string[4] == "00":
                    return
            else:
                string = self.get(self.lba_addr * 512 + 446)

                ext_arr = string[16:]
                string = string[:16]
                if ext_arr[4] == "05":
                    temp = ext_arr[8:12]
                    temp.reverse()
                    lba = int("".join(temp), 16)
                    if lba != 1259648:
                        lba += 1259648
                else:
                    self.part_num += 1
                    self.print_part(string)
                    self.detail(string, self.lba_addr)
                    return

            self.part_num += 1
            self.index += 16
            self.print_part(string)
            if not self.extend:
                self.detail(string)
            else:
                self.detail(string, self.lba_addr)
                self.lba_addr = lba

    def print_part(self, part_arr):
        print(f"Partition [{self.part_num}]", end=" ")
        print(" ".join(part_arr), end=" ")
        print()

    def detail(self, part_arr, lba_addr=None):
        if part_arr[0] == "80":
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
            print(f"LBA Start    {lba_addr + int(''.join(temp), 16)}")
        else:
            print(f"LBA Start    {int(''.join(temp), 16)}")
        temp = part_arr[12:16]
        temp.reverse()
        print(f"size         {int(''.join(temp), 16) * 512 // 1024 // 1024} Mbyte")
        print()


class ShowFat32Info(Func):
    part_num = 0
    index = 0
    lba_addr = 0
    extend = False

    def __init__(self, new_dir):
        super(ShowFat32Info, self).__init__(new_dir)
        self.read_range = 16

    def show(self):
        print("\nFAT32 정보\n")

        while True:
            if not self.extend:
                string = self.get(446 + self.index)
                if string[4] == "05":
                    self.extend = True
                    temp = string[8:12]
                    temp.reverse()
                    self.lba_addr = int("".join(temp), 16)
                    self.read_range = 32
                    continue
                elif string[4] == "00":
                    return
            else:
                string = self.get(self.lba_addr * 512 + 446)
                ext_arr = string[16:]
                string = string[:16]
                if ext_arr[4] == "05":
                    temp = ext_arr[8:12]
                    temp.reverse()
                    lba = int("".join(temp), 16)
                    if lba != 1259648:
                        lba += 1259648
                elif ext_arr[4] == "0C":
                    temp = string[8:12]
                    temp.reverse()
                    self.part_num += 1
                    self.detail(self.lba_addr + int(''.join(temp), 16))
                    return
                else:
                    return

            self.part_num += 1
            self.index += 16
            if string[4] == "0C":
                temp = string[8:12]
                temp.reverse()
                self.detail(self.lba_addr + int(''.join(temp), 16))
            if self.extend:
                self.lba_addr = lba

    def detail(self, lba):
        self.read_range = 90
        print(f"Partition [{self.part_num}]-------------------------\n")
        string = self.get(lba * 512)

        reserved_sector_count = int("".join(string[15:13:-1]), 16)
        fat_size_32 = int("".join(string[39:35:-1]), 16)

        print("Bytes Per Sector              " + str(int("".join(string[12:10:-1]), 16)))
        print("Sectors Per Cluster           " + str(int("".join(string[13]), 16)))
        print("Reserved Sector Count         " + str(reserved_sector_count))
        print("Total Sector FAT32            " + str(int("".join(string[35:31:-1]), 16)))
        print("FAT Size 32                   " + str(fat_size_32))

        print("VBR start               " + str(lba))
        print("FAT#1 start             " + str(lba + reserved_sector_count))
        print("FAT#2 start             " + str(lba + reserved_sector_count + fat_size_32))
        print("Root Directory start    " + str(lba + reserved_sector_count + fat_size_32 * 2))
        print()

        # 11-12 : Bytes per sector
        # 13-13 : Sectors per cluster
        # 14-15 : Reserved sector count
        # 32-35 : Total sector FAT32
        # 36-39 : FAT size 32

        # VBR Start : lba_addr
        # FAT#1 Start : lba_addr + Reserved Sector Count
        # FAT#2 Start : FAT#1 Start + FAT size 32
        # Root Directory Start : FAT#2 Start + FAT size 32


class ShowFilesInfo(Func):
    part_num = 0
    index = 0
    lba_addr = 0
    extend = False

    def __init__(self, new_dir):
        super(ShowFilesInfo, self).__init__(new_dir)
        self.read_range = 16

    def show(self):
        while True:
            if not self.extend:
                string = self.get(446 + self.index)
                if string[4] == "05":
                    self.extend = True
                    temp = string[8:12]
                    temp.reverse()
                    self.lba_addr = int("".join(temp), 16)
                    self.read_range = 32
                    continue
                elif string[4] == "00":
                    return
            else:
                string = self.get(self.lba_addr * 512 + 446)
                ext_arr = string[16:]
                string = string[:16]
                if ext_arr[4] == "05":
                    temp = ext_arr[8:12]
                    temp.reverse()
                    lba = int("".join(temp), 16)
                    if lba != 1259648:
                        lba += 1259648
                elif ext_arr[4] == "0C":
                    temp = string[8:12]
                    temp.reverse()
                    self.part_num += 1
                    self.detail(self.lba_addr + int(''.join(temp), 16))
                    return
                else:
                    return

            self.part_num += 1
            self.index += 16
            if string[4] == "0C":
                temp = string[8:12]
                temp.reverse()
                self.detail(self.lba_addr + int(''.join(temp), 16))
            if self.extend:
                self.lba_addr = lba

    def detail(self, lba):
        self.read_range = 90
        string = self.get(lba * 512)
        reserved_sector_count = int("".join(string[15:13:-1]), 16)
        fat_size_32 = int("".join(string[39:35:-1]), 16)

        root_directory_start = lba + reserved_sector_count + fat_size_32 * 2

        self.root_dir(root_directory_start)

    def root_dir(self, sector):
        self.read_range = 512
        print()
        print(f"파일 정보(Root Dir 섹터번호:{sector})")
        print()
        string = self.get(sector * 512)
        t = 0
        for i in range(16):
            temp = string[i*32:i*32+32]
            attr = temp[11]
            if attr == "01":
                print("Read Only")
            elif attr == "02":
                print("Hidden File")
            elif attr == "04":
                print("System File")
            elif attr == "08":
                print("Volume Label")
                print(f"      Volume name : {self.get_name(temp[:11])}")
                print(f"      Last Written Date : {self.get_date(temp[25:23:-1])}")
                print(f"      Lst Written Time : {self.get_time(temp[23:21:-1])}")
            elif int("0x20", 16) > int(''.join(attr), 16) >= int("0x10", 16):
                print("Directory")
                print(f"      name : {self.get_name(temp[:8]) + '.' + self.get_name(temp[8:11])}")
                print(f"      Create Date : {self.get_date(temp[17:15:-1])}")
                print(f"      Create Time : {self.get_time(temp[15:13:-1])}")
                print(f"      Last Written Date : {self.get_date(temp[25:23:-1])}")
                print(f"      Last Written Time : {self.get_time(temp[23:21:-1])}")
                print(f"      Last Accessed Date : {self.get_date(temp[19:17:-1])}")
                print(f"      Size : {self.get_size(temp[:27:-1])}")
            elif int("0x30", 16) > int(''.join(attr), 16) >= int("0x20", 16):
                if temp[0] == "E5":
                    print("Deleted Archive")
                    try:
                        print(f"      name : {self.get_name(temp[:8]) + '.' + self.get_name(temp[8:11])}")
                    except:
                        print(f"      name : {self.get_name(temp[1:8]) + '.' + self.get_name(temp[8:11])}")
                else:
                    print("Archive")
                    print(f"      name : {self.get_name(temp[:8]) + '.' + self.get_name(temp[8:11])}")
                print(f"      Create Date : {self.get_date(temp[17:15:-1])}")
                print(f"      Create Time : {self.get_time(temp[15:13:-1])}")
                print(f"      Last Written Date : {self.get_date(temp[25:23:-1])}")
                print(f"      Last Written Time : {self.get_time(temp[23:21:-1])}")
                print(f"      Last Accessed Date : {self.get_date(temp[19:17:-1])}")
                print(f"      Size : {self.get_size(temp[:27:-1])}")

            elif attr == "0F":
                if temp[0] == "E5":
                    print("Deleted ", end="")
                print("Long File Name")

        print()
        self.read_range = 16

    def get_name(self, data):
        result = bytearray(b'')
        for i in range(len(data)):
            result.append(int(''.join(data[i]), 16))
        return result.decode("cp949")

    def get_date(self, data):
        result = ""
        binary = bin(int(''.join(data), 16))[2:].zfill(16)
        result += str(1980 + int(binary[:7], 2)) + "년 "
        result += str(int(binary[7:11], 2)) + "월 "
        result += str(int(binary[11:], 2)) + "일"
        return result

    def get_time(self, data):
        result = ""
        binary = bin(int(''.join(data), 16))[2:].zfill(16)
        result += str(int(binary[:5], 2)).zfill(2) + "시 "
        result += str(int(binary[5:11], 2)).zfill(2) + "분 "
        result += str(int(binary[11:], 2) * 2).zfill(2) + "초"
        return result

    def get_size(self, data):
        return str(int(''.join(data), 16))
