from itertools import count
from project_euler.figurate import pentagonal, hexagonal


def solve():
    h = []
    for i in count(144):
        p = pentagonal(i)
        h.append(hexagonal(i))
        if p in h:
            return p


def test():
    assert solve() == 1533776805
