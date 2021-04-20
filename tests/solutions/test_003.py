import math
import project_euler.prime as pr


def solution():
    n = 600851475143
    p = reversed(list(pr.primes(end=math.sqrt(n))))
    return next(i for i in p if n % i == 0)


def test():
    assert solution() == 6857
