import project_euler.fibonacci as fib


def solve():
    return sum(x for x in fib.fibonaccis(end=4000000) if x % 2 == 0)


def test():
    assert solve() == 4613732
