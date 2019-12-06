from math import factorial


def pascals_triangle(row, col):
    if col > row:
        return None
    else:
        return factorial(row) / (factorial(col) * factorial(row - col))
