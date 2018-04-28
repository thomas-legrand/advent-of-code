from collections import defaultdict


TEST_KEY = 'flqrgnkx'
KEY = 'uugsqrei'


def to_hexa(n):
    h = hex(n)
    if len(h) == 3:
        return '0' + h[-1]
    return hex(n)[-2:]


def dense_hash(numbers):
    d = []
    for i in range(16):
        j = i * 16
        d += [reduce(lambda x, y: x ^ y, numbers[j: j + 16])]
    return ''.join(map(to_hexa, d))


def reverse(numbers, pos, length, skip):
    stack = []
    for i in range(pos, pos + length):
        stack.append(numbers[i % len(numbers)])
    for i in range(pos, pos + length):
        numbers[i % len(numbers)] = stack.pop()
    return numbers, (pos + length + skip) % len(numbers)


def get_lengths(s):
    return map(ord, s) + [17, 31, 73, 47, 23]


def knot_hash(r, inp):
    skip = 0
    pos = 0
    inp_lengths = get_lengths(inp)
    numbers = [i for i in range(r)]
    for i in range(64):
        for length in inp_lengths:
            numbers, pos = reverse(numbers, pos, length, skip)
            skip += 1
    return dense_hash(numbers)


def get_row(h):
    return bin(int(h, 16))[2:].zfill(128)


def get_grid(key):
    input_strings = [key + '-' + str(i) for i in range(128)]
    hashes = map(lambda s: knot_hash(256, s), input_strings)
    output = map(get_row, hashes)
    return output


def count(key):
    return sum([t.count('1') for t in get_grid(key)])


def print_grid(grid, size):
    for g in grid[:size]:
        print g[:size]


def get_islands(grid, size):
    islands = defaultdict(list)
    position_assignment = {}
    next_id = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '1':
                position = tuple((i, j))
                assigned = False
                if i > 0 and tuple((i-1, j)) in position_assignment:
                    # assign new position to existing island
                    island = position_assignment[tuple((i-1, j))]
                    islands[island] += [position]
                    position_assignment[position] = int(island)
                    assigned = True
                if j > 0 and tuple((i, j-1)) in position_assignment:
                    if not assigned:
                        # assign new position to existing island
                        island = position_assignment[tuple((i, j-1))]
                        islands[island] += [position]
                        position_assignment[position] = int(island)
                        assigned = True
                    else:
                        # in this case, the position was already assigned to existing island on the left
                        # we check if the island on top is the same
                        other_island = position_assignment[tuple((i, j-1))]
                        if other_island != island:
                            # if not, we reassign all positions from the island on top to the island on the left
                            for p in islands[other_island]:
                                position_assignment[p] = int(island)
                                islands[island] += [p]
                            del islands[other_island]
                if not assigned:
                    # assign new island to the position, because we didn't find existing island at left/top
                    islands[int(next_id)] += [position]
                    position_assignment[position] = int(next_id)
                    next_id += 1
    print position_assignment
    print islands
    return len(islands.keys())


def run_test():
    assert count(TEST_KEY) == 8108
    assert len(get_row('55eab3c4fbfede16dcec2c66dda26464')) == 128
    grid = get_grid(TEST_KEY)
    # print_grid(grid, 10)
    assert get_islands(grid, 10) == 10
    assert get_islands(grid, 128) == 1242


def main():
    run_test()
    print count(KEY)
    grid = get_grid(KEY)
    print get_islands(grid, 128)


if __name__ == '__main__':
    main()
