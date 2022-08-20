def list_stat(A):
    stat = {}
    for number in A:
        if number in stat:
            stat[number] +=1
        else:
            stat[number] = 1
    return stat

def list_stat_2(A):
    stat ={}
    for number in set (A) :# перебираем все цифры из словаря
        stat[number] = A.count(number)
    return stat