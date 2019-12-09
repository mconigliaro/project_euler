def data(file):
    f = open(file, 'r')
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines
