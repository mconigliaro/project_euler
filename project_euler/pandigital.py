from itertools import permutations


def pandigital(num=None, chars='1234567890'):
    for i, n in enumerate(sorted(permutations(chars))):
        n = ''.join(n)
        if not num or num and i < num:
            yield n
        else:
            return n


def is_pandigital(n, chars='1234567890'):
    return set(chars) - set(str(n)) == set()
