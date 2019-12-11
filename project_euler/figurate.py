from math import sqrt


def triangular(n):
    return int(n * (n + 1) / 2)


def is_triangular(n):
    return ((sqrt(8 * n + 1) - 1) / 2).is_integer()


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagonal(n):
    return ((sqrt(24 * n + 1) + 1) / 6).is_integer()


def hexagonal(n):
    return n * (2 * n - 1)


def is_hexagonal(n):
    return ((sqrt(8 * n + 1) + 1) / 4).is_integer()
