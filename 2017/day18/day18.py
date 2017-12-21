from collections import defaultdict

REGISTER = defaultdict(int)
SET = 'set'
ADD = 'add'
MUL = 'mul'
MOD = 'mod'
SND = 'snd'
RCV = 'rcv'
JGZ = 'jgz'


def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()


def calc(v):
    global REGISTER
    try:
        return int(v)
    except ValueError as e:
        return REGISTER[v]


def read(instructions):
    global REGISTER
    REGISTER = defaultdict(int)
    i = 0
    last_played = 0
    while 0 <= i < len(instructions):
        tokens = instructions[i].split()
        if tokens[0] == SET:
            REGISTER[tokens[1]] = calc(tokens[2])
        elif tokens[0] == ADD:
            REGISTER[tokens[1]] += calc(tokens[2])
        elif tokens[0] == MUL:
            REGISTER[tokens[1]] *= calc(tokens[2])
        elif tokens[0] == MOD:
            REGISTER[tokens[1]] = REGISTER[tokens[1]] % calc(tokens[2])
        elif tokens[0] == SND:
            last_played = REGISTER[tokens[1]]
        elif tokens[0] == RCV:
            if calc(tokens[1]) != 0:
                return last_played
        elif tokens[0] == JGZ:
            i = i + calc(tokens[2]) if REGISTER[tokens[1]] > 0 else i + 1
            continue
        i += 1


def run_test():
    inp = get_multi_line_input('test_input')
    assert read(inp) == 4


def main():
    run_test()
    inp = get_multi_line_input('input')
    print read(inp)

if __name__ == '__main__':
    main()
