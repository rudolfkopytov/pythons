import random

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:

    user = input('Ваш вариант')
    computer = random.choice(['r', 's', 'p'])

    print('Компьютер выбрал:', computer)

    if user == computer:
        print('Ничья')

    elif user == 'r':
        if computer == 's':
            print('Игрок победил! Камень ломает ножницы!')
            player_wins += 1
        else:
            print('Компьютер победил! Бумага закрывает камень!')
            computer_wins += 1

    elif user == 'p':
        if computer == 'r':
            print('Компьютер победил! Бумага закрывает камень!')
            computer_wins += 1
        else:
            print('Игрок победил! Ножницы режут бумагу!')
            player_wins += 1

    elif user == 's':
        if computer == 'p':
            print('Игрок победил! Ножницы режут бумагу!')
            player_wins += 1
        else:
            print('Компьютер победил! Камень ломает ножницы!')
            computer_wins += 1

    print('Счет: ', player_wins, ':', computer_wins)

if player_wins > computer_wins:
    print('По итогам трех раундов победил игрок')
else:
    print('По итогам трех раундов победил компьютер')