def square(x):
    return x**2


numbers = [1,2,3,4,5]
square = map(square, numbers)

print(list(square))