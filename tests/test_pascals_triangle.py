import pytest
from project_euler.pascals_triangle import pascals_triangle


@pytest.fixture
def known_pascals_triangle():
    return [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1]
    ]


def test_pascals_triangle(known_pascals_triangle):
    for i in range(len(known_pascals_triangle)):
        for j in range(len(known_pascals_triangle[0])):
            assert pascals_triangle(i, j) == known_pascals_triangle[i][j]
