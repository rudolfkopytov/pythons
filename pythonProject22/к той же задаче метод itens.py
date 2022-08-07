def list_stat(A):
    stat = {}
    for number in A:
        if number in stat:
            stat[number] +=1
        else:
            stat[number] =1
    return stat


def list_sort(A):
    stat = list_stat(A)
    items = list(stat.items())
    items.sort(key = lambda x: x[1])
    print(items)

list_sort([1, 2, 1, 1, 2, 3, 4,6, 4, 4, 10])