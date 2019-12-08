from collections import deque
from project_euler.prime import primes, is_prime


def rotations(n):
    if n < 10:
        return [n]
    else:
        r = []
        digits = deque(i for i in str(n))
        for i in range(len(digits) - 1):
            digits.append(digits.popleft())
            r.append(int(''.join(digits)))
        return r


def solve():
    return sum(1 for i in primes(end=1000000)
               if all(is_prime(r) for r in rotations(i)))


def test():
    assert solve() == 55
