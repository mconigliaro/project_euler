from math import sqrt


def divisors(n, proper=False):
    d = [1]
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            d.extend([x, int(n / x)])
    if not proper:
        d.append(n)
    return list(set(d))
