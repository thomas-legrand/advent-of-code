import json

registry = {'b': 46065}
instructions = []


def get_multi_line_input(f_name):
    f = open(f_name)
    return f


def process_file(f_name, method):
    s = 0
    for line in get_multi_line_input('input'):
        print method(line)
        s += method(line)
    return s


def diff1(line):
    return len(line) - len(line.decode('string-escape')) + 2


def diff2(line):
    l = line.replace('\n', '')
    return len(json.dumps(l)) - len(l)


def run_test():
    assert diff1(r'""') == 2
    assert diff1(r'"aaa\"aaa"') == 3
    assert diff1(r'"\x27"') == 5
    print diff2(r'""')
    assert diff2(r'""') == 4
    assert diff2(r'"abc"') == 4
    assert diff2(r'"aaa\"aaa"') == 6
    assert diff2(r'"\x27"') == 5


def main():
    run_test()
    print process_file('input', diff1)
    print process_file('input', diff2)


if __name__ == '__main__':
    main()