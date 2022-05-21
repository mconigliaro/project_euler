import itertools as it
import project_euler.divisor as div


def solution():
    m = 28123
    abundant = [x for x in range(12, m) if sum(div.divisors(x, proper=True)) > x]
    sums = set(sum(x) for x in it.combinations_with_replacement(abundant, 2))
    return sum(x for x in range(m) if x not in sums)


def test():
    assert solution() == 4179871
