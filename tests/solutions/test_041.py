import project_euler.pandigital as pd
import project_euler.prime as pr


def solution():
    for i in reversed(range(1, 10)):
        digits = list(reversed(range(1, i + 1)))
        for j in pd.pandigital(digits=digits):
            if pr.is_prime(j):
                return j


def test():
    assert solution() == 7652413
