from project_euler.prime import primes
from decimal import getcontext, Decimal
import re


def solve():
    longest = (0, 0)
    getcontext().prec = 2048
    for i in primes(end=1000):
        match = re.search(r'(\d{2,}?)(?=\1)+', str(Decimal(1) / i))
        if match:
            size = len(match.group())
            if size > longest[1]:
                longest = (i, size)
    return longest[0]


def test():
    assert solve() == 983
