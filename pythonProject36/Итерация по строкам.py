# итерация по строкам
company_name = 'SkillFactory'
# мы сами задаем имя переменной в которую будут последовательно помещаться каждый элемент нашего объекта
for letter in company_name:
    letter = letter.upper()
    print(f'*{letter}*', end='')