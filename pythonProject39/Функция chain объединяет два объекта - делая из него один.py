from itertools import chain # вызываем  библиотеку
a = [1,2,3]
b = [6,5,4]
for x in chain(a, b):
    print(x)# и мы слепили 2 значения переменных.
    