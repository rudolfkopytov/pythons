text = ""
inp_str = input("Введите текст: ")
while inp_str:
    text += inp_str
    inp_str = input()

un = set(text)
print(len(un))#нет никакой возможности скопировать в терминал текст