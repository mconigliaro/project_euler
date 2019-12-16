from project_euler.pandigital import pandigital


def solve():
    return list(pandigital(1000000))[-1]


def test():
    assert solve() == 2783915460
