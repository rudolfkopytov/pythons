num = int(input(" Введите целое число"))# заводим переменную "num" int - сообщает нам о том что пользователь должен ввести целое число, в ином случае перед imput ставим float ( дробное число) и input - само предложение ввода.
# #далее идёт условие: if nun % 2 == 0 - перевод: если введённое число делиться на 2 без остатка (== 0)с тавим двоеточие(:), а не чётного числа 1

if num % 2 == 0:
    print(" Чётное число")
else: # ИНАЧЕ!!!
    print(" Не чётное число")
