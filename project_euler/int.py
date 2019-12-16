from itertools import count
from math import log10


def int_digits(n, num=None):
    if n == 0:
        yield 0
    else:
        n = abs(n)
        n_len = int(log10(n)) + 1
        for i in count():
            if i >= n_len or num and i >= abs(num):
                break
            elif num and num < 0:
                n, digit = divmod(n, 10)
            else:
                digit = int((n / (10 ** (n_len - i - 1))) % 10)
            yield digit
