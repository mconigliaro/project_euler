from project_euler.data import data


def solve():
    matrix = []
    for l in data('problems/data/011.txt'):
        matrix.append([int(x) for x in l.split(' ')])
    chunk = 4
    m = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            l2r = dl2r = t2b = dr2l = 1
            for k in range(chunk):
                try:
                    l2r *= matrix[i][j + k]
                except IndexError:
                    l2r = 0

                try:
                    dl2r *= matrix[i + k][j + k]
                except IndexError:
                    dl2r = 0

                try:
                    t2b *= matrix[i + k][j]
                except IndexError:
                    t2b = 0

                try:
                    dr2l *= matrix[i + k][j - k]
                except IndexError:
                    dr2l = 0

            for p in [l2r, dl2r, t2b, dr2l]:
                if p > m:
                    m = p
    return m


def test():
    assert solve() == 70600674
