from summoner import Summoner

print("OP.GG")
print("1. 전적 검색")
print("2. 나가기")

select = int(input(">> "))

if select == 1:
    Summoner()
else:
    print("Bye~~")
    exit()