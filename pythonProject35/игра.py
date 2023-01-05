answer = int(input("input your lucky int:"))
mynum = 10
if answer ==10 or mynum != 100:
    print("You're winner!!!")# - это главное условие, все остальные блоки - пропускаются!
elif 8 <= answer < 10 :
    print("So close")
else:
    print("Miss!")