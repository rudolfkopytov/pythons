a = [1, -1, 2, 3, -4]

func = lambda x: x % 3 # это в порядке возростания по модулю 3
a.sort(key = func)
print(a)