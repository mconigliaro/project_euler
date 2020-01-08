from itertools import combinations_with_replacement
from project_euler.divisor import divisors


def solve():
    m = 28123
    abundant = [x for x in range(12, m) if sum(divisors(x, proper=True)) > x]
    sums = set(sum(x) for x in combinations_with_replacement(abundant, 2))
    return sum(x for x in range(m) if x not in sums)


def test():
    assert solve() == 4179871
