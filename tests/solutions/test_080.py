import decimal as dec


def solution():
    s = 0
    dec.getcontext().prec = 102
    for i in range(100):
        sqrt = dec.Decimal(i).sqrt()
        if not sqrt == int(sqrt):
            digits = list(str(sqrt).replace(".", "")[0:100])
            s += sum(int(x) for x in digits)
    return s


def test():
    assert solution() == 40886
