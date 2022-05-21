from project_euler.data import data


def test_data():
    assert data("tests/data/test.txt") == ["test"]
