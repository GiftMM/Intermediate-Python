def is_prime(x):

    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

def primes_below(x):
    List = []

    for i in range(x):
        if is_prime(i):
            List.append(i)
    return List