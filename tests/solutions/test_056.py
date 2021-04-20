def solution():
    m = 0
    for i in range(100):
        for j in range(100):
            s = sum(int(x) for x in list(str(i ** j)))
            if s > m:
                m = s
    return m


def test():
    assert solution() == 972
