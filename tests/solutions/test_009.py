import math
import project_euler.pythagoras as pyt


def solution():
    n = 1000
    for x in pyt.pythagorean_triplets(n):
        if sum(x) == n:
            return math.prod(x)


def test():
    assert solution() == 31875000
