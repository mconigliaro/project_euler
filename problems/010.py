from project_euler.prime import primes


def solve():
    return sum(primes(end=2000000))


def test():
    assert solve() == 142913828922
