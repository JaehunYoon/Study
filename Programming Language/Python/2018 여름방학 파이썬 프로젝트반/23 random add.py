import random

while True:
    a = random.randrange(1,100)
    b = random.randrange(1,100)

    answer = int(input(f"{a} + {b} = "))

    if answer == a+b:
        print("정답입니다. 추카포카")
        break
    else:
        print("땡! 다시 입력하세요")
