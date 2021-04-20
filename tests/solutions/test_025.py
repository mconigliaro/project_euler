import project_euler.fibonacci as fib


def solution():
    for i, x in enumerate(fib.fibonaccis()):
        if len(str(x)) == 1000:
            return i


def test():
    assert solution() == 4782
