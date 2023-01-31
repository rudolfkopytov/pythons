login_correct = 'admin'
pswd_correct = 'admin'
k = 3#это количество попыток.
for i in range(0, k):
    login = input( ' Ведите логин')
    pswd = input ( ' Введите пароль')
    if login != login_correct or pswd != pswd_correct:
        k -= 1
        print(f' Осталось {k} попытки')
    else:
        print( ' Дщбро пожаловать!')
        break
    if k == 0:
        print(' Вход заблокирван')