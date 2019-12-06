import pytest
from project_euler.divisor import divisor_count


@pytest.fixture
def known_divisors_of_1000():
    return [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]


def test_divisor_count(known_divisors_of_1000):
    assert divisor_count(1000) == len(known_divisors_of_1000)
