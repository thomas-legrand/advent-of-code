import sys
sys.path.append("../..")
from common import input_utils

OP = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
}

r = {}


def ev(val):
    global r
    try:
        return int(val)
    except ValueError as e:
        if val in r:
            return r[val]
        return 0


def interp(inst):
    global r
    s = inst.split(' if ')
    cond = s[1].split()
    cond_true = OP[cond[1]](ev(cond[0]), ev(cond[2]))
    if not cond_true:
        return
    ope = s[0].split()
    r[ope[0]] = OP[ope[1]](ev(ope[0]), ev(ope[2]))


def run(inp):
    global r
    r = {}
    for i in inp:
        interp(i)
    return max(r.values())


def run2(inp):
    global r
    r = {}
    m = 0
    for i in inp:
        interp(i)
        if r.values() and max(r.values()) > m:
            m = max(r.values())
    return m


def run_test():
    global r
    inp_test = input_utils.get_multi_line_input('input_test')
    assert run(inp_test) == 1
    assert run2(inp_test) == 10


def main():
    run_test()
    inp = input_utils.get_multi_line_input('input')
    print run(inp)
    print run2(inp)

if __name__ == '__main__':
    main()
