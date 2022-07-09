# задача : напишите декоратор, который печатает имя функции при её вызове
def my_decorator(fn):
    def wrapper():
        print(fn._name_)
        return  fn()
    return wrapper

# my_decorator
def my():
    return  1

myf2=my_decorator(myf2)
print(myf2())