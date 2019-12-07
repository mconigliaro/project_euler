import pytest
from project_euler.divisor import divisors


@pytest.fixture
def known_divisors_of_1000():
    return [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]


def test_divisors(known_divisors_of_1000):
    assert divisors(1000) == known_divisors_of_1000


def test_proper_divisors(known_divisors_of_1000):
    d = divisors(1000, proper=True)
    assert len(d) == len(known_divisors_of_1000) - 1
    assert 1000 not in d
