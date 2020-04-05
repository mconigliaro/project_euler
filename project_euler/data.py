def data(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]
