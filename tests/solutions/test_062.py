import itertools as it
import project_euler.figurate as fig


def solve():
    cubes = {}
    for i in it.count(1):
        cube = fig.cubic(i)
        key = ''.join(sorted(str(cube)))
        cubes.setdefault(key, []).append(cube)
        if len(cubes[key]) == 5:
            return min(cubes[key])


def test():
    assert solve() == 127035954683
