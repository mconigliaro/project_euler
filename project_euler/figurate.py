from math import sqrt


def is_triangular(n):
    if n == 0:
        return True
    else:
        x = (sqrt(8 * n + 1) - 1) / 2
        return x == int(x)


def triangular(n):
    return int(n * (n + 1) / 2)


def is_pentagonal(n):
    if n == 0:
        return True
    else:
        x = (sqrt(24 * n + 1) + 1) / 6
        return x == int(x)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)
