# РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР°
def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    if len(lys) == 1:
        return lis[0]
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
print(binary_search([10,20,30,40,50], 20))
#print(timeit.timeit("binary_search([1,4,5,6,7,10,20,30,40,50], 20)", setup="from __main__ import binary_search", number=1))
