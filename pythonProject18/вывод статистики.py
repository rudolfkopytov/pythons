def stat_all_time(data):
    income_stat = defaultdict(list)
    spend_stat = defaultdict(list)

    for typ, cat, date, cost in data:
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