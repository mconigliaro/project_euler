def solve():
    r = range(1, 101)
    return sum(r) ** 2 - sum(x ** 2 for x in r)


def test():
    assert solve() == 25164150
