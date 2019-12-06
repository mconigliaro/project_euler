import pytest
from project_euler.figurate import triangular


@pytest.fixture
def known_triangular():
    return [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136,
            153, 171, 190, 210, 231, 253, 276, 300, 325]


def test_triangular(known_triangular):
    i = 0
    for x in known_triangular:
        assert triangular(i) == known_triangular[i]
        i += 1
