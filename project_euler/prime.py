from math import sqrt


def primes(num=0, up_to=None):
    memo = {}
    x = 2
    i = 0
    while True:
        if (num > 0 and i >= num) or (up_to and x >= up_to):
            break
        elif x not in memo:
            yield x
            memo[x ** 2] = [x]
            i += 1
        else:
            for p in memo[x]:
                memo.setdefault(p + x, []).append(p)
            del memo[x]
        x += 1


def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        return not any(n % x == 0 for x in range(3, int(sqrt(n)) + 1, 2))
