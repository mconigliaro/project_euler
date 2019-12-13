import pytest
from project_euler.figurate import cubic, is_cubic, triangular, is_triangular,\
  pentagonal, is_pentagonal, hexagonal, is_hexagonal


@pytest.fixture
def known_cubic():
    return [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197,
            2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167,
            13824, 15625, 17576, 19683, 21952, 24389, 27000, 29791, 32768,
            35937, 39304, 42875, 46656, 50653, 54872, 59319, 64000]


@pytest.fixture
def known_not_cubic(known_cubic):
    r = range(known_cubic[0], known_cubic[-1])
    return [x for x in r if x not in known_cubic]


@pytest.fixture
def known_triangular():
    return [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136,
            153, 171, 190, 210, 231, 253, 276, 300, 325]


@pytest.fixture
def known_not_triangular(known_triangular):
    r = range(known_triangular[0], known_triangular[-1])
    return [x for x in r if x not in known_triangular]


@pytest.fixture
def known_pentagonal():
    return [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330,
            376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001]


@pytest.fixture
def known_not_pentagonal(known_pentagonal):
    r = range(known_pentagonal[0], known_pentagonal[-1])
    return [x for x in r if x not in known_pentagonal]


@pytest.fixture
def known_hexagonal():
    return [1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435,
            496, 561, 630, 703, 780, 861, 946]


@pytest.fixture
def known_not_hexagonal(known_hexagonal):
    r = range(known_hexagonal[0], known_hexagonal[-1])
    return [x for x in r if x not in known_hexagonal]


def test_cubic(known_cubic, known_not_cubic):
    for i, x in enumerate(known_cubic):
        assert cubic(i + 1) == x
        assert is_cubic(x)

    assert not any(is_cubic(x) for x in known_not_cubic)


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
