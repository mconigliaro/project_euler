from project_euler.prime import primes, is_prime


def solve():
    m = 1000000
    p = list(primes(end=m))
    p_length = len(p)

    last = 0
    s = 0
    while s < m:
        last += 1
        s = sum(p[0:last])

    s = 0
    while not is_prime(s):
        offset = 0
        while offset + last <= p_length and not is_prime(s):
            s = sum(p[offset:last])
            if s > m:
                break
            else:
                offset += 1
        last -= 1
    return s


def test():
    assert solve() == 997651
