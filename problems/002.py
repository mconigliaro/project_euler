from project_euler.fibonacci import fibonaccis


def solve():
    return sum(x for x in fibonaccis(end=4000000) if x % 2 == 0)


def test():
    assert solve() == 4613732
