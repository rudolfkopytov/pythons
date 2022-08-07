fio = input( " Введите  ФИО:")
f, i, o = fio.split()

answer = f"{f.capitalize()} {i[0].upper()}.{o[0].upper()}."
print(answer)