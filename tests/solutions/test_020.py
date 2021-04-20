import math


def solution():
    return sum(int(x) for x in str(math.factorial(100)))


def test():
    assert solution() == 648
