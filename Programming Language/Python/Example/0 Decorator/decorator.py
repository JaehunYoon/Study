import datetime


def decorator_func(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated()


@decorator_func
def main_function_1():
    print("Main 1")


@decorator_func
def main_function_2():
    print("Main 2")


@decorator_func
def main_function_3():
    print("Main 3")
