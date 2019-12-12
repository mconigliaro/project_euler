from project_euler.data import data


def traverse(matrix, path=[], paths=[], x=0, y=0):
    if x >= len(matrix) or y >= len(matrix[x]):
        return

    path.append(matrix[x][y])

    traverse(matrix, path, paths, x + 1, y)
    traverse(matrix, path, paths, x + 1, y + 1)

    if len(path) == len(matrix):
        paths.append(path.copy())
    path.pop()

    return paths


def solve():
    matrix = []
    for l in data('problems/data/018.txt'):
        matrix.append([int(x) for x in l.split(' ')])
    return max(sum(x) for x in traverse(matrix))


def test():
    assert solve() == 1074
