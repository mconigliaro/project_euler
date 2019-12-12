from project_euler.pascal import pascals_triangle


def solve():
    return pascals_triangle(20 * 2, 20)


def test():
    assert solve() == 137846528820
