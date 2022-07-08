s = "Hello!"
print(s[0])
print(s[4])
print(s[1:4])
print(len(s))
print(s.find('e'))
print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
print(s.find('l')) # встречается в индексах 2 и 3
print(s.isdigit()) # строка состоит из цифр?
print(s.isalpha()) # строка состоит из букв
print(s.isalnum()) # строка состоит из цифр и букв?
print(s.upper())
print(s.lower())