A = [1,1,1,3,4,4,5,5,6,7]
first_min = min(A)
A = list(filter(lambda elem: elem  != first_min, A))
A = [elem for elem in A if elem != first_min]# сколько бы не повторялись наши цифры мы их отфильтровываем

second_min = min(A)
A.remove(second_min)

third_min = min(A)

print(second_min, third_min)
