def solution():
    return 1 + sum(4 * i**2 - 6 * i + 6 for i in range(3, 1002, 2))


def test():
    assert solution() == 669171001
