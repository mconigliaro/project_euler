import datetime as dt


def solution():
    days = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            if dt.date(y, m, 1).weekday() == 6:
                days += 1
    return days


def test():
    assert solution() == 171
