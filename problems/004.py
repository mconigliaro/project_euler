def solve():
    r = range(100, 999)
    largest = 0
    for x in r:
        for y in r:
            product = x * y
            r_product = int(''.join(reversed(str(product))))
            if product == r_product and product > largest:
                largest = product
    return largest


def test():
    assert solve() == 906609
