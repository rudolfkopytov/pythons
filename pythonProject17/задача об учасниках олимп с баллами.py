candidates = [
    ("Иван Иванов" , 200),
    ("Сергей Иванов" , 500),
    ("Андрей Иванов" , 220),
    ("Иван Сергееы" , 100),
]

beg = 200
end = 400

for name, points in candidates:
    if beg <= points <= end:
        print(name)