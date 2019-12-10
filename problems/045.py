from project_euler.figurate import pentagonal, hexagonal


def solve():
    h = []
    i = 144
    while True:
        p = pentagonal(i)
        h.append(hexagonal(i))
        if p in h:
            return p
        i += 1


def test():
    assert solve() == 1533776805
