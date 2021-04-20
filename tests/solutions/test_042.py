import project_euler.data as dat
import project_euler.figurate as fig
import project_euler.string as st


def solve():
    d = dat.data('tests/data/042.txt')
    words = [x.replace('"', '') for x in d[0].split(',')]
    return len([x for x in words if fig.is_triangular(st.string_value(x))])


def test():
    assert solve() == 162
