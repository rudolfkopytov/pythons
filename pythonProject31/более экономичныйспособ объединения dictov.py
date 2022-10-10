my_dict_1 = {
    'name': 'Garry',
    'age' : 28
}
my_dict_2 = {
    'phone' : '+7 911 021 71 38',
    'country': 'Russia'
}
new_dict = {**my_dict_1, **my_dict_2}# это как раз и есть тот синтаксический сахар в pythone!!- мы объеденили 2 (только!!) dicta , но можем объединить сколько угодно dictov : ** - это распаковка dictov.
# к примеру мы создаём ещё один dict: my_dict_3 = ' country' : ' Russia'} и добаляем его так же в распаковку. - и всё получится!
print(new_dict)