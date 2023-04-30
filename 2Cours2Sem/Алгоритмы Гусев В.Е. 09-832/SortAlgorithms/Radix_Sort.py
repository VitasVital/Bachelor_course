def radixsort(A):
    length = len(str(max(A)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)]
        for x in A:
            figure = x // 10**i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A = A + B[k]
    return A