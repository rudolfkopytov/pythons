lucky_number = int(input(" Загадайте число."))
print("Перед Вами образовалась пещера, как по волшебству.")
enter = input("Ххотите ли Вы войти в пещеру? (y/n)")
answer = None
if enter == "n":
    print(" Вы не решились зайти в пещеру и ушли так и не узнав, что можно там найти. ")
else:
    print(" Вы зашли в пещеру и, пройдя 10 метров, обнаружили развилку на 5 разных тунелей .")
    answer = int(input('В какой из тунелей Вы отправитесь? (1-5)'))
if answer >= 2 and lucky_number > 10 :
    print("B этом тунеле Вас поджидал медведь, который не оставаил Вам и шанса")
    end = "Bed"
elif answer >= 2 and lucky_number <= 10:
    print("В этом тунеле Вас  поджидал тоже медведь. На Ваше счастье он спит. ")
    end = "Time for nothing"
else:
    print(" Вы дошли до выхода из пещеры, где обнаружили сундук с золотом")
    end = "Good"
print(f" Ваша концовка - {end}")