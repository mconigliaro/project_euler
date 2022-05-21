def solution():
    return int(str(sum(x**x for x in range(1, 1001)))[-10:])


def test():
    assert solution() == 9110846700
