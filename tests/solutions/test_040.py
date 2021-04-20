import functools as ft


def solution():
    digits = [10 ** x for x in range(7)]
    digit_str = ""
    n = 1
    while len(digit_str) < digits[-1]:
        digit_str += str(n)
        n += 1
    return ft.reduce(lambda x, y: x * int(digit_str[y - 1:y]), digits)


def test():
    assert solution() == 210
