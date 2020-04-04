import math


def solve():
    return sum(int(x) for x in str(math.factorial(100)))


def test():
    assert solve() == 648
