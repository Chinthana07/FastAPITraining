#concept : decorator is a python that lets you modify a function using @ symbol
def my_decorator(func):
    def Wrapper():
        print("Before")
        func()
        print("After")
    return Wrapper   

@my_decorator
def say_hello():
    print("Hello !")
say_hello()
