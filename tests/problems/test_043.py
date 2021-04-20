import project_euler.pandigital as pd
import project_euler.prime as pr


def solve():
    digits = list(str(x) for x in range(10))
    chunk_by = 3
    chunks = len(digits) - chunk_by + 1
    p = list(pr.primes(chunks))
    pandigitals = []
    for n in pd.pandigital(digits=digits):
        if all(int(n[i:i + chunk_by]) % p[i - 1] == 0
               for i in range(1, chunks)):
            pandigitals.append(int(n))
    return sum(pandigitals)


def test():
    assert solve() == 16695334890
