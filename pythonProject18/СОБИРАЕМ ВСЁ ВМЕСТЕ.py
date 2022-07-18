def ask_file(FILENAME):
    print("-----------------------------")
    print(" Путь к файлу по-умолчанию:  ")
    print(f" {FILENAME}")
    print("-----------------------------")
    print("  Нажмите Enter для работы   ")
    print("       с этим файлом.        ")
    print("  Введите имя файла, если    ")
    print("  нужно работать с другим    ")
    command = input()
    if command:
        if os.path.isfile(command):
            FILENAME = command
            print("-----------------------------")
            print("  Файл выбран!     ")
        else:
            print("-----------------------------")
            print("  Такого файла нет!    ")
            print("  Использую файл по-умолчанию    ")
    return FILENAME