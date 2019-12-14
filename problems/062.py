from itertools import count
from project_euler.figurate import cubic


def solve():
    cubes = {}
    for i in count(1):
        cube = cubic(i)
        key = ''.join(sorted(str(cube)))
        cubes.setdefault(key, []).append(cube)
        if len(cubes[key]) == 5:
            return min(cubes[key])


def test():
    assert solve() == 127035954683
