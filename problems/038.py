from project_euler.pandigital import is_pandigital


def solve():
    cat_prods = []
    chars = '123456789'
    len_chars = len(chars)
    for i in range(1, 9999):
        cat_prod = ''
        j = 1
        while len(cat_prod) < len_chars:
            cat_prod += ''.join(str(i * j))
            j += 1
        if len(cat_prod) == len_chars and is_pandigital(cat_prod, chars):
            cat_prods.append(int(cat_prod))
    return max(cat_prods)


def test():
    assert solve() == 932718654
