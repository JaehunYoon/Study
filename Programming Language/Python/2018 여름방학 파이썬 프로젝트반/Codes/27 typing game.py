'''
* 타자게임

- 총 7문제 진행
- 랜덤으로 주어지는 단어에 맞게 타자 입력
- 올바르게 입력 시 다음 문제 진행(문제 삭제)
- 오타 시 다시 랜덤 출력
- 타자게임 진행한 시간 마지막에 출력
'''
from time import time
from random import choice

word_list = ['teacher', 'handsome', 'really', 'nice', 'pretty', 'computer', 'meister']
result = True
i = 1
start = time()

while word_list != []:
    temp = choice(word_list)
    
    print(f"[문제 {i}]")
    print(temp)
    answer = input(">> ")
    
    if answer == temp:
        print("Good~")
        i += 1
        result = True
        word_list.remove(temp)
    else:
        print("다시!!")
    print()
end = time()
print("Clear!!!")
print("[Clear Time] : {:.2f} Second".format(end - start))