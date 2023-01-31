import random
number = random.randint(0,100)
print(number)
max_tries = 3# число попыток пользователя.
tries = 0

while tries < max_tries:
    guess = int (input(' Назови свой вариант'))
    if guess < number:
        print ( ' Загадай число больше' )
    elif guess > number:
        print ( ' Загадай число меньше')
    else:
        print( " Ты угадал!")
        break

    tries +=1

if tries >= max_tries :
    print(' Вы проиграли')