a = [
    (1, 2),
    (2, 3),
    (1, 1),
    (18, -3)
]

func = lambda x: x[0]*x[1]
m = min(a, key = func)
print(m)