import project_euler.data as dat


def solution():
    numbers = []
    for line in dat.data('tests/data/013.txt'):
        numbers.append(int(line))
    return int(str(sum(numbers))[0:10])


def test():
    assert solution() == 5537376230
