from project_euler.fibonacci import fibonaccis
from project_euler.int import int_digits
from project_euler.pandigital import is_pandigital


def solve():
    start = 329000  # FIXME: Improve performance so we can start at 0
    digits = list(range(1, 10))
    len_digits = len(digits)
    for i, f in enumerate(fibonaccis(start=start), start=start):
        if i % 10000 == 0:
            print(f'{i}')
        last = set(int_digits(f, len_digits * -1))
        if is_pandigital(last, digits):
            first = list(int_digits(f, len_digits))
            if is_pandigital(first, digits):
                return i


def test():
    assert solve() == 329468
