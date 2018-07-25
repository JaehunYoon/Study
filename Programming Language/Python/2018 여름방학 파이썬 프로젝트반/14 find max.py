# 리스트 입력 받아 최댓값 찾는 함수

values = list(map(int, input("please input values >> ").split()))

max = values[0]
check_max = lambda x: max < x

for value in values:
    if check_max(value):
        max = value

print(max)