def get_input():
    f = open('input')
    return f.readline()


def realloc(inp):
    states = set()
    current = list(inp)
    c = 0
    while tuple(current) not in states:
        c += 1
        states.add(tuple(current))
        i = current.index(max(current))
        v = current[i]
        current[i] = 0
        while v > 0:
            i = (i + 1) % len(current)
            current[i] += 1
            v -= 1
    return c


def seen_again(inp):
    states = []
    current = list(inp)
    while True:
        if tuple(current) in states:
            return len(states) - states.index(tuple(current))
        states.append(tuple(current))
        i = current.index(max(current))
        v = current[i]
        current[i] = 0
        while v > 0:
            i = (i + 1) % len(current)
            current[i] += 1
            v -= 1


def run_test():
    assert realloc([0, 2, 7, 0]) == 5
    assert seen_again([0, 2, 7, 0]) == 4


def main():
    run_test()
    inp = map(int, get_input().split())
    print realloc(inp)
    print seen_again(inp)


if __name__ == '__main__':
    main()
