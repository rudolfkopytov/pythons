import json

OPEN_TIME = 10
CLOSE_TIME = 21


def check_date(str_date):
    if len(str_date.split("-")) != 3:
        return False

    year, month, day = str_date.split("-")
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    if not(year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year, month, day = int(year), int(month), int(day)

    if 2000 <= year <= 3000 and 1 <= month<= 12 and 1 <= day <= 31:
        return True
    else:
        return False

def ask_date():
    print(" Ведите дату:")
    date = None
    while date is None:
        temp = input()
        if check_date(temp):
            date = temp
        else:
            print(" Введена не корректная дата")
    return date


def check_int(number, begin, end):
    if not(number.isdigit()):
        return False
    number = int(number)

    return begin <= number <= end


def ask_int(begin, end):
    number = None
    while number is None:
        temp = input()
        if check_int(temp, begin, end):
            number = int(temp)
        else:
            print(" Ведено не корректное число")

    return number

def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)

def load_info():
    with open("info.json") as f:
        info = json.load(f)

    return info

def ask_user():
    print(" Введите время ожидания очереди(в часах):")
    wait = ask_int(0, 12)

    print(f" Введите час, в котором Вы посещали МФЦ:(от {OPEN_TIME} до {CLOSE_TIME} )")
    hour = ask_int(OPEN_TIME, CLOSE_TIME)

    print(f"Введите дату посещения (в формате YYYY-MM-DD):")
    date = ask_date()

    return {
        "wait": wait,
        "hour": hour,
        "date": date
    }


def main():
    stat = load_info()

    while True:
        stat.append(ask_user())

        print(" Продолжить заполнение анкеты (Да/Нет)?")

        temp = input()
        if temp.lower() != " да ":
            break

    save_info(stat)

main()