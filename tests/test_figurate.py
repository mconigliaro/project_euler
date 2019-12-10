import pytest
from project_euler.figurate import triangular, is_triangular, \
  pentagonal, is_pentagonal, hexagonal, is_hexagonal


@pytest.fixture
def known_triangular():
    return [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136,
            153, 171, 190, 210, 231, 253, 276, 300, 325]


@pytest.fixture
def known_not_triangular(known_triangular):
    r = range(known_triangular[0], known_triangular[-1])
    return list(set(r) - set(known_triangular))


@pytest.fixture
def known_pentagonal():
    return [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330,
            376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001]


@pytest.fixture
def known_not_pentagonal(known_pentagonal):
    r = range(known_pentagonal[0], known_pentagonal[-1])
    return list(set(r) - set(known_pentagonal))


@pytest.fixture
def known_hexagonal():
    return [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435,
            496, 561, 630, 703, 780, 861, 946]


@pytest.fixture
def known_not_hexagonal(known_hexagonal):
    r = range(known_hexagonal[0], known_hexagonal[-1])
    return list(set(r) - set(known_hexagonal))


def test_triangular(known_triangular, known_not_triangular):
    for i, x in enumerate(known_triangular):
        assert triangular(i + 1) == x
        assert is_triangular(x)

    assert not any(is_triangular(x) for x in known_not_triangular)


def test_pentagonal(known_pentagonal, known_not_pentagonal):
    for i, x in enumerate(known_pentagonal):
        assert pentagonal(i + 1) == x
        assert is_pentagonal(x)

    assert not any(is_pentagonal(x) for x in known_not_pentagonal)


def test_hexagonal(known_hexagonal, known_not_hexagonal):
    for i, x in enumerate(known_hexagonal):
        assert hexagonal(i + 1) == x
        assert is_hexagonal(x)

    assert not any(is_hexagonal(x) for x in known_not_hexagonal)
