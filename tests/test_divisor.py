import pytest
from project_euler.divisor import divisors, greatest_common_divisor


@pytest.fixture
def known_divisors_of_1000():
    return [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]


def test_divisors(known_divisors_of_1000):
    assert sorted(divisors(1000)) == known_divisors_of_1000


def test_proper_divisors(known_divisors_of_1000):
    assert sorted(divisors(1000, proper=True)) == known_divisors_of_1000[:-1]


def test_greatest_common_divisor():
    assert greatest_common_divisor(2, 4) == 2
    assert greatest_common_divisor(24, 16) == 8
