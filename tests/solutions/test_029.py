import itertools as it


def solution():
    terms = []
    for i, j in it.product(range(2, 101), repeat=2):
        terms.append(i ** j)
    return len(sorted(set(terms)))


def test():
    assert solution() == 9183
