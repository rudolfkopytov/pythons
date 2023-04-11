def merge(A, B):
    i, j, C = 0, 0, []
    while True:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
            if i == len(A):
                C.extend(B[j:])
                break

        else:
            C.append(B[j])
            j += 1
            if j == len(B):
                C.extend(A[i:])
                break

    return C