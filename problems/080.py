from decimal import getcontext, Decimal


def solve():
    s = 0
    getcontext().prec = 102
    for i in range(100):
        sqrt = Decimal(i).sqrt()
        if not sqrt == int(sqrt):
            digits = list(str(sqrt).replace('.', '')[0:100])
            s += sum(int(x) for x in digits)
    return s


def test():
    assert solve() == 40886
