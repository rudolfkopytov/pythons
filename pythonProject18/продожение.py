def ask_cost(ask_str):
    number = None
    while number is None:
        num_str = input("  Введите сумму:             ")
        if num_str.isdigit():
            number = int(num_str)
        else:
            print(" Вы ввели некорректное число!")
            continue
    return number


def ask_date(ask_str):
    date = None
    while date is None:
        date_str = input(ask_str)
        splitted = date_str.split("-")

        if len(splitted) != 3:
            print(" Введена некорректная дата!  ")
            continue

        check = []
        for string in splitted:
            check.append(string.isdigit())

        if not (all(check)):
            print(" Часть даты- не число!       ")
            continue

        splitted[0] = "20" + splitted[0]
        year, month, day = map(int, splitted)
        date = dt.date(year, month, day)
    return date