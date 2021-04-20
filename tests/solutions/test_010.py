import project_euler.prime as pr


def solution():
    return sum(pr.primes(end=2000000))


def test():
    assert solution() == 142913828922
