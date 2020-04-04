import project_euler.data as dat
import project_euler.string as st


def solve():
    d = dat.data('problems/data/022.txt')
    names = sorted(x.replace('"', '') for x in d[0].split(','))
    return sum(st.string_value(n) * (i + 1) for i, n in enumerate(names))


def test():
    assert solve() == 871198282
