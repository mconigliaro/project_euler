from math import factorial
from project_euler.divisor import divisors


def solve():
    amicable = []
    for i in range(1, 10001):
        a = sum(divisors(i, proper=True))
        if a > 0:
            b = sum(divisors(a, proper=True))
            if b == i and a != b:
                amicable.extend([a, b])
    return sum(set(amicable))


def test():
    assert solve() == 31626
