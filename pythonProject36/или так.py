geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
geo_logs_copy = geo_logs.copy()

for log in geo_logs_copy:
    # print(list(log.values())[0])
    if 'Россия' not in list(log.values())[0]:
        geo_logs.remove(log)

print(geo_logs)