import sys
sys.path.append("../..")
from common import input_utils


def sum_next(s):
    i = 0
    c = 0
    while i < len(s):
        ind = (i + 1) % len(s)
        if s[i] == s[ind]:
            c += int(s[i])
        i += 1
    return c


def sum_next2(s):
    i = 0
    c = 0
    while i < len(s):
        ind = (i + len(s) / 2) % len(s)
        if s[i] == s[ind]:
            c += int(s[i])
        i += 1
    return c


def run_test():
    assert sum_next('1122') == 3
    assert sum_next('1111') == 4
    assert sum_next('1234') == 0
    assert sum_next2('1212') == 6
    assert sum_next2('1221') == 0
    assert sum_next2('123425') == 4


def main():
    run_test()
    inp = input_utils.get_input('input')
    print sum_next(inp)
    print sum_next2(inp)

if __name__ == '__main__':
    main()
