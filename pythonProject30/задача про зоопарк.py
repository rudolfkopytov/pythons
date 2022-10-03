baby_price = 0.0
child_price= 14.0
adult_price= 23.0
senior_price = 18.0

baby_limit = 2
child_limit = 12
adult_limit = 64

total = 0 # -общая сумма всех посещений
line = input(" Введите возраст посетителя (пустая строка - для окончания ввода)")
# заводим цикл while (пока наша переменная line (!=) - ровна  пустой строке: " "
while line != " ":
# завожу новую переменную age с помощью функц int  преобразовываю из введённой строчной формы в число:
    age = int(line)
# и дальше я определяю условия:
    if age <= baby_limit:
        total = total + baby_price
    elif age <= child_limit:
        total = total + child_price
    elif age <= adult_limit:
        total = total + adult_price
    else:
        total = total + senior_price

    line = input(" Введите возраст посетителя (пустая строка - для окончания ввода)")
print(" Сумма цены билетов для посещения нашего зоопарка этой группой , составит $%.2f" % total)