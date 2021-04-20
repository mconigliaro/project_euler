def solution():
    sum = 0
    for i in range(1, 1000000):
        d = str(i)
        b = bin(i)[2:]
        if d == d[::-1] and b == b[::-1]:
            sum += i
    return sum


def test():
    assert solution() == 872187
