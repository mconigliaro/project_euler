from math import sqrt
from project_euler.prime import primes


def solve():
    n = 600851475143
    p = reversed(list(primes(end=sqrt(n))))
    return next(i for i in p if n % i == 0)


def test():
    assert solve() == 6857
