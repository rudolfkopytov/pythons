# работает и с числами и со списками!!!!!


def map_decorator(func):
    def wrapper(arg):
        if isinstance(arg, int):
            return func(arg)
        else:
            return list(map(func, sp))

    return wrapper


@map_decorator
def f(a):
    return a ** 5 + 4 * a ** 2 + 10 * a - 3


@map_decorator
def g(a):
    return a ** 2.71 - 10 + 155 ** (a ** 0.5)


sp = [1, 20, 1, 4, 7, 3]
print(g(sp))
print(g(123))