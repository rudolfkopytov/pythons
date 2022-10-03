edibles = [" Отбивные "," Пельмени"," яйца", "орехи"]

for food in edibles:
    if food == " Пельмени ":
        print(" Я не ем Пельмени!")
        continue
    print(" Отлично, вкусные " + food )
else:
    print(" Ненавижу Пельмени!")
print(" Ужин окончен.")