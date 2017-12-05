def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def run_test():
    pass


def is_valid(p):
    s = set()
    for w in p.split():
        if w not in s:
            s.add(w)
        else:
            return False
    return True


def is_valid2(p):
    s = set()
    for w in p.split():
        ss = frozenset([l for l in w])
        if ss not in s:
            s.add(ss)
        else:
            return False
    return True

def main():
    run_test()
    inp = get_multi_line_input()
    print sum(map(is_valid, inp))
    print sum(map(is_valid2, inp))

if __name__ == '__main__':
    main()
