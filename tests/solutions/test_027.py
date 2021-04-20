import math
import project_euler.prime as pr


def solution():
    max_coefficients = []
    max_primes = 0

    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            n = 0
            while pr.is_prime(n ** 2 + i * n + j):
                n += 1

            if n > max_primes:
                max_coefficients = [i, j]
                max_primes = n

    return math.prod(max_coefficients, start=1)


def test():
    assert solution() == -59231
