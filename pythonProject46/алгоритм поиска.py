
A = [1,2,5,7,8,35,67,89,100]
K=int(input("Введите значение элемента"))
i = 0
if K < A[0] or K > A[len(A)-1]:
    print("Нет соответствия условию")
else:
    while A[i] < K and A [i+1] < K:
        i+=1
    print(i)

mid = len(A) // 2
low = 0
high = len(A) - 1
s=0
if K<A[0] or K > A[len(A)-1]:
    print("Нет соответствия условию")
else:
    while low <= high:
        if A[mid] == K and A[mid-1] < K:
            s=mid-1
            break
        elif A[mid] < K < A[mid + 1]:
            s = mid
            break
        elif K > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
print(s)