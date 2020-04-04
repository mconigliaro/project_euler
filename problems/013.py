import project_euler.data as dat


def solve():
    numbers = []
    for l in dat.data('problems/data/013.txt'):
        numbers.append(int(l))
    return int(str(sum(numbers))[0:10])


def test():
    assert solve() == 5537376230
