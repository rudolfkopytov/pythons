d={
  "20": [
    {
      "name": "RUB",
      "cost": 0.1354,
      "amount": 1000
    },
    {
      "name": "BTC",
      "cost": 36008,
      "amount": 0.003
    }
  ],
  "21": [
    {
      "name": "RUB",
      "cost": 0.1354,
      "amount": 2000
    },
    {
      "name": "BTC",
      "cost": 36008,
      "amount": 0.006
    }
  ]
}


import json #- работает только со строками


def save_data(data):
    with open("data.json","w")as f:# открытие файла
        json.dump(data,f,indent = 2)# - сохранение в него


def load_data():
    with open("data.json") as f: # открытие файла
        data = json.load(f) # -считывание с него
    return data

#save_data(d)# - появился файл datajson, в колтором сохраненна вся информация.
def show_percent(name, percent, widht = 50):
  fill ="█"
  empty = "-"
  bars = round(percent * widht)

  progress = fill * bars + empty * (widht - bars)
  print(f"{name:7} - {round(percent * 100)}% |{progress}|")


#show_percent("RUB",0.6)
#show_percent("BITCOIN",0.4)- это горизонтальный график,теперь: -вертикальный!!
def plot_stat(data, signs, height = 12):

    for i in range(height):
        if i % 3 ==0 :
            current = max(data) - (max(data) - min(data)) / height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = " "*10
        for num in data:
            if max(data) - (max(data)-min(data))/height*(i+1) < num:
                line += "█   "
            else:
                line += "    "

        print(line)

    print(f"{str(round(min(data), 2)):10}" + "█   " * len(data))
    print(" "*10 + "█   " * len(data))
    line = " "*10
    for sign in signs:
        line += f"{sign:4}"

    print(line)

plot_stat([3, 5, 1, 4],["A","B","C","D"])