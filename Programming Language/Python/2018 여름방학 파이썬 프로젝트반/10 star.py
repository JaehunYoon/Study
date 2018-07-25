select = int(input("please input star type that you want >> "))

def star1():
    for i in range(5):
        print('{:<5}'.format('*' * (i+1)))

def star2():
    for i in range(5):
        print('{:>5}'.format('*' * (i+1)))

def star3():
    for i in range(5, 0, -1):
        print('{:<5}'.format('*' * i))

def star4():
    for i in range(5, 0, -1):
        print('{:>5}'.format('*' * i))

def star5():
    for i in range(1, 11, 2):
        print('{:^10}'.format('*' * i))
    
def star6():
    for i in range(1, 11, 2):
        print('{:^10}'.format('*' * i))
    for i in range(7, 0, -2):
        print('{:^10}'.format('*' * i))

if select == 1:
    star1()
elif select == 2:
    star2()
elif select == 3:
    star3()
elif select == 4:
    star4()
elif select == 5:
    star5()
elif select == 6:
    star6()