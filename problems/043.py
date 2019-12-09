from itertools import permutations
from project_euler.prime import primes


def solve():
    chars = '0123456789'
    chunk_by = 3
    chunks = len(chars) - chunk_by + 1
    p = list(primes(chunks))
    pandigitals = []
    for n in permutations(chars):
        if all(int(''.join(n[i:i + chunk_by])) % p[i - 1] == 0
           for i in range(1, chunks)):
            pandigitals.append(int(''.join(n)))
    return sum(pandigitals)


def test():
    assert solve() == 16695334890
