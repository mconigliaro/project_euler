import project_euler.pythagoras as pyt


def solve():
    m = 1000
    triplets = {}
    for x in pyt.pythagorean_triplets(m / 2):
        key = sum(x)
        if key <= m:
            triplets.setdefault(key, []).append(x)

    max_item = (0, 0)
    for k, v in triplets.items():
        score = len(v)
        if score > max_item[1]:
            max_item = (k, score)

    return max_item[0]


def test():
    assert solve() == 840
