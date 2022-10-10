# ДИНАМИЧЕСКИЙ -это: когда в строку мы можем щавести число:
#a  = "str"
#a = 2
#print(a)# мы в строку завели число и у нас ничего не поломалось
#def my_func(a,b):
#    return a*b

#print(my_func('strihg',3))# и вот она напечала string аж 3 раза
def my_func(a: str, b: int) -> str:
    return a * b
a: str = 123
print(my_func('string',3))# - то более правильное написание предыдущей функции.

