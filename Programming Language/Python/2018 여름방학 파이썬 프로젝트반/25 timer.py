import datetime
from random import randrange as r
from time import sleep

while True:
    now = datetime.datetime.now()
    second = now.second
    if second % 2 == 0:
        print(f"{second} Second -> 짝수")
    else:
        print(f"{second} Second -> 홀수")
    sleep(r(1,4))