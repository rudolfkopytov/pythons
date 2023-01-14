people = {1: {'name': 'Oleg', 'age': '29', 'sex': 'Male'},
          2: {'name': 'Kate', 'age': '21', 'sex': 'Female'},
          3: {'name': 'Liza', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Pavel', 'age': '36', 'sex': 'Male'}}
age = 0
for person in people.values():
    age += int(person['age'])
print(age / len(people))