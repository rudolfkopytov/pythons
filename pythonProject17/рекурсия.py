def m(L):
    if len(L) == 1:
        return L[0]

    result = m(L[1:])

    if result < L[0]:
        return result
    else:
        return L[0]


m([10, 12, 1, 4])
