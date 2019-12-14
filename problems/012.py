from itertools import count
from project_euler.divisor import divisors
from project_euler.figurate import triangular


def solve():
    target = 500
    for i in count():
        t = triangular(i)
        if len(divisors(t)) > target:
            return t


def test():
    assert solve() == 76576500
