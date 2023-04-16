Y = input().split()
Y = list(map(int, Y))
for i in range(1, len(Y)):
    b = Y[i]
    j = i-1
    while (j >= 0) and (b < Y[j]):
        Y[j+1] = Y[j]
        j-=1
    Y[j+1] = b
print(Y)# - это программы выполняет поиск от самого маленького к самому большому (сортировка)
