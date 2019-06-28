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
    ext_index = 0
    lba_addr = 0
    extend = False
    string = []

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
            else:
                string = self.get(self.lba_addr * 512 + 446)
                ext_arr = string[16:32]
                ext_arr.reverse()
                if self.lba_addr != 1259648:
                    self.lba_addr += 1259648
                string = string[0:16]
                if string[4] == "00":
                    return

            self.part_num += 1
            self.index += 16
            self.print_part(string)
            if not self.extend:
                self.detail(string)
            else:
                self.detail(string, self.lba_addr)
                return

    def print_part(self, part_arr, ext=False):
        if ext:
            i = self.ext_index
        else:
            i = self.index
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
