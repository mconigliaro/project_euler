import itertools as it


def solve():
    largest = 0
    for x, y in it.product(range(100, 999), repeat=2):
        product = x * y
        r_product = int(str(product)[::-1])
        if product == r_product and product > largest:
            largest = product
    return largest


def test():
    assert solve() == 906609
