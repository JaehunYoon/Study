a, b = map(int, input("please input two values >> ").split())

if a > b:
    print(a * b)
elif a <= b:
    print(b - a)

# print(a*b if a>b else b-a) -> 파이썬에서 삼항 연산자 사용하기
