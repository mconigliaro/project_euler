import project_euler.fibonacci as fib
import project_euler.int as it
import project_euler.pandigital as pd


def solve():
    start = 329000  # FIXME: Improve performance so we can start at 0
    digits = list(range(1, 10))
    len_digits = len(digits)
    for i, f in enumerate(fib.fibonaccis(start=start), start=start):
        if i % 10000 == 0:
            print(f'{i}')
        last = set(it.int_digits(f, len_digits * -1))
        if pd.is_pandigital(last, digits):
            first = list(it.int_digits(f, len_digits))
            if pd.is_pandigital(first, digits):
                return i


def test():
    assert solve() == 329468
