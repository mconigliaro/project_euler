from itertools import permutations


def solve():
    p = sorted(permutations('0123456789'))[999999]
    return int(''.join(str(x) for x in p))


def test():
    assert solve() == 2783915460
