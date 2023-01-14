login_correct = 'admin'
pswd_correct = 'admin'
k = 3
for i in range(0, k):
    login = input('Ввелите логин')
    pswd = input('Введите пароль')
    if login != login_correct or pswd != pswd_correct:
        k -= 1
        print(f'Осталось {k} попытки')
    else:
        print('Добро пожаловать!')
        break
if k == 0:
    print('Вход заблокирован')