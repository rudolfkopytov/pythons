M = 1000
K = 70
r = 6

count = 0
while M > 0:
    count += 1
    M += M * (r/100)
    M -= K

print(count)