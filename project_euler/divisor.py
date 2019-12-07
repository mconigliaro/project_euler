from math import sqrt


def divisors(n, proper=False):
    d = []
    for x in range(1, int(sqrt(n))):
        if n % x == 0:
            d.extend([x, int(n / x)])
    d = sorted(set(d))
    return d[0:-1] if proper else d
