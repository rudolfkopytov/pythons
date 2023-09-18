import time
import numpy as np

def method1(li1,li2):
    temp = []
    for element in li1:
        if element not in li2:
            temp.append(element)
    return temp
# это метод поиска из одного списка в элементах другого списка (просто сравниваем списки на повторения элементов)
def methodnp(npl1,npl2):
    npdif1 = np.setiffl1d(npl1, npl2)
    npdif2 = np.setdiff1d(npl2, npl1)
    return np.concatenate((npdif1, npdif2))


list1 = (10,15,20,25,30,35,40)
list2 = (25,40,35)

print(f"{method1.__name__}:", method1(list1,list2))

t1 = time.time()
for i in range(0,100000):

    method1(list1, list2)
t2 = time.time()
print(f"{method1. __name__}: {t2-t1}")
# это сравнение по скорости - взято 100000 операций и время на это вычисление понапдобившееся.
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)
print(f"{method1.__name__}:", method1(sorted_list1,sorted_list2))
# отсортировал списки и разницу посчиталэ.


t1 = time.time()
for i in range (0,100000):
    method1(sorted_list1, sorted_list2)
t2 = time.time()
print(f"{method1.__name__} sorted: {t2-t1}")

s2 = set(list2)
_t3 = [x for x in list1 if x not in s2]
print(f"method set: ",_t3)

t1 = time.time()
for i in range(0,100000):
    _t3 = [x for x in list1 if x not in s2]
t2 = time.time()
print(f"method set: {t2-t1}")
# здесь ищем уже елементы не из списка, а уже из сэта и прсчитали скоростные характеристики
#nplist1 = np.array(list1)
#nplist2 = np.array(list2)

#print(f"{methodnp.__name__}", list(methodnp(nplist1,nplist2))

#t1 = time.time()
#for i in range(0,100000):
#    methodnp(nplist1, nplist2)
#t2 = time.time()
#print(f"method np: {t2-t1} ")
# гдето нужно было взять эти вшивые "np" - сделать теже вычисления с np.

sl1 = set(list1)
sl2 = set(list2)

set_dif = sl1.symmetric_difference(sl2)
print(f"method set_dif:", list(set_dif))

t1 = time.time()
for i in range(0,100000):
    set_dif = sl1.symmetric_difference(sl2)
t2 = time.time()
print(f"method set_dif: {t2-t1}")
# здесь преобразовал оба списка в сеты и вызвал симметричную разницу.