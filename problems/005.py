def test_005():
    divisors = range(11, 19)
    gcd = max(divisors)
    n = gcd + 1
    found = None
    while not found:
        for d in divisors:
            if n % d != 0:
                n += gcd + 1
                break
            elif d == gcd:
                found = n
    assert found == 232792560
