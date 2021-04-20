def solve():
    return int(str(sum(x ** x for x in range(1, 1001)))[-10:])


def test():
    assert solve() == 9110846700
