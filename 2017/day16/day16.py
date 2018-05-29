import sys
sys.path.append("../..")
from common import input_utils


def spin(s, n):
    return s[-n:] + s[:-n]


def exchange(s, i, j):
    st = list(s)
    tmp = st[i]
    st[i] = st[j]
    st[j] = tmp
    return "".join(st)


def partner(s, p1, p2):
    # st = list(s)
    i = s.index(p1)
    j = s.index(p2)
    return exchange(s, i, j)


def parse(inst):
    if inst[0] == 's':
        return lambda s: spin(s, int(inst[1:]))
    elif inst[0] == 'x':
        pos = map(int, inst[1:].split('/'))
        return lambda s: exchange(s, pos[0], pos[1])
    elif inst[0] == 'p':
        prog = inst[1:].split('/')
        return lambda s: partner(s, prog[0], prog[1])


def whole_dance(instructions, programs):
    N = 1000000000
    cache = {}
    n_cache_hits = 0
    initial_positions = str(programs)
    i = 0
    while i < N:
        if i > 0 and programs == initial_positions:
            # we reached a loop in the dance, we compute the cycle length and fast-forward through the cycles
            print 'reached loop at i = {}'.format(i)
            cycle_length = int(i)
            cycles = N // cycle_length
            i = cycle_length * cycles
            print 'advancing to i = {}'.format(i)
        i += 1
        if programs in cache:
            programs = cache[programs]
            n_cache_hits += 1
            continue
        old_positions = str(programs)
        for inst in instructions:
            programs = parse(inst)(programs)
        cache[old_positions] = programs
    return programs


def run_test():
    assert spin('abcde', 3) == 'cdeab'
    assert exchange('eabcd', 3, 4) == 'eabdc'
    assert partner('eabdc', 'e', 'b') == 'baedc'
    programs = 'abcde'
    instructions = input_utils.get_comma_separated_single_line_input('test_input')
    for inst in instructions:
        programs = parse(inst)(programs)
    assert programs == 'baedc'
    for inst in instructions:
        programs = parse(inst)(programs)
    assert programs == 'ceadb'


def main():
    run_test()
    print '#1 ----'
    programs = 'abcdefghijklmnop'
    instructions = input_utils.get_comma_separated_single_line_input('input')
    for inst in instructions:
        programs = parse(inst)(programs)
    print programs
    print '#2 ----'
    programs = 'abcdefghijklmnop'
    print whole_dance(instructions, programs)


if __name__ == '__main__':
    main()
