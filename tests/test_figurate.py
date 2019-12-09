import pytest
from project_euler.figurate import is_triangular, triangular, \
  is_pentagonal, pentagonal


@pytest.fixture
def known_triangular():
    return [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136,
            153, 171, 190, 210, 231, 253, 276, 300, 325]


@pytest.fixture
def known_not_triangular(known_triangular):
    return list(set(range(known_triangular[-1])) - set(known_triangular))


@pytest.fixture
def known_pentagonal():
    return [0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330,
            376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001]


@pytest.fixture
def known_not_pentagonal(known_pentagonal):
    return list(set(range(known_pentagonal[-1])) - set(known_pentagonal))


def test_triangular(known_triangular, known_not_triangular):
    for i, x in enumerate(known_triangular):
        assert triangular(i) == x
        assert is_triangular(x)

    assert not any(is_triangular(x) for x in known_not_triangular)


def test_pentagonal(known_pentagonal, known_not_pentagonal):
    for i, x in enumerate(known_pentagonal):
        assert pentagonal(i) == x
        assert is_pentagonal(x)

    assert not any(is_pentagonal(x) for x in known_not_pentagonal)
