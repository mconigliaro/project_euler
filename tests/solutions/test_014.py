def solve():
    memo = {}
    max_start = None
    max_len = 0

    for i in range(1, 1000000):
        cur_last = i
        cur_len = 1

        while cur_last > 1:
            if cur_last in memo:
                memo[i] = cur_len = memo[cur_last] + cur_len
                cur_last = 1
            else:
                if cur_last % 2 == 0:
                    cur_last = cur_last / 2
                else:
                    cur_last = 3 * cur_last + 1
                memo[i] = cur_len
                cur_len += 1

        if cur_len > max_len:
            max_start = i
            max_len = cur_len

    return max_start


def test():
    assert solve() == 837799
