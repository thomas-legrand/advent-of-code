import sys
sys.path.append("../..")
from common import input_utils


def parse(inp):
    assert len(inp) % 2 == 1
    l = len(inp)
    infected = set()
    offset = - (l // 2)
    for y in range(l):
        for x in range(l):
            if inp[y][x] == '.':
                continue
            infected.add(complex(x + offset, - (y + offset)))
    return infected


def run(inp, iterations=10000, start=0):
    infected = parse(inp)
    current_position = start
    current_direction = 1j
    n_infections = 0
    for i in range(iterations):
        # print 'current position: ' + str(current_position)
        # print 'current direction: ' + str(current_direction)
        if current_position in infected:
            # print 'found infected'
            infected.remove(current_position)
            current_direction *= -1j
            current_position += current_direction
        else:
            # print 'found not infected'
            infected.add(current_position)
            current_direction *= 1j
            current_position += current_direction
            n_infections += 1

    return n_infections


def run2(inp, iterations=10000000, start=0):
    infected = parse(inp)
    current_position = start
    current_direction = 1j
    n_infections = 0
    weakened = set()
    flagged = set()
    for i in range(iterations):
        # print 'current position: ' + str(current_position)
        # print 'current direction: ' + str(current_direction)
        if current_position in infected:
            # print 'found infected'
            # turn right and mark node as flagged
            infected.remove(current_position)
            flagged.add(current_position)
            current_direction *= -1j
            current_position += current_direction
        elif current_position in flagged:
            # print 'found flagged'
            # reverse direction and mark node as clean
            flagged.remove(current_position)
            current_direction *= -1
            current_position += current_direction
        elif current_position in weakened:
            # print 'found weakened'
            # don't turn and mark node as infected
            weakened.remove(current_position)
            infected.add(current_position)
            current_position += current_direction
            n_infections += 1
        else:
            # print 'found clean'
            # turn left and mark node as weakened
            weakened.add(current_position)
            current_direction *= 1j
            current_position += current_direction
    return n_infections


def run_test():
    inp = input_utils.get_multi_line_input('test_input')
    assert parse(inp) == {(1+1j), (-1+0j)}
    assert run(inp) == 5587
    assert run2(inp, iterations=100) == 26
    assert run2(inp) == 2511944


def main():
    run_test()
    inp = input_utils.get_multi_line_input('input')
    print run(inp)
    print run2(inp)


if __name__ == '__main__':
    main()
