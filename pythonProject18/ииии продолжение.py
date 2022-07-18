def ask_income():
    print("-----------------------------")
    cat = input("  Введите категорию:         ")
    cost = ask_cost("  Введите сумму поступления:")
    date = ask_date("  Введите дату поступления: ")
    return ["+",cat, date, cost]

def ask_spend():
    print("-----------------------------")
    cat = input("  Введите категорию:         ")
    cost = ask_cost("  Введите сумму траты:      ")
    date = ask_date("  Введите дату траты:       ")
    return ["-",cat, date, cost]