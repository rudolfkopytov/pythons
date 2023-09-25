import sqlite3

database = sqlite3.connect("log_and_pass.db")
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT)""")

database.commit()

if input("Вход или регистрация? 1\2: ") =="1":
    login = input("Login:")

    cursor.execute(f"SELECT login FROM users WHERE login = '{login}")
    if not cursor.fetchall() is None:
        password = input("Password:")

    cursor.execute(f"SELECT login, password FROM users WHERE login = '{login}'")
    if cursor.fetchone()[1] == password:
        print( "Вы вошли в систему!")
    else:
        print(" Не верный пароль!")
else:
    inp_login = input("Login:")
    inp_password = input("Password:")

    cursor.execute(f"SELECT login FROM users WHERE login = '{inp_login}'")
    if cursor.fetchall() is None:
       cursor.execute ("INSERT INTO users VALUES (?,?)", (inp_login, inp_password))
       database.commit()
    else:
        print(" Такой пользователь уже есть!")