'''
input interval (int)
input sentence (str)

Python is a programming language that lets you work quickly

'''

interval = int(input("please input interval value (only integer) >> "))
sentence = list(input("please input sentence >> "))
num = 0

if len(sentence) < interval:
    print("Wrong")

for i in range(len(sentence) - interval):
    for j in range(0, interval):
        print(sentence[i+j], end='')
    print()