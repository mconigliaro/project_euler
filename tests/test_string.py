from project_euler.string import string_value


def test_string_value():
    assert string_value("a") == 1
    assert string_value("abc") == 1 + 2 + 3
