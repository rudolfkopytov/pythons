def my_dec(func):
    def wrapper(func):
        print("Hello")
        return func()
    return wrapper(func)

@my_dec
def my_func():
    print("World")

my_func