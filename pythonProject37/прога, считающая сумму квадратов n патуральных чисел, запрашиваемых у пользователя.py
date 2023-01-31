n = int(input(' Введите число'))
sum_= 0
for num in range(1, n + 1):
    sum_+= num ** 2
    print( ' Сумма на шаге' , num , ':', sum_)

sum_