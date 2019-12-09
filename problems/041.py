from itertools import permutations
from project_euler.prime import is_prime


def solve():
    for i in reversed(range(1, 10)):
        for j in reversed(sorted(permutations(range(1, i + 1)))):
            n = int(''.join(str(x) for x in j))
            if is_prime(n):
                return n


def test():
    assert solve() == 7652413
