# ссылка на условие - http://joxi.ru/bmoLRPOHoydqj2
n = int(input()) # запрашиваем у пользователя число
counter = 0# - счётчик попыток.
while n !=1:# пока число не равно 0
    counter += 1 # прибавляем по одному
    if counter == 1000: # количество попыток
        break
    if n % 2 ==0:
        n = n / 2
    else:
        n = (n * 3 + 1) / 2
print (n, counter)
