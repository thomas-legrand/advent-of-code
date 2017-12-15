def get_input_map(f_name):
    f = open(f_name)
    firewall = [map(int, e.split(': ')) for e in f.read().splitlines()]
    return {e[0]: e[1] for e in firewall}


def traverse(inp):
    positions, _ = get_traversal_positions(inp)
    return sum([i * inp[i] for i in inp if positions[i] == 0])


def can_traverse(positions):
    for i in positions:
        if positions[i] == 0:
            return False
    return True


def get_traversal_positions(ranges):
    positions = {k: 0 for k in ranges}
    dirs = {k: 1 for k in ranges}
    for k in positions:
        i = 0
        while i < k:
            positions[k] += dirs[k]
            if positions[k] == ranges[k] - 1 or positions[k] == 0:
                dirs[k] *= -1
            i += 1
    return positions, dirs


def update_positions(positions, dirs, ranges):
    for k in positions:
        positions[k] += dirs[k]
        if positions[k] == ranges[k] - 1 or positions[k] == 0:
            dirs[k] *= -1


def pick_start(inp):
    start = 0
    positions, dirs = get_traversal_positions(inp)
    while not can_traverse(positions):
        update_positions(positions, dirs, inp)
        start += 1
    return start


def run_test():
    inp = get_input_map('test_input')
    assert traverse(inp) == 24
    assert pick_start(inp) == 10


def main():
    run_test()
    inp = get_input_map('input')
    print traverse(inp)
    print pick_start(inp)

if __name__ == '__main__':
    main()
