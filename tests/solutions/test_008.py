import math
import project_euler.data as dat


def solution():
    d = "".join(dat.data("tests/data/008.txt"))
    offset = 0
    chunk = 13
    greatest = 0
    while offset + chunk <= len(d):
        digits = [int(x) for x in list(d[offset : offset + chunk])]
        product = math.prod(digits, start=1)
        if product > greatest:
            greatest = product
        offset += 1
    return greatest


def test():
    assert solution() == 23514624000
