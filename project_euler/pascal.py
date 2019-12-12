from math import factorial


def pascals_triangle(i, j):
    return None if j > i else factorial(i) / (factorial(j) * factorial(i - j))
