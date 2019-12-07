from math import sqrt


def divisors(n, proper=False):
    d = []
    for x in range(1, int(sqrt(n))):
        if n % x == 0:
            d.extend([x, int(n / x)])
    if proper and n in d:
        d.remove(n)
    return list(set(d))
