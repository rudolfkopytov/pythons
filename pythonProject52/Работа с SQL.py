import psycopg2
DBNAME = "skilfactory"
USER = 'skilfactory'
HOST = '84.201.134.129'
PASSWORD = 'cCkxxLVrDE8EbvjueeMedPKt'#gfhjkm? конечно не действеннен, нужно брать, запрашивать пароль для подключения в SQL
PORT = 5432

connection = psycopg2.connect(
    dbname=DBNAME,
    user=USER,
    host=HOST,
    password=PASSWORD,
    port=PORT)

n = 10
query = f'''select*from sql.pokemon limit {n}'''
# Выполнение запроса и чтение результатов:
# 1 варик:
# Курсор - это специальный механизм, позволяющий работать со строками в базе данных по очереди , одна за другой:
cursor = connection.cursor()
# Выполняем запрос:
сursor.execute(query)
# а теперь извлекаем результаты:
# сделать это можно с помощью специальных методов:
# 1:
print('1.')
# и если поставить правильный пароль,и всё что там дано в блоке - то всё получится
# И извлекаем строки по одной
# При первом вызове fetchone() вернёт none
record = cursor.fetchone()
print(record)
# 2 - ой  метод
print('2.')
# метод fetchall() применяется, что бы вернуть все строки, содержащиеся в курсоре
# Сейчас он возврашает 2 строки, так как одну мы уже вытащили с помощью fetchone:
rows = cursor.fetchall()
# rows - это список из кортежей:
print(type(rows), type(rows[0]))
print(*rows, sep="\n")
# и закрываем курсор:
cursor.close()

cursor = connection.cursor()
cursor.execute(query)
lst = cursor.fetchall()
cursor.close()
lst
# и он в первом методе должен выдавать пронумерованный список.
# Второй метод:через pandas сразу в датафрейм.
import pandas as pd
df = pd.read sql query(query, connection)
df
# и не забываем закрыть соединение:
connection.close()




