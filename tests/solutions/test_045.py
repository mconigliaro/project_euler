import itertools as it
import project_euler.figurate as fig


def solution():
    h = []
    for i in it.count(144):
        p = fig.pentagonal(i)
        h.append(fig.hexagonal(i))
        if p in h:
            return p


def test():
    assert solution() == 1533776805
