# -а это как пример от куда идёт сличение

nick=input("Введите ваше имя:")# эта шняга подходит без "базы данных на сайте"
pwd=input("Введите ваш пароль:")
if nick in passwords:
    if passwords[nick]==pwd:
        print("Вы вошли в систему")
    else:
        print(" Не верный пароль")
else:
    print("Такого пользователя нет!")