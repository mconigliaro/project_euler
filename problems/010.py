import project_euler.prime as pr


def solve():
    return sum(pr.primes(end=2000000))


def test():
    assert solve() == 142913828922
