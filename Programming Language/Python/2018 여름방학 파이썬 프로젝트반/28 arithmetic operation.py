'''
- 5문제의 사칙연산 문제 맞추기
- 오답이 0개 일때
'천재입니다!' 문자 출력
- 문제를 맞추면 정답!
틀리면 오답! 출력
'''

from random import *

operating_symbol = ['+', '-', '*', '/']
incorrect_count = 0

for i in range(1, 6):
    a = randrange(1, 10)
    b = randrange(1, 10)
    o = choice(operating_symbol)
    print(f"[문제 {i}]")
    if o == '/':
        print("나눗셈은 몫만 입력해주세요")
    print(a, o, b)
    result = int(input(">> "))

    if o == '/':
        if result == eval(f'{a}//{b}'):
            print("정답!")
        else:
            print("오답!")
            incorrect_count += 1
    else:
        if result == eval(f'{a}{o}{b}'):
            print("정답!")
        else:
            print("오답!")
            incorrect_count += 1

if incorrect_count == 0:
    print("천재입니다!")