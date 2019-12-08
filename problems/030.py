def solve():
    p = 5
    return sum(i for i in range(2, (9 ** p) * 9)
               if i == sum(int(x) ** p for x in list(str(i))))


def test():
    assert solve() == 4438399
