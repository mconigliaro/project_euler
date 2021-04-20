import math


def solve():
    return sum(i for i in range(3, 50000)
               if i == sum(math.factorial(int(x)) for x in str(i)))


def test():
    assert solve() == 40730
