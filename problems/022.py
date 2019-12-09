from project_euler.data import data
from project_euler.string import string_value


def solve():
    d = data('problems/data/022.txt')
    names = sorted([x.replace('"', '') for x in d[0].split(',')])
    return sum(string_value(n) * (i + 1) for i, n in enumerate(names))


def test():
    assert solve() == 871198282
