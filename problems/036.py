def solve():
    sum = 0
    for i in range(1, 1000000):
        d = str(i)
        b = bin(i)[2:]
        if d == ''.join(reversed(list(d))) and b == ''.join(reversed(list(b))):
            sum += i
    return sum


def test():
    assert solve() == 872187
