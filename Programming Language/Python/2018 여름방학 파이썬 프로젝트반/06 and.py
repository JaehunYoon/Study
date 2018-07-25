'''
* 논리연산 AND 표현하기

0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
'''

for i in range(0, 2):
    for j in range(0, 2):
        print(f"{i} {j} |", end=' ')
        print("1" if i == 1 and j == 1 else "0")
