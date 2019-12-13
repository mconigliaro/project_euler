from project_euler.pandigital import pandigital
from project_euler.prime import is_prime


def solve():
    for i in reversed(range(1, 10)):
        c = ''.join(str(x) for x in range(1, i + 1))
        for j in reversed(list(pandigital(chars=c))):
            n = int(j)
            if is_prime(n):
                return n


def test():
    assert solve() == 7652413
