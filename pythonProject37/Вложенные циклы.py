# изучаем синтаксис и пытаемся понять логику работы цикла
for number in range (1,6):
    print (f' Это внешний цикл, number = {number}')
    for i in range(3):
        print('\t ха - ха - ха!')
    print()