cook_book = {
  'салат': [
     {'ingredient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingredient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingredient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingredient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingredient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingredient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingredient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingredient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingredient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingredient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingredient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingredient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingredient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingredient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingredient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingredient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingredient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
for dish in cook_book:
#   print(dish)
  print(f'\n{dish[0].title()}:')
  for food in dish[1]:
    print(f'{food[0]}, {food[1] * person}{food[2]}')