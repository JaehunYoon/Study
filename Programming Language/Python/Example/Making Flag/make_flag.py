import os

def makeFlag(plain):
    flag = "FLAG{" + plain.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace(" ", "_") + "}"
    return flag


def copy(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


while True:
    inp = input("Input plain text >> ")
    DSMCTF = makeFlag(inp)
    print(DSMCTF)
    copy(DSMCTF)
