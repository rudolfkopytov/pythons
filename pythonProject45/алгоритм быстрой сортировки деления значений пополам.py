def top_down_merge_sort(A):
    if len(A) == 1:
        return A

    d = len(A) // 2
    left = top_down_merge_sort(A[:d])
    right = top_down_merge_sort(A[d:])

    return merge(left, right)