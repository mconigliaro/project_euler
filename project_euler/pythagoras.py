from math import sqrt
from project_euler.divisor import greatest_common_divisor


def pythagorean_triplets(end, primitive=False):
    a_start = 3
    a_end = int(sqrt(end ** 2 / 2)) + 1
    for a in range(a_start, a_end):
        b_start = a + 1
        b_end = int(sqrt((end ** 2) - (a ** 2))) + 1
        for b in range(b_start, b_end):
            if not primitive or \
                  (primitive and greatest_common_divisor(a, b) == 1):
                c_start = int(sqrt(a ** 2 + b ** 2))
                c_end = int(sqrt(a ** 2 + b ** 2)) + 2
                for c in range(c_start, c_end):
                    if c ** 2 == a ** 2 + b ** 2:
                        triplet = tuple(sorted([a, b, c]))
                        yield triplet