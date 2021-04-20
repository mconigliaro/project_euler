import project_euler.prime as pr


def solution():
    p = [p for p in pr.primes(end=9999)
         if p >= 1000 and p not in [1487, 4817, 8147]]
    d = {}
    for n in p:
        d.setdefault(''.join(sorted(str(n))), []).append(n)
    for s in [v for v in d.values() if len(v) >= 3]:
        for offset in range(len(s) - 3 + 1):
            if s[offset + 2] - s[offset + 1] == s[offset + 1] - s[offset]:
                return int(''.join(str(x) for x in s[offset:offset + 3]))


def test():
    assert solution() == 296962999629
