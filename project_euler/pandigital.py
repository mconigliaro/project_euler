from itertools import permutations
from typing import Generator, Iterable, Union


def pandigital(
    num: Union[int, None] = None, digits: Iterable = list(range(10))
) -> Generator:
    strings = any(type(x) is str for x in digits)

    for i, digit_list in enumerate(permutations(digits)):
        if strings:
            n = "".join(digit_list)
        else:
            n = sum(n * (10**i) for i, n in enumerate(reversed(digit_list)))

        if num and i >= num:
            break

        yield n


def is_pandigital(x: Iterable, digits: Iterable = list(range(10))) -> bool:
    return set(digits).issubset(set(x))
