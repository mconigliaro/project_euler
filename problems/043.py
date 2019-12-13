from project_euler.pandigital import pandigital
from project_euler.prime import primes


def solve():
    c = '0123456789'
    chunk_by = 3
    chunks = len(c) - chunk_by + 1
    p = list(primes(chunks))
    pandigitals = []
    for n in pandigital(chars=c):
        if all(int(n[i:i + chunk_by]) % p[i - 1] == 0
               for i in range(1, chunks)):
            pandigitals.append(int(n))
    return sum(pandigitals)


def test():
    assert solve() == 16695334890
