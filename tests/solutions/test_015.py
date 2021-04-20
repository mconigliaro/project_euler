import project_euler.pascal as pas


def solution():
    return pas.pascals_triangle(20 * 2, 20)


def test():
    assert solution() == 137846528820
