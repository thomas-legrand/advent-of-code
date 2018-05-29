import sys
sys.path.append("../..")
from common import input_utils


def get_custom_input():
    f = open('input')
    return [int(n) for n in f.readline().split(',')]


def reverse(numbers, pos, length, skip):
    stack = []
    for i in range(pos, pos + length):
        stack.append(numbers[i % len(numbers)])
    for i in range(pos, pos + length):
        numbers[i % len(numbers)] = stack.pop()
    return numbers, (pos + length + skip) % len(numbers)


def process(numbers, inp_lengths):
    skip = 0
    pos = 0
    for length in inp_lengths:
        numbers, pos = reverse(numbers, pos, length, skip)
        skip += 1
    return numbers[0] * numbers[1]


def get_lengths(s):
    return map(ord, s) + [17, 31, 73, 47, 23]


def dense_hash(numbers):
    d = []
    for i in range(16):
        j = i * 16
        d += [reduce(lambda x, y: x ^ y, numbers[j: j + 16])]
    return ''.join(map(to_hexa, d))


def process2(r, inp):
    skip = 0
    pos = 0
    inp_lengths = get_lengths(inp)
    numbers = [i for i in range(r)]
    for i in range(64):
        for length in inp_lengths:
            numbers, pos = reverse(numbers, pos, length, skip)
            skip += 1
    return dense_hash(numbers)


def to_hexa(n):
    h = hex(n)
    if len(h) == 3:
        return '0' + h[-1]
    return hex(n)[-2:]


def run_test():
    assert reverse([0, 1, 2, 3, 4], 0, 3, 0) == ([2, 1, 0, 3, 4], 3)
    assert reverse([2, 1, 0, 3, 4], 3, 4, 1) == ([4, 3, 0, 1, 2], 3)
    assert process([0, 1, 2, 3, 4], [3, 4, 1, 5]) == 12
    assert get_lengths('1,2,3') == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    assert 65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 == 64
    assert to_hexa(64) == '40'
    assert to_hexa(7) == '07'
    assert to_hexa(255) == 'ff'
    assert process2(256, '') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert process2(256, 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'


def main():
    run_test()
    numbers = [i for i in range(0, 256)]
    inp = get_custom_input()
    print process(numbers, inp)
    inp = input_utils.get_input('input')
    print process2(256, inp)


if __name__ == '__main__':
    main()
