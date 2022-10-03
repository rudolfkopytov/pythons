#def find_smallest_int(arr):
#    return min(arr)
#print(find_smallest_int([2,5,66,0,678,352]))# min - это метод, и мы создали программу с использованием методов (не круто), а теперь без методов -(круто!):


def find_smallest_int(arr):
    smallest = arr[0]
    for i in range(0, len(arr)): # перебираем наше множество от нуля до конца писка.
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest
print(find_smallest_int([2,678,5,0.98]))# код работает!