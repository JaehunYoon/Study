message = input("please input message >> ")
temp = {}

for i in message:
    temp.setdefault(i, message.count(i))

print(temp)