# 메시지에서 모음의 개수만 카운트

message = input("please input message >> ")
temp = {}

for i in sorted(message):
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        continue
    temp.setdefault(i, message.count(i))

print(temp)