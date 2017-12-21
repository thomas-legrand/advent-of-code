def get_input(f_name):
    f = open(f_name)
    return f.readline().split(',')


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


def run_test():
    assert spin('abcde', 3) == 'cdeab'
    assert exchange('eabcd', 3, 4) == 'eabdc'
    assert partner('eabdc', 'e', 'b') == 'baedc'
    programs = 'abcde'
    instructions = get_input('test_input')
    for inst in instructions:
        programs = parse(inst)(programs)
    assert programs == 'baedc'


def main():
    run_test()
    programs = 'abcdefghijklmnop'
    instructions = get_input('input')
    for inst in instructions:
        programs = parse(inst)(programs)
    print programs


if __name__ == '__main__':
    main()
