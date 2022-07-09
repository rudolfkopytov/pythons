def my_decorator(fn):
   def wrapper():
       print(fn.__name__)
       return fn()
   return wrapper

@my_decorator
def myf():
    return 1
print(myf())