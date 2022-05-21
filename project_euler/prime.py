from itertools import count
from math import sqrt
from typing import Generator, Union


def primes(num: Union[int, None] = None, end: Union[int, None] = None) -> Generator:
    memo = {}
    i = 0
    for x in count(2):
        if (num and i >= num) or (end and x >= end):
            break
        elif x not in memo:
            memo[x**2] = [x]
            i += 1
            yield x
        else:
            for p in memo[x]:
                memo.setdefault(p + x, []).append(p)
            del memo[x]


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        return not any(n % x == 0 for x in range(3, int(sqrt(n)) + 1, 2))
