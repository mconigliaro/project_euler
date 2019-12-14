from project_euler.fibonacci import fibonaccis


def solve():
    for i, x in enumerate(fibonaccis()):
        if len(str(x)) == 1000:
            return i


def test():
    assert solve() == 4782
