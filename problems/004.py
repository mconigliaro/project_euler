def test_004():
    r = range(100, 999)
    largest = 0
    for x in r:
        for y in r:
            p = x * y
            if p > largest and p == int(''.join(list(str(p))[::-1])):
                largest = p
    return largest
