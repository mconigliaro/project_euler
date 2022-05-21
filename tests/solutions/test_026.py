import project_euler.prime as pr
import decimal as dec
import re


def solution():
    longest = (0, 0)
    dec.getcontext().prec = 2048
    for i in pr.primes(end=1000):
        match = re.search(r"(\d{2,}?)(?=\1)+", str(dec.Decimal(1) / i))
        if match:
            size = len(match.group())
            if size > longest[1]:
                longest = (i, size)
    return longest[0]


def test():
    assert solution() == 983
