def get_input():
    f = open('input')
    return f.readline()


def visited_houses(inp):
    current_loc = complex()
    visited_locations = {current_loc}
    for direction in inp:
        if direction == '^':
            current_loc += 1j
            visited_locations.add(current_loc)
        elif direction == '>':
            current_loc += 1
            visited_locations.add(current_loc)
        elif direction == '<':
            current_loc -= 1
            visited_locations.add(current_loc)
        elif direction == 'v':
            current_loc -= 1j
            visited_locations.add(current_loc)
    return visited_locations


def unique_houses(inp):
    return len(visited_houses(inp))


def team_robo(inp):
    inp_santa = inp[1::2]
    inp_robo_santa = inp[::2]
    visited_locations = visited_houses(inp_santa).union(visited_houses(inp_robo_santa))
    return len(visited_locations)


def run_test():
    assert unique_houses('>') == 2
    assert unique_houses('^>v<') == 4
    assert unique_houses('^v^v^v^v^v') == 2
    assert team_robo('^v') == 3
    assert team_robo('^>v<') == 3
    assert team_robo('^v^v^v^v^v') == 11


def main():
    run_test()
    inp = get_input()
    print unique_houses(inp)
    print team_robo(inp)


if __name__ == '__main__':
    main()
