professions = ['IT', 'Физика', 'Математика']
persons = [['Гейтс', 'Джобс', 'Возняк'], ['Эйнштейн', 'Фейнман'], ['Эвклид', 'Ньютон']]
for pro, person_list in zip(professions, persons):
    print(f'{pro}:')
    for person in person_list:
        print(person)
    print()