operList = ['+','-', '*', '/' ]# это сипсок функций

def mozhno():
    print (' \n Доступны функции:')
    for i in operList:
        print (i, end =" ")


def chis(a):
    try:
        chislo = int(a)
    except ValueError as e:
        try:
            chislo = float(a)
        except ValueError as e:
            print ('\n Введён не верный символ вместо числа ')
            chislo = None
    return chislo

def dlina(b):
    if len (str(b))> 12:
        print('\n Калькулятор простой, а Вы ввели слишком длинное число!')
        chislo = None
    else:
        chislo = b

    return chislo
print( ' очень простой калькулятор')

mozhno()
vyvod = True

while vyvod:
    x = None
    y = None
    while x is None:
        x = chis(input('\n Введите первое число' ))
        x = dlina(x)

    oper = input('\n Введите оператор: ')
    while oper not in operList:
        print( '\n  Не верный оператор!')
        mozhno()
        oper = input('\n Введите оператор:')

    while y is None:
        y = chis(input('\n Введите второе число:'))
        y = dlina(y)

    while oper == '/' and not y:
        y == None
        print('\n На ноль делить нельзя!')
        while y is None:
            y = chis(input('\n Введите второе исло:'))
            y = dlina(y)

    if oper == '/':
        otvet = x / y
    elif oper == '*':
        otvet = x*y
    elif oper=='-':
        otvet = x-y
    elif oper == '+':
        otvet = x+y

    if x < 0:
        x = (' ( ' + str(x) + ' )')
    if y < 0:
        y = (' ( ' + str(y) + ')')

    print('\n   Результат вычислений:' , x , oper, y , '*', round(otvet, 12))
    vyvod = not ( ' + ' == (input(' \n Введите "+" для выхода или прдожите вычисления:')))