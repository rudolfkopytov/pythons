n = int(input('Введите число '))
sum_ = 1
for num in range(1, n + 1):
    sum_ *= num
    print(f'Сумма на шаге {num}: {sum_}')
print(sum_) 