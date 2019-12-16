from project_euler.pandigital import pandigital
from project_euler.prime import is_prime


def solve():
    for i in reversed(range(1, 10)):
        digits = list(reversed(range(1, i + 1)))
        for j in pandigital(digits=digits):
            if is_prime(j):
                return j


def test():
    assert solve() == 7652413
