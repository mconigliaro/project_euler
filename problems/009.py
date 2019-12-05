def solve():
    n = 1000
    for i in range(3, n):
        for j in range(4, n):
            a = j ** 2 - i ** 2
            b = 2 * i * j
            c = i ** 2 + j ** 2
            if a + b + c == n:
                return a * b * c


def test():
    assert solve() == 31875000
