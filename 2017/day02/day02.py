def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def diff(s):
    i = [int(n) for n in s.split()]
    return max(i) - min(i)


def check(s):
    nb = [int(n) for n in s.split()]
    for i in range(len(nb)):
        for j in range(len(nb)):
            if i != j and nb[i] % nb[j] == 0:
                return nb[i] / nb[j]


def run_test():
    assert diff('5 1 9 5') == 8


def main():
    run_test()
    inp = get_multi_line_input()
    print sum(map(diff, inp))
    print sum(map(check, inp))


if __name__ == '__main__':
    main()
