from random import shuffle

temp1 = [str(i) for i in range(1, 11)]
temp2 = [str(i) for i in range(11, 21)]
temp3 = [str(i) for i in range(11, 21)]
temp4 = [str(i) for i in range(21, 31)]
temp5 = ['★']

random = temp1 + temp2 + temp3 + temp4 + temp5

# print(len(random))
num = 1
while True:
    key = input("[뽑기를 하려면 엔터 키를 눌러주세요]")
    shuffle(random)
    random_pop = random.pop()
    
    print(f"{num}번째 뽑기 결과는 [{random_pop}]!!")
    num += 1
    if num > 20:
        print("끝!!")
        exit()