from math import prod
from project_euler.pythagoras import pythagorean_triplets


def solve():
    n = 1000
    for x in pythagorean_triplets(n):
        if sum(x) == n:
            return prod(x)


def test():
    assert solve() == 31875000
