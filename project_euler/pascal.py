from math import factorial
from typing import Union


def pascals_triangle(i: int, j: int) -> Union[int, float, None]:
    return None if j > i else factorial(i) / (factorial(j) * factorial(i - j))
