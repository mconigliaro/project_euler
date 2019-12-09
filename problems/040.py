from functools import reduce


def solve():
    digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digit_str = ""
    n = 1
    while len(digit_str) < digits[-1]:
        digit_str += str(n)
        n += 1
    return reduce(lambda x, y: x * int(digit_str[y - 1:y]), digits)


def test():
    assert solve() == 210
