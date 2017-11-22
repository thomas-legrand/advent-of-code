SIZE = 1000


def init():
    global grid
    grid = [[0] * SIZE for _ in range(SIZE)]


def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def parse_command(c):
    words = c.split(' ')
    upper_right = [int(n) for n in words[-3].split(',')]
    lower_left = [int(n) for n in words[-1].split(',')]
    x_range, y_range = zip(upper_right, lower_left)
    return [words[-4], x_range, y_range]


def count_lights_on(a):
    return sum(map(sum, a))


def switch(parsed_command):
    global grid
    action = parsed_command[0]
    x0, x1 = parsed_command[1]
    y0, y1 = parsed_command[2]
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            if action == 'on':
                grid[j][i] = 1
            elif action == 'off':
                grid[j][i] = 0
            else:
                grid[j][i] = 1 if grid[j][i] == 0 else 0


def switch_2(parsed_command):
    global grid
    action = parsed_command[0]
    x0, x1 = parsed_command[1]
    y0, y1 = parsed_command[2]
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            if action == 'on':
                grid[j][i] += 1
            elif action == 'off':
                grid[j][i] = max(grid[j][i] - 1, 0)
            else:
                grid[j][i] += 2


def execute(instructions_list, switch_fun):
    init()
    parsed_instructions = map(parse_command, instructions_list)
    map(switch_fun, parsed_instructions)
    return count_lights_on(grid)


def run_test():
    global grid
    assert count_lights_on([[0, 1], [1, 0]]) == 2
    assert parse_command('turn off 152,628 through 582,896') == ['off', (152, 582), (628, 896)]
    assert parse_command('turn off 537,651 through 641,816') == ['off', (537, 641), (651, 816)]
    assert parse_command('toggle 537,651 through 641,816') == ['toggle', (537, 641), (651, 816)]
    init()
    switch(parse_command('turn on 0,0 through 999,999'))
    switch(parse_command('toggle 0,0 through 999,0'))
    switch(parse_command('turn off 499,499 through 500,500'))
    assert count_lights_on(grid) == 998996
    init()
    switch_2(parse_command('turn on 0,0 through 999,999'))
    switch_2(parse_command('toggle 0,0 through 999,0'))
    switch_2(parse_command('turn off 499,499 through 500,500'))
    assert count_lights_on(grid) == 1001996


def main():
    run_test()
    inp = get_multi_line_input()
    print execute(inp, switch)
    print execute(inp, switch_2)

if __name__ == '__main__':
    main()
