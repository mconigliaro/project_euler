import project_euler.data as dat


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
    for line in dat.data('problems/data/018.txt'):
        matrix.append([int(x) for x in line.split(' ')])
    return max(sum(x) for x in traverse(matrix))


def test():
    assert solve() == 1074
