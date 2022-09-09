def func(a, b):
    if a > b:
        c = a - b
        x = c*c
    else:
        x = a + b
    return x

res = func(44, 4)# - почему-то не работает с 2-ух значными цифрами.
print(res)

