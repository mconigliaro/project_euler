import project_euler.divisor as div


def solution():
    amicable = []
    for i in range(1, 10001):
        a = sum(div.divisors(i, proper=True))
        if a > 0:
            b = sum(div.divisors(a, proper=True))
            if b == i and a != b:
                amicable.extend([a, b])
    return sum(set(amicable))


def test():
    assert solution() == 31626
