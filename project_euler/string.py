def string_value(s: str) -> int:
    return sum(ord(x.upper()) - 64 for x in list(s))
