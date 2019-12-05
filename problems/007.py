from project_euler.prime import primes


def solve():
    return list(primes(10001))[-1]


def test():
    assert solve() == 104743
