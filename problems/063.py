def solve():
    numbers = []
    p = 1
    while p < 22:  # FIXME
        i = 1
        n = 1
        while len(str(n)) <= p:
            if len(str(n)) == p:
                numbers.append(n)
            i = i + 1
            n = i ** p
        i = 0
        p += 1
    return len(numbers)


def test():
    assert solve() == 49
