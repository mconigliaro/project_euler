from math import factorial


def solve():
    return sum(int(x) for x in list(str(factorial(100))))


def test():
    assert solve() == 648