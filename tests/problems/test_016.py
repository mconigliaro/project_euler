def solve():
    return sum(int(x) for x in str(2 ** 1000))


def test():
    assert solve() == 1366
