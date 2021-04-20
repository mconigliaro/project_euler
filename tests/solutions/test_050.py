import project_euler.prime as pr


def solution():
    m = 1000000
    p = list(pr.primes(end=m))
    p_length = len(p)

    last = 0
    s = 0
    while s < m:
        last += 1
        s = sum(p[0:last])

    s = 0
    while not pr.is_prime(s):
        offset = 0
        while offset + last <= p_length and not pr.is_prime(s):
            s = sum(p[offset:last])
            if s > m:
                break
            else:
                offset += 1
        last -= 1
    return s


def test():
    assert solution() == 997651
