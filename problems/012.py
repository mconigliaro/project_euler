from project_euler.divisor import divisors
from project_euler.figurate import triangular


def solve():
    target = 500
    i = 0
    found = None
    while not found:
        i += 1
        t = triangular(i)
        if len(divisors(t)) > target:
            found = t
    return found


def test():
    assert solve() == 76576500
