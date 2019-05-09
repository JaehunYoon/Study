with open("kernel32_dll.txt", "r") as f:
    temp = f.readlines()

func_input = input("func name > ").lower()

for i in temp:
    t = i.strip().split()
    if t[-1].lower() == func_input:
        if len(t) < 4:
            print(t[0], t[1])
        else:
            print(t[0], t[1], t[2])
        exit()

print("없네용")
