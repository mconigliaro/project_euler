from project_euler.figurate import pentagonal, is_pentagonal


def solve():
    p_hist = []
    i = 1
    while True:
        p_curr = pentagonal(i)
        for p in p_hist:
            if is_pentagonal(p_curr - p) and is_pentagonal(p_curr + p):
                return p_curr - p
        p_hist.append(p_curr)
        i += 1


def test():
    assert solve() == 5482660
