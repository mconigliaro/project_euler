from itertools import permutations


def pandigital(num=None, digits=list(range(10))):
    strings = any(type(x) is str for x in digits)

    for i, digit_list in enumerate(permutations(digits)):
        if strings:
            n = ''.join(digit_list)
        else:
            n = sum(n * (10 ** i) for i, n in enumerate(reversed(digit_list)))

        if not num or (num and i < num):
            yield n
        else:
            return n


def is_pandigital(x, digits=list(range(10))):
    return set(digits).issubset(set(x))
