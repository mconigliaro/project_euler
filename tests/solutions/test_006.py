def solution():
    r = range(1, 101)
    return sum(r) ** 2 - sum(x**2 for x in r)


def test():
    assert solution() == 25164150
