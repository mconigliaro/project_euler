from project_euler.prime import primes


def solve():
    p = [p for p in primes(end=9999)
         if p >= 1000 and p not in [1487, 4817, 8147]]

    d = {}
    for n in p:
        key = ''.join(sorted(str(n)))
        d.setdefault(key, []).append(n)

    chunk_by = 3
    for s in [v for v in d.values() if len(v) >= chunk_by]:
        chunks = len(s) - chunk_by + 1
        for i in range(chunks):
            if s[i + 2] - s[i + 1] == s[i + 1] - s[i]:
                return int(''.join(str(x) for x in s[i:i + chunk_by]))


def test():
    assert solve() == 296962999629
