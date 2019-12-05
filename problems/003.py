from math import sqrt
from project_euler.prime import primes


def test_003():
    n = 600851475143
    p = reversed(list(primes(up_to=sqrt(n))))
    largest = next(i for i in p if n % i == 0)
    assert largest == 6857
