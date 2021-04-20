import project_euler.fibonacci as fib


def solve():
    for i, x in enumerate(fib.fibonaccis()):
        if len(str(x)) == 1000:
            return i


def test():
    assert solve() == 4782
