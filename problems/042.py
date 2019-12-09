from project_euler.data import data
from project_euler.figurate import is_triangular
from project_euler.string import string_value


def solve():
    d = data('problems/data/042.txt')
    words = [x.replace('"', '') for x in d[0].split(',')]
    return len([x for x in words if is_triangular(string_value(x))])


def test():
    assert solve() == 162
