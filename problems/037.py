import project_euler.prime as pr


def solve():
    t_primes = []
    for p in pr.primes():
        if p > 7:
            truncations = set()
            digits = str(p)
            for i in range(len(digits) - 1):
                truncations.add(int(digits[(i + 1):]))
                truncations.add(int(digits[:((i + 1) * -1)]))
            if all(pr.is_prime(x) for x in truncations):
                t_primes.append(p)
                if len(t_primes) == 11:
                    return sum(t_primes)


def test():
    assert solve() == 748317
