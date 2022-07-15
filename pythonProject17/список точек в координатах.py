points = [
    (1, 3),
    (2, 10),
    (15, 1),
    (1, 1)
]

min(points, key = lambda pair: pair[0]**2 + pair[1]**2)# поиск  т очки с минимальным расстоянием от начала отчёта
print (points)