def string_value(s):
    return sum(ord(x.upper()) - 64 for x in list(s))
