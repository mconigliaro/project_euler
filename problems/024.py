from itertools import permutations


def solve():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p = sorted(permutations(digits))[999999]
    return int(''.join(str(x) for x in p))


def test():
    assert solve() == 2783915460
