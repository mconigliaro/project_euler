def solve():
    return sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)


def test():
    assert solve() == 233168
