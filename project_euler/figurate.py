from math import sqrt


def cubic(n: int) -> int:
    return n**3


def is_cubic(n: int) -> bool:
    return int(round(n ** (1 / 3))) ** 3 == n


def triangular(n: int) -> int:
    return int(n * (n + 1) / 2)


def is_triangular(n: int) -> bool:
    return ((sqrt(8 * n + 1) - 1) / 2).is_integer()


def pentagonal(n: int) -> int:
    return int(n * (3 * n - 1) / 2)


def is_pentagonal(n: int) -> bool:
    return ((sqrt(24 * n + 1) + 1) / 6).is_integer()


def hexagonal(n: int) -> int:
    return n * (2 * n - 1)


def is_hexagonal(n: int) -> bool:
    return ((sqrt(8 * n + 1) + 1) / 4).is_integer()
