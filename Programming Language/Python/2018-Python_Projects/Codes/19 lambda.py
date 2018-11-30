'''
use lambda func
-10에서 10 사이의 정수에서 3의 배수를 출력하시오
'''

temp = list(filter(lambda x: x % 3 == 0 and x != 0, range(-10, 11)))

print(temp)