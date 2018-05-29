import sys
sys.path.append("../..")
from common import input_utils


def exit_inst(inst):
    inp = list(inst)
    i = 0
    c = 0
    while 0 <= i < len(inp):
        inp[i] += 1
        i += inp[i] - 1
        c += 1
    return c


def exit_inst2(inst):
    inp = list(inst)
    i = 0
    c = 0
    while 0 <= i < len(inp):
        if inp[i] >= 3:
            inp[i] -= 1
            i += inp[i] + 1
        else:
            inp[i] += 1
            i += inp[i] - 1
        c += 1
    return c


def run_test():
    inp_test = [int(n) for n in input_utils.get_multi_line_input('input_test')]
    assert exit_inst(inp_test) == 5
    assert exit_inst2(inp_test) == 10


def main():
    run_test()
    inp = [int(n) for n in input_utils.get_multi_line_input('input')]
    print exit_inst(inp)
    print exit_inst2(inp)


if __name__ == '__main__':
    main()
