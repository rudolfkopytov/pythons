import password as password

nick = input(" Введите ваше имя:")
pwd = input("Введите ваш пароль:")
if nick in password:
    if password[nick] == pwd:
        print("Вы вошли в систему")
    print("Неверный пароль")
else:
    pprint("Hет такого пользователя")