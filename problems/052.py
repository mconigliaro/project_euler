def solve():
    i = 1
    while True:
        if all(sorted(str((i * j))) == sorted(str(i)) for j in range(2, 6)):
            return i
        i += 1


def test():
    assert solve() == 142857
