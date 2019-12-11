from project_euler.figurate import cubic


def solve():
    cubes = {}
    i = 1
    while True:
        cube = cubic(i)
        key = ''.join(sorted(str(cube)))
        cubes.setdefault(key, []).append(cube)
        if len(cubes[key]) == 5:
            return min(cubes[key])
        i += 1


def test():
    assert solve() == 127035954683
