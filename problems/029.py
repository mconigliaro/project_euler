def solve():
    r = range(2, 101)
    terms = []
    for i in r:
        for j in r:
            terms.append(i ** j)
    return len(sorted(set(terms)))


def test():
    assert solve() == 9183
