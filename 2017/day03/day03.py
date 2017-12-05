def dist(n):
    i = 1
    pos = 0j
    dir = 1
    steps = 1
    while i <= n:
        for r in range(2):
            for s in range(steps):
                if i == n:
                    return abs(pos.real) + abs(pos.imag)
                pos += dir
                i += 1
            dir *= 1j
        steps += 1


def sum_adj(m, pos):
    s = 0
    for r in [-1, 0,  1]:
        for i in [-1j, 0,  1j]:
            if pos + r + i in m:
                s += m[pos + r + i]
    return s


def dist2(n):
    i = 1
    pos = 0j
    map = {pos: i}
    dir = 1
    steps = 1
    while i <= n:
        for r in range(2):
            for s in range(steps):
                pos += dir
                i = sum_adj(map, pos)
                map[pos] = i
                if i > n:
                    return i
            dir *= 1j
        steps += 1


def run_test():
    assert dist(1) == 0
    assert dist(12) == 3
    assert dist(23) == 2
    assert dist(1024) == 31
    assert sum_adj({}, 0) == 0
    assert sum_adj({0: 1}, 1) == 1
    assert sum_adj({0: 1, 1: 1}, 1 + 1j) == 2
    assert dist2(120) == 122
    assert dist2(800) == 806


def main():
    run_test()
    magic_input = 361527
    print dist(magic_input)
    print dist2(magic_input)

if __name__ == '__main__':
    main()
