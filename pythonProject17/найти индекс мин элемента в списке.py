a = [1, 2, 10, 13, -1, 2, -5, 10, -20, 4, 10, 10]

min(enumerate(a), key = lambda pair: pair[1])[0]
