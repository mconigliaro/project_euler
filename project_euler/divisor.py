from math import sqrt


def divisors(n: int, proper: bool = False) -> list:
    d = [1]
    for x in range(2, int(sqrt(n)) + 1):
        q = n / x
        if q.is_integer():
            d.extend([x, int(q)])
    if not proper:
        d.append(n)
    return list(set(d))
