import project_euler.pascal as pas


def solve():
    return pas.pascals_triangle(20 * 2, 20)


def test():
    assert solve() == 137846528820
