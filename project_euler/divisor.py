from math import sqrt


def divisor_count(n):
    return len([x for x in range(1, int(sqrt(n))) if n % x == 0]) * 2
