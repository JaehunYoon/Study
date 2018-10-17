import datetime

# class의 __call__ 함수로 정의해주는게 nested 함수 형식으로 정의한 것 보다 더 깔끔해 보인다.


class DatetimeDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())


class MainClass:
    @DatetimeDecorator
    def main_function_1():
        print("Main 1")

    @DatetimeDecorator
    def main_function_2():
        print("Main 2")

    @DatetimeDecorator
    def main_function_3():
        print("Main 3")

my = MainClass()
my.main_function_1()
my.main_function_2()
my.main_function_3()
