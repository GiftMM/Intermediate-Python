def big_fibonacci(n):
    n1 = 0
    n2 = 1
    n3 = n1 + n2

    while len(str(n3)) < n:
        n1 = n2
        n2 = n3
        n3 = n1 + n2

    return n3