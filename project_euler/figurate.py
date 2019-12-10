from math import sqrt


def triangular(n):
    return int(n * (n + 1) / 2)


def is_triangular(n):
    x = (sqrt(8 * n + 1) - 1) / 2
    return x == int(x)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagonal(n):
    x = (sqrt(24 * n + 1) + 1) / 6
    return x == int(x)


def hexagonal(n):
    return n * (2 * n - 1)


def is_hexagonal(n):
    x = (sqrt(8 * n + 1) + 1) / 4
    return x == int(x)
