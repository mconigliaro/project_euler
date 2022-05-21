import collections as col
import project_euler.prime as pr


def rotations(n):
    if n < 10:
        return [n]
    else:
        r = []
        digits = col.deque(i for i in str(n))
        for i in range(len(digits) - 1):
            digits.append(digits.popleft())
            r.append(int("".join(digits)))
        return r


def solution():
    return sum(
        1 for i in pr.primes(end=1000000) if all(pr.is_prime(r) for r in rotations(i))
    )


def test():
    assert solution() == 55
