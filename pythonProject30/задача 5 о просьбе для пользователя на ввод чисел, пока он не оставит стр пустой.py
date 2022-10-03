# http://joxi.ru/xAeby9eTVwdoNr - условие задачи.
words = []
word = input(' Введите слово')
while word != '':# пока слова , введённые пользователем не равны пустой строке. # если (if) пользователь(word) не ввёл в наш список (words)
    if word not in words: # то я добавлюю с помощью метода (append) в КОНЕЦ СПИСКА - потому, что этот метод так и работает (добавляет элемент в конец списка) word .
        words.append(word)
    word = input(' Введите слово')
for item in words:   # заводим цикл  for (перебора элементов водимых в список words
    print(item)
