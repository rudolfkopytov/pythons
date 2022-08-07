str_date = "2021-05-26"

def check_date(str_date):
    if len(str_date.split("-")) != 3:
        return False

    year, month, day = str_date.split("-")
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    if not(year.isdigit() and  month.isdigit() and day.isdigit()):
        return False
    year, month, day = int(year), int(month), int(day)
    if 2000 <= year <= 3000 and 1 <= month <= 12 and 1<= day <= 31:
        return True

def ask_date():
    print(" Введите дату:")
    date = None
    while date is None:
        temp = input()
        if check_date(temp):
            date = temp
        else:
            print(" Введена не корректная дата")
    return date
# и это жопа не работает! смотри его код!!