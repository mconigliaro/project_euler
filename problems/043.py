from project_euler.pandigital import pandigital
from project_euler.prime import primes


def solve():
    digits = list(str(x) for x in range(10))
    chunk_by = 3
    chunks = len(digits) - chunk_by + 1
    p = list(primes(chunks))
    pandigitals = []
    for n in pandigital(digits=digits):
        if all(int(n[i:i + chunk_by]) % p[i - 1] == 0
               for i in range(1, chunks)):
            pandigitals.append(int(n))
    return sum(pandigitals)


def test():
    assert solve() == 16695334890
