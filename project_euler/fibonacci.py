from itertools import count


def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        return (c, d) if n % 2 == 0 else (d, c + d)


def fibonaccis(start=0, num=None, end=None):
    a, b = fibonacci(start)
    for i in count(start):
        if (num and i >= num) or (end and a >= end):
            break
        else:
            yield a
            a, b = b, a + b
