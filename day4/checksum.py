import os
import string
import collections
from functools import partial


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
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


def decode_char(c, sector_id):
    letters = string.ascii_lowercase
    n = len(letters)
    i = letters.index(c)
    offset = sector_id % n
    new_i = (offset + i) % n
    return letters[new_i]


def decrypt_string(s):
    spl = s.split("-")
    useful_stuff = spl[:-1]
    sector_id = int(spl[-1])
    decode = partial(decode_char, sector_id=sector_id)
    words = ["".join(map(decode, stuff)) for stuff in useful_stuff]
    return " ".join(words)


def run_test_part1():
    input_path = os.path.join('input', 'test')
    data = get_input(input_path)
    valid_names = [d for d in data if compute_checksum(d[0]) == d[1]]
    assert sum([int(d[2]) for d in valid_names]) == 1514


def run_test_decoding():
    assert decode_char("a", 5) == "f"


def run_test_part2():
    input_string = 'qzmt-zixmtkozy-ivhz-343'
    actual_string = decrypt_string(input_string)
    expected_string = 'very encrypted name'
    assert expected_string == actual_string


def main():
    run_test_part1()
    run_test_decoding()
    run_test_part2()
    input_path = os.path.join('input', 'data')
    data = get_input(input_path)
    valid_names = [d for d in data if compute_checksum(d[0]) == d[1]]
    print(sum([int(d[2]) for d in valid_names]))
    decrypted_names = [[decrypt_string(d[0]),d[2]] for d in valid_names]
    print(len(decrypted_names))
    print(decrypted_names)
    print(filter(lambda x: "north" in x[0], decrypted_names))

if __name__ == '__main__':
    main()
