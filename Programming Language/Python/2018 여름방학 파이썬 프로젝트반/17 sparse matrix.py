n = int(input("please input values >> "))

temp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp[i][i] = 1

for i in range(n):
    print(temp[i])