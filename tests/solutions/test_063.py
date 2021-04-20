def solve():
    numbers = []
    for p in range(1, 23):  # FIXME: How do we know the upper bound?
        i = 1
        n = 1
        while len(str(n)) <= p:
            if len(str(n)) == p:
                numbers.append(n)
            i = i + 1
            n = i ** p
        i = 0
    return len(numbers)


def test():
    assert solve() == 49
