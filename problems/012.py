import itertools as it
import project_euler.divisor as div
import project_euler.figurate as fig


def solve():
    target = 500
    for i in it.count():
        t = fig.triangular(i)
        if len(div.divisors(t)) > target:
            return t


def test():
    assert solve() == 76576500
