def is_triangular(n):
    return (8 * n + 1) ** 0.5 % 1 == 0


def triangular(n):
    return int(n * (n + 1) / 2)
