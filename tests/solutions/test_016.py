def solution():
    return sum(int(x) for x in str(2 ** 1000))


def test():
    assert solution() == 1366
