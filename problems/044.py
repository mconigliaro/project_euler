import itertools as it
import project_euler.figurate as fig


def solve():
    p_hist = []
    for i in it.count(1):
        p_curr = fig.pentagonal(i)
        for p in p_hist:
            if fig.is_pentagonal(p_curr - p) and fig.is_pentagonal(p_curr + p):
                return p_curr - p
        p_hist.append(p_curr)


def test():
    assert solve() == 5482660
