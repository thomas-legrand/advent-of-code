import os
import string
import collections


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    print rows
    data = [r.rstrip("]\n").split("[") for r in rows]
    for d in data:
        assert len(d[1]) == 5
        d.append(d[0].split("-")[-1])
    return data


def compute_checksum(s):
    c = collections.Counter(s)
    sorted_chars = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    allowed_chars = filter(lambda x: x[0] in string.ascii_lowercase, sorted_chars)
    return ''.join([char[0] for char in allowed_chars[:5]])


def run_test():
    input_path = os.path.join('input', 'test')
    data = get_input(input_path)
    valid_names = [d for d in data if compute_checksum(d[0]) == d[1]]
    assert sum([int(d[2]) for d in valid_names]) == 1514


def main():
    run_test()
    input_path = os.path.join('input', 'data')
    data = get_input(input_path)
    valid_names = [d for d in data if compute_checksum(d[0]) == d[1]]
    print sum([int(d[2]) for d in valid_names])

if __name__ == '__main__':
    main()
