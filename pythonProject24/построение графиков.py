import json

def save_data(data):
    with open("data.json", "w") as f:# открытие файла
        json.dump(data,f, indent = 2) # сохранение в файл инфы


def load_data():
    with open("data.json") as f: # открытие файла
        data = json.load(f) # считывание из него.


    return data

#save_data(d) - это сохранение нашего файла
#print(load_data()) # - а это считывание их файла.

def show_percent(name, percent, width = 50):
    fill = chr(9608)
    empty = "-"
    bars = round(percent * width)

    progress = fill * bars + empty * (width - bars)
    print(f"{name:7} - {round(percent * 100)}% |{progress}|")
#show_percent("RUB", 0.6)
#show_percent("BITCOIN", 0.6 )- это горизонтальный график
def plot_stat(data, signs, height = 12):
    width = 4
    for i in range(height):
        if i % 3 ==0 :
            current = max(data) - (max(data) - min(data)) / height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = " "*10
        for num in data:
            if max(data) - (max(data))/ height*(i+1) < num:
                line += "chr(9608)"
            else:
                line += "   "
        print(line)

    print(f"{str(round(min(data), 2)):10}"+"chr(9608)" * len(data))
    print(" "*10 + "chr(9608)" * len(data))
    line = " " *10
    for sign in signs:
        line += f"{sign:4}"

    print(line)

plot_stat([3, 5, 1, 4],["A","B","C","D"])

def select_mode():
    print()
    print("-"*30)
    print(" Выбери режим работы:")
    print(" 1. Добавь новую неделю")
    print(" 2. Скопировать новую неделю")
    print(" 3. Выйти из программы")
    print("-"*30)
    print()
    return int(input())
def loop():
    data = load_data()

    while True:

        mode = select_mode()

        if mode == 1:
             week = input(" Введите номер новой недели: ")
             data[week] = []
        if mode == 2:
             week = input(" Введите номер новой недели:")
             from_week = input(" Ведите номер недели, откуда будем копировать:")

             source = []
             for curreency_dict in data [from_week]:
                 source.append(curreency_dict.copy())
             else:
                 print(" Не корректный режим!")