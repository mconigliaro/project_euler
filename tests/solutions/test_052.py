import itertools as it


def solution():
    for i in it.count(1):
        if all(sorted(str((i * j))) == sorted(str(i)) for j in range(2, 6)):
            return i


def test():
    assert solution() == 142857
