import project_euler.prime as pr


def solution():
    return list(pr.primes(10001))[-1]


def test():
    assert solution() == 104743
