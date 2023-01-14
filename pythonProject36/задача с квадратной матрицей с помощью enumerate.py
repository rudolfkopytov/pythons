data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35]
]
sum_ = 0

for i, el in enumerate(data):
    sum_ += el[i]

print(sum_)