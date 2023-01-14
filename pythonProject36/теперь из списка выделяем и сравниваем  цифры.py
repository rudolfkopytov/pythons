my_list_1 = [1, 2, 3, 4 ,5, 6]
my_list_2 = [4, 5, 6, 7]

for number in my_list_1:
    if number in my_list_2:
        print('Такое число есть')
    else:
        print('Такое число не найдено')