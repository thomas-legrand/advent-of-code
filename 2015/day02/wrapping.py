def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def sides(x):
    return [x[0] * x[1], x[1] * x[2], x[0] * x[2]]


def req_wrapping(present):
    present_dims = [int(n) for n in present.split('x')]
    s = sides(present_dims)
    return 2 * sum(s) + min(s)


def req_ribbon_length(present):
    present_dims_sorted = sorted([int(n) for n in present.split('x')])
    return (present_dims_sorted[0] + present_dims_sorted[1]) * 2 + reduce(lambda x, y: x*y, present_dims_sorted)


def run_test():
    assert req_wrapping('2x3x4') == 58
    assert req_wrapping('1x1x10') == 43
    assert req_ribbon_length('2x3x4') == 34
    assert req_ribbon_length('1x1x10') == 14


def main():
    run_test()
    inp = get_multi_line_input()
    print sum(map(req_wrapping, inp))
    print sum(map(req_ribbon_length, inp))

if __name__ == '__main__':
    main()
