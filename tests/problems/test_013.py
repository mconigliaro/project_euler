import project_euler.data as dat


def solve():
    numbers = []
    for line in dat.data('tests/data/013.txt'):
        numbers.append(int(line))
    return int(str(sum(numbers))[0:10])


def test():
    assert solve() == 5537376230
