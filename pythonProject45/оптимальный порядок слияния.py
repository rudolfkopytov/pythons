def chunking(A):
    chunks = []
    a, d = 0, 0
    for b in range(1, len(A)):
        if d == 0:
            d = A[b] - A[a]
            continue

        if (A[b] - A[b-1])*d < 0:
            chunks.append((a, b-1) if d > 0 else (b-1, a))
            a, d = b, 0

    chunks.append((a, b) if d > 0 else (b, a))

    return chunks