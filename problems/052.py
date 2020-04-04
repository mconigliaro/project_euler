import itertools as it


def solve():
    for i in it.count(1):
        if all(sorted(str((i * j))) == sorted(str(i)) for j in range(2, 6)):
            return i


def test():
    assert solve() == 142857
