from math import sqrt
from project_euler.prime import primes, is_prime


def test_003():
    n = 600851475143
    p = list(primes(up_to=sqrt(n)))
    while not is_prime(n):
        n = n / list(filter(lambda i: n % i == 0, p))[0]
    assert n == 6857
