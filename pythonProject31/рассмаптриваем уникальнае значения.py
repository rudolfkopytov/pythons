set_1 = { '1', '2', '5'}
set_2 = { '1', '3', '6'}# и мы !! вдруг!! захотели вывести 2 и 5
#print(set_1 - set_2)# мы берём первый set и вычитаем из рнего второй и выводим лишь те значения, что не повторяются во втором sete
# а 3 и 6 - не вывелась потому что мы хотели посмотреть значение в первом sete ? а значит закономерно если мы захотим посмотьреть значения во втором sete то делаем следующее:
#print(set_2 - set_1)# результат есть и он -3 и 6
#print(set_1. intersection(set_2) )# этот метод вычисляет похожие значения и в данном случае - это 1
