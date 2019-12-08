def solve():
    return 1 + sum(4 * i ** 2 - 6 * i + 6 for i in range(3, 1002, 2))


def test():
    assert solve() == 669171001
