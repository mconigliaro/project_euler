def solution():
    p = 5
    return sum(i for i in range(2, (9 ** p) * 9)
               if i == sum(int(x) ** p for x in str(i)))


def test():
    assert solution() == 443839
