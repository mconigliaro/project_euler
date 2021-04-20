import project_euler.pandigital as pd


def solution():
    return list(pd.pandigital(1000000))[-1]


def test():
    assert solution() == 2783915460
