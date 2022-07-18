def ask_interval():
    date1 = ask_date("  Введите начало интервала:")
    date2 = ask_date("  Введите конец интервала: ")
    return (date1, date2)


def stat(data, date1, date2):
    income_stat = defaultdict(list)
    spend_stat = defaultdict(list)

    for typ, cat, date, cost in data:
        if date >= date1 and date <= date2:
            if typ == "+":
                income_stat[cat].append(cost)
            if typ == "-":
                spend_stat[cat].append(cost)

    print("-----------------------------")
    print("  Статистика поступлений:    ")
    print("-----------------------------")
    for cat, cost_list in income_stat.items():
        print(f"  {cat:20} - {sum(cost_list)}")
    print("-----------------------------")
    print("  Статистика трат:           ")
    print("-----------------------------")
    for cat, cost_list in spend_stat.items():
        print(f"  {cat:20} - {sum(cost_list)}")