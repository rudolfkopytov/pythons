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

print(load_data())