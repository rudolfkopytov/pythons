# итерция по строкам
company_name = 'skillFactory'
# мы сами задаём переменную (в данном случае - letter )d которую будет последовательно помещаться каждый элемент нашего обьекта
for letter in company_name:
    letter = letter.upper()
    print('*', letter,'*', sep='', end='')