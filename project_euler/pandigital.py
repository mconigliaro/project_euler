from itertools import permutations


def pandigital(num=None, chars='0123456789'):
    for i, n in enumerate(permutations(chars)):
        n = ''.join(n)
        if not num or num and i < num:
            yield n
        else:
            return n


def is_pandigital(n, chars='0123456789'):
    return set(chars).issubset(set(str(n)))
