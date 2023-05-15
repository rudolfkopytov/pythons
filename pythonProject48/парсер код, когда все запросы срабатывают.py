import requests

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа