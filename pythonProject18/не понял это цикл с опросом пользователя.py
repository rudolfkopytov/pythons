def loop(data):
    greet()

    while True:
        mode = ask_mode()
        if mode == "1":
            data.append(ask_income())
        elif mode == "2":
            data.append(ask_spend())
        elif mode == "3":
            beg, end = ask_interval()
            stat(data, beg, end)
        elif mode == "4":
            break
        else:
            wrong()

    print("-----------------------------")
    print("      Данные сохранены!      ")
    print("-----------------------------")

    return data