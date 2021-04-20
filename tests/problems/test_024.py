import project_euler.pandigital as pd


def solve():
    return list(pd.pandigital(1000000))[-1]


def test():
    assert solve() == 2783915460
