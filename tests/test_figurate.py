import pytest
from project_euler.figurate import is_triangular, triangular


@pytest.fixture
def known_triangular():
    return [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136,
            153, 171, 190, 210, 231, 253, 276, 300, 325]


def test_triangular(known_triangular):
    for i, x in enumerate(known_triangular):
        assert triangular(i) == x
        assert is_triangular(x)
