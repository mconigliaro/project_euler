import project_euler.prime as pr


def solve():
    return list(pr.primes(10001))[-1]


def test():
    assert solve() == 104743
