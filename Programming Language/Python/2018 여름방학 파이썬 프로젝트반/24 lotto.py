from random import randrange as r

how_much = int(input("복권 얼마어치 사실거에요? >> "))

# temp = [[r(1, 45 + 1) for _ in range(6)] for _ in range(int(how_much / 1000))]

lotto = [[0 for _ in range(6)] for _ in range(int(how_much / 1000))]

for i in range(int(how_much / 1000)):
    for j in range(6):
        while True:
            temp = r(1, 46)
            if temp in lotto[i]:
                continue
            else:
                break
        lotto[i][j] = temp
    lotto[i].sort()

for i in range(len(lotto)):
    print(lotto[i])
