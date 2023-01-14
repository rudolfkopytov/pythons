#Выведем информацию о компаниях, которые харанятся во вложенных списках в виде:
#`Company's capitalizations is ***`
companies_capitalization = [
    ['Orange', 1.3],
    ['Maxisoft', 1.5],
    ['Headbook', 0.8],
    ['Nicola', 2.2]
]
for company in companies_capitalization:
    # print(company)
    print(f"{company[0]}'s capitalization is {company[1]}")