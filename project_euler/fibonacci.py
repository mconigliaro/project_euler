def fibonacci(num=None, end=None):
    a, b = 0, 1
    i = 0
    while True:
        if (num and i >= num) or (end and a >= end):
            break
        else:
            yield a
            a, b = b, a + b
            i += 1
