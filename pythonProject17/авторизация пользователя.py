passwords = {
    "user" : "12345",
    "root" : "10 101",
    "admin": "aaa"
}

nick = input("Введите ваше имя: ")
pwd = input("Введите ваш пароль: ")
if nick in passwords:
    if passwords[nick] == pwd:
        print("Вы вошли в систему!")
    else:
        print("Неверный пароль!")
else:
    print("Такого пользователя нет!")