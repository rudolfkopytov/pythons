# РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР° (СЂРµРєСѓСЂСЃРёРІРЅС‹Р№)
def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search((arr[mid:]), target)
            return mid + callback_response
        else:
            return recursive_binary_search((arr[:mid]), target)
print(recursive_binary_search([10,20,30,40,50,60], 20))
#print(timeit.timeit("recursive_binary_search([1,4,5,6,7,10,20,30,40,50], 20)", setup="from __main__ import recursive_binary_search", number=1))