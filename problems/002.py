from project_euler.fibonacci import fibonacci


def solve():
    return sum(x for x in fibonacci(up_to=4000000) if x % 2 == 0)


def test():
    assert solve() == 4613732
