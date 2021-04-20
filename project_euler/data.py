def data(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]
