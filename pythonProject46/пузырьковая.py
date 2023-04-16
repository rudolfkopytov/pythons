#Пузырьковая сортировка
from random import randint
A = [randint(1, 100) for i in range(20)]
A
i = 0
while i < len(A):
    for j in range(i+1, len(A)):
        if A[j-1]>A[j]:
            c = A[j-1]
            A[j-1] = A[j]
            A[j] = c
    i+=1
A
A = [x for x in range(1000000)]
K = int(input())
i = 0
if A[i] >= K or A[len(A)-1] < K:
    print("Нет элементов, соответствующих условию задачи")
else:
    while A[i+1]<K:
        i+=1
    print(i)


