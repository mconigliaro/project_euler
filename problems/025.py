from project_euler.fibonacci import fibonacci


def solve():
    for i, x in enumerate(fibonacci()):
        if len(list(str(x))) == 1000:
            return i


def test():
    assert solve() == 4782
