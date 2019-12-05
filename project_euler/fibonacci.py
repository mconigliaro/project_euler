def fibonacci(num=0, up_to=None):
    a, b = 0, 1
    i = 0
    while True:
        if (num > 0 and i >= num) or (up_to and a >= up_to):
            break
        else:
            yield a
            a, b = b, a + b
            i += 1
