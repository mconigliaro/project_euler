from math import gcd, sqrt
from typing import Generator


def pythagorean_triplets(end: int, primitive: bool = False) -> Generator:
    a_start = 3
    a_end = int(sqrt(end**2 / 2)) + 1
    for a in range(a_start, a_end):
        b_start = a + 1
        b_end = int(sqrt((end**2) - (a**2))) + 1
        for b in range(b_start, b_end):
            if not primitive or (primitive and gcd(a, b) == 1):
                c_start = int(sqrt(a**2 + b**2))
                c_end = c_start + 2
                for c in range(c_start, c_end):
                    if c**2 == a**2 + b**2:
                        triplet = tuple(sorted([a, b, c]))
                        yield triplet
